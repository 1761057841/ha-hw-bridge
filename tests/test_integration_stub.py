"""Cross-module tests for setup, subentry changes and legacy adoption.

Home Assistant is not installed in this environment, so a small in-process stub
provides the handful of objects the integration touches. The stub never
replaces a real Home Assistant: when ``homeassistant`` imports successfully the
whole module is skipped.
"""

from __future__ import annotations

import asyncio
import json
import sys
import tempfile
import types
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _install_stub() -> bool:
    """Register a minimal Home Assistant stub; False if the real one exists."""

    try:
        import homeassistant  # noqa: F401, PLC0415

        return False
    except ImportError:
        pass

    def module(name, package=False, **attrs):
        mod = types.ModuleType(name)
        if package:
            mod.__path__ = []
        for key, value in attrs.items():
            setattr(mod, key, value)
        sys.modules[name] = mod
        return mod

    class ConfigSubentry:
        def __init__(self, *, data=None, subentry_id="sid", subentry_type="child",
                     title="t", unique_id=None):
            self.data = data or {}
            self.subentry_id = subentry_id
            self.subentry_type = subentry_type
            self.title = title
            self.unique_id = unique_id

    class ConfigFlow:
        VERSION = 1
        MINOR_VERSION = 1

        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__()

        def async_show_form(self, **kwargs):
            return kwargs

        def async_abort(self, **kwargs):
            return kwargs

        def async_create_entry(self, **kwargs):
            return kwargs

        async def async_set_unique_id(self, *args, **kwargs):
            return None

        def _abort_if_unique_id_configured(self):
            return None

    class ConfigSubentryFlow(ConfigFlow):
        def _get_entry(self):
            return ConfigEntry()

        def _get_reconfigure_subentry(self):
            return ConfigSubentry()

        def async_update_and_abort(self, entry, subentry, **kwargs):
            return kwargs

    class OptionsFlow(ConfigFlow):
        @property
        def config_entry(self):
            return ConfigEntry()

    class ConfigEntry:
        def __init__(self, **kwargs):
            self.entry_id = "e1"
            self.data = {}
            self.options = {}
            self.subentries = {}
            self.version = 3
            self.title = "t"
            for key, value in kwargs.items():
                setattr(self, key, value)

        def add_update_listener(self, callback):
            return lambda: None

    class HomeAssistantError(Exception):
        pass

    async def async_get_translations(*args, **kwargs):
        return {}

    def passthrough(fn):
        return fn

    class _AnySelector:
        def __init__(self, *args, **kwargs):
            pass

    module("homeassistant", package=True)
    module("homeassistant.components", package=True)
    module(
        "homeassistant.components.persistent_notification",
        async_create=lambda *a, **k: None,
        async_dismiss=lambda *a, **k: None,
    )
    module("homeassistant.components.sensor", SensorEntity=object)
    module(
        "homeassistant.components.binary_sensor",
        BinarySensorDeviceClass=types.SimpleNamespace(CONNECTIVITY="connectivity"),
        BinarySensorEntity=object,
    )
    module("homeassistant.components.button", ButtonEntity=object)
    module(
        "homeassistant.config_entries",
        ConfigEntry=ConfigEntry,
        ConfigSubentry=ConfigSubentry,
        ConfigFlow=ConfigFlow,
        ConfigSubentryFlow=ConfigSubentryFlow,
        OptionsFlow=OptionsFlow,
    )
    module("homeassistant.core", HomeAssistant=object, callback=passthrough)
    module("homeassistant.exceptions", HomeAssistantError=HomeAssistantError)
    module("homeassistant.helpers", package=True)
    module("homeassistant.helpers.translation", async_get_translations=async_get_translations)
    module(
        "homeassistant.helpers.event",
        async_call_later=lambda *a, **k: (lambda: None),
        async_track_state_change_event=lambda *a, **k: (lambda: None),
    )
    module("homeassistant.helpers.entity", DeviceInfo=dict, Entity=object)
    module(
        "homeassistant.helpers.selector",
        EntitySelector=_AnySelector,
        EntitySelectorConfig=dict,
    )
    module("homeassistant.helpers.config_validation", multi_select=lambda choices: choices)
    module("homeassistant.const", EntityCategory=types.SimpleNamespace(DIAGNOSTIC="diagnostic"))
    module("homeassistant.data_entry_flow")
    module("homeassistant.util", package=True)
    module("homeassistant.util.ulid", ulid_now=lambda: "01ULID")
    sys.modules["homeassistant"].config_entries = sys.modules["homeassistant.config_entries"]
    try:
        import voluptuous  # noqa: F401, PLC0415

        return True
    except ImportError:
        return False


HA_STUBBED = _install_stub()

if HA_STUBBED:
    if "ha_hw_bridge" not in sys.modules:
        package = types.ModuleType("ha_hw_bridge")
        package.__path__ = [str(ROOT)]
        sys.modules["ha_hw_bridge"] = package
    # The package __init__ is not executed by a bare ModuleType, so run it here
    # exactly once to expose async_setup_entry and friends.
    _package = sys.modules["ha_hw_bridge"]
    if not hasattr(_package, "async_setup_entry"):
        _init_path = ROOT / "__init__.py"
        exec(
            compile(_init_path.read_text(encoding="utf-8"), str(_init_path), "exec"),
            _package.__dict__,
        )
    import ha_hw_bridge as INTEGRATION  # noqa: E402
    from ha_hw_bridge.const import CONF_REUSE_SERIAL, DOMAIN  # noqa: E402
    from ha_hw_bridge.storage import GatewayStore  # noqa: E402


class FakeRuntime:
    def __init__(self, serial: str) -> None:
        self.serial = serial
        self.status = "offline"
        self.pin = None
        self.child_count = 0
        self.plan = None
        self.reloaded = None

    def set_gateway_plan(self, plan):
        self.plan = plan

    def set_entity_bridge(self, bridge):
        pass

    def add_listener(self, listener):
        return lambda: None

    def has_bound_material(self):
        return True

    def start(self):
        pass

    def stop(self):
        pass

    def reload_plan(self, plan, timeout=120.0):
        self.reloaded = plan

    def enqueue_child_state(self, *args):
        return True


class FakeManager:
    def __init__(self) -> None:
        self.created: list[FakeRuntime] = []

    def create(self, config):
        runtime = FakeRuntime(config.serial)
        self.created.append(runtime)
        return runtime

    def remove(self, runtime):
        pass


class FakeConfigEntries:
    def __init__(self, entry) -> None:
        self.entry = entry

    def async_add_subentry(self, entry, subentry):
        entry.subentries[subentry.subentry_id] = subentry
        return True

    def async_get_entry(self, entry_id):
        return self.entry

    async def async_forward_entry_setups(self, entry, platforms):
        return None

    async def async_unload_platforms(self, entry, platforms):
        return True

    def async_update_entry(self, entry, **kwargs):
        for key, value in kwargs.items():
            setattr(entry, key, value)
        return True

    def async_update_subentry(self, entry, subentry, **kwargs):
        return True


class FakeHass:
    def __init__(self, entry, config_dir: str) -> None:
        self.data: dict = {}
        self.config_entries = FakeConfigEntries(entry)
        self.config = types.SimpleNamespace(
            path=lambda: config_dir, language="zh-Hans"
        )
        loop = types.SimpleNamespace(call_soon_threadsafe=lambda fn: fn())
        self.loop = loop
        services = types.SimpleNamespace(
            has_service=lambda *a: True, async_register=lambda *a, **k: None
        )
        self.services = services

    async def async_add_executor_job(self, func, *args):
        return func(*args)

    def async_create_task(self, coroutine):
        async def runner():
            try:
                await coroutine
            except Exception:  # noqa: BLE001 - background task in the stub
                pass

        return asyncio.get_event_loop().create_task(runner())


def make_entry(config_dir: str, serial: str = "SER1", reuse: bool = False):
    from ha_hw_bridge.config_flow import HAHWBridgeConfigFlow  # noqa: F401, PLC0415

    class Entry:
        entry_id = "e1"

        def __init__(self) -> None:
            self.data = {
                "interface_ip": "192.168.1.2",
                "mac": "AABBCCDDEEFF",
                "serial": serial,
                CONF_REUSE_SERIAL: reuse,
            }
            self.options: dict = {}
            self.subentries: dict = {}
            self.version = 3
            self.title = serial

        def add_update_listener(self, callback):
            self._update_callback = callback
            return lambda: None

    return Entry()


CHILD_DATA = {
    "prod_id": "9MU7",
    "sub_prod_id": "00",
    "device_type": "119",
    "manufacturer": "002",
    "model": "haTest10",
    "friendly_name": "灯",
    "protocol_type": 6,
    "setup_type": 0,
    "known_fields_only": False,
    "room": "客厅",
    "services": [{"st": "switch", "sid": "switch"}],
    "bindings": [{"sid": "switch", "entities": ["light.lamp"]}],
}


def make_subentry(subentry_id: str):
    from ha_hw_bridge.config_flow import SUBENTRY_TYPE_CHILD  # noqa: PLC0415

    subentry = types.SimpleNamespace(
        subentry_id=subentry_id,
        subentry_type=SUBENTRY_TYPE_CHILD,
        title="灯",
        unique_id=f"child:{subentry_id}",
        data={"key": subentry_id, **CHILD_DATA},
    )
    return subentry


@unittest.skipUnless(HA_STUBBED, "real Home Assistant or voluptuous unavailable")
class SetupEntryTest(unittest.TestCase):
    def test_setup_compiles_the_subentry_plan(self):
        config_dir = tempfile.mkdtemp()
        entry = make_entry(config_dir)
        entry.subentries = {"SUBKEY01": make_subentry("SUBKEY01")}
        hass = FakeHass(entry, config_dir)
        hass.data[DOMAIN] = {
            "manager": FakeManager(),
            "runtimes": {},
            "forwarded_entries": set(),
            "reload_callbacks": {},
        }

        self.assertTrue(asyncio.run(INTEGRATION.async_setup_entry(hass, entry)))
        runtime = hass.data[DOMAIN]["manager"].created[0]
        self.assertEqual([child.key for child in runtime.plan.children], ["SUBKEY01"])

    def test_subentry_update_reapplies_the_plan(self):
        config_dir = tempfile.mkdtemp()
        entry = make_entry(config_dir)
        entry.subentries = {"SUBKEY01": make_subentry("SUBKEY01")}
        hass = FakeHass(entry, config_dir)
        hass.data[DOMAIN] = {
            "manager": FakeManager(),
            "runtimes": {},
            "forwarded_entries": set(),
            "reload_callbacks": {},
        }

        asyncio.run(INTEGRATION.async_setup_entry(hass, entry))
        runtime = hass.data[DOMAIN]["manager"].created[0]
        entry.subentries["SECOND01"] = make_subentry("SECOND01")
        asyncio.run(entry._update_callback(hass, entry))
        self.assertEqual(
            sorted(child.key for child in runtime.reloaded.children),
            ["SECOND01", "SUBKEY01"],
        )

    def test_unload_removes_runtime(self):
        config_dir = tempfile.mkdtemp()
        entry = make_entry(config_dir)
        hass = FakeHass(entry, config_dir)
        hass.data[DOMAIN] = {
            "manager": FakeManager(),
            "runtimes": {},
            "forwarded_entries": set(),
            "reload_callbacks": {},
        }
        asyncio.run(INTEGRATION.async_setup_entry(hass, entry))
        self.assertTrue(asyncio.run(INTEGRATION.async_unload_entry(hass, entry)))
        self.assertEqual(hass.data[DOMAIN]["runtimes"], {})


@unittest.skipUnless(HA_STUBBED, "real Home Assistant or voluptuous unavailable")
class LegacyAdoptionTest(unittest.TestCase):
    def _seed_legacy(self, config_dir: str, serial: str) -> Path:
        storage = Path(config_dir) / ".storage"
        material_dir = storage / "oneconnect_bridge" / "gateways" / serial / "cloud"
        material_dir.mkdir(parents=True)
        (material_dir / "material.json").write_text(
            json.dumps({"devId": "D1", "secret": "S1", "cloudPrimaryUrl": "h:1"}),
            encoding="utf-8",
        )
        (storage / "core.config_entries").write_text(
            json.dumps(
                {
                    "version": 1,
                    "data": {
                        "entries": [
                            {
                                "entry_id": "old1",
                                "domain": "oneconnect_bridge",
                                "data": {"serial": serial},
                                "subentries": {
                                    "OLDSUB001": {
                                        "subentry_id": "OLDSUB001",
                                        "subentry_type": "child",
                                        "title": "旧灯",
                                        "unique_id": "child:OLDSUB001",
                                        "data": {"key": "OLDSUB001", **CHILD_DATA},
                                    }
                                },
                            }
                        ]
                    },
                }
            ),
            encoding="utf-8",
        )
        return material_dir

    def test_storage_is_adopted_and_children_restored(self):
        config_dir = tempfile.mkdtemp()
        self._seed_legacy(config_dir, "OLDSER")
        entry = make_entry(config_dir, serial="OLDSER", reuse=True)
        hass = FakeHass(entry, config_dir)
        hass.data[DOMAIN] = {
            "manager": FakeManager(),
            "runtimes": {},
            "forwarded_entries": set(),
            "reload_callbacks": {},
        }

        self.assertTrue(asyncio.run(INTEGRATION.async_setup_entry(hass, entry)))
        self.assertEqual(sorted(entry.subentries), ["OLDSUB001"])
        runtime = hass.data[DOMAIN]["manager"].created[0]
        self.assertEqual([child.key for child in runtime.plan.children], ["OLDSUB001"])
        adopted = GatewayStore(config_dir, "OLDSER").read_json("cloud/material.json")
        self.assertEqual(adopted["devId"], "D1")
        self.assertTrue(
            (Path(config_dir) / ".storage" / "oneconnect_bridge").is_dir(),
            "the legacy directory must be kept as a backup",
        )

    def test_existing_children_are_not_imported_twice(self):
        config_dir = tempfile.mkdtemp()
        self._seed_legacy(config_dir, "OLDSER")
        entry = make_entry(config_dir, serial="OLDSER", reuse=True)
        entry.subentries = {"KEEP01": make_subentry("KEEP01")}
        hass = FakeHass(entry, config_dir)
        asyncio.run(INTEGRATION._restore_legacy_children(hass, entry, "OLDSER"))
        self.assertEqual(sorted(entry.subentries), ["KEEP01"])


@unittest.skipUnless(HA_STUBBED, "real Home Assistant or voluptuous unavailable")
class MigrationTest(unittest.TestCase):
    def test_version_two_subentries_get_a_stable_key(self):
        entry = make_entry(tempfile.mkdtemp())
        entry.version = 2
        subentry = make_subentry("LEGACYID")
        subentry.data = dict(CHILD_DATA)  # no key
        entry.subentries = {"LEGACYID": subentry}
        captured: dict = {}

        class RecordingEntries:
            def async_update_subentry(self, entry_, subentry_, **kwargs):
                captured["data"] = kwargs["data"]

            def async_update_entry(self, entry_, **kwargs):
                captured["version"] = kwargs.get("version")

        entry_hass = types.SimpleNamespace(config_entries=RecordingEntries())
        self.assertTrue(asyncio.run(INTEGRATION.async_migrate_entry(entry_hass, entry)))
        self.assertEqual(captured["data"]["key"], "LEGACYID")
        self.assertEqual(captured["version"], 3)


if __name__ == "__main__":
    unittest.main()