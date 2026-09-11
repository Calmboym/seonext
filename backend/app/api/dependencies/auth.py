"""`get_current_user` — the first place `PHASE-1.2` wires
`backend.app.security.authentication.tokens.decode_access_token` into a
real authenticated route, closing the gap
`backend.app.api.errors.exceptions.AuthenticationError`'s own docstring
named at `PHASE-0.4`: "Raise this from a route once `PHASE-1` wires a
`get_current_user`-style dependency around ... `decode_access_token` — no
protected route exists yet to raise it from."

This proves *who* is calling (authentication) — it does not check *what*
they're allowed to do (authorization, `PHASE-1.3`, per
`03_MASTER_RULES.md` § 108, "Authentication ≠ Authorization"; see
`.ai/WBS.md` §4B's `PHASE-1.3` entry, whose own Purpose says exactly
this: "`PHASE-1.2` only proves *who*; this proves *what they're allowed
to do*").

NOTE (PHASE-1.2, session 9): `ast.parse`-checked only —
`fastapi`/`sqlalchemy` are not installed in this sandbox (Risk R9).
Verification status: `IMPLEMENTED / UNVERIFIED`.
"""

from __future__ import annotations

from fastapi import Depends, Header
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api.dependencies.db import get_db_session
from backend.app.api.errors.exceptions import AuthenticationError
from backend.app.domain.user.entity import User
from backend.app.infrastructure.repositories.user_repository import UserRepository
from backend.app.security.authentication.tokens import TokenError, decode_access_token

_BEARER_PREFIX = "Bearer "


def _extract_bearer_token(authorization: str | None) -> str:
    if not authorization or not authorization.startswith(_BEARER_PREFIX):
        raise AuthenticationError("missing or malformed Authorization header")
    token = authorization[len(_BEARER_PREFIX) :].strip()
    if not token:
        raise AuthenticationError("missing or malformed Authorization header")
    return token


async def get_current_user(
    authorization: str | None = Header(default=None),
    session: AsyncSession = Depends(get_db_session),
) -> User:
    """Extracts and verifies a Bearer access token from the
    `Authorization` header, then loads and returns the real `User` it
    belongs to. Raises `AuthenticationError` (401) for: a missing or
    malformed header; an invalid, expired, or wrong-type token
    (`TokenError`); or a token whose subject no longer corresponds to an
    active account (deleted or disabled since the token was issued).

    Per `docs/03_MASTER_RULES.md` § 109 ("Never Trust Client-Supplied
    Identity"): the only thing trusted here is the token's cryptographic
    signature, verified by `decode_access_token` against the server's own
    secret key — the `Authorization` header's string content proves
    nothing on its own until that verification succeeds.
    """

    token = _extract_bearer_token(authorization)
    try:
        user_id = decode_access_token(token)
    except TokenError as exc:
        raise AuthenticationError("invalid or expired access token") from exc

    users = UserRepository(session)
    user = await users.get_by_id(user_id)
    if user is None or not user.is_active:
        raise AuthenticationError("access token does not correspond to an active account")

    return user
