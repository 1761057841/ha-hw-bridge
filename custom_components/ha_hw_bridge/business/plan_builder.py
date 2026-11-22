"""Build a runtime ``GatewayPlan`` from config-entry subentries.

Each child device added through the UI is stored as one subentry whose
``data`` holds everything: the product identity fields at the top level
and ``services``/``bindings`` lists beside them. This module is the
single place that translates that UI shape into the frozen ``models``
objects consumed by ``ChildManager``.
"""

from __future__ import annotations

from typing import Any

from ..const import MAX_CHILD_DEVICES_PER_GATEWAY
from .adapters import get_adapter_for_service, get_service_adapter
from .models import ChildPlan, GatewayPlan, ProductSpec, ServiceBinding, ServiceRef

# Child keys become storage directory names and cloud child identities.
_KEY_CHARS = frozenset(
    "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-"
)


class PlanBuilderError(ValueError):
    """Raised when stored subentry data cannot build a valid child plan."""


def product_from_subentry(data: dict[str, Any]) -> ProductSpec:
    """Read the product identity stored in a subentry's ``data``."""

    try:
        return ProductSpec(
            prod_id=str(data["prod_id"]),
            sub_prod_id=str(data.get("sub_prod_id", "")),
            device_type=str(data["device_type"]),
            manufacturer=str(data["manufacturer"]),
            model=str(data["model"]),
            protocol_type=int(data["protocol_type"]),
            setup_type=int(data["setup_type"]),
            friendly_name=(
                str(data["friendly_name"])
                if data.get("friendly_name") is not None
                else None
            ),
            known_fields_only=bool(data.get("known_fields_only", False)),
        )
    except (KeyError, TypeError, ValueError) as error:
        raise PlanBuilderError(f"child identity is incomplete: {error}") from error


def room_from_subentry(data: dict[str, Any]) -> str | None:
    value = data.get("room")
    if value is None:
        return None
    if not isinstance(value, str):
        raise PlanBuilderError("room must be text when present")
    return value


def key_from_subentry(data: dict[str, Any], fallback: str | None = None) -> str:
    """Read the stable child key, falling back to the subentry id.

    New subentries always persist ``key``. The fallback keeps entries created
    before the key existed usable even if the version-3 migration could not
    write them back; it is stable because a subentry id never changes.
    """

    key = data.get("key") or fallback
    if not isinstance(key, str) or not key:
        raise PlanBuilderError("child key is missing; re-add this child device")
    if any(char not in _KEY_CHARS for char in key):
        raise PlanBuilderError(f"child key {key!r} contains an unsafe character")
    return key


def services_from_subentry(data: dict[str, Any]) -> tuple[ServiceRef, ...]:
    """Read the enabled services stored in a subentry's ``data``."""

    services: list[ServiceRef] = []
    seen: set[str] = set()
    for raw in data.get("services") or []:
        if not isinstance(raw, dict):
            raise PlanBuilderError("each service entry must be a mapping")
        service_type = raw.get("st")
        service_id = raw.get("sid")
        if not isinstance(service_type, str) or not service_type:
            raise PlanBuilderError("service entry is missing st")
        if not isinstance(service_id, str) or not service_id:
            raise PlanBuilderError("service entry is missing sid")
        if service_id in seen:
            raise PlanBuilderError(f"service {service_id} is selected twice")
        contract_raw = raw.get("contract") or {}
        if not isinstance(contract_raw, dict):
            raise PlanBuilderError(f"service {service_id} contract must be a mapping")
        # Repair the sid-in-``st`` mistake made by earlier UI flows: st and sid
        # are different Profile fields, and a wrong st invalidates the service.
        # A Profile's ``st`` is authoritative: many vendor sids share one
        # serviceType, so resolve the adapter by (sid, serviceType).
        try:
            adapter = get_adapter_for_service(service_id, service_type)
        except ValueError as error:
            raise PlanBuilderError(str(error)) from error
        canonical_type = getattr(adapter, "service_type", None)
        if isinstance(canonical_type, str) and canonical_type != service_type:
            service_type = canonical_type
        contract = tuple(contract_raw.items())
        service = ServiceRef(service_type, service_id, contract)
        try:
            adapter.validate_service(service)
        except ValueError as error:
            raise PlanBuilderError(
                f"service {service_id} is invalid: {error}"
            ) from error
        seen.add(service_id)
        services.append(service)
    return tuple(services)


def bindings_from_subentry(data: dict[str, Any]) -> tuple[ServiceBinding, ...]:
    """Read the entity bindings stored in a subentry's ``data``."""

    bindings: list[ServiceBinding] = []
    seen: set[str] = set()
    for raw in data.get("bindings") or []:
        if not isinstance(raw, dict):
            raise PlanBuilderError("each binding entry must be a mapping")
        service_id = raw.get("sid")
        entity_ids = raw.get("entities")
        if not isinstance(service_id, str) or not service_id:
            raise PlanBuilderError("binding entry is missing sid")
        if service_id in seen:
            raise PlanBuilderError(f"service {service_id} is bound twice")
        if not isinstance(entity_ids, list) or not entity_ids:
            raise PlanBuilderError(
                f"binding {service_id} must contain non-empty entities"
            )
        if any(
            not isinstance(entity_id, str) or not entity_id
            for entity_id in entity_ids
        ):
            raise PlanBuilderError(
                f"binding {service_id} must contain non-empty entities"
            )
        # Older UI flow versions called list() on a single selector string,
        # persisting an entity ID as one-character strings. Repair that shape
        # when it is unambiguous instead of making the gateway unusable.
        if len(entity_ids) > 1 and all(len(item) == 1 for item in entity_ids):
            repaired = "".join(entity_ids)
            if "." in repaired:
                entity_ids = [repaired]
        seen.add(service_id)
        bindings.append(ServiceBinding(service_id, tuple(entity_ids)))
    return tuple(bindings)


def child_from_subentry(subentry) -> ChildPlan:
    """Build one ``ChildPlan`` from a config subentry."""

    data = subentry.data
    key = key_from_subentry(data, fallback=getattr(subentry, "subentry_id", None))
    product = product_from_subentry(data)
    room = room_from_subentry(data)
    services = services_from_subentry(data)
    bindings = bindings_from_subentry(data)
    selected = {service.service_id for service in services}
    unknown = sorted({binding.service_id for binding in bindings} - selected)
    if unknown:
        raise PlanBuilderError(
            f"child {key} has bindings for unselected services: "
            f"{', '.join(unknown)}"
        )
    for binding in bindings:
        try:
            get_service_adapter(binding.service_id).validate_entities(
                binding.entity_ids
            )
        except ValueError as error:
            raise PlanBuilderError(
                f"child {key} service {binding.service_id} is invalid: {error}"
            ) from error
    return ChildPlan(
        key=key,
        product=product,
        room=room,
        services=services,
        bindings=bindings,
    )


def plan_from_subentries(
    gateway_serial: str | None, subentries
) -> GatewayPlan:
    """Build the merged runtime plan from every child subentry."""

    children: list[ChildPlan] = []
    seen_keys: set[str] = set()
    for subentry in subentries:
        child = child_from_subentry(subentry)
        if child.key in seen_keys:
            raise PlanBuilderError(f"child key {child.key} is used by two devices")
        seen_keys.add(child.key)
        children.append(child)
    if len(children) > MAX_CHILD_DEVICES_PER_GATEWAY:
        raise PlanBuilderError(
            f"{len(children)} child devices are configured; "
            f"the maximum is {MAX_CHILD_DEVICES_PER_GATEWAY}"
        )
    return GatewayPlan(gateway_serial=gateway_serial, children=tuple(children))