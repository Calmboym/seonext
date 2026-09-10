"""Structured (JSON) logging configuration.

Satisfies PHASE-0.7 acceptance criterion (1): "each request is logged with
structured fields (not raw string logs)" (.ai/WBS.md §4). Deliberately
dependency-free (no `structlog`/`python-json-logger`) — the Python
standard library's `logging` module, plus a small custom `Formatter`, is
sufficient for this foundation-level need, and avoids introducing a new
external dependency this sandbox cannot install or verify anyway (no
network access — the same limitation recorded for `fastapi`/`sqlalchemy`/
`alembic` in PHASE-0.2-.4, see .ai/PROJECT_STATE.md Risk R9). A later
phase may swap the formatter implementation without touching call sites,
since callers only use `configure_logging()` / `get_logger()` below —
matching the same swappability principle
backend/app/observability/metrics/registry.py applies to `prometheus_client`.

NOTE (PHASE-0.7, session 7): this module is syntax-checked (`ast.parse`)
only — it has never been imported or executed (no Python interpreter with
this project's dependencies installed was available this session either,
though this specific module has zero third-party imports and would import
cleanly under any stdlib-only interpreter; it has still not been *run*, so
`configure_logging()`'s actual runtime behavior is UNVERIFIED, not merely
its syntax).
"""

import json
import logging
import sys
from typing import Any

from backend.app.infrastructure.config import get_settings

# Attributes every stdlib LogRecord carries. Anything in `record.__dict__`
# beyond these came from a caller's `extra={...}` and should be surfaced as
# a structured field (e.g. `request_id`, `duration_ms` — see
# backend/app/api/middleware/logging.py).
_STANDARD_RECORD_ATTRS = frozenset(
    {
        "name",
        "msg",
        "args",
        "levelname",
        "levelno",
        "pathname",
        "filename",
        "module",
        "exc_info",
        "exc_text",
        "stack_info",
        "lineno",
        "funcName",
        "created",
        "msecs",
        "relativeCreated",
        "thread",
        "threadName",
        "processName",
        "process",
        "asctime",
        "taskName",
    }
)

_CONFIGURED = False


class JSONFormatter(logging.Formatter):
    """Renders one JSON object per log line: timestamp, level, logger name,
    message, any `extra=` fields, and a formatted exception if present.
    Never emits a raw unstructured string — satisfies PHASE-0.7 criterion
    (1) by construction, for every logger that uses this formatter."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S%z"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        for key, value in record.__dict__.items():
            if key in _STANDARD_RECORD_ATTRS:
                continue
            payload[key] = value
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, default=str)


def configure_logging() -> None:
    """Wire the root logger to emit JSON lines on stdout at the configured
    level (backend/app/infrastructure/config/settings.py's
    `ApplicationSettings.log_level`). Idempotent — safe to call more than
    once (e.g. once from `create_app()` and once from a test fixture)
    without duplicating handlers. Call this once, early, at process
    startup (backend/app/main.py's `create_app()`), matching the same
    "validate/configure at startup, not lazily" principle
    `get_settings()` already applies."""

    global _CONFIGURED
    if _CONFIGURED:
        return

    settings = get_settings()

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(JSONFormatter())

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(settings.app.log_level.upper())

    _CONFIGURED = True


def get_logger(name: str) -> logging.Logger:
    """Thin wrapper around `logging.getLogger` so call sites import from
    this module rather than reaching for stdlib `logging` directly —
    keeps the JSON-formatting behavior swappable in one place."""

    return logging.getLogger(name)
