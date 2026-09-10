"""Contract tests: does each declared response schema accept the shapes
it should and reject the shapes it shouldn't — independent of any live
HTTP round trip (that's backend/tests/api/test_health_endpoint.py's job).

Contract-tests category (docs/20_PROJECT_STRUCTURE.md §61's CI stage
order; .ai/WBS.md §4, PHASE-0.8). Validates
backend/app/api/schemas/health.py's `HealthResponse` (introduced by this
same subtask so there was a concrete contract to test) and
backend/app/api/schemas/errors.py's `ErrorResponse`/`ErrorBody`
(PHASE-0.4).

NOTE (PHASE-0.8, session 7): requires `pydantic`, not installed in this
session's sandbox (Risk R9). Syntax-checked (`ast.parse`) only.
"""

import pytest
from pydantic import ValidationError


class TestHealthResponseContract:
    def test_a_status_ok_body_satisfies_the_health_response_contract(self):
        from backend.app.api.schemas.health import HealthResponse

        parsed = HealthResponse.model_validate({"status": "ok"})

        assert parsed.status == "ok"

    def test_a_body_missing_status_violates_the_health_response_contract(self):
        from backend.app.api.schemas.health import HealthResponse

        with pytest.raises(ValidationError):
            HealthResponse.model_validate({})


class TestErrorResponseContract:
    def test_a_well_formed_error_body_satisfies_the_error_response_contract(self):
        """Mirrors the exact shape documented in
        backend/app/api/schemas/errors.py's module docstring, which
        itself mirrors docs/07_TECHNICAL_ARCHITECTURE.md §19 — this test
        exists so an accidental field rename in ErrorBody is caught here,
        not the first time a real error response fails to parse
        client-side."""
        from backend.app.api.schemas.errors import ErrorBody, ErrorResponse

        parsed = ErrorResponse.model_validate(
            {
                "error": {
                    "code": "VALIDATION_FAILED",
                    "message": "The topic slug must be lowercase.",
                    "details": {"field": "slug"},
                    "request_id": "req_123",
                    "retryable": False,
                }
            }
        )

        assert isinstance(parsed.error, ErrorBody)
        assert parsed.error.code == "VALIDATION_FAILED"
        assert parsed.error.retryable is False

    def test_an_error_body_missing_a_required_field_violates_the_contract(self):
        """`request_id` has no default (backend/app/api/schemas/errors.py)
        — every error response must be traceable to server-side logs;
        this test protects that requirement from silently becoming
        optional."""
        from backend.app.api.schemas.errors import ErrorResponse

        with pytest.raises(ValidationError):
            ErrorResponse.model_validate(
                {
                    "error": {
                        "code": "VALIDATION_FAILED",
                        "message": "The topic slug must be lowercase.",
                        "retryable": False,
                        # request_id deliberately omitted
                    }
                }
            )

    def test_error_details_defaults_to_none_when_omitted(self):
        """`details` is optional (not every error has structured
        context) — but the default must be `None`, not an empty dict,
        so a client can distinguish "no details were provided" from
        "details were provided as an empty object"."""
        from backend.app.api.schemas.errors import ErrorResponse

        parsed = ErrorResponse.model_validate(
            {
                "error": {
                    "code": "NOT_FOUND",
                    "message": "Topic not found.",
                    "request_id": "req_456",
                    "retryable": False,
                }
            }
        )

        assert parsed.error.details is None
