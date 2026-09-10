"""Health-check response schema.

Introduced by PHASE-0.8 (Testing Foundation & CI) so the health endpoint
(PHASE-0.4) has a concrete, importable contract for
backend/tests/contract/test_response_schemas.py to validate against —
mirroring how backend/app/api/schemas/errors.py already gives every error
response a typed shape. `backend/app/api/routes/health.py` declares this
as its `response_model`; the route's actual returned dict is unchanged.
"""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Body of a successful `GET /api/v1/health` response."""

    status: str = Field(..., description="Liveness indicator. 'ok' if the process can handle a request.")
