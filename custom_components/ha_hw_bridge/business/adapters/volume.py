"""Huawei ``volume`` service: speaker/appliance volume percentage.

52 of the 78 Profiles carry a single ``volume`` int (0..100); a few add
``action`` or ``key`` around it, which this adapter ignores because they are
remote-control codes, not state.

contract
    field : characteristic name (default ``volume``)
    min/max : int range (default 0..100)
"""

from __future__ import annotations

import math

from ..models import ServiceRef


class VolumeServiceAdapter:
    service_id = "volume"
    service_type = "volume"
    entity_domains = ("media_player", "number", "input_number")
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "volume":
            raise ValueError("volume requires st: volume")
        unknown = set(dict(service.contract)) - {"field", "min", "max"}
        if unknown:
            raise ValueError(
                f"volume has unsupported contract keys: {', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field", "volume")
        if not isinstance(field, str) or not field:
            raise ValueError("volume contract field must be non-empty text")
        _range(service)

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError("volume requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in self.entity_domains:
            raise ValueError("volume requires a media_player or number entity")

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        domain = entity_ids[0].partition(".")[0]
        raw: object
        if domain == "media_player":
            # HA reports 0.0..1.0; the Profile wants 0..100.
            raw = state.attributes.get("volume_level")
            if isinstance(raw, bool) or not isinstance(raw, (int, float)):
                return {}
            raw = float(raw) * 100
        else:
            raw = state.state
        try:
            value = float(raw)
        except (TypeError, ValueError):
            return {}
        if not math.isfinite(value):
            return {}
        minimum, maximum = _range(service)
        return {str(service.contract_value("field", "volume")):
                int(round(min(max(value, minimum), maximum)))}

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        raw = payload.get(str(service.contract_value("field", "volume")))
        if isinstance(raw, bool) or not isinstance(raw, (int, float)):
            return
        value = float(raw)
        if not math.isfinite(value):
            return
        minimum, maximum = _range(service)
        if not minimum <= value <= maximum:
            return
        domain = entity_ids[0].partition(".")[0]
        if domain == "media_player":
            await hass.services.async_call(
                "media_player",
                "volume_set",
                {"entity_id": entity_ids[0], "volume_level": value / 100},
                blocking=True,
            )
            return
        await hass.services.async_call(
            domain,
            "set_value",
            {"entity_id": entity_ids[0], "value": value},
            blocking=True,
        )


def _range(service: ServiceRef) -> tuple[float, float]:
    for key in ("min", "max"):
        value = service.contract_value(key)
        if value is None:
            continue
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"volume contract {key} must be a number")
    minimum = float(service.contract_value("min", 0))
    maximum = float(service.contract_value("max", 100))
    if minimum >= maximum:
        raise ValueError("volume contract min must be smaller than max")
    return minimum, maximum


ADAPTER = VolumeServiceAdapter()