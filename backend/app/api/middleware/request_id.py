"""Request-ID middleware.

Every response carries a request ID: reused from an incoming `X-Request-ID`
header if the caller supplied one (useful for tracing across services),
otherwise generated fresh. Stored in a ContextVar so error handlers
(backend/app/api/errors/handlers.py) can read it without threading it
through every function signature, and so PHASE-0.7 (Observability
Foundation, not yet authorized) can attach it to structured log lines
without redesigning this middleware.

This directly supports the `request_id` field required by the error
envelope in docs/07_TECHNICAL_ARCHITECTURE.md §19.
"""

import uuid
from collections.abc import Awaitable, Callable
from contextvars import ContextVar

from starlette.requests import Request
from starlette.responses import Response

_request_id_ctx: ContextVar[str] = ContextVar("request_id", default="")

REQUEST_ID_HEADER = "X-Request-ID"


def get_request_id() -> str:
    """Current request's ID, or "" outside a request context (e.g. at
    import time — callers needing a guaranteed value should call this only
    from within a request-handling path)."""

    return _request_id_ctx.get()


async def request_id_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    incoming = request.headers.get(REQUEST_ID_HEADER)
    request_id = incoming if incoming else f"req_{uuid.uuid4().hex}"
    token = _request_id_ctx.set(request_id)
    try:
        response = await call_next(request)
    finally:
        _request_id_ctx.reset(token)
    response.headers[REQUEST_ID_HEADER] = request_id
    return response
