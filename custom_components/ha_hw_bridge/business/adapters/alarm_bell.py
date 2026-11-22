"""Huawei ``alarmBell`` read-only service adapter.

Default contract source
    prodId   : ``9MTM``
    Profile  : https://smarthome-drcn.dbankcdn.com/device/guide/9MTM/9MTM.json
    common   : HA-exclusive pressure-sensor profile; the ``alarmBell`` service
               reports a two-value enum on the ``mode`` characteristic.
    verified : no -- the enum mapping follows the Profile field by field
               (1 = no pressure, 2 = pressure); a real projection is still
               required before promoting it out of "unverified".

The Profile describes pressure presence, and this adapter maps a bound
binary sensor the same way: ``off`` -> 1 (none), ``on`` -> 2 (present).
"""

from __future__ import annotations

from ..models import ServiceRef


class AlarmBellServiceAdapter:
    service_id = "alarmBell"
    # Huawei serviceType from the Profile; it is not always the sid.
    service_type = "mode"
    # Declared for the UI entity selector; validate_entities enforces the same rule.
    entity_domains = ("binary_sensor",)
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "mode":
            raise ValueError("alarmBell requires st: mode")
        if service.contract:
            raise ValueError("alarmBell does not accept contract overrides")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1 or not entity_ids[0].startswith("binary_sensor."):
            raise ValueError("alarmBell requires exactly one binary_sensor entity")

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None:
            return {}
        if state.state == "on":
            return {"mode": 2}
        if state.state == "off":
            return {"mode": 1}
        return {}

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        # Read-only per the Profile (method: R).
        self.validate_service(service)
        self.validate_entities(entity_ids)


ADAPTER = AlarmBellServiceAdapter()
