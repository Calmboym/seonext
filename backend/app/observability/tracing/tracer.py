"""Lightweight in-process span tracking.

docs/07_TECHNICAL_ARCHITECTURE.md §3 lists `tracing` as part of the
observability stack without mandating a specific backend/exporter. At
PHASE-0 there is no distributed system to trace across (a single FastAPI
process, no workers, no external service calls yet — `integrations/` is
empty by design) and no tracing backend (Jaeger/Tempo/etc.) is wired up.
Rather than pull in a full OpenTelemetry SDK (with its exporter
configuration, resource attributes, and sampler setup) for a foundation
that has nothing yet to export to, this module provides the minimum
useful primitive — a named span that logs its own start/end and duration
via backend/app/observability/logging — matching the same "placeholder
now, real implementation once the later phase that needs it arrives"
approach `backend/app/infrastructure/config/settings.py`'s
`RuntimeSettings` already takes for AI-runtime routing.

A later phase wiring a real tracing backend can replace `start_span`'s
body with actual span creation (e.g. OpenTelemetry) without changing call
sites, since callers only ever do:

    with start_span("some_operation"):
        ...

NOTE (PHASE-0.7, session 7): syntax-checked (`ast.parse`) only — not
executed. Zero third-party imports, so it would import cleanly under any
stdlib-only interpreter, but "would import cleanly" is not the same as
"has been run" — its actual runtime behavior (context propagation across
awaits, log output) is UNVERIFIED this session.
"""

import time
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar

from backend.app.api.middleware.request_id import get_request_id
from backend.app.observability.logging import get_logger

logger = get_logger("seonex.tracing")

_span_path: ContextVar[tuple[str, ...]] = ContextVar("span_path", default=())


@contextmanager
def start_span(name: str) -> Iterator[None]:
    """Mark a named span. Spans nest: a `start_span("b")` opened inside an
    outer `start_span("a")` block logs its `span_path` as `"a.b"`, so
    nesting is visible in the structured log output without needing a
    real trace-ID/span-ID propagation scheme yet (reserved for the later
    phase that wires a real backend — see module docstring)."""

    parent_path = _span_path.get()
    full_path = parent_path + (name,)
    token = _span_path.set(full_path)
    started = time.perf_counter()
    request_id = get_request_id()

    logger.info(
        "span_start",
        extra={"span": name, "span_path": ".".join(full_path), "request_id": request_id},
    )
    try:
        yield
    finally:
        duration_ms = (time.perf_counter() - started) * 1000
        logger.info(
            "span_end",
            extra={
                "span": name,
                "span_path": ".".join(full_path),
                "request_id": request_id,
                "duration_ms": round(duration_ms, 3),
            },
        )
        _span_path.reset(token)
