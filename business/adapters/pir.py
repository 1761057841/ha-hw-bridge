"""Huawei ``pir`` presence status adapter for Profile 2RJB."""

from __future__ import annotations

from ..models import ServiceRef


class PirServiceAdapter:
    service_id = "pir"
    entity_domains = ("binary_sensor",)
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "status":
            raise ValueError("pir requires st: status")
        unknown = set(dict(service.contract)) - {"states", "fallback"}
        if unknown:
            raise ValueError(f"pir has unsupported contract keys: {', '.join(sorted(unknown))}")
        if not service.contract_value("states") and service.contract_value("fallback") is None:
            raise ValueError("pir requires states or fallback")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1 or not entity_ids[0].startswith("binary_sensor."):
            raise ValueError("pir requires exactly one binary_sensor entity")

    async def read_state(self, hass, service: ServiceRef, entity_ids: tuple[str, ...]) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        states = service.contract_value("states", {})
        if isinstance(states, dict) and state.state in states:
            return {"status": states[state.state]}
        fallback = service.contract_value("fallback")
        return {"status": fallback} if isinstance(fallback, int) else {}

    async def apply_command(self, hass, service: ServiceRef, entity_ids: tuple[str, ...], payload: dict[str, object]) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)


ADAPTER = PirServiceAdapter()
