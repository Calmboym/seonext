"""Application-layer errors.

Per docs/07_TECHNICAL_ARCHITECTURE.md §14 (Dependency Direction: API →
Application → ... ), the API layer depends on the Application layer, not
the reverse — so, exactly like
`backend.app.security.authentication.tokens.TokenError`
(`PHASE-0.5`) and `backend.app.domain.user.entity.UserDomainError`
(`PHASE-1.1`) before it, these are plain exceptions, not
`backend.app.api.errors.exceptions.AppError` subclasses. Translating one
of these into an HTTP-appropriate `AppError` (and status code) is
`backend/app/api/routes/auth.py`'s job, in exactly one place, so the
mapping doesn't get duplicated or drift.
"""

from __future__ import annotations


class ApplicationError(Exception):
    """Base class for every error an application-layer use case raises."""


class EmailAlreadyRegisteredError(ApplicationError):
    """Raised by the register use case when the email is already taken.
    Maps to `ConflictAppError` (409) at the API boundary."""


class InvalidCredentialsError(ApplicationError):
    """Raised by the login use case for *either* an unknown email or a
    wrong password — deliberately the same error either way (docs/07 §52,
    Security Testing: a login endpoint that distinguishes "no such user"
    from "wrong password" leaks which emails have accounts). Maps to
    `AuthenticationError` (401) at the API boundary."""


class AccountDisabledError(ApplicationError):
    """Raised by the login use case when the account exists, the password
    is correct, but the account has been deactivated
    (`backend.app.domain.user.entity.UserStatus.DISABLED`). Kept distinct
    from `InvalidCredentialsError` internally (a disabled account is not
    the same failure mode as a wrong password and a future session may
    want to log/alert on it differently), but still maps to the same
    `AuthenticationError` (401) at the API boundary today — a disabled
    account is not information a login response should distinguish for
    an external caller either, at least not until this project has an
    actual "your account was disabled, contact support" support flow to
    point them to."""


class InvalidOrExpiredResetTokenError(ApplicationError):
    """Raised by the password-reset-confirm use case when the reset token
    is malformed, expired, or was not issued as a password-reset token.
    Maps to `AuthenticationError` (401) at the API boundary — proving
    control of the reset token *is* the authentication step for this
    flow, there being no other credential involved."""
