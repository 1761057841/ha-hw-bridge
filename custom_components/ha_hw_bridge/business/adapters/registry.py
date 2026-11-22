"""Explicit registry of trusted Huawei service adapters."""

from __future__ import annotations

from .action import ADAPTER as ACTION
from .alarm import ADAPTER as ALARM
from .alarm_bell import ADAPTER as ALARM_BELL
from .battery import ADAPTER as BATTERY
from .air_detector import ADAPTER as AIR_DETECTOR
from .luminance import ADAPTER as LUMINANCE
from .pir import ADAPTER as PIR
from .target_distance import ADAPTER as TARGET_DISTANCE
from .brightness import ADAPTER as BRIGHTNESS
from .cct import ADAPTER as CCT
from .child_lock_switch import ADAPTER as CHILD_LOCK_SWITCH
from .light_switch import ADAPTER as LIGHT_SWITCH
from .light_mode import ADAPTER as LIGHT_MODE
from .colour_mode import ADAPTER as COLOUR_MODE
from .pm25 import ADAPTER as PM25
from .mode_setting import ADAPTER as MODE_SETTING
from .gear import ADAPTER as GEAR
from .filter_element import FilterElementServiceAdapter
from .light import ADAPTER as LIGHT
from .volume import ADAPTER as VOLUME
from .cleaner_robot import ADAPTER as CLEANER_ROBOT
from .colour import ADAPTER as COLOUR
from .gas_sensor import ADAPTER as GAS_SENSOR
from .fan import ADAPTER as FAN
from .hcho import ADAPTER as HCHO
from .humidity import ADAPTER as HUMIDITY
from .mode import ADAPTER as MODE
from .motor import ADAPTER as MOTOR
from .open_level import ADAPTER as OPEN_LEVEL
from .opener import ADAPTER as OPENER
from .status import ADAPTER as STATUS
from .switch import ADAPTER as SWITCH
from .temperature import ADAPTER as TEMPERATURE

from .api import ServiceAdapter


_SERVICE_ADAPTERS: dict[str, ServiceAdapter] = {
    adapter.service_id: adapter
    for adapter in (
        SWITCH,
        BRIGHTNESS,
        CCT,
        COLOUR,
        TEMPERATURE,
        PM25,
        MODE_SETTING,
        GEAR,
        LIGHT,
        VOLUME,
        CHILD_LOCK_SWITCH,
        LIGHT_SWITCH,
        LIGHT_MODE,
        COLOUR_MODE,
        HUMIDITY,
        AIR_DETECTOR,
        MOTOR,
        OPEN_LEVEL,
        OPENER,
        HCHO,
        ALARM,
        ALARM_BELL,
        BATTERY,
        LUMINANCE,
        PIR,
        TARGET_DISTANCE,
        GAS_SENSOR,
        MODE,
        FAN,
        CLEANER_ROBOT,
        STATUS,
        ACTION,
    )
}
for _service_id in ("switch1", "switch2", "switch3"):
    _SERVICE_ADAPTERS[_service_id] = SWITCH
_SERVICE_ADAPTERS["leftAction"] = ACTION
_SERVICE_ADAPTERS["leftOpener"] = OPENER
# filterElement1..N all share one shape; register each sid explicitly so a
# Profile that names filterElement5 resolves without the serviceType fallback.
for _index in range(1, 13):
    _SERVICE_ADAPTERS[f"filterElement{_index}"] = FilterElementServiceAdapter(
        f"filterElement{_index}"
    )

# Vendors reuse one documented serviceType under many custom sids. These maps
# let an unregistered sid resolve to the adapter of its serviceType, so
# ``deviceSwitch`` behaves like ``switch`` instead of failing validation.
_SERVICE_TYPE_ADAPTERS: dict[str, ServiceAdapter] = {
    adapter.service_type: adapter
    for adapter in _SERVICE_ADAPTERS.values()
    if getattr(adapter, "service_type", None)
}


def get_service_adapter(service_id: str) -> ServiceAdapter:
    """Return the adapter registered for one Huawei ``sid``.

    A Profile pairs a vendor-defined ``sid`` with a documented ``serviceType``.
    Products reuse the same serviceType under many different sids
    (``deviceSwitch`` / ``ledSwitch`` / ``indicator`` are all ``switch``), so an
    unregistered sid falls back to the adapter of its serviceType instead of
    being rejected. Callers that know the serviceType should use
    :func:`get_adapter_for_service` so the fallback is explicit.
    """

    adapter = _SERVICE_ADAPTERS.get(service_id)
    if adapter is not None:
        return adapter
    adapter = _SERVICE_TYPE_ADAPTERS.get(service_id)
    if adapter is not None:
        return adapter
    raise ValueError(f"unknown Huawei service: {service_id}")


def get_adapter_for_service(service_id: str, service_type: str | None) -> ServiceAdapter:
    """Resolve an adapter by sid, falling back to its declared serviceType."""

    adapter = _SERVICE_ADAPTERS.get(service_id)
    if adapter is not None:
        return adapter
    if service_type:
        adapter = _SERVICE_TYPE_ADAPTERS.get(service_type)
        if adapter is not None:
            return adapter
    raise ValueError(
        f"unknown Huawei service: {service_id} (serviceType {service_type!r})"
    )
