"""Typed, validated-at-startup configuration. See docs/07_TECHNICAL_ARCHITECTURE.md §58."""

from .settings import Environment, Settings, get_settings

__all__ = ["Environment", "Settings", "get_settings"]
