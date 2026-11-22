"""Huawei ``alarm`` read-only service adapter.

Default contract source
    prodId   : ``2GEB``
    Profile  : https://smarthome-drcn.dbankcdn.com/device/guide/2GEB/2GEB.json
    common   : specialized gas-detector alarm state
    verified : implementation follows the Profile's read-only ``alarm`` bool
               enum (0 normal / 1 alarm); a real projection is still required
"""

from __future__ import annotations

from ..models import ServiceRef

# A camera's alarmEvent exposes many detector flags. ``alarm`` is the generic one
# and the only flag on gas detectors, so it stays the default; a camera binds one
# binary_sensor per detector and names it in the contract instead.
_ALARM_FIELDS = (
    "alarm",
    "humanBodyAlarm",
    "videoAlarm",
    "audioAlarm",
    "babyCryAlarm",
    "animalAlarm",
    "carAlarm",
    "rangeAlarm",
    "auxiliaryFireAlarm",
    "invadeAlarm",
    "shelterAlarm",
    "humanStayAlarm",
    "enterZoneAlarm",
    "leaveZoneAlarm",
    "acrossLineAlarm",
    "humanGatherAlarm",
    "strangerAlarm",
    "licensePlateAlarm",
)


class AlarmServiceAdapter:
    service_id = "alarm"
    # Huawei serviceType from the Profile; it is not always the sid.
    service_type = "alarm"
    # Declared for the UI entity selector; validate_entities enforces the same rule.
    entity_domains = ("binary_sensor",)
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "alarm":
            raise ValueError("alarm requires st: alarm")
        unknown = set(dict(service.contract)) - {"field"}
        if unknown:
            raise ValueError(
                f"alarm has unsupported contract keys: {', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field")
        if field is not None:
            if not isinstance(field, str) or not field:
                raise ValueError("alarm contract field must be non-empty text")
            if field not in _ALARM_FIELDS:
                raise ValueError(
                    "alarm contract field must be one of: "
                    + ", ".join(sorted(_ALARM_FIELDS))
                )

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1 or not entity_ids[0].startswith("binary_sensor."):
            raise ValueError("alarm requires exactly one binary_sensor entity")

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        self.validate_service(service)
        self.validate_entities(entity_ids)
        state = hass.states.get(entity_ids[0])
        if state is None:
            return {}
        field = self._field(service)
        if state.state == "on":
            return {field: 1}
        if state.state == "off":
            return {field: 0}
        return {}

    @staticmethod
    def _field(service: ServiceRef) -> str:
        explicit = service.contract_value("field")
        if isinstance(explicit, str) and explicit:
            return explicit
        return _ALARM_FIELDS[0]

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        self.validate_service(service)
        self.validate_entities(entity_ids)


ADAPTER = AlarmServiceAdapter()
