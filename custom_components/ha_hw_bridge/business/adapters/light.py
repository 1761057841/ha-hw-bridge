"""Huawei ``light`` service on appliances (range hood light, mirror light).

``light`` is a boolean light on an appliance: 189 of the 207 Profiles carry a
single ``on`` characteristic, some use ``light`` or ``value`` instead.

It is the same shape as ``lightSwitch`` but sits on its own serviceType, and
some Profiles add a brightness characteristic. That is why it is a separate
adapter rather than a registry alias.

contract
    field : characteristic name (default ``on``; ``light``, ``value`` accepted)
    swap  : bool, mirror an entity that means "off"
"""

from __future__ import annotations

from ..models import ServiceRef

_FIELDS = ("on", "light", "value")


class LightServiceAdapter:
    service_id = "light"
    service_type = "light"
    entity_domains = ("light", "switch", "binary_sensor", "input_boolean")
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "light":
            raise ValueError("light requires st: light")
        unknown = set(dict(service.contract)) - {"field", "swap"}
        if unknown:
            raise ValueError(
                f"light has unsupported contract keys: {', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field")
        if field is not None and (not isinstance(field, str) or not field):
            raise ValueError("light contract field must be non-empty text")
        if not isinstance(service.contract_value("swap", False), bool):
            raise ValueError("light contract swap must be boolean")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError("light requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in self.entity_domains:
            raise ValueError("light requires a light, switch or binary_sensor entity")

    @staticmethod
    def _field(service: ServiceRef) -> str:
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
        if state.state not in {"on", "off"}:
            return {}
        enabled = state.state == "on"
        if bool(service.contract_value("swap", False)):
            enabled = not enabled
        return {self._field(service): enabled}

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        field = self._field(service)
        raw = payload.get(field)
        if raw is None:
            for alias in _FIELDS:
                if alias in payload:
                    raw = payload[alias]
                    break
        enabled = _as_bool(raw)
        if enabled is None:
            return
        if bool(service.contract_value("swap", False)):
            enabled = not enabled
        domain = entity_ids[0].partition(".")[0]
        await hass.services.async_call(
            domain,
            "turn_on" if enabled else "turn_off",
            {"entity_id": entity_ids[0]},
            blocking=True,
        )


def _as_bool(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str) and value in {"0", "1", "on", "off", "true", "false"}:
        return value in {"1", "on", "true"}
    return None


ADAPTER = LightServiceAdapter()