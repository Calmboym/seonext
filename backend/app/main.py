"""FastAPI application factory.

This is the one place the API application is assembled: routes,
middleware, exception handlers, versioning prefix. `apps/api/main.py`
(the thin, runnable entrypoint per docs/20_PROJECT_STRUCTURE.md §5.1)
imports `app` from here rather than duplicating this wiring.

NOTE (PHASE-0.4, session 6; extended PHASE-0.7, session 7): fastapi/
uvicorn/prometheus_client are declared in pyproject.toml but were NOT
installed in this session's sandbox (no network access), so this module
has been syntax-checked (ast.parse) only — it has never actually been
imported or run. The acceptance criteria "API boots locally" and
"/api/v1/health responds" (.ai/WBS.md §4, PHASE-0.4) remain IMPLEMENTED
but UNVERIFIED at runtime, and the same now applies to PHASE-0.7's
observability wiring below. See .ai/PROJECT_STATE.md § 14 and Risk R9.
"""

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from backend.app.api.errors.handlers import register_exception_handlers
from backend.app.api.middleware.logging import request_logging_middleware
from backend.app.api.middleware.request_id import request_id_middleware
from backend.app.api.routes import v1_router
from backend.app.api.routes.metrics import router as metrics_router
from backend.app.infrastructure.config import get_settings
from backend.app.observability.logging import configure_logging

API_V1_PREFIX = "/api/v1"


def create_app() -> FastAPI:
    configure_logging()
    settings = get_settings()

    app = FastAPI(
        title="Seonex API",
        version="0.1.0",
        debug=settings.app.debug,
    )

    # Starlette's `add_middleware` inserts each new entry at the *front*
    # of its internal middleware list, so the middleware added LAST ends
    # up OUTERMOST and runs FIRST on the way in (and last on the way out).
    # request_id_middleware is added second (last) here specifically so it
    # runs first, setting the request ID in a ContextVar *before*
    # request_logging_middleware (added first, so inner) reads it via
    # get_request_id() — get the order backwards and every log line for
    # a request would show an empty request_id.
    app.add_middleware(BaseHTTPMiddleware, dispatch=request_logging_middleware)
    app.add_middleware(BaseHTTPMiddleware, dispatch=request_id_middleware)
    register_exception_handlers(app)
    app.include_router(v1_router, prefix=API_V1_PREFIX)
    app.include_router(metrics_router)  # unversioned — see routes/metrics.py

    return app


# Module-level instance for ASGI servers (`uvicorn backend.app.main:app`)
# and for apps/api/main.py to import directly.
app = create_app()
