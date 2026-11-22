"""Huawei ``colourMode`` enum service for lights.

Same shape and behaviour as ``lightMode`` (one ``mode`` enum, RW); the registry
needs a distinct adapter because it keys by ``service_id``.
"""

from __future__ import annotations

from .light_mode import LightModeServiceAdapter

ADAPTER = LightModeServiceAdapter("colourMode")