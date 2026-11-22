"""Huawei ``gear`` services: a discrete level (sensitivity, fan gear, power gear).

Unlike ``fan`` (which is an air-conditioner gear tied to ``climate.fan_mode``),
``gear`` appears on sensors and appliances as a plain level setting: radar
sensitivity on a presence sensor, suction power on a vacuum, water temperature
on a bidet.

Profile evidence
    ``2RJB`` / ``2Q8M`` — ``sensitivity`` carries ``gear`` / ``radarGear`` enums, RW
    ``9MZV``          — ``gear`` carries a single ``gear`` enum, RW

The enum values are device specific, so they are never guessed: bind an
``input_select`` and map the Profile's own values with ``contract.values``.

contract
    field  : characteristic name (default ``gear``; ``radarGear``, ``powerGear``
             are accepted aliases)
    values : HA option -> Huawei enum value
    step   : optional int reported as the gear count instead of an enum
"""

from __future__ import annotations

from ..models import ServiceRef

_FIELDS = ("gear", "radarGear", "powerGear", "sensitivity")


class GearServiceAdapter:
    service_id = "gear"
    service_type = "gear"
    entity_domains = ("input_select", "select", "input_number", "number", "sensor")
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "gear":
            raise ValueError("gear requires st: gear")
        unknown = set(dict(service.contract)) - {"field", "values", "step"}
        if unknown:
            raise ValueError(
                f"gear has unsupported contract keys: {', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field")
        if field is not None and (not isinstance(field, str) or not field):
            raise ValueError("gear contract field must be non-empty text")
        _values(service)

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError("gear requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in self.entity_domains:
            raise ValueError("gear requires a select, number or sensor entity")

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
        field = self._field(service)
        values = _values(service)
        if values and state.state in values:
            return {field: values[state.state]}
        if not values:
            number = _int(state.state)
            if number is not None:
                return {field: number}
        return {}

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
        value = _int(raw)
        if value is None:
            return
        domain = entity_ids[0].partition(".")[0]
        if domain in {"input_number", "number"}:
            await hass.services.async_call(
                domain,
                "set_value",
                {"entity_id": entity_ids[0], "value": value},
                blocking=True,
            )
            return
        if domain in {"input_select", "select"}:
            reverse = {enum: name for name, enum in _values(service).items()}
            option = reverse.get(value)
            if option is None:
                return
            state = hass.states.get(entity_ids[0])
            options = state.attributes.get("options") if state else None
            if isinstance(options, list) and options and option not in options:
                return
            await hass.services.async_call(
                domain,
                "select_option",
                {"entity_id": entity_ids[0], "option": option},
                blocking=True,
            )


def _values(service: ServiceRef) -> dict[str, int]:
    raw = service.contract_value("values")
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ValueError("gear contract values must be a mapping")
    result: dict[str, int] = {}
    for name, value in raw.items():
        if not isinstance(name, str) or not name:
            raise ValueError("gear contract values keys must be non-empty text")
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("gear contract values must be integers")
        result[name] = value
    return result


def _int(value: object) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        try:
            return int(float(value))
        except (TypeError, ValueError):
            return None
    return None


ADAPTER = GearServiceAdapter()