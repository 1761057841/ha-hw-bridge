from __future__ import annotations

import logging
import re
import secrets
import socket
from typing import Any

import psutil
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.selector import EntitySelector, EntitySelectorConfig

from .business.product_templates import PRESET_PRODUCTS, resolve_template
from .const import (
    CONF_ENABLE_TRACE,
    CONF_INTERFACE_IP,
    CONF_MAC,
    CONF_REUSE_SERIAL,
    CONF_SERIAL,
    DOMAIN,
    MAX_CHILD_DEVICES_PER_GATEWAY,
)

SUBENTRY_TYPE_CHILD = "child"
_LOGGER = logging.getLogger(__name__)


def _interface_options() -> dict[str, str]:
    options: dict[str, str] = {}
    for name, addresses in psutil.net_if_addrs().items():
        for address in addresses:
            if address.family != socket.AF_INET:
                continue
            if address.address.startswith("127."):
                continue
            options[address.address] = f"{name} — {address.address}"
    return options


def _interface_mac(interface_ip: str) -> str:
    for _name, addresses in psutil.net_if_addrs().items():
        ipv4 = {address.address for address in addresses if address.family == socket.AF_INET}
        if interface_ip not in ipv4:
            continue
        for address in addresses:
            if getattr(address.family, "name", "") in {"AF_LINK", "AF_PACKET"}:
                value = address.address.replace(":", "").replace("-", "").upper()
                if len(value) == 12:
                    return value
    raise ValueError(f"no MAC address found for interface {interface_ip}")


def _preset_labels() -> dict[str, str]:
    labels = {
        key: str(template["friendly_name"])
        for key, template in PRESET_PRODUCTS.items()
    }
    labels["custom"] = "Custom product (by prodId)"
    return labels


def _adapter_for(service_id: str):
    from .business.adapters import get_service_adapter

    return get_service_adapter(service_id)


def _service_type_for(service_id: str) -> str:
    """Return the Huawei serviceType for one sid.

    The two are not the same field: Profiles pair a vendor-defined ``sid``
    (``childLockSwitch``, ``lightMode``, ``leftAction`` …) with a documented
    ``st`` (``switch``, ``mode``, ``action`` …). Writing the sid into ``st``
    makes the service look like a different Profile service, and validation
    then rejects it.
    """

    return _adapter_for(service_id).service_type


def _service_multi_select(template: dict[str, Any]):
    services = template.get("services") or []
    choices = {
        str(item["sid"]): f"{item['st']} ({item['sid']})"
        for item in services
        if isinstance(item, dict) and item.get("sid")
    }
    return cv.multi_select(choices)


def _entity_field(service_id: str) -> str:
    """Return the form field name for one service, in HA's key format.

    Subentry form fields become translation keys, and Hassfest only allows
    ``[a-z0-9-_]``. Service ids such as ``airDetector`` are camelCase, so the
    field name is normalized; the stored binding keeps the real sid.
    """
    normalized = re.sub(r"[^a-zA-Z0-9]+", "_", service_id)
    normalized = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", normalized)
    return f"entity_{normalized.lower()}"


def _entity_selector_for(service_id: str):
    adapter = _adapter_for(service_id)
    counts = getattr(adapter, "entity_counts", None)
    multiple = bool(counts) and counts[1] > 1
    # EntitySelectorConfig is a TypedDict in HA core; construct a plain
    # mapping rather than calling the TypedDict class at runtime.
    selector_config: EntitySelectorConfig = {
        "domain": list(adapter.entity_domains),
        "multiple": multiple,
    }
    return EntitySelector(selector_config)


def _legacy_gateway_serials(config_dir: str) -> list[str]:
    """List serials paired under the pre-rename domain that can be reused."""

    from pathlib import Path

    from .const import LEGACY_DOMAINS

    result: list[str] = []
    for legacy in LEGACY_DOMAINS:
        root = Path(config_dir) / ".storage" / legacy / "gateways"
        if not root.is_dir():
            continue
        for child in sorted(root.iterdir()):
            if not child.is_dir():
                continue
            if (child / "cloud" / "material.json").is_file():
                result.append(child.name)
    return result


def _child_subentries(entry) -> list:
    subentries = getattr(entry, "subentries", None) or {}
    values = list(subentries.values()) if hasattr(subentries, "values") else list(subentries)
    return [
        item
        for item in values
        if getattr(item, "subentry_type", SUBENTRY_TYPE_CHILD) == SUBENTRY_TYPE_CHILD
    ]


class HAHWBridgeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle the gateway entry flow."""

    VERSION = 3
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        options = await self.hass.async_add_executor_job(_interface_options)
        if not options:
            return self.async_abort(reason="no_ipv4_interface")

        legacy_serials = await self.hass.async_add_executor_job(
            _legacy_gateway_serials, self.hass.config.path()
        )
        errors: dict[str, str] = {}
        if user_input is not None:
            interface_ip = user_input[CONF_INTERFACE_IP]
            reuse_serial = str(user_input.get(CONF_REUSE_SERIAL) or "").strip()
            try:
                mac = await self.hass.async_add_executor_job(
                    _interface_mac, interface_ip
                )
            except ValueError:
                errors[CONF_INTERFACE_IP] = "mac_not_found"
            else:
                serial = reuse_serial or secrets.token_hex(8).upper()
                if reuse_serial and reuse_serial not in legacy_serials:
                    errors[CONF_REUSE_SERIAL] = "unknown_legacy_serial"
                    serial = ""
                if serial:
                    await self.async_set_unique_id(serial)
                    self._abort_if_unique_id_configured()
                    return self.async_create_entry(
                        title=serial,
                        data={
                            CONF_INTERFACE_IP: interface_ip,
                            CONF_MAC: mac,
                            CONF_SERIAL: serial,
                            CONF_REUSE_SERIAL: bool(reuse_serial),
                        },
                    )

        schema_dict: dict[Any, Any] = {
            vol.Required(CONF_INTERFACE_IP): vol.In(options)
        }
        if legacy_serials:
            schema_dict[
                vol.Optional(CONF_REUSE_SERIAL, default="")
            ] = vol.In([""] + legacy_serials)
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(schema_dict),
            errors=errors,
        )

    @classmethod
    @callback
    def async_get_supported_subentry_types(cls, config_entry):
        """Expose the per-child-device subentry flow."""

        return {SUBENTRY_TYPE_CHILD: ChildDeviceSubentryFlow}

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        # HA's current OptionsFlow is initialized without positional args;
        # the linked entry is available later through self.config_entry.
        return HAHWBridgeOptionsFlow()


class ChildDeviceSubentryFlow(config_entries.ConfigSubentryFlow):
    """Add or reconfigure one child-device subentry."""

    async def async_step_user(self, user_input=None):
        """Entry point for the device page's "Add device" action."""

        entry = self._get_entry()
        if len(_child_subentries(entry)) >= MAX_CHILD_DEVICES_PER_GATEWAY:
            return self.async_abort(
                reason="child_limit",
                description_placeholders={
                    "limit": str(MAX_CHILD_DEVICES_PER_GATEWAY)
                },
            )
        return await self.async_step_child_product(user_input)

    async def async_step_child_product(self, user_input=None):
        """Step 1: pick the preset product or a custom identity."""

        errors: dict[str, str] = {}
        if user_input is not None:
            template_key = user_input["product_template"]
            if template_key == "custom":
                return await self.async_step_child_custom()
            template = resolve_template(template_key)
            if template is None:
                errors["product_template"] = "unknown_template"
            else:
                self.context["template"] = template
                self.context["template_key"] = template_key
                return await self.async_step_child_services()
        return self.async_show_form(
            step_id="child_product",
            data_schema=vol.Schema({
                vol.Required("product_template"): vol.In(_preset_labels()),
            }),
            errors=errors,
        )

    async def async_step_child_custom(self, user_input=None):
        """Advanced: type a full product identity by hand."""

        errors: dict[str, str] = {}
        if user_input is not None:
            prod_id = str(user_input.get("prod_id", "")).strip()
            if not prod_id:
                errors["prod_id"] = "required"
            else:
                self.context["template"] = {
                    "prod_id": prod_id,
                    "sub_prod_id": str(user_input.get("sub_prod_id", "")).strip(),
                    "device_type": str(user_input.get("device_type", "")).strip(),
                    "manufacturer": str(user_input.get("manufacturer", "002")).strip(),
                    "model": str(user_input.get("model", "")).strip(),
                    "friendly_name": (
                        str(user_input["friendly_name"]).strip()
                        if user_input.get("friendly_name")
                        else None
                    ),
                    "protocol_type": user_input.get("protocol_type", 6),
                    "setup_type": user_input.get("setup_type", 0),
                    "known_fields_only": user_input.get("known_fields_only", False),
                    "services": [],
                }
                return await self.async_step_child_custom_services()
        return self.async_show_form(
            step_id="child_custom",
            data_schema=vol.Schema({
                vol.Required("prod_id"): str,
                vol.Optional("sub_prod_id", default=""): str,
                vol.Required("device_type"): str,
                vol.Optional("manufacturer", default="002"): str,
                vol.Required("model"): str,
                vol.Optional("friendly_name"): str,
                vol.Required("protocol_type", default=6): vol.All(
                    vol.Coerce(int), vol.Range(min=0)
                ),
                vol.Optional("setup_type", default=0): vol.Coerce(int),
                vol.Optional("known_fields_only", default=False): bool,
            }),
            errors=errors,
        )

    async def async_step_child_custom_services(self, user_input=None):
        """Custom product: type one or more service ids (one per line)."""

        template = self.context.get("template")
        if template is None:
            return await self.async_step_child_product()

        errors: dict[str, str] = {}
        if user_input is not None:
            raw = str(user_input.get("service_ids", ""))
            service_ids = [line.strip() for line in raw.splitlines() if line.strip()]
            valid: list[str] = []
            invalid: list[str] = []
            for service_id in service_ids:
                try:
                    _adapter_for(service_id)
                except ValueError:
                    invalid.append(service_id)
                else:
                    valid.append(service_id)
            if invalid:
                errors["service_ids"] = "unknown_service"
            elif not valid:
                errors["service_ids"] = "no_services_selected"
            else:
                self.context["selected_services"] = valid
                template["services"] = [
                    {"st": _service_type_for(sid), "sid": sid}
                    for sid in valid
                ]
                return await self.async_step_child_entities()
        return self.async_show_form(
            step_id="child_custom_services",
            data_schema=vol.Schema({
                vol.Required("service_ids"): str,
            }),
            errors=errors,
        )

    async def async_step_child_services(self, user_input=None):
        """Step 2: choose the services of the selected product."""

        template = self.context.get("template")
        if template is None:
            return await self.async_step_child_product()
        if not template.get("services"):
            return await self.async_step_child_custom_services()

        errors: dict[str, str] = {}
        if user_input is not None:
            services = user_input.get("services") or []
            if isinstance(services, str):
                services = [services]
            if not services:
                errors["services"] = "no_services_selected"
            else:
                self.context["selected_services"] = list(services)
                return await self.async_step_child_entities()
        return self.async_show_form(
            step_id="child_services",
            description_placeholders={
                "prod_id": str(template["prod_id"]),
            },
            data_schema=vol.Schema({
                vol.Required("services"): _service_multi_select(template),
            }),
            errors=errors,
        )

    async def async_step_child_entities(self, user_input=None):
        """Step 3: bind each selected service to HA entities."""

        selected = self.context.get("selected_services") or []
        template = self.context.get("template")
        if not selected or template is None:
            return await self.async_step_child_product()

        errors: dict[str, str] = {}
        if user_input is not None:
            bindings: list[dict[str, Any]] = []
            for service_id in selected:
                entities = user_input.get(_entity_field(service_id))
                if not entities:
                    errors[_entity_field(service_id)] = "entity_required"
                    continue
                # EntitySelector returns a string for single selection and a
                # list only when multiple=True; normalize both shapes.
                entity_list = [entities] if isinstance(entities, str) else list(entities)
                try:
                    _adapter_for(service_id).validate_entities(tuple(entity_list))
                except ValueError as error:
                    _LOGGER.debug(
                        "Rejected entity binding sid=%s: %s", service_id, error
                    )
                    errors[_entity_field(service_id)] = "invalid_entities"
                    continue
                bindings.append({"sid": service_id, "entities": entity_list})
            if not errors:
                self.context["bindings"] = bindings
                return await self.async_step_child_details()
        schema_dict: dict[Any, Any] = {}
        try:
            for service_id in selected:
                schema_dict[
                    vol.Required(_entity_field(service_id))
                ] = _entity_selector_for(service_id)
        except ValueError:
            return await self.async_step_child_product()
        return self.async_show_form(
            step_id="child_entities",
            data_schema=vol.Schema(schema_dict),
            errors=errors,
        )

    async def async_step_child_details(self, user_input=None):
        """Step 4: friendly name, room, then create the subentry."""

        template = self.context.get("template")
        bindings = self.context.get("bindings")
        if template is None or bindings is None:
            return await self.async_step_child_product()

        if user_input is not None:
            name = str(user_input.get("friendly_name", "")).strip()
            room = str(user_input.get("room", "")).strip()
            if not name:
                name = str(template.get("friendly_name") or template["prod_id"])
            selected = self.context.get("selected_services") or []
            # The child key is generated once and never derived from the
            # display name, so renames keep the cloud child identity.
            key = secrets.token_hex(8).upper()
            data = {
                "key": key,
                "prod_id": str(template["prod_id"]),
                "sub_prod_id": str(template.get("sub_prod_id", "")),
                "device_type": str(template["device_type"]),
                "manufacturer": str(template["manufacturer"]),
                "model": str(template["model"]),
                "friendly_name": name,
                "protocol_type": template["protocol_type"],
                "setup_type": template.get("setup_type", 0),
                "known_fields_only": bool(template.get("known_fields_only", False)),
                "room": room or None,
                "services": [
                    dict(raw)
                    for raw in template.get("services", [])
                    if raw.get("sid") in selected
                ],
                "bindings": bindings,
            }
            # The entry's update listener re-applies the child plan once
            # async_add_subentry fires; no manual reload needed here.
            return self.async_create_entry(
                title=name, data=data, unique_id=f"child:{key}"
            )
        return self.async_show_form(
            step_id="child_details",
            description_placeholders={
                "prod_id": str(template["prod_id"]),
            },
            data_schema=vol.Schema({
                vol.Optional(
                    "friendly_name",
                    default=str(template.get("friendly_name") or ""),
                ): str,
                vol.Optional("room", default=""): str,
            }),
        )

    # ------------------------------------------------------------------
    # Reconfigure (edit an existing child device)
    # ------------------------------------------------------------------

    async def async_step_reconfigure(self, user_input=None):
        """Edit the entities and labels of an existing child-device subentry."""

        subentry = self._get_reconfigure_subentry()
        data = dict(subentry.data)
        bindings = {
            item["sid"]: list(item["entities"])
            for item in data.get("bindings", [])
            if isinstance(item, dict) and item.get("sid")
        }
        services = [
            item["sid"]
            for item in data.get("services", [])
            if isinstance(item, dict) and item.get("sid")
        ]

        errors: dict[str, str] = {}
        if user_input is not None:
            new_bindings: list[dict[str, Any]] = []
            for service_id in services:
                entities = user_input.get(_entity_field(service_id))
                if not entities:
                    errors[_entity_field(service_id)] = "entity_required"
                    continue
                entity_list = [entities] if isinstance(entities, str) else list(entities)
                try:
                    _adapter_for(service_id).validate_entities(tuple(entity_list))
                except ValueError as error:
                    _LOGGER.debug(
                        "Rejected entity binding sid=%s: %s", service_id, error
                    )
                    errors[_entity_field(service_id)] = "invalid_entities"
                    continue
                new_bindings.append({"sid": service_id, "entities": entity_list})
            name = str(user_input.get("friendly_name", "")).strip() or subentry.title
            room_input = str(user_input.get("room", "")).strip()
            room = room_input or None
            if not errors:
                data["bindings"] = new_bindings
                data["friendly_name"] = name
                data["room"] = room
                # Keep the stored child key stable; only repair legacy data.
                data.setdefault("key", subentry.subentry_id)
                entry = self._get_entry()
                # update_and_abort (not update_reload_and_abort): the entry
                # has an update listener that re-applies the child plan, and
                # _reload_ would raise for entries with listeners.
                return self.async_update_and_abort(
                    entry, subentry, data=data, title=name
                )
        schema_dict: dict[Any, Any] = {
            vol.Optional("friendly_name", default=subentry.title): str,
            vol.Optional("room", default=str(data.get("room") or "")): str,
        }
        try:
            for service_id in services:
                schema_dict[
                    vol.Required(
                        _entity_field(service_id),
                        default=bindings.get(service_id, []),
                    )
                ] = _entity_selector_for(service_id)
        except ValueError:
            errors["base"] = "unknown_service"
        return self.async_show_form(
            step_id="reconfigure",
            data_schema=vol.Schema(schema_dict),
            errors=errors,
        )


class HAHWBridgeOptionsFlow(config_entries.OptionsFlow):
    """Configure the gateway entry: pairing interface and cloud trace."""

    async def async_step_init(self, user_input=None):
        options = await self.hass.async_add_executor_job(_interface_options)
        entry = self.config_entry
        current_ip = entry.options.get(
            CONF_INTERFACE_IP, entry.data.get(CONF_INTERFACE_IP)
        )
        current_trace = bool(
            entry.options.get(
                CONF_ENABLE_TRACE, entry.data.get(CONF_ENABLE_TRACE, False)
            )
        )
        current_mac = entry.options.get(CONF_MAC, entry.data.get(CONF_MAC))
        if not options:
            return self.async_abort(reason="no_ipv4_interface")

        errors: dict[str, str] = {}
        if user_input is not None:
            interface_ip = user_input[CONF_INTERFACE_IP]
            try:
                mac = await self.hass.async_add_executor_job(
                    _interface_mac, interface_ip
                )
            except ValueError:
                errors[CONF_INTERFACE_IP] = "mac_not_found"
            else:
                # A plain OptionsFlow does not reload the entry; changing the
                # pairing interface only takes effect after a reload.
                if interface_ip != current_ip or mac != current_mac:
                    self.hass.config_entries.async_schedule_reload(entry.entry_id)
                return self.async_create_entry(
                    title="",
                    data={
                        CONF_INTERFACE_IP: interface_ip,
                        CONF_MAC: mac,
                        CONF_ENABLE_TRACE: bool(user_input.get(CONF_ENABLE_TRACE)),
                    },
                )
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Required(CONF_INTERFACE_IP, default=current_ip): vol.In(options),
                vol.Optional(
                    CONF_ENABLE_TRACE, default=current_trace
                ): bool,
            }),
            errors=errors,
        )