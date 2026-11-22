"""Tests for the service adapters; no Home Assistant runtime required."""

from __future__ import annotations

import sys
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "custom_components" / "ha_hw_bridge"
# The repository root is itself the integration directory (HACS layout), so
# register it as a package without executing __init__.py, which needs HA.
if "ha_hw_bridge" not in sys.modules:
    package = types.ModuleType("ha_hw_bridge")
    package.__path__ = [str(ROOT)]
    sys.modules["ha_hw_bridge"] = package

from ha_hw_bridge.business.adapters import get_service_adapter  # noqa: E402
from ha_hw_bridge.business.models import ServiceRef  # noqa: E402


class FakeState:
    def __init__(self, state: str, **attributes: object) -> None:
        self.state = state
        self.attributes = attributes


class FakeStates:
    def __init__(self, mapping: dict[str, FakeState]) -> None:
        self._mapping = mapping

    def get(self, entity_id: str) -> FakeState | None:
        return self._mapping.get(entity_id)


class FakeServices:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, dict[str, object]]] = []

    async def async_call(self, domain, service, data, blocking=True):
        self.calls.append((domain, service, dict(data)))


class FakeHass:
    def __init__(self, states: dict[str, FakeState] | None = None) -> None:
        self.states = FakeStates(states or {})
        self.services = FakeServices()


def run(coroutine):
    import asyncio

    return asyncio.run(coroutine)


def svc(service_id: str, st: str | None = None, **contract: object) -> ServiceRef:
    return ServiceRef(st or service_id, service_id, tuple(contract.items()))


class BatteryAdapterTest(unittest.TestCase):
    def test_rejects_out_of_range_level(self):
        adapter = get_service_adapter("battery")
        hass = FakeHass({"sensor.b": FakeState("150")})
        self.assertEqual(run(adapter.read_state(hass, svc("battery"), ("sensor.b",))), {})

    def test_accepts_valid_level(self):
        adapter = get_service_adapter("battery")
        hass = FakeHass({"sensor.b": FakeState("87")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("battery"), ("sensor.b",))), {"level": 87.0}
        )

    def test_binary_sensor_is_presence_not_percentage(self):
        adapter = get_service_adapter("battery")
        hass = FakeHass({"binary_sensor.b": FakeState("on")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("battery"), ("binary_sensor.b",))),
            {"level": 100},
        )

    def test_contract_field_must_be_text(self):
        adapter = get_service_adapter("battery")
        with self.assertRaises(ValueError):
            adapter.validate_service(ServiceRef("battery", "battery", (("field", 5),)))


class LuminanceAdapterTest(unittest.TestCase):
    def test_non_numeric_scale_is_a_config_error(self):
        adapter = get_service_adapter("luminance")
        with self.assertRaises(ValueError):
            adapter.validate_service(ServiceRef("luminance", "luminance", (("scale", "x"),)))

    def test_reads_scaled_value(self):
        adapter = get_service_adapter("luminance")
        hass = FakeHass({"sensor.l": FakeState("12.5")})
        self.assertEqual(
            run(
                adapter.read_state(
                    hass, svc("luminance", scale=2), ("sensor.l",)
                )
            ),
            {"current": 25.0},
        )


class TargetDistanceAdapterTest(unittest.TestCase):
    def test_field_contract_renames_the_payload_key(self):
        adapter = get_service_adapter("targetDistance")
        hass = FakeHass({"sensor.d": FakeState("3")})
        result = run(
            adapter.read_state(hass, svc("targetDistance", field="range"), ("sensor.d",))
        )
        self.assertEqual(result, {"range": 3.0})


class BrightnessAdapterTest(unittest.TestCase):
    def test_scales_255_to_contract_range(self):
        adapter = get_service_adapter("brightness")
        hass = FakeHass({"light.l": FakeState("on", brightness=255)})
        result = run(
            adapter.read_state(hass, svc("brightness", min=1, max=100), ("light.l",))
        )
        self.assertEqual(result, {"brightness": 100})

    def test_step_must_divide_range(self):
        adapter = get_service_adapter("brightness")
        with self.assertRaises(ValueError):
            adapter.validate_service(svc("brightness", min=0, max=100, step=7))


class SwitchAdapterTest(unittest.TestCase):
    def test_climate_turn_off_uses_hvac_mode(self):
        adapter = get_service_adapter("switch")
        hass = FakeHass({"climate.c": FakeState("cool", hvac_modes=["off", "cool"])})
        run(adapter.apply_command(hass, svc("switch"), ("climate.c",), {"on": 0}))
        self.assertEqual(hass.services.calls[0][1], "set_hvac_mode")
        self.assertEqual(hass.services.calls[0][2]["hvac_mode"], "off")

    def test_unknown_on_value_is_ignored(self):
        adapter = get_service_adapter("switch")
        hass = FakeHass({"switch.s": FakeState("off")})
        run(adapter.apply_command(hass, svc("switch"), ("switch.s",), {"on": 9}))
        self.assertEqual(hass.services.calls, [])


class OpenerAdapterTest(unittest.TestCase):
    def test_invert_flips_position(self):
        adapter = get_service_adapter("opener")
        hass = FakeHass({"cover.c": FakeState("closed", current_position=0)})
        result = run(
            adapter.read_state(hass, svc("opener", invert=True), ("cover.c",))
        )
        self.assertEqual(result, {"current": 100, "target": 100})

    def test_target_off_step_is_rejected(self):
        adapter = get_service_adapter("opener")
        hass = FakeHass({"cover.c": FakeState("open", current_position=50)})
        run(
            adapter.apply_command(
                hass, svc("opener", step=10), ("cover.c",), {"target": 55}
            )
        )
        self.assertEqual(hass.services.calls, [])


class BinarySwitchAdapterTest(unittest.TestCase):
    def test_reports_boolean_not_int(self):
        adapter = get_service_adapter("childLockSwitch")
        hass = FakeHass({"switch.lock": FakeState("on")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("childLockSwitch", st="switch"),
                                   ("switch.lock",))),
            {"on": True},
        )

    def test_swap_inverts_both_directions(self):
        adapter = get_service_adapter("childLockSwitch")
        hass = FakeHass({"binary_sensor.lock": FakeState("off")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("childLockSwitch", st="switch", swap=True),
                                   ("binary_sensor.lock",))),
            {"on": True},
        )
        run(adapter.apply_command(
            hass, svc("childLockSwitch", st="switch", swap=True),
            ("binary_sensor.lock",), {"on": True}))
        self.assertEqual(hass.services.calls[0][1], "turn_off")

    def test_numeric_string_on_is_accepted(self):
        adapter = get_service_adapter("lightSwitch")
        hass = FakeHass({"switch.light": FakeState("off")})
        run(adapter.apply_command(
            hass, svc("lightSwitch", st="switch"), ("switch.light",), {"on": "1"}))
        self.assertEqual(hass.services.calls[0][1], "turn_on")


class LightModeAdapterTest(unittest.TestCase):
    def test_unmapped_state_is_not_forwarded(self):
        adapter = get_service_adapter("lightMode")
        hass = FakeHass({"input_select.scene": FakeState("movie")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("lightMode", st="mode",
                                             values={"warm": 1}), ("input_select.scene",))),
            {},
        )

    def test_fallback_is_used_when_configured(self):
        adapter = get_service_adapter("lightMode")
        hass = FakeHass({"input_select.scene": FakeState("movie")})
        self.assertEqual(
            run(adapter.read_state(
                hass, svc("lightMode", st="mode", values={"warm": 1}, fallback=0),
                ("input_select.scene",))),
            {"mode": 0},
        )

    def test_command_selects_the_matching_option(self):
        adapter = get_service_adapter("colourMode")
        hass = FakeHass({"input_select.m": FakeState("warm", options=["warm", "cold"])})
        run(adapter.apply_command(
            hass, svc("colourMode", st="mode", values={"warm": 1, "cold": 3}),
            ("input_select.m",), {"mode": 3}))
        self.assertEqual(hass.services.calls[0][1:], ("select_option", {"entity_id": "input_select.m", "option": "cold"}))

    def test_duplicate_enum_values_are_rejected(self):
        adapter = get_service_adapter("lightMode")
        with self.assertRaises(ValueError):
            adapter.validate_service(svc("lightMode", st="mode", values={"a": 1, "b": 1}))


class Pm25AdapterTest(unittest.TestCase):
    def test_reads_current_without_level(self):
        adapter = get_service_adapter("pm25")
        hass = FakeHass({"sensor.pm": FakeState("37")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("pm25"), ("sensor.pm",))), {"current": 37}
        )

    def test_level_map_derives_the_enum(self):
        adapter = get_service_adapter("pm25")
        hass = FakeHass({"sensor.pm": FakeState("90")})
        result = run(adapter.read_state(
            hass,
            svc("pm25", level_map=[{"max": 35, "value": 1}, {"max": 75, "value": 2},
                                   {"max": 115, "value": 3}]),
            ("sensor.pm",)))
        self.assertEqual(result, {"current": 90, "level": 3})

    def test_values_are_clamped_to_the_profile_range(self):
        adapter = get_service_adapter("pm25")
        hass = FakeHass({"sensor.pm": FakeState("5000")})
        self.assertEqual(
            run(adapter.read_state(hass, svc("pm25"), ("sensor.pm",))), {"current": 1000}
        )


class RegistryTest(unittest.TestCase):
    def test_every_registered_adapter_declares_its_contract(self):
        from ha_hw_bridge.business.adapters import registry

        for service_id, adapter in registry._SERVICE_ADAPTERS.items():
            with self.subTest(service_id=service_id):
                self.assertTrue(adapter.service_id)
                self.assertTrue(adapter.entity_domains)


if __name__ == "__main__":
    unittest.main()