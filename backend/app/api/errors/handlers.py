"""Exception handlers: the one place every error path is converted into the
standard envelope (backend/app/api/schemas/errors.py) with correct HTTP
semantics (docs/07_TECHNICAL_ARCHITECTURE.md §20).

Three cases are handled, covering every response that can leave this API:

1. `AppError` (and subclasses, backend/app/api/errors/exceptions.py) —
   application/domain code raised something specific; render it as-is.
2. `RequestValidationError` — FastAPI/Pydantic rejected malformed input
   *before* it reached any route handler body, satisfying the PHASE-0.4
   acceptance criterion "malformed input is rejected before reaching any
   domain logic placeholder" (.ai/WBS.md §4) structurally, via the
   framework's own request-parsing boundary.
3. Anything else (`Exception`) — an unhandled/unexpected error. Rendered
   as a bare 500 with no `details`, so an internal stack trace is never
   exposed to the end user (§19's explicit requirement).

Register all three via `register_exception_handlers(app)` in
backend/app/main.py.
"""

import logging

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from backend.app.api.errors.exceptions import AppError
from backend.app.api.middleware.request_id import get_request_id
from backend.app.api.schemas.errors import ErrorBody, ErrorResponse

logger = logging.getLogger(__name__)


def _envelope(*, code: str, message: str, details: dict | None, retryable: bool) -> dict:
    return ErrorResponse(
        error=ErrorBody(
            code=code,
            message=message,
            details=details,
            request_id=get_request_id(),
            retryable=retryable,
        )
    ).model_dump(mode="json")


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    return JSONResponse(
        status_code=exc.http_status,
        content=_envelope(
            code=exc.code,
            message=exc.message,
            details=exc.details,
            retryable=exc.retryable,
        ),
    )


async def validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    # exc.errors() is already structured (field path, message, type) —
    # exactly the "structured_context" §19 asks for in `details`. Never
    # includes a stack trace.
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=_envelope(
            code="VALIDATION_FAILED",
            message="Request validation failed.",
            details={"errors": exc.errors()},
            retryable=False,
        ),
    )


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    # Log the full exception server-side (with request_id for correlation)
    # but never surface it to the client — §19: "Internal stack traces
    # must not be exposed to end users."
    logger.exception("Unhandled exception", extra={"request_id": get_request_id()})
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=_envelope(
            code="INTERNAL_ERROR",
            message="An unexpected error occurred.",
            details=None,
            retryable=False,
        ),
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)
