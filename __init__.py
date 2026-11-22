from __future__ import annotations

import logging

from homeassistant.components import persistent_notification
from homeassistant.config_entries import ConfigEntry, ConfigSubentry
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers.translation import async_get_translations
from homeassistant.util import ulid as ulid_util
import voluptuous as vol

from .business.plan_builder import PlanBuilderError, plan_from_subentries
from .const import CONF_REUSE_SERIAL, DOMAIN, MAX_GATEWAY_INSTANCES
from .business.child_cleanup import ChildCleanupClient
from .gateway import GatewayConfig, GatewayLimitError, GatewayManager, GatewayRuntime
from .ha_adapter import HAEntityBridge
from .legacy_import import legacy_child_payloads
from .storage import GatewayStore


PLATFORMS: list[str] = ["binary_sensor", "sensor", "button"]
_LOGGER = logging.getLogger(__name__)


def _read_gateway_removal_material(config_dir: str, serial: str):
    """Read removal-time files outside Home Assistant's event loop."""

    store = GatewayStore(config_dir, serial)
    material = store.read_json("cloud/material.json")
    ca_path = store.path("certificates/huawei_root_ca_trust.json")
    return (
        material,
        ca_path if ca_path.is_file() else None,
        store.read_child_materials(),
    )


def _remove_gateway_storage(config_dir: str, serial: str) -> None:
    """Remove one gateway's storage outside Home Assistant's event loop."""

    GatewayStore(config_dir, serial).remove_gateway()


def _build_plan_from_subentries(entry: ConfigEntry):
    """Compile the child plan from UI subentries; None when absent/invalid.

    Returns (plan, error) where plan is None with error set only when a
    stored subentry is invalid; (None, None) means "no child devices yet".
    """

    subentries = getattr(entry, "subentries", None) or {}
    if not subentries:
        return None, None
    # HA stores subentries as a mapping keyed by subentry_id. Keep a
    # list-compatible fallback for older HA releases/test doubles.
    values = subentries.values() if hasattr(subentries, "values") else subentries
    try:
        return (
            plan_from_subentries(entry.data.get("serial"), values),
            None,
        )
    except (PlanBuilderError, AttributeError, TypeError, ValueError) as error:
        return None, PlanBuilderError(f"invalid child subentry data: {error}")


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    await async_get_translations(
        hass,
        hass.config.language,
        "exceptions",
        integrations={DOMAIN},
    )
    data = hass.data.setdefault(
        DOMAIN,
        {
            "manager": GatewayManager(),
            "runtimes": {},
            "forwarded_entries": set(),
            "reload_callbacks": {},
        },
    )
    if not hass.services.has_service(DOMAIN, "start_pairing"):
        async def start_pairing(call) -> None:
            serial = call.data["serial"]
            runtime = data["manager"].get(serial)
            if runtime is None:
                raise HomeAssistantError(
                    translation_domain=DOMAIN,
                    translation_key="unknown_gateway",
                    translation_placeholders={"serial": serial},
                )
            await hass.async_add_executor_job(runtime.start_pairing)

        hass.services.async_register(
            DOMAIN,
            "start_pairing",
            start_pairing,
            schema=vol.Schema({vol.Required("serial"): vol.Coerce(str)}),
        )
    return True


async def _restore_legacy_children(
    hass: HomeAssistant, entry: ConfigEntry, serial: str
) -> None:
    """Recreate child subentries stored under the pre-rename domain, once."""

    if _child_subentries(entry):
        return
    payloads = await hass.async_add_executor_job(
        legacy_child_payloads, hass.config.path(), serial
    )
    if not payloads:
        return
    for payload in payloads:
        try:
            subentry = ConfigSubentry(
                title=payload["title"],
                data=payload["data"],
                subentry_type="child",
                unique_id=payload["unique_id"],
                subentry_id=payload["subentry_id"] or ulid_util.ulid_now(),
            )
            # async_add_subentry is a sync @callback, not a coroutine.
            hass.config_entries.async_add_subentry(entry, subentry)
        except Exception as error:  # noqa: BLE001 - a single child must not block setup
            _LOGGER.warning(
                "Unable to restore legacy child %s: %s", payload["title"], error
            )
    _LOGGER.info(
        "Restored %d child devices from the pre-rename entry for gateway %s",
        len(payloads),
        serial,
    )


def _child_subentries(entry: ConfigEntry) -> list:
    """Return the child-device subentries stored on one config entry."""

    subentries = getattr(entry, "subentries", None) or {}
    values = subentries.values() if hasattr(subentries, "values") else subentries
    return [
        item
        for item in values
        if getattr(item, "subentry_type", "child") == "child"
    ]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    data = hass.data.setdefault(
        DOMAIN,
        {
            "manager": GatewayManager(),
            "runtimes": {},
            "forwarded_entries": set(),
            "reload_callbacks": {},
        },
    )
    notification_translations = await async_get_translations(
        hass,
        hass.config.language,
        "common",
        integrations={DOMAIN},
    )

    def create_notification(
        key: str,
        notification_id: str,
        **placeholders: str,
    ) -> None:
        prefix = f"component.{DOMAIN}.common.{key}"
        message_template = notification_translations.get(f"{prefix}_message")
        title_template = notification_translations.get(f"{prefix}_title")
        # A missing optional translation must not abort integration setup.
        if message_template is None or title_template is None:
            _LOGGER.error("Missing notification translation for %s", key)
            title_template = title_template or "HA HW Bridge"
            message_template = message_template or "Configuration error: {error}"
        persistent_notification.async_create(
            hass,
            message_template.format(**placeholders),
            title=title_template.format(**placeholders),
            notification_id=notification_id,
        )

    config = GatewayConfig(
        config_dir=hass.config.path(),
        interface_ip=entry.options.get("interface_ip", entry.data["interface_ip"]),
        mac=entry.options.get("mac", entry.data["mac"]),
        serial=entry.data["serial"],
        enable_trace=bool(
            entry.options.get(
                "enable_trace",
                entry.data.get("enable_trace", False),
            )
        ),
    )
    try:
        runtime = data["manager"].create(config)
    except GatewayLimitError as error:
        create_notification(
            "gateway_limit",
            notification_id=f"{DOMAIN}_gateway_limit",
            limit=str(MAX_GATEWAY_INSTANCES),
            error=str(error),
        )
        raise HomeAssistantError(
            translation_domain=DOMAIN,
            translation_key="gateway_limit",
            translation_placeholders={"limit": str(MAX_GATEWAY_INSTANCES)},
        ) from error
    persistent_notification.async_dismiss(hass, f"{DOMAIN}_gateway_limit")
    data["runtimes"][entry.entry_id] = runtime

    # Adopting a pre-rename serial leaves its child devices on the old entry.
    # Recreate them before the first plan is compiled so nothing re-registers
    # as a brand-new cloud child.
    if entry.data.get(CONF_REUSE_SERIAL):
        await _restore_legacy_children(hass, entry, runtime.serial)
        entry = hass.config_entries.async_get_entry(entry.entry_id) or entry

    # Child devices come from UI subentries only; there is no YAML source.
    gateway_plan, subentry_error = _build_plan_from_subentries(entry)
    plan_notification_id = f"{DOMAIN}_{runtime.serial}_plan_error"
    if subentry_error is not None:
        _LOGGER.error(
            "Invalid stored child devices for %s: %s",
            runtime.serial,
            subentry_error,
        )
        create_notification(
            "plan_invalid",
            notification_id=plan_notification_id,
            serial=runtime.serial,
            error=str(subentry_error),
        )
    else:
        persistent_notification.async_dismiss(hass, plan_notification_id)

    runtime.set_gateway_plan(gateway_plan)
    entity_bridge = HAEntityBridge(hass)
    runtime.set_entity_bridge(entity_bridge)

    def install_state_listeners(plan) -> None:
        old_state_remover = data.setdefault("state_removers", {}).pop(entry.entry_id, None)
        if old_state_remover is not None:
            old_state_remover()
        old_startup_remover = data.setdefault("startup_sync_removers", {}).pop(
            entry.entry_id, None
        )
        if old_startup_remover is not None:
            old_startup_remover()
        if plan is not None:
            data["state_removers"][entry.entry_id] = entity_bridge.setup_state_listener(
                plan,
                runtime.enqueue_child_state,
            )
            data["startup_sync_removers"][entry.entry_id] = entity_bridge.schedule_startup_sync(
                plan,
                runtime.enqueue_child_state,
            )

    install_state_listeners(gateway_plan)
    if gateway_plan is None:
        _LOGGER.debug("Gateway %s has no child devices configured yet", runtime.serial)
    else:
        _LOGGER.info(
            "Loaded %d child mappings for gateway %s",
            len(gateway_plan.children),
            runtime.serial,
        )

    async def reload_children() -> None:
        new_plan, subentry_error = _build_plan_from_subentries(entry)
        if subentry_error is not None:
            _LOGGER.error(
                "Gateway %s stored child devices are invalid: %s",
                runtime.serial,
                subentry_error,
            )
            raise HomeAssistantError(
                translation_domain=DOMAIN,
                translation_key="mapping_reload_failed",
                translation_placeholders={"error": str(subentry_error)},
            )
        persistent_notification.async_dismiss(hass, plan_notification_id)
        try:
            await hass.async_add_executor_job(runtime.reload_plan, new_plan)
        except Exception as error:  # noqa: BLE001 - button reports failure in logs
            _LOGGER.error("Gateway %s child mapping reload failed: %s", runtime.serial, error)
            raise HomeAssistantError(
                translation_domain=DOMAIN,
                translation_key="mapping_reload_failed",
                translation_placeholders={"error": str(error)},
            ) from error
        install_state_listeners(new_plan)
        _LOGGER.info("Gateway %s child mapping reload requested", runtime.serial)

    data.setdefault("reload_callbacks", {})[entry.entry_id] = reload_children
    forwarded_entries: set[str] = data.setdefault("forwarded_entries", set())
    has_bound_material = await hass.async_add_executor_job(runtime.has_bound_material)

    async def on_entry_update(hass: HomeAssistant, updated_entry: ConfigEntry) -> None:
        """Re-apply the child plan when subentries are added/edited/removed."""

        new_plan, build_error = _build_plan_from_subentries(updated_entry)
        if build_error is not None:
            create_notification(
                "plan_invalid",
                notification_id=plan_notification_id,
                serial=runtime.serial,
                error=str(build_error),
            )
            return
        persistent_notification.async_dismiss(hass, plan_notification_id)
        try:
            await hass.async_add_executor_job(runtime.reload_plan, new_plan)
        except Exception as error:  # noqa: BLE001 - listener must not raise
            _LOGGER.error(
                "Gateway %s child plan update failed: %s", runtime.serial, error
            )
            create_notification(
                "plan_invalid",
                notification_id=plan_notification_id,
                serial=runtime.serial,
                error=str(error),
            )
            return
        install_state_listeners(new_plan)
        _LOGGER.info(
            "Gateway %s child plan re-applied after subentry change",
            runtime.serial,
        )

    data.setdefault("update_listener_removers", {})[entry.entry_id] = (
        entry.add_update_listener(on_entry_update)
    )

    notification_id = f"{DOMAIN}_{runtime.serial}_pairing"

    def sync_pairing_notification() -> None:
        if runtime.status == "pairing" and runtime.pin:
            create_notification(
                "pairing",
                notification_id=notification_id,
                serial=runtime.serial,
                pin=runtime.pin,
            )
        else:
            persistent_notification.async_dismiss(hass, notification_id)

    async def forward_platforms() -> None:
        try:
            await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
        except Exception:
            forwarded_entries.discard(entry.entry_id)
            _LOGGER.exception(
                "Unable to create HA HW Bridge entities for %s",
                runtime.serial,
            )

    def schedule_platforms_if_online() -> None:
        if (
            not has_bound_material
            and runtime.status != "online"
        ) or entry.entry_id in forwarded_entries:
            return
        forwarded_entries.add(entry.entry_id)
        hass.async_create_task(forward_platforms())

    def on_runtime_change() -> None:
        def update_on_loop() -> None:
            sync_pairing_notification()
            schedule_platforms_if_online()

        hass.loop.call_soon_threadsafe(update_on_loop)

    data.setdefault("notification_removers", {})[entry.entry_id] = runtime.add_listener(
        on_runtime_change
    )
    await hass.async_add_executor_job(runtime.start)
    sync_pairing_notification()
    schedule_platforms_if_online()
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unloaded = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if not unloaded:
        return False
    data = hass.data[DOMAIN]
    data.get("forwarded_entries", set()).discard(entry.entry_id)
    data.get("reload_callbacks", {}).pop(entry.entry_id, None)
    listener_remover = data.get("update_listener_removers", {}).pop(entry.entry_id, None)
    if listener_remover is not None:
        listener_remover()
    state_remover = data.get("state_removers", {}).pop(entry.entry_id, None)
    if state_remover is not None:
        state_remover()
    startup_sync_remover = data.get("startup_sync_removers", {}).pop(entry.entry_id, None)
    if startup_sync_remover is not None:
        startup_sync_remover()
    runtime: GatewayRuntime | None = data["runtimes"].pop(entry.entry_id, None)
    if runtime is not None:
        remover = data.get("notification_removers", {}).pop(entry.entry_id, None)
        if remover is not None:
            remover()
        await hass.async_add_executor_job(runtime.stop)
        persistent_notification.async_dismiss(
            hass, f"{DOMAIN}_{runtime.serial}_pairing"
        )
        persistent_notification.async_dismiss(
            hass, f"{DOMAIN}_{runtime.serial}_plan_error"
        )
        data["manager"].remove(runtime)
    return True


async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Remove this gateway's persisted identity and runtime materials."""

    serial = entry.data.get("serial")
    if not isinstance(serial, str) or not serial:
        return
    data = hass.data.get(DOMAIN)
    if data is not None:
        data.get("forwarded_entries", set()).discard(entry.entry_id)
        data.get("reload_callbacks", {}).pop(entry.entry_id, None)
        listener_remover = data.get("update_listener_removers", {}).pop(
            entry.entry_id, None
        )
        if listener_remover is not None:
            listener_remover()
        state_remover = data.get("state_removers", {}).pop(entry.entry_id, None)
        if state_remover is not None:
            state_remover()
        startup_sync_remover = data.get("startup_sync_removers", {}).pop(entry.entry_id, None)
        if startup_sync_remover is not None:
            startup_sync_remover()
        runtime: GatewayRuntime | None = data.get("runtimes", {}).pop(entry.entry_id, None)
        if runtime is not None:
            await hass.async_add_executor_job(runtime.stop)
            data["manager"].remove(runtime)
        remover = data.get("notification_removers", {}).pop(entry.entry_id, None)
        if remover is not None:
            remover()
        persistent_notification.async_dismiss(
            hass, f"{DOMAIN}_{serial}_pairing"
        )
        persistent_notification.async_dismiss(
            hass, f"{DOMAIN}_{serial}_plan_error"
        )

    material, ca_path, child_materials = await hass.async_add_executor_job(
        _read_gateway_removal_material,
        hass.config.path(),
        serial,
    )
    mac = entry.data.get("mac")
    if (
        material
        and isinstance(mac, str)
        and isinstance(material.get("devId"), str)
        and isinstance(material.get("secret"), str)
        and isinstance(material.get("cloudPrimaryUrl"), str)
    ):
        client = ChildCleanupClient(
            serial_number=serial,
            mac=mac,
            cloud_primary_url=material["cloudPrimaryUrl"],
            cloud_standby_url=(
                material.get("cloudStandbyUrl")
                if isinstance(material.get("cloudStandbyUrl"), str)
                else None
            ),
            ca_json=ca_path,
        )
        try:
            result = await hass.async_add_executor_job(
                client.remove_children_then_revoke,
                material,
                child_materials,
            )
            if result.failed:
                _LOGGER.warning(
                    "Gateway %s was revoked, but child cloud deletion failed for: %s",
                    serial,
                    ", ".join(result.failed),
                )
            else:
                _LOGGER.info(
                    "Gateway %s child devices deleted before parent revoke: %d",
                    serial,
                    len(result.deleted),
                )
        except Exception as error:  # noqa: BLE001 - local deletion must finish
            _LOGGER.warning(
                "Gateway %s cloud child cleanup/revoke failed during HA removal; local materials "
                "will still be deleted: %s",
                serial,
                error,
            )
    await hass.async_add_executor_job(
        _remove_gateway_storage,
        hass.config.path(),
        serial,
    )


async def async_migrate_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Migrate old config entries to the subentry-only schema."""

    if entry.version > 3:
        # Downgrades are not supported; keep the entry as-is.
        return True
    if entry.version < 3:
        # Version 2 stored children without a stable ``key``. Pin each child to
        # its subentry id so the plan builder keeps reusing the same cloud child
        # identity. New entries already persist a key, so nothing changes there.
        subentries = getattr(entry, "subentries", None) or {}
        values = subentries.values() if hasattr(subentries, "values") else subentries
        for subentry in values:
            data = dict(subentry.data)
            if isinstance(data.get("key"), str) and data["key"]:
                continue
            data["key"] = subentry.subentry_id
            hass.config_entries.async_update_subentry(
                entry, subentry, data=data
            )
        hass.config_entries.async_update_entry(entry, version=3, minor_version=1)
        _LOGGER.info("Migrated HA HW Bridge entry %s to version 3", entry.title)
    return True