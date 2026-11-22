"""Huawei ``lightMode`` / ``colourMode`` enum services for lights.

Profile evidence (catalogue ``ver_202609_hmos``, 5926 readable Profiles)
    lightMode  : 264 devices, 259 carry a single ``mode`` enum
                 (0 未开启 / 1 暖光 / 2 日光 / 3 冷光 / 4 夜灯 / 5 舒适 …)
    colourMode : 206 devices, 201 carry a single ``mode`` enum
    方向       : ``RW`` on every Profile

Both are the same shape: one enum characteristic named ``mode``. The enum is
device specific, so it is never guessed here — bind an ``input_select`` (or a
``light`` for a coarse preset) and map the Profile's own values with
``contract.values``.

contract
    values  : HA state -> Profile enum value, e.g. ``{warm: 1, daylight: 2}``
    field   : characteristic name, default ``mode`` (aliases ``lightMode``,
              ``colourMode``, ``status``)
    fallback: optional value reported when the HA state has no mapping
"""

from __future__ import annotations

from ..models import ServiceRef

_FIELDS = {
    "lightMode": ("mode", "lightMode"),
    "colourMode": ("mode", "colourMode"),
}
_DEFAULT_FIELDS = ("mode", "lightMode", "colourMode", "status")


class LightModeServiceAdapter:
    entity_domains = ("light", "input_select", "select", "sensor")
    entity_counts = None

    def __init__(self, service_id: str) -> None:
        self.service_id = service_id

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "mode":
            raise ValueError(f"{self.service_id} requires st: mode")
        unknown = set(dict(service.contract)) - {"values", "field", "fallback"}
        if unknown:
            raise ValueError(
                f"{self.service_id} has unsupported contract keys: "
                f"{', '.join(sorted(unknown))}"
            )
        _values(service)
        field = service.contract_value("field")
        if field is not None and (not isinstance(field, str) or not field):
            raise ValueError(f"{self.service_id} contract field must be non-empty text")
        fallback = service.contract_value("fallback")
        if fallback is not None and (
            isinstance(fallback, bool) or not isinstance(fallback, int)
        ):
            raise ValueError(f"{self.service_id} contract fallback must be an integer")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError(f"{self.service_id} requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in {"light", "input_select", "select", "sensor"}:
            raise ValueError(
                f"{self.service_id} requires a light, input_select, select or "
                "sensor entity"
            )

    def _field(self, service: ServiceRef) -> str:
        explicit = service.contract_value("field")
        if isinstance(explicit, str) and explicit:
            return explicit
        for candidate in _FIELDS.get(self.service_id, _DEFAULT_FIELDS):
            return candidate
        return "mode"

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        values = _values(service)
        if state.state in values:
            return {self._field(service): values[state.state]}
        fallback = service.contract_value("fallback")
        if isinstance(fallback, int):
            return {self._field(service): fallback}
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
            raw = payload.get("mode")
        value = _wire_int(raw)
        if value is None:
            return
        reverse = {enum: name for name, enum in _values(service).items()}
        target = reverse.get(value)
        if target is None:
            return
        domain = entity_ids[0].partition(".")[0]
        if domain in {"input_select", "select"}:
            state = hass.states.get(entity_ids[0])
            options = state.attributes.get("options") if state else None
            if isinstance(options, list) and options and target not in options:
                return
            await hass.services.async_call(
                domain,
                "select_option",
                {"entity_id": entity_ids[0], "option": target},
                blocking=True,
            )
            return
        if domain == "light":
            # A light has no preset states; only on/off is meaningful.
            if target in {"on", "off"}:
                await hass.services.async_call(
                    "light",
                    "turn_on" if target == "on" else "turn_off",
                    {"entity_id": entity_ids[0]},
                    blocking=True,
                )


def _values(service: ServiceRef) -> dict[str, int]:
    raw = service.contract_value("values")
    if raw is None:
        return {}
    if not isinstance(raw, dict):
        raise ValueError("mode contract values must be a mapping")
    result: dict[str, int] = {}
    for name, value in raw.items():
        if not isinstance(name, str) or not name:
            raise ValueError("mode contract values keys must be non-empty text")
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("mode contract values must be integers")
        result[name] = value
    if len(set(result.values())) != len(result):
        raise ValueError("mode contract values must be unique")
    return result


def _wire_int(value: object) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return None


ADAPTER = LightModeServiceAdapter("lightMode")