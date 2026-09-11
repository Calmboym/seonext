"""Password-recovery use cases (`PHASE-1.2` acceptance criterion 4: "the
account-recovery path has a real (if minimal) implementation, not a
stub").

Same dependency-injection rationale as `register.py`/`login.py` in this
package — read `register.py`'s module docstring first.

Design note on account enumeration (docs/07 §52, Security Testing):
`request_password_reset` returns `None` for both "no account exists for
this email" and "the account exists but is disabled" — the same outcome
a real attacker probing for valid emails would see either way. It never
raises for an unknown email. The caller
(`backend/app/api/routes/auth.py`) must always return the same generic
`PasswordResetRequestData.message` regardless of what this function
returns — the non-`None` case (the actual token) is not put in the HTTP
response body at all (see that function's own docstring for why: there
is no notification/email-delivery subsystem yet — `integrations/` is
empty by design, the same gap `tokens.py`'s own `PHASE-0.5` docstring
already named — so the route logs the token server-side instead, as this
phase's honest, minimal stand-in for a real delivery flow, not a stub of
the reset mechanism itself, which works correctly end-to-end given the
token).
"""

from __future__ import annotations

from typing import Protocol

from backend.app.application.errors import InvalidOrExpiredResetTokenError
from backend.app.domain.user.entity import User


class PasswordHasher(Protocol):
    def __call__(self, plain_password: str) -> str: ...


class ResetTokenIssuer(Protocol):
    def __call__(self, subject: str) -> str: ...


class ResetTokenDecoder(Protocol):
    """May raise on an invalid/expired/wrong-type token — this module
    does not know or care what exception type that is (it propagates
    unchanged from `confirm_password_reset`); the real implementation
    (`tokens.decode_password_reset_token`) raises
    `backend.app.security.authentication.tokens.TokenError`, which
    `backend/app/api/routes/auth.py`'s composition root imports directly
    to catch, since this module deliberately does not."""

    def __call__(self, token: str) -> str: ...


class UserReader(Protocol):
    async def get_by_email(self, email: str) -> User | None: ...

    async def get_by_id(self, user_id: str) -> User | None: ...


class UserWriter(Protocol):
    async def save(self, user: User) -> None: ...


async def request_password_reset(
    *,
    email: str,
    users: UserReader,
    issue_reset_token: ResetTokenIssuer,
) -> str | None:
    """Returns the freshly-minted reset token if (and only if) an active
    account exists for `email`; returns `None` otherwise. Never raises
    for "no such account" — see module docstring."""

    normalized_email = email.strip().lower()
    user = await users.get_by_email(normalized_email)
    if user is None or not user.is_active:
        return None
    return issue_reset_token(user.id)


async def confirm_password_reset(
    *,
    reset_token: str,
    new_password: str,
    decode_reset_token: ResetTokenDecoder,
    users: UserReader,
    user_writer: UserWriter,
    hash_password: PasswordHasher,
) -> None:
    """Raises whatever `decode_reset_token` raises for an invalid/expired
    token, unchanged. Raises `InvalidOrExpiredResetTokenError` itself if
    the token decodes successfully but no matching *active* user exists
    — an edge case a token-expiry check alone wouldn't catch (the account
    could have been disabled, or deleted, after the token was issued but
    before it was redeemed)."""

    user_id = decode_reset_token(reset_token)
    user = await users.get_by_id(user_id)
    if user is None or not user.is_active:
        raise InvalidOrExpiredResetTokenError(
            "reset token no longer corresponds to an active account"
        )

    updated_user = user.change_password_hash(hash_password(new_password))
    await user_writer.save(updated_user)
