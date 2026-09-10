"""Structured request logging + metrics middleware.

Satisfies both PHASE-0.7 acceptance criteria in one pass over every
request (.ai/WBS.md §4):

    (1) "each request is logged with structured fields (not raw string
        logs)" — via backend/app/observability/logging.
    (2) "a metrics endpoint or exporter is reachable" — this middleware is
        what actually *populates* the counters/histogram that
        backend/app/api/routes/metrics.py's `/metrics` endpoint renders.

Registered in backend/app/main.py's `create_app()`, alongside
request_id_middleware — see that function's comment for the exact
add_middleware ordering this depends on (request_id_middleware must run
*before* this middleware, so `get_request_id()` below returns a real
value, not the empty-string default).
"""

import time
from collections.abc import Awaitable, Callable

from starlette.requests import Request
from starlette.responses import Response

from backend.app.api.middleware.request_id import get_request_id
from backend.app.observability.logging import get_logger
from backend.app.observability.metrics import http_request_duration_seconds, http_requests_total

logger = get_logger("seonex.request")


async def request_logging_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    started = time.perf_counter()
    response = await call_next(request)
    duration_seconds = time.perf_counter() - started

    # `request.url.path` is the raw path, not a route *template*. PHASE-0
    # has exactly one real route (`/api/v1/health`, no path parameters),
    # so raw-path and template are identical today and cardinality is
    # bounded. A later phase adding parameterized routes (e.g.
    # `/entities/{id}`) should switch this to the route template (e.g.
    # `request.scope["route"].path`) before label cardinality grows
    # unbounded — flagged here rather than silently left as a footgun.
    method = request.method
    path = request.url.path
    status_code = str(response.status_code)

    http_requests_total.labels(method=method, path=path, status_code=status_code).inc()
    http_request_duration_seconds.labels(method=method, path=path).observe(duration_seconds)

    logger.info(
        "request_handled",
        extra={
            "request_id": get_request_id(),
            "http_method": method,
            "http_path": path,
            "http_status_code": response.status_code,
            "duration_ms": round(duration_seconds * 1000, 3),
        },
    )
    return response
