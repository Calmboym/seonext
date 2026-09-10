"""Application error hierarchy.

Maps the response-contract categories from docs/07_TECHNICAL_ARCHITECTURE.md
§18 (success / validation failure / authorization failure / not found /
conflict / provider failure / workflow failure / partial result) onto the
HTTP semantics table in §20:

    400 → malformed request
    401 → unauthenticated
    403 → unauthorized
    404 → resource unavailable
    409 → state/conflict
    422 → validation failure
    429 → rate limited
    500 → internal failure
    502/503 → external dependency failure
    504 → timeout

"Partial result" (§18) is not modeled here — it describes a *successful*
response shape carrying incompleteness metadata, not an error, and has no
concrete meaning until a domain endpoint exists to return one (none do at
PHASE-0). Left for the phase that introduces the first such endpoint.

Raise one of these from application/domain code; backend/app/api/errors/
handlers.py converts it into the ErrorResponse envelope
(backend/app/api/schemas/errors.py). Route handlers should not construct
ErrorResponse directly — raise the appropriate AppError subclass instead,
so the mapping stays centralized in one place.
"""

from typing import Any


class AppError(Exception):
    """Base class for every error the API layer knows how to render.

    Not meant to be raised directly — raise one of the subclasses below,
    or add a new one if none fits, rather than reaching for a generic
    Exception (which handlers.py renders as an opaque 500 with no
    `details`, since an unrecognized exception's internals must not leak
    to the client per §19).
    """

    code: str = "APP_ERROR"
    http_status: int = 500
    retryable: bool = False

    def __init__(self, message: str, *, details: dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details


class ValidationAppError(AppError):
    """422 — validation failure. Framework-level request-shape validation
    (missing/malformed fields) is handled automatically by FastAPI/Pydantic
    before a route body ever runs (see handlers.py's RequestValidationError
    handler); raise this directly for *domain*-level validation failures
    that Pydantic's schema validation can't express."""

    code = "VALIDATION_FAILED"
    http_status = 422
    retryable = False


class AuthenticationError(AppError):
    """401 — unauthenticated. Raise this from a route once PHASE-1 wires
    a `get_current_user`-style dependency around
    backend/app/security/authentication/tokens.py's `decode_access_token`
    (PHASE-0.5) — no protected route exists yet to raise it from."""

    code = "UNAUTHENTICATED"
    http_status = 401
    retryable = False


class AuthorizationError(AppError):
    """403 — unauthorized. Per-resource authorization is explicitly out of
    scope until PHASE-1 (see .ai/WBS.md §4, PHASE-0.5's acceptance
    criteria); reserved for when it exists."""

    code = "UNAUTHORIZED"
    http_status = 403
    retryable = False


class NotFoundAppError(AppError):
    """404 — resource unavailable."""

    code = "NOT_FOUND"
    http_status = 404
    retryable = False


class ConflictAppError(AppError):
    """409 — state/conflict."""

    code = "CONFLICT"
    http_status = 409
    retryable = False


class RateLimitedError(AppError):
    """429 — rate limited. No rate limiter exists yet (docs/07_TECHNICAL_
    ARCHITECTURE.md §69 is out of PHASE-0 scope); reserved for when one
    does."""

    code = "RATE_LIMITED"
    http_status = 429
    retryable = True


class ProviderFailureError(AppError):
    """502 — external dependency failure. No external provider integration
    exists yet at PHASE-0 (integrations/ is empty by design); reserved."""

    code = "PROVIDER_FAILURE"
    http_status = 502
    retryable = True


class WorkflowFailureError(AppError):
    """500 — internal failure, workflow-specific. No workflow engine exists
    yet (backend/app/orchestration/ is empty); reserved."""

    code = "WORKFLOW_FAILURE"
    http_status = 500
    retryable = False


class UpstreamTimeoutError(AppError):
    """504 — timeout."""

    code = "UPSTREAM_TIMEOUT"
    http_status = 504
    retryable = True


class InternalError(AppError):
    """500 — internal failure, generic. Prefer a more specific subclass
    where one applies."""

    code = "INTERNAL_ERROR"
    http_status = 500
    retryable = False
