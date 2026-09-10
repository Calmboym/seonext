"""Metrics registry.

Satisfies PHASE-0.7 acceptance criterion (2): "a metrics endpoint or
exporter is reachable" (.ai/WBS.md §4). Backed by `prometheus_client`
(newly declared in pyproject.toml by this subtask) rather than a
hand-rolled exposition-format writer — Prometheus text format has enough
edge cases (bucket cumulative semantics, label escaping, `+Inf` handling)
that reusing the standard, widely-verified library is the safer choice
even though it cannot be installed or import-tested in this session's
sandbox (no network access — the same limitation already recorded for
`fastapi`/`sqlalchemy`/`alembic`/`pydantic-settings` in PHASE-0.2-.4, see
.ai/PROJECT_STATE.md Risk R9).

Call sites (backend/app/api/middleware/logging.py,
backend/app/api/routes/metrics.py) import from this module rather than
from `prometheus_client` directly, so the library stays swappable behind
one seam — the same principle backend/app/infrastructure/database/
session.py already applies to SQLAlchemy.

Only foundation-level HTTP request metrics are registered here. Domain-
specific and AI-specific metrics (docs/20_PROJECT_STRUCTURE.md §24's AI
execution fields: model, provider, token usage, cost, etc.) are added by
the phases that introduce the thing being measured — nothing here
fabricates those ahead of an actual AI runtime, per PHASE-0.7's
acceptance criterion 3.

NOTE (PHASE-0.7, session 7): syntax-checked (`ast.parse`) only — not
import-tested or executed. `prometheus_client`'s actual API surface is
applied here from established knowledge of the library, not verified
against an installed copy this session.
"""

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest

http_requests_total = Counter(
    "http_requests_total",
    "Total HTTP requests processed, labeled by method, path, and status code.",
    labelnames=("method", "path", "status_code"),
)

http_request_duration_seconds = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds, labeled by method and path.",
    labelnames=("method", "path"),
)


def render_prometheus_text() -> bytes:
    """Render every registered metric in Prometheus text exposition
    format. Returns bytes, matching `prometheus_client.generate_latest`'s
    own return type — callers (backend/app/api/routes/metrics.py) pass
    this straight through as an HTTP response body."""

    return generate_latest()


__all__ = [
    "CONTENT_TYPE_LATEST",
    "http_requests_total",
    "http_request_duration_seconds",
    "render_prometheus_text",
]
