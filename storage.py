from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
from typing import Any

from .const import DOMAIN, LEGACY_DOMAINS


class GatewayStore:
    """Store runtime material below HA's .storage directory."""

    def __init__(self, config_dir: str, serial: str) -> None:
        if not serial or any(char not in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_-" for char in serial):
            raise ValueError("gateway serial contains an unsafe path character")
        self._serial = serial
        self._storage_root = Path(config_dir) / ".storage"
        self._gateways_root = self._storage_root / DOMAIN / "gateways"
        self.root = self._gateways_root / serial
        if not self.root.is_dir():
            self._adopt_legacy_root(serial)
        self.root.mkdir(mode=0o700, parents=True, exist_ok=True)

    def _adopt_legacy_root(self, serial: str) -> None:
        """Copy this gateway's material from the pre-rename domain, once.

        The integration used to be stored as ``oneconnect_bridge``. Renaming
        the domain would otherwise force every existing gateway to pair again,
        so the old directory is copied over and left untouched as a backup.
        """

        for legacy in LEGACY_DOMAINS:
            source = (self._storage_root / legacy / "gateways" / serial).resolve()
            expected_parent = (self._storage_root / legacy / "gateways").resolve()
            if source.parent != expected_parent or source.name != serial:
                continue
            if not source.is_dir():
                continue
            self.root.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            shutil.copytree(source, self.root, dirs_exist_ok=False)
            return

    def path(self, relative: str) -> Path:
        path = (self.root / relative).resolve()
        if self.root.resolve() not in path.parents and path != self.root.resolve():
            raise ValueError("storage path escapes the gateway directory")
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        return path

    def read_json(self, relative: str) -> dict[str, Any] | None:
        path = self.path(relative)
        if not path.is_file():
            return None
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError(f"stored JSON object expected: {path}")
        return value

    def read_child_materials(self) -> dict[str, dict[str, Any]]:
        """Read all child material files in this gateway's storage scope."""

        children_root = self.root / "children"
        if not children_root.is_dir():
            return {}

        materials: dict[str, dict[str, Any]] = {}
        for child_root in sorted(children_root.iterdir(), key=lambda path: path.name):
            if not child_root.is_dir():
                continue
            material_path = child_root / "material.json"
            if not material_path.is_file():
                materials[child_root.name] = {}
                continue
            try:
                value = json.loads(material_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                value = None
            materials[child_root.name] = value if isinstance(value, dict) else {}
        return materials

    def write_json(self, relative: str, value: dict[str, Any]) -> Path:
        path = self.path(relative)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(
            json.dumps(value, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        os.chmod(temporary, 0o600)
        temporary.replace(path)
        os.chmod(path, 0o600)
        return path

    def remove_gateway(self) -> None:
        """Remove exactly this gateway's storage scope."""

        root = self.root.resolve()
        gateways_root = self._gateways_root.resolve()
        if root.parent != gateways_root or root.name != self._serial:
            raise ValueError("refusing to remove an unexpected gateway path")
        if root.is_dir():
            shutil.rmtree(root)

    def remove_child(self, key: str) -> None:
        """Remove exactly one child storage scope."""

        if not key or any(
            char not in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-"
            for char in key
        ):
            raise ValueError("child key contains an unsafe path character")
        children_root = (self.root / "children").resolve()
        child_root = (children_root / key).resolve()
        if child_root.parent != children_root or child_root.name != key:
            raise ValueError("refusing to remove an unexpected child path")
        if child_root.is_dir():
            shutil.rmtree(child_root)