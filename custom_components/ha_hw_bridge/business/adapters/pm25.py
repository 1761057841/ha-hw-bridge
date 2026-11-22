"""Huawei ``pm25`` read-only measurement with an optional qualitative level.

Profile evidence (catalogue ``ver_202609_hmos``, 5926 readable Profiles)
    pm25     : 92 devices
               - 55 carry ``current`` + ``level``
               - 30 carry only ``current``
               - 3  use ``currentFloat``
               - 1  uses ``pm25`` + ``pm25Level``
    unit     : µg/m³, ``current`` range 0..1000, both characteristics ``R``
    verified : no — the shape is copied from the Profiles; a real projection is
               still required before promoting it out of "unverified".

The Profile never states the thresholds behind ``level`` (18 Profiles with a
level used 10 different enums), so the adapter never guesses it. Configure
``level_map`` exactly like the ``hcho`` adapter if the bound Profile declares a
level; leave it out for the 30 Profiles that only expose ``current``.

contract
    field     : characteristic holding the reading (default ``current``)
    scale     : multiplier applied to the HA value (default 1)
    min/max   : clamp range in µg/m³ (default 0 / 1000)
    level_map : list of ``{max, value}`` thresholds, ascending
"""

from __future__ import annotations

import math

from ..models import ServiceRef


class Pm25ServiceAdapter:
    service_id = "pm25"
    # Huawei serviceType from the Profile; it is not always the sid.
    service_type = "pm25"
    entity_domains = ("sensor",)
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "pm25":
            raise ValueError("pm25 requires st: pm25")
        unknown = set(dict(service.contract)) - {
            "field",
            "scale",
            "min",
            "max",
            "level_map",
        }
        if unknown:
            raise ValueError(
                f"pm25 has unsupported contract keys: {', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field", "current")
        if not isinstance(field, str) or not field:
            raise ValueError("pm25 contract field must be non-empty text")
        _limits(service)
        _levels(service)

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1 or not entity_ids[0].startswith("sensor."):
            raise ValueError("pm25 requires exactly one sensor entity")

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        try:
            number = float(state.state)
        except (TypeError, ValueError):
            return {}
        if not math.isfinite(number):
            return {}
        number *= float(service.contract_value("scale", 1))
        minimum, maximum = _limits(service)
        value = int(round(min(max(number, minimum), maximum)))
        payload: dict[str, object] = {str(service.contract_value("field", "current")): value}
        levels = _levels(service)
        if levels:
            payload["level"] = _level(levels, value)
        return payload

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        # ``current`` is read-only in every Profile; writes are meaningless.
        self.validate_service(service)
        self.validate_entities(entity_ids)


def _limits(service: ServiceRef) -> tuple[float, float]:
    for key in ("scale", "min", "max"):
        value = service.contract_value(key)
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"pm25 contract {key} must be a number")
    minimum = float(service.contract_value("min", 0))
    maximum = float(service.contract_value("max", 1000))
    if minimum >= maximum:
        raise ValueError("pm25 contract min must be smaller than max")
    scale = service.contract_value("scale", 1)
    if float(scale) <= 0:
        raise ValueError("pm25 contract scale must be positive")
    return minimum, maximum


def _levels(service: ServiceRef) -> tuple[tuple[float, int], ...] | None:
    raw = service.contract_value("level_map")
    if raw is None:
        return None
    if not isinstance(raw, (list, tuple)) or not raw:
        raise ValueError("pm25 contract level_map must be a non-empty list")
    result: list[tuple[float, int]] = []
    previous: float | None = None
    for item in raw:
        if not isinstance(item, dict) or set(item) != {"max", "value"}:
            raise ValueError("pm25 contract level_map entries must be {max, value}")
        maximum = item["max"]
        value = item["value"]
        if isinstance(maximum, bool) or not isinstance(maximum, (int, float)):
            raise ValueError("pm25 contract level_map max must be a number")
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("pm25 contract level_map value must be an integer")
        if previous is not None and float(maximum) <= previous:
            raise ValueError("pm25 contract level_map max must increase")
        previous = float(maximum)
        result.append((float(maximum), value))
    return tuple(result)


def _level(levels: tuple[tuple[float, int], ...], value: int) -> int:
    for maximum, enum in levels:
        if value <= maximum:
            return enum
    return levels[-1][1]


ADAPTER = Pm25ServiceAdapter()