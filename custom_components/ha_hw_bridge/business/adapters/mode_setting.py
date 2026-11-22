"""Huawei ``modeSetting`` services: device configuration exposed as settings.

Vendors use ``modeSetting`` for parameters that are configured once and then
reported, not for a running state: radar detection range, auto-interference
suppression, screen brightness of an air detector. A Profile typically also
marks them ``RW``, so the card can change them.

Profile evidence (human-presence sensors)
    ``2RJB`` / ``2Q8M`` — ``detectionPara`` carries ``cfgMode``, ``triggerDistance``
                          (100..600) and ``detectionDistance`` (100..400);
                          ``envNoiseMgmt`` carries ``mode``, ``autoAntiInterference``
                          and ``disturbanceDist``
    方向 — ``cfgMode`` / ``autoAntiInterference`` 为 RW，``disturbanceDist`` 为 R

contract
    fields : ordered list of characteristic names to report/apply. Each entry is
             ``{name, kind, min?, max?, scale?, values?}`` where ``kind`` is
             ``int`` | ``bool`` | ``enum``.
    target : optional HA entity that carries the value (``input_number`` for
             numeric settings, ``input_boolean`` for switches,
             ``input_select`` for enums). Omit it to report constants only.

Only the characteristics listed here are ever reported. A setting the Profile
declares but this table does not name is dropped instead of forwarded with a
guessed type.
"""

from __future__ import annotations

import math

from ..models import ServiceRef

_KINDS = {"int", "bool", "enum", "float"}


class ModeSettingServiceAdapter:
    service_id = "detectionPara"
    service_type = "modeSetting"
    entity_domains = ("input_number", "number", "input_boolean", "switch",
                      "input_select", "select", "sensor")
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "modeSetting":
            raise ValueError(f"{self.service_id} requires st: modeSetting")
        unknown = set(dict(service.contract)) - {"fields", "target"}
        if unknown:
            raise ValueError(
                f"{self.service_id} has unsupported contract keys: "
                f"{', '.join(sorted(unknown))}"
            )
        fields = _fields(service)
        if not fields:
            raise ValueError(f"{self.service_id} requires a non-empty contract fields")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError(f"{self.service_id} requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in self.entity_domains:
            raise ValueError(
                f"{self.service_id} requires a number, boolean or select entity"
            )

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None or state.state in {"unknown", "unavailable"}:
            return {}
        domain = entity_ids[0].partition(".")[0]
        payload: dict[str, object] = {}
        for field in _fields(service):
            name = field["name"]
            kind = field["kind"]
            if kind == "bool":
                if state.state in {"on", "off"}:
                    payload[name] = state.state == "on"
                continue
            if kind == "enum":
                target = _explicit_value(field, state)
                if target is not None:
                    payload[name] = target
                continue
            # int / float settings read the entity's numeric state directly.
            try:
                number = float(state.state)
            except (TypeError, ValueError):
                # An int setting may still be expressed as a named option.
                target = _explicit_value(field, state)
                if target is not None:
                    payload[name] = target
                continue
            if math.isfinite(number):
                payload[name] = _clamp(number, field)
        del domain
        return payload

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        domain = entity_ids[0].partition(".")[0]
        for field in _fields(service):
            name = field["name"]
            if name not in payload:
                continue
            raw = payload[name]
            if field["kind"] == "bool":
                enabled = _as_bool(raw)
                if enabled is None:
                    continue
                if domain in {"switch", "input_boolean"}:
                    await hass.services.async_call(
                        domain,
                        "turn_on" if enabled else "turn_off",
                        {"entity_id": entity_ids[0]},
                        blocking=True,
                    )
                return
            number = _wire_int(raw)
            if number is None:
                continue
            if domain in {"number", "input_number"}:
                await hass.services.async_call(
                    domain,
                    "set_value",
                    {"entity_id": entity_ids[0], "value": number},
                    blocking=True,
                )
                return
            if domain in {"select", "input_select"}:
                values = field.get("values") or {}
                reverse = {v: k for k, v in values.items()}
                option = reverse.get(number)
                if option is not None:
                    await hass.services.async_call(
                        domain,
                        "select_option",
                        {"entity_id": entity_ids[0], "option": option},
                        blocking=True,
                    )
                return


def _fields(service: ServiceRef) -> tuple[dict[str, object], ...]:
    raw = service.contract_value("fields")
    if not isinstance(raw, (list, tuple)) or not raw:
        return ()
    result: list[dict[str, object]] = []
    for item in raw:
        if not isinstance(item, dict):
            raise ValueError(f"{service.service_id} contract fields entries must be mappings")
        name = item.get("name")
        kind = item.get("kind", "int")
        if not isinstance(name, str) or not name:
            raise ValueError(f"{service.service_id} contract fields need a name")
        if kind not in _KINDS:
            raise ValueError(
                f"{service.service_id} contract field {name} kind must be one of "
                f"{', '.join(sorted(_KINDS))}"
            )
        entry: dict[str, object] = {"name": name, "kind": kind}
        for key in ("min", "max", "scale"):
            if key in item:
                value = item[key]
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    raise ValueError(
                        f"{service.service_id} contract field {name} {key} must be numeric"
                    )
                entry[key] = float(value)
        if "values" in item:
            values = item["values"]
            if not isinstance(values, dict):
                raise ValueError(
                    f"{service.service_id} contract field {name} values must be a mapping"
                )
            entry["values"] = dict(values)
        result.append(entry)
    return tuple(result)


def _explicit_value(field: dict[str, object], state) -> object | None:
    values = field.get("values")
    if isinstance(values, dict) and state.state in values:
        return values[state.state]
    return None


def _clamp(value: float, field: dict[str, object]) -> float | int:
    minimum = field.get("min")
    maximum = field.get("max")
    if isinstance(minimum, float):
        value = max(value, minimum)
    if isinstance(maximum, float):
        value = min(value, maximum)
    return int(value) if float(value).is_integer() else value


def _as_bool(value: object) -> bool | None:
    if isinstance(value, bool):
        return value
    if isinstance(value, int) and value in {0, 1}:
        return bool(value)
    if isinstance(value, str) and value in {"0", "1", "on", "off", "true", "false"}:
        return value in {"1", "on", "true"}
    return None


def _wire_int(value: object) -> int | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return None


ADAPTER = ModeSettingServiceAdapter()