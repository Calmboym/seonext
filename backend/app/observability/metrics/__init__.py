"""In-process metrics registry (`prometheus_client`-backed). See
registry.py and docs/20_PROJECT_STRUCTURE.md §24."""

from .registry import (
    CONTENT_TYPE_LATEST,
    http_request_duration_seconds,
    http_requests_total,
    render_prometheus_text,
)

__all__ = [
    "CONTENT_TYPE_LATEST",
    "http_requests_total",
    "http_request_duration_seconds",
    "render_prometheus_text",
]
