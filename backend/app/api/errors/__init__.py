"""Error architecture. See docs/07_TECHNICAL_ARCHITECTURE.md §19 (Error Architecture), §20 (HTTP Error Semantics).

Re-exports only the AppError hierarchy (exceptions.py), which has zero
third-party imports. `register_exception_handlers` (handlers.py) is
deliberately NOT re-exported here — handlers.py imports `fastapi`, and
nothing in this codebase actually imports `register_exception_handlers`
via this package's top level (backend/app/main.py imports it directly
from `.handlers`); re-exporting it here would force every caller of
`from backend.app.api.errors import AppError`-style imports to have
fastapi installed even when they only want the exception classes —
exactly the coupling backend/tests/unit/test_error_hierarchy.py (PHASE-0.8)
relies on NOT existing. Import from `.handlers` directly if you need
`register_exception_handlers`.
"""

from .exceptions import (
    AppError,
    AuthenticationError,
    AuthorizationError,
    ConflictAppError,
    InternalError,
    NotFoundAppError,
    ProviderFailureError,
    RateLimitedError,
    UpstreamTimeoutError,
    ValidationAppError,
    WorkflowFailureError,
)

__all__ = [
    "AppError",
    "AuthenticationError",
    "AuthorizationError",
    "ConflictAppError",
    "InternalError",
    "NotFoundAppError",
    "ProviderFailureError",
    "RateLimitedError",
    "UpstreamTimeoutError",
    "ValidationAppError",
    "WorkflowFailureError",
]
