"""Standard error response envelope.

Matches docs/07_TECHNICAL_ARCHITECTURE.md §19 exactly:

    error:
      code: TOPIC_VALIDATION_FAILED
      message: Human-readable description
      details: structured_context
      request_id: req_123
      retryable: false

Every error response from this API — validation failures, domain errors,
provider failures, unhandled exceptions — is serialized through this
shape. Internal stack traces are never included in `details` (§19: "Internal
stack traces must not be exposed to end users.").
"""

from typing import Any

from pydantic import BaseModel, Field


class ErrorBody(BaseModel):
    code: str = Field(..., description="Stable, machine-readable error code, e.g. VALIDATION_FAILED.")
    message: str = Field(..., description="Human-readable description. Safe to display to an end user.")
    details: dict[str, Any] | None = Field(
        default=None,
        description="Structured context (e.g. which fields failed validation). Never a raw stack trace.",
    )
    request_id: str = Field(..., description="Correlates this response with server-side logs.")
    retryable: bool = Field(..., description="Whether retrying the same request might succeed.")


class ErrorResponse(BaseModel):
    """Top-level response body for every non-2xx response."""

    error: ErrorBody
