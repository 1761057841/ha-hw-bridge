"""Huawei ``lightSwitch`` / ``childLockSwitch`` style boolean services.

Aliases of `child_lock_switch` with the appliance-light characteristic first.
Each module needs its own factory because the registry keys the adapter by
``service_id``, but the behaviour is shared.
"""

from __future__ import annotations

from .child_lock_switch import BinarySwitchServiceAdapter

ADAPTER = BinarySwitchServiceAdapter(
    "lightSwitch",
    "switch",
    aliases=("on", "lightSwitch", "switch", "action"),
)