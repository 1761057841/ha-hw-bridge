"""Huawei ``childLockSwitch`` / ``lightSwitch`` style binary switches.

Both services are `switch`-typed booleans on an ``on`` characteristic, and the
only thing that differs between the 296 child-lock devices and the 207 appliance
light devices is the characteristic name some Profiles use instead of ``on``.

Profile evidence (catalogue ``ver_202609_hmos``, 5926 readable Profiles)
    childLockSwitch : 296 devices, 294 use ``on``; aliases ``switch``,
                      ``childLockSwitch``
    lightSwitch     : 207 devices, 188 use ``on``; alias ``lightSwitch``
    方向            : ``RW`` on every Profile; commands are accepted

contract
    field    : characteristic name to report. Defaults to the alias list above.
    on_value : bool reported when the bound entity is on (default true)
    off_value: bool reported when the bound entity is off (default false)

Both bind a ``switch`` or ``binary_sensor`` entity, so a lock exposed as a
binary sensor still works. ``swap`` mirrors a device whose entity means
"unlocked".
"""

from __future__ import annotations

from ..models import ServiceRef

_ALIASES = ("on", "switch", "childLockSwitch", "lightSwitch")


class BinarySwitchServiceAdapter:
    """`switch`-typed service carrying a single boolean characteristic."""

    entity_domains = ("switch", "binary_sensor", "input_boolean")
    entity_counts = None

    def __init__(
        self,
        service_id: str,
        service_type: str = "switch",
        aliases: tuple[str, ...] = _ALIASES,
    ) -> None:
        self.service_id = service_id
        self.service_type = service_type
        self._aliases = aliases

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "switch":
            raise ValueError(f"{self.service_id} requires st: switch")
        unknown = set(dict(service.contract)) - {"field", "swap"}
        if unknown:
            raise ValueError(
                f"{self.service_id} has unsupported contract keys: "
                f"{', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field")
        if field is not None and (not isinstance(field, str) or not field):
            raise ValueError(f"{self.service_id} contract field must be non-empty text")
        if not isinstance(service.contract_value("swap", False), bool):
            raise ValueError(f"{self.service_id} contract swap must be boolean")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError(f"{self.service_id} requires exactly one HA entity")
        domain, separator, _object_id = entity_ids[0].partition(".")
        if not separator or domain not in {"switch", "binary_sensor", "input_boolean"}:
            raise ValueError(
                f"{self.service_id} requires a switch, binary_sensor or "
                "input_boolean entity"
            )

    def _field(self, service: ServiceRef) -> str:
        return str(service.contract_value("field", self._aliases[0]))

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
        raw = payload.get(self._field(service))
        if raw is None:
            raw = payload.get("on")
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


ADAPTER = BinarySwitchServiceAdapter("childLockSwitch")
"""Registry entry: childLockSwitch."""