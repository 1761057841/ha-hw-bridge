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
        field = service.contract_value("field", "current")
        if not isinstance(field, str) or not field:
            raise ValueError("luminance contract field must be non-empty text")
        scale = service.contract_value("scale", 1)
        if isinstance(scale, bool) or not isinstance(scale, (int, float)):
            raise ValueError("luminance contract scale must be numeric")
        if not math.isfinite(float(scale)) or float(scale) <= 0:
            raise ValueError("luminance contract scale must be positive and finite")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1 or not entity_ids[0].startswith("sensor."):
            raise ValueError("luminance requires exactly one sensor entity")

    async def read_state(self, hass, service: ServiceRef, entity_ids: tuple[str, ...]) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        scale = float(service.contract_value("scale", 1))
        try:
            raw = float(state.state)
        except (TypeError, ValueError):
            return {}
        if not math.isfinite(raw):
            return {}
        value = raw * scale
        field = service.contract_value("field", "current")
        return {field: value} if math.isfinite(value) else {}

    async def apply_command(self, hass, service: ServiceRef, entity_ids: tuple[str, ...], payload: dict[str, object]) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)


ADAPTER = LuminanceServiceAdapter()