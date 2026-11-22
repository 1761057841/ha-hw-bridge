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


def get_service_adapter(service_id: str) -> ServiceAdapter:
    try:
        return _SERVICE_ADAPTERS[service_id]
    except KeyError as error:
        raise ValueError(f"unknown Huawei service: {service_id}") from error
