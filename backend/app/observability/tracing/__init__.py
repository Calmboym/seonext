"""Lightweight in-process span tracking (no external tracing backend
wired yet). See tracer.py."""

from .tracer import start_span

__all__ = ["start_span"]
