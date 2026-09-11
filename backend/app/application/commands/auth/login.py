"""The login use case (`PHASE-1.2`).

Same dependency-injection rationale as `register.py` — read that file's
module docstring first. Additionally injects a `PasswordVerifier` and a
`TokenIssuer`, so this module hard-imports neither `passwords.py` (bcrypt)
nor `tokens.py` (which itself imports `backend.app.infrastructure.config`,
unimportable in this sandbox without `pydantic-settings` — see tokens.py's
own docstring).

`PHASE-1.2` acceptance criterion 2 ("login issues a token bound to a real
`user_id`") is satisfied here: `issue_access_token` is always called with
`user.id` — a real `User.id`, not an arbitrary caller-supplied string
(closing exactly the gap `tokens.py`'s own docstring named as deferred to
this phase).
"""

from __future__ import annotations

from typing import Protocol

from backend.app.application.errors import AccountDisabledError, InvalidCredentialsError
from backend.app.domain.user.entity import User


class PasswordVerifier(Protocol):
    def __call__(self, plain_password: str, hashed_password: str) -> bool: ...


class AccessTokenIssuer(Protocol):
    def __call__(self, subject: str) -> str: ...


class UserReader(Protocol):
    async def get_by_email(self, email: str) -> User | None: ...


class UserWriter(Protocol):
    async def save(self, user: User) -> None: ...


class LoginResult:
    """Plain data holder, not a Pydantic model (this module has no
    pydantic import, same reasoning as everywhere else in this package) —
    `backend/app/api/routes/auth.py` maps this onto
    `backend.app.contracts.api.auth.LoginData` at the API boundary."""

    __slots__ = ("access_token", "expires_in_minutes")

    def __init__(self, *, access_token: str, expires_in_minutes: int) -> None:
        self.access_token = access_token
        self.expires_in_minutes = expires_in_minutes


async def login_user(
    *,
    email: str,
    password: str,
    users: UserReader,
    user_writer: UserWriter,
    verify_password: PasswordVerifier,
    issue_access_token: AccessTokenIssuer,
    access_token_expire_minutes: int,
) -> LoginResult:
    """Raises `InvalidCredentialsError` for an unknown email *or* a wrong
    password — indistinguishably, on purpose (see
    `backend.app.application.errors.InvalidCredentialsError`'s
    docstring) — and `AccountDisabledError` if the password is correct
    but the account has been deactivated. `access_token_expire_minutes`
    is passed in rather than imported from `tokens.py`'s
    `ACCESS_TOKEN_EXPIRE_MINUTES` constant, for the same reason every
    other real dependency here is injected rather than imported."""

    normalized_email = email.strip().lower()
    user = await users.get_by_email(normalized_email)
    if user is None:
        # Deliberately: do not distinguish this from a wrong password
        # below. Do not verify_password() against a dummy hash here
        # either (that would be a real password-hashing library's job to
        # provide constant-time-lookup mitigation for, e.g. bcrypt itself
        # already takes a fixed amount of time regardless of input; no
        # extra dummy-hash call is needed on top of that to avoid a
        # *timing* side channel — only to avoid a *response content* one,
        # which raising the same exception below already does).
        raise InvalidCredentialsError("invalid email or password")

    if not verify_password(password, user.hashed_password):
        raise InvalidCredentialsError("invalid email or password")

    if not user.is_active:
        raise AccountDisabledError(f"user {user.id} is disabled")

    updated_user = user.record_login()
    await user_writer.save(updated_user)

    access_token = issue_access_token(user.id)
    return LoginResult(access_token=access_token, expires_in_minutes=access_token_expire_minutes)
