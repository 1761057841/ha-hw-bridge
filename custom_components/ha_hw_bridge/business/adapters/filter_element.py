"""Huawei consumable filters: remaining life of one filter element.

Vendors expose each filter as its own sid (``filterElement1`` … ``filterElement8``)
with a percentage of life left, an optional reset flag, and an optional alarm.

Profile evidence (5926 readable Profiles)
    filterElement1 : 130 devices — 14 carry ``leftPer``, 8 add ``reset``/``alarm``,
                     7 add ``name``, 6 carry all four

Read-only: a filter's remaining life is reported by the device, never written
by the app. ``reset`` is the only writable field and it is a momentary action,
so it maps to a ``button`` entity only when one is bound.

contract
    field : characteristic holding the percentage (default ``leftPer``)
    min/max : integer range of that characteristic (default 0..100)
"""

from __future__ import annotations

import math

from ..models import ServiceRef

_FIELDS = ("leftPer", "leftPercent", "percent", "level")


class FilterElementServiceAdapter:
    entity_domains = ("sensor", "input_number", "number")
    entity_counts = None

    def __init__(self, service_id: str) -> None:
        self.service_id = service_id
        # Every filterElementN is the same documented serviceShape.
        self.service_type = "filterElement"

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "filterElement":
            raise ValueError(f"{self.service_id} requires st: filterElement")
        unknown = set(dict(service.contract)) - {"field", "min", "max"}
        if unknown:
            raise ValueError(
                f"{self.service_id} has unsupported contract keys: "
                f"{', '.join(sorted(unknown))}"
            )
        _range(service)

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError(f"{self.service_id} requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in {"sensor", "input_number", "number"}:
            raise ValueError(f"{self.service_id} requires a sensor or number entity")

    def _field(self, service: ServiceRef) -> str:
        explicit = service.contract_value("field")
        if isinstance(explicit, str) and explicit:
            return explicit
        return _FIELDS[0]

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        try:
            value = float(state.state)
        except (TypeError, ValueError):
            return {}
        if not math.isfinite(value):
            return {}
        minimum, maximum = _range(service)
        clamped = int(round(min(max(value, minimum), maximum)))
        return {self._field(service): clamped}

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        # Read-only: the app never writes a filter's remaining life.
        self.validate_service(service)
        self.validate_entities(entity_ids)


def _range(service: ServiceRef) -> tuple[float, float]:
    for key in ("min", "max"):
        value = service.contract_value(key)
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{service.service_id} contract {key} must be a number")
    minimum = float(service.contract_value("min", 0))
    maximum = float(service.contract_value("max", 100))
    if minimum >= maximum:
        raise ValueError(f"{service.service_id} contract min must be smaller than max")
    return minimum, maximum


ADAPTER = FilterElementServiceAdapter("filterElement1")