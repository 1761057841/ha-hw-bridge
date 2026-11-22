"""Huawei ``battery`` read-only adapter for battery-powered sensors."""

from __future__ import annotations

import math

from ..models import ServiceRef


class BatteryServiceAdapter:
    service_id = "battery"
    entity_domains = ("sensor", "binary_sensor")
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "battery":
            raise ValueError("battery requires st: battery")
        unknown = set(dict(service.contract)) - {"field"}
        if unknown:
            raise ValueError(f"battery has unsupported contract keys: {', '.join(sorted(unknown))}")
        field = service.contract_value("field", "level")
        if not isinstance(field, str) or not field:
            raise ValueError("battery contract field must be non-empty text")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError("battery requires exactly one sensor or binary_sensor entity")
        if not entity_ids[0].startswith(("sensor.", "binary_sensor.")):
            raise ValueError("battery requires a sensor or binary_sensor entity")

    async def read_state(self, hass, service: ServiceRef, entity_ids: tuple[str, ...]) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        # A binary_sensor reports presence, not a percentage: on = ok, off = low.
        if entity_ids[0].startswith("binary_sensor."):
            if state.state == "on":
                return {str(service.contract_value("field", "level")): 100}
            if state.state == "off":
                return {str(service.contract_value("field", "level")): 0}
            return {}
        try:
            level = float(state.state)
        except (TypeError, ValueError):
            return {}
        if not math.isfinite(level) or not 0 <= level <= 100:
            return {}
        return {str(service.contract_value("field", "level")): level}

    async def apply_command(self, hass, service: ServiceRef, entity_ids: tuple[str, ...], payload: dict[str, object]) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)


ADAPTER = BatteryServiceAdapter()