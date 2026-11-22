"""Preset child product templates offered by the UI add-device flow.

Each template fills the Huawei product identity a child device needs to
register. The preset models are the Home Assistant-exclusive profiles
documented in ``docs/preconfigured-child-products.md``; ``custom`` allows
advanced users to register any other profile by ``prodId``.
"""

from __future__ import annotations

from typing import Any

PRESET_PRODUCTS: dict[str, dict[str, Any]] = {
    "smart_switch_a0op": {
        "prod_id": "A0OP",
        "sub_prod_id": "",
        "device_type": "005",
        "manufacturer": "20f",
        "model": "Smart wall switch",
        "friendly_name": "智能单通道开关（A0OP）",
        "protocol_type": 1,
        "setup_type": 0,
        "known_fields_only": True,
        "services": [
            {"st": "switch", "sid": "switch"},
        ],
    },
    "smart_plug_a0do": {
        "prod_id": "A0DO",
        "sub_prod_id": "",
        "device_type": "01D",
        "manufacturer": "318",
        "model": "SMARTPLUG",
        "friendly_name": "普通智能插座（A0DO）",
        "protocol_type": 1,
        "setup_type": 0,
        "known_fields_only": True,
        "services": [
            {"st": "switch", "sid": "switch"},
        ],
    },
    "nightlight_9mtj": {
        "prod_id": "9MTJ",
        "sub_prod_id": "00",
        "device_type": "21F",
        "manufacturer": "002",
        "model": "haTest1",
        "friendly_name": "智控夜灯",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
            {"st": "brightness", "sid": "brightness",
             "contract": {"min": 1, "max": 100, "step": 1}},
            {"st": "cct", "sid": "cct"},
            {"st": "status", "sid": "status",
             "contract": {"states": {"off": 0, "on": 1}}},
        ],
    },
    "bedside_lamp_9mtl": {
        "prod_id": "9MTL",
        "sub_prod_id": "00",
        "device_type": "10E",
        "manufacturer": "002",
        "model": "haTest2",
        "friendly_name": "智控床头灯",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
            {"st": "brightness", "sid": "brightness",
             "contract": {"min": 1, "max": 100, "step": 1}},
            {"st": "cct", "sid": "cct"},
        ],
    },
    "pressure_sensor_9mtm": {
        "prod_id": "9MTM",
        "sub_prod_id": "00",
        "device_type": "1F1",
        "manufacturer": "002",
        "model": "haTest4",
        "friendly_name": "智控压力传感器",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "mode", "sid": "alarmBell"},
        ],
    },
    "kettle_9mtr": {
        "prod_id": "9MTR",
        "sub_prod_id": "00",
        "device_type": "09A",
        "manufacturer": "002",
        "model": "haTest5",
        "friendly_name": "智控水壶",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
            {"st": "mode", "sid": "mode",
             "contract": {"values": {
                 "off": 0, "fan_only": 1, "cool": 2, "dry": 3,
                 "auto": 4, "heat": 5, "eco": 6, "boost": 7,
                 "sleep": 8, "idle": 9, "quiet": 10, "slow": 11,
             }}},
            {"st": "status", "sid": "status",
             "contract": {"states": {
                 "off": 0, "idle": 0, "standby": 0,
                 "on": 3, "active": 3, "operating": 3,
                 "heating": 2, "heating_up": 2,
                 "cooking": 3, "working": 3, "running": 3,
                 "warming": 4, "hold": 4, "keep_warm": 4,
                 "paused": 5, "pause": 5,
                 "done": 6, "finished": 6, "complete": 6, "completed": 6,
             }, "fallback": 0}},
            {"st": "temperature", "sid": "temperature"},
        ],
    },
    "mosquito_repellent_9mtv": {
        "prod_id": "9MTV",
        "sub_prod_id": "00",
        "device_type": "0B0",
        "manufacturer": "002",
        "model": "haTest6",
        "friendly_name": "智控灭蚊器",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
        ],
    },
    "rice_cooker_9mtw": {
        "prod_id": "9MTW",
        "sub_prod_id": "00",
        "device_type": "026",
        "manufacturer": "002",
        "model": "haTest7",
        "friendly_name": "智控电饭煲",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
            {"st": "action", "sid": "action",
             "contract": {"commands": {0: "pause", 1: "start", 2: "cancel"}}},
            {"st": "status", "sid": "status",
             "contract": {"states": {
                 "off": 0, "idle": 0, "standby": 0,
                 "cleaning": 1, "working": 1, "running": 1, "on": 1,
                 "paused": 2, "pause": 2,
                 "ordered": 3, "scheduled": 3,
                 "suspend": 4,
                 "done": 5, "finished": 5, "complete": 5, "completed": 5,
             }, "fallback": 0}},
        ],
    },
    "breaker_9mtx": {
        "prod_id": "9MTX",
        "sub_prod_id": "00",
        "device_type": "211",
        "manufacturer": "002",
        "model": "haTest8",
        "friendly_name": "智控断路器",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
        ],
    },
    "bulb_9mu7": {
        "prod_id": "9MU7",
        "sub_prod_id": "00",
        "device_type": "119",
        "manufacturer": "002",
        "model": "haTest10",
        "friendly_name": "智控灯泡",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch"},
            {"st": "brightness", "sid": "brightness",
             "contract": {"min": 0, "max": 100, "step": 1}},
            {"st": "cct", "sid": "cct"},
        ],
    },
    "air_conditioner_9mxo": {
        "prod_id": "9MXO",
        "sub_prod_id": "00",
        "device_type": "012",
        "manufacturer": "002",
        "model": "test20",
        "friendly_name": "智控空调",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "switch", "sid": "switch", "contract": {"on_mode": "cool"}},
            {"st": "mode", "sid": "mode",
             "contract": {"values": {"cool": 2, "heat": 3, "fan_only": 4}}},
            {"st": "temperature", "sid": "temperature"},
            {"st": "fan", "sid": "fan",
             "contract": {
                 "gear_values": {"auto": 0, "low": 1, "medium": 2, "high": 3},
                 "direction_enabled": False,
             }},
        ],
    },
    "curtain_9my5": {
        "prod_id": "9MY5",
        "sub_prod_id": "00",
        "device_type": "01C",
        "manufacturer": "002",
        "model": "haTest23",
        "friendly_name": "智控窗帘",
        "protocol_type": 6,
        "setup_type": 0,
        "known_fields_only": False,
        "services": [
            {"st": "action", "sid": "leftAction",
             "contract": {"commands": {0: "close", 1: "open", 2: "stop"}}},
            {"st": "opener", "sid": "opener"},
        ],
    },
}

# Aliases keep the historical example keys working through the UI too.
TEMPLATE_ALIASES = {
    "color_bulb_9mu7": "bulb_9mu7",
    "air_conditioner_9mxo": "air_conditioner_9mxo",
    "curtain_9my5": "curtain_9my5",
}


def resolve_template(key: str) -> dict[str, Any] | None:
    """Return the preset template for a template key, if known."""

    resolved = TEMPLATE_ALIASES.get(key, key)
    template = PRESET_PRODUCTS.get(resolved)
    if template is None:
        return None
    # Return a copy so callers can mutate defaults freely.
    result = dict(template)
    result["services"] = [dict(item) for item in template["services"]]
    return result
