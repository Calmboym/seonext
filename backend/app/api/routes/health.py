"""Health-check endpoint.

The only route in scope for PHASE-0.4 (.ai/WBS.md §4: "No domain endpoints
... are in scope; those belong to the phases that build the domains behind
them."). Deliberately has no request body/query parameters to validate —
malformed-input rejection is demonstrated structurally by the
RequestValidationError handler (backend/app/api/errors/handlers.py) being
wired and ready for the first endpoint that does take input.

`response_model=HealthResponse` added by PHASE-0.8 (Testing Foundation &
CI) — the route's behavior is unchanged; this only gives the response a
declared, importable contract for backend/tests/contract/
test_response_schemas.py to validate against.
"""

from fastapi import APIRouter

from backend.app.api.schemas.health import HealthResponse

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health() -> dict[str, str]:
    """Liveness check. Returns 200 with a fixed shape if the process is up
    and able to handle a request. Does not check the database or any other
    dependency — that is a deliberately separate concern (a readiness
    check), not introduced here to keep this subtask's scope to exactly
    what .ai/WBS.md §4 asks for.
    """

    return {"status": "ok"}
