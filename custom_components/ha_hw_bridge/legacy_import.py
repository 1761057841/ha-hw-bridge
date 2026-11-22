"""One-time import of child devices from a pre-rename config entry.

The integration used to be published as ``oneconnect_bridge``. Renaming the
domain leaves the old config entry unusable, and child devices live on that
entry, so a user who adopts an already-paired serial would otherwise have to
re-add every child device by hand (and each re-added child would register as a
new cloud device).

This module reads only ``.storage/core.config_entries`` and returns plain
dictionaries that the caller turns back into subentries. Every field is
validated defensively: an unreadable or unexpected file yields an empty list so
setup continues normally.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from .const import LEGACY_DOMAINS

_LOGGER = logging.getLogger(__name__)

_ENTRY_FILE = "core.config_entries"
_SUBENTRY_TYPE_CHILD = "child"


def legacy_child_payloads(config_dir: str, serial: str) -> list[dict[str, Any]]:
    """Return ``{title, unique_id, data}`` items stored under an old domain."""

    if not serial:
        return []
    path = Path(config_dir) / ".storage" / _ENTRY_FILE
    if not path.is_file():
        return []
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        _LOGGER.warning("Unable to read %s for legacy child import: %s", path, error)
        return []
    if not isinstance(document, dict):
        return []
    data = document.get("data")
    entries = data.get("entries") if isinstance(data, dict) else None
    if not isinstance(entries, list):
        return []

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        if entry.get("domain") not in LEGACY_DOMAINS:
            continue
        entry_data = entry.get("data")
        if not isinstance(entry_data, dict) or entry_data.get("serial") != serial:
            continue
        return _payloads_from_entry(entry)
    return []


def _payloads_from_entry(entry: dict[str, Any]) -> list[dict[str, Any]]:
    subentries = entry.get("subentries")
    if not isinstance(subentries, dict):
        return []
    payloads: list[dict[str, Any]] = []
    seen_unique_ids: set[str] = set()
    seen_subentry_ids: set[str] = set()
    for subentry in subentries.values():
        if not isinstance(subentry, dict):
            continue
        if subentry.get("subentry_type", _SUBENTRY_TYPE_CHILD) != _SUBENTRY_TYPE_CHILD:
            continue
        subentry_data = subentry.get("data")
        title = subentry.get("title")
        if not isinstance(subentry_data, dict) or not isinstance(title, str) or not title:
            continue
        unique_id = subentry.get("unique_id")
        if not isinstance(unique_id, str) or not unique_id:
            unique_id = None
        if unique_id is not None:
            if unique_id in seen_unique_ids:
                unique_id = None
            else:
                seen_unique_ids.add(unique_id)
        # Keep the original subentry id: it is the child key used by storage
        # directories and by the cloud child identity for UI-added devices.
        subentry_id = subentry.get("subentry_id")
        if not isinstance(subentry_id, str) or not subentry_id:
            subentry_id = None
        elif subentry_id in seen_subentry_ids:
            subentry_id = None
        else:
            seen_subentry_ids.add(subentry_id)
        payloads.append(
            {
                "title": title,
                "unique_id": unique_id,
                "subentry_id": subentry_id,
                "data": dict(subentry_data),
            }
        )
    return payloads