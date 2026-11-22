"""Huawei ``luminance`` read-only measurement adapter."""

from __future__ import annotations

import math

from ..models import ServiceRef


class LuminanceServiceAdapter:
    service_id = "luminance"
    entity_domains = ("sensor",)
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "luminance":
            raise ValueError("luminance requires st: luminance")
        unknown = set(dict(service.contract)) - {"field", "scale"}
        if unknown:
            raise ValueError(f"luminance has unsupported contract keys: {', '.join(sorted(unknown))}")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1 or not entity_ids[0].startswith("sensor."):
            raise ValueError("luminance requires exactly one sensor entity")

    async def read_state(self, hass, service: ServiceRef, entity_ids: tuple[str, ...]) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        try:
            value = float(state.state) * float(service.contract_value("scale", 1))
        except (TypeError, ValueError, OverflowError):
            return {}
        field = service.contract_value("field", "current")
        return {field: value} if isinstance(field, str) and math.isfinite(value) else {}

    async def apply_command(self, hass, service: ServiceRef, entity_ids: tuple[str, ...], payload: dict[str, object]) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)


ADAPTER = LuminanceServiceAdapter()
