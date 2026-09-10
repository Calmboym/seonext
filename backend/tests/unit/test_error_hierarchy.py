"""Unit tests for the AppError hierarchy (backend/app/api/errors/exceptions.py).

Backend-unit category (.ai/WBS.md §4, PHASE-0.8's first named category).

Deliberately the one test file in this suite with zero third-party
imports — `backend.app.api.errors.exceptions` imports nothing beyond
`typing.Any`, so this file can be (and was) actually executed in a
plain-Python interpreter this session, not just syntax-checked. See the
`if __name__ == "__main__"` block at the bottom and .ai/PROJECT_STATE.md
§ 14 for the session-7 record of that run. Written in ordinary pytest
style (bare `assert`, no fixtures, no `pytest.raises`) specifically so it
remains both real-pytest-compatible *and* directly callable without
pytest installed — this is a deliberate exception to how the rest of
this suite is written, not the new house style.
"""

from backend.app.api.errors.exceptions import (
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


def test_every_app_error_subclass_maps_to_the_http_status_table_in_docs_07_section_20():
    """docs/07_TECHNICAL_ARCHITECTURE.md §20's status-code table is the
    single source of truth every AppError subclass must match — this test
    exists so an accidental edit to one class's `http_status` is caught
    immediately, rather than discovered the first time a client parses an
    unexpected status code."""

    expected_status_by_class = {
        ValidationAppError: 422,
        AuthenticationError: 401,
        AuthorizationError: 403,
        NotFoundAppError: 404,
        ConflictAppError: 409,
        RateLimitedError: 429,
        ProviderFailureError: 502,
        WorkflowFailureError: 500,
        UpstreamTimeoutError: 504,
        InternalError: 500,
    }
    for error_class, expected_status in expected_status_by_class.items():
        assert error_class.http_status == expected_status, (
            f"{error_class.__name__}.http_status was {error_class.http_status}, "
            f"expected {expected_status} per docs/07_TECHNICAL_ARCHITECTURE.md §20"
        )


def test_every_app_error_subclass_has_a_unique_stable_code():
    """`code` is the machine-readable identifier clients branch on
    (docs/07_TECHNICAL_ARCHITECTURE.md §19) — two subclasses accidentally
    sharing one would silently merge two distinct failure modes from a
    caller's perspective."""

    all_subclasses = [
        ValidationAppError,
        AuthenticationError,
        AuthorizationError,
        NotFoundAppError,
        ConflictAppError,
        RateLimitedError,
        ProviderFailureError,
        WorkflowFailureError,
        UpstreamTimeoutError,
        InternalError,
    ]
    codes = [cls.code for cls in all_subclasses]
    assert len(codes) == len(set(codes)), f"duplicate AppError .code values found: {codes}"


def test_rate_limited_and_provider_and_timeout_errors_are_marked_retryable():
    """`retryable` drives client backoff behavior — a transient failure
    (429/502/504) marked non-retryable would tell a well-behaved client
    to give up on something that might succeed on retry."""

    assert RateLimitedError.retryable is True
    assert ProviderFailureError.retryable is True
    assert UpstreamTimeoutError.retryable is True


def test_validation_and_auth_and_notfound_errors_are_not_marked_retryable():
    """The inverse of the above: a client-caused failure (422/401/403/404)
    marked retryable would tell a client to blindly resend a request that
    will fail identically every time."""

    assert ValidationAppError.retryable is False
    assert AuthenticationError.retryable is False
    assert AuthorizationError.retryable is False
    assert NotFoundAppError.retryable is False


def test_app_error_carries_its_message_and_optional_details():
    """The base class's constructor is what every handler
    (backend/app/api/errors/handlers.py) reads `message`/`details` off
    of — a regression here would silently drop error context from every
    single error response."""

    error_without_details = NotFoundAppError("topic 123 not found")
    assert error_without_details.message == "topic 123 not found"
    assert error_without_details.details is None
    assert str(error_without_details) == "topic 123 not found"

    error_with_details = ValidationAppError(
        "invalid topic slug", details={"field": "slug", "reason": "must be lowercase"}
    )
    assert error_with_details.message == "invalid topic slug"
    assert error_with_details.details == {"field": "slug", "reason": "must be lowercase"}


def test_app_error_subclasses_are_actually_exceptions():
    """Every subclass must be raisable — a typo turning `class Foo(AppError)`
    into `class Foo:` would break every `raise Foo(...)` call site at
    first use, not at import time, unless a test like this catches it
    first."""

    for error_class in (NotFoundAppError, AuthenticationError, ValidationAppError):
        assert issubclass(error_class, AppError)
        assert issubclass(error_class, Exception)
        try:
            raise error_class("test")
        except error_class as caught:
            assert caught.message == "test"


if __name__ == "__main__":
    # Manual runner: this file has zero third-party dependencies (see
    # module docstring), so it can be executed directly with `python3
    # backend/tests/unit/test_error_hierarchy.py` even in an environment
    # with no pytest installed — which is exactly this session's sandbox.
    # This is how these six tests were actually run and confirmed passing
    # in session 7 (.ai/PROJECT_STATE.md § 14), not merely ast.parse'd.
    test_functions = [
        test_every_app_error_subclass_maps_to_the_http_status_table_in_docs_07_section_20,
        test_every_app_error_subclass_has_a_unique_stable_code,
        test_rate_limited_and_provider_and_timeout_errors_are_marked_retryable,
        test_validation_and_auth_and_notfound_errors_are_not_marked_retryable,
        test_app_error_carries_its_message_and_optional_details,
        test_app_error_subclasses_are_actually_exceptions,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
