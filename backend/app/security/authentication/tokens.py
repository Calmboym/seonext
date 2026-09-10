"""Session/token issuance and verification.

Implements docs/07_TECHNICAL_ARCHITECTURE.md §53's "session or
token-based authentication" and "session expiration" requirements,
scoped exactly to PHASE-0.5's Observation #1 interpretation
(.ai/WBS.md §4): a bare mechanism, independently testable without any
user/workspace/project record existing yet. Every function below
operates on a caller-supplied `subject` string (an opaque identifier — a
future user ID, once PHASE-1's user model exists), never on an ORM model
or a database row. Satisfies acceptance criterion (3) by construction —
there is nothing here *to* couple to a user domain.

Two token types are issued from the same primitive:
    - "access"         — a short-lived session token
                          (ACCESS_TOKEN_EXPIRE_MINUTES).
    - "password_reset" — a short-lived, single-purpose token satisfying
                          §53's "account recovery" requirement's
                          *mechanism* half. The other half — an actual
                          email-delivery flow — needs a notifications
                          subsystem that doesn't exist yet
                          (integrations/ is empty by design) and is
                          deferred to whichever later phase adds one.
                          This module only proves a reset token can be
                          minted and verified.

§53 also lists "OAuth where approved" — no OAuth provider has been
approved (nothing in docs/ names one), so nothing OAuth-related is
implemented here; this is a scope gap by design, not an oversight, exactly
like acceptance criterion (4) below.

No per-resource authorization is implemented here (criterion 4) —
`decode_access_token` returns only the verified subject; nothing here
checks what that subject is *allowed* to do, which is explicitly
PHASE-1 scope (docs/24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md §18).

NOTE (PHASE-0.5, session 7): PyJWT *is* importable in this session's
sandbox (version 2.7.0 — confirmed directly, unlike every other
third-party dependency this project has declared) and the exact
encode/decode/exception-handling pattern used below was spot-checked
against that real installed copy before being written here (round-trip
encode→decode, expired-token → `ExpiredSignatureError`, wrong-secret →
`InvalidTokenError`/`InvalidSignatureError` — all confirmed to behave as
assumed). What is NOT verified: this module still cannot be *imported*
end-to-end this session, because `get_settings()` (below) pulls in
`backend.app.infrastructure.config`, which requires `pydantic-settings`
— not installed in this sandbox (Risk R9). So: the PyJWT mechanics this
module relies on are genuinely runtime-checked; the module as a whole is
still `ast.parse`-checked only.
"""

from __future__ import annotations

import time
from typing import Any, Literal

import jwt

from backend.app.infrastructure.config import get_settings

TokenType = Literal["access", "password_reset"]

ACCESS_TOKEN_EXPIRE_MINUTES = 30
PASSWORD_RESET_TOKEN_EXPIRE_MINUTES = 15
JWT_ALGORITHM = "HS256"


class TokenError(Exception):
    """Raised when a token is malformed, expired, or of the wrong type.

    Deliberately a plain exception, not an
    backend.app.api.errors.exceptions.AppError subclass — this module
    must not import from api/ (docs/20_PROJECT_STRUCTURE.md §2.2's
    dependency-direction rule: security is a lower layer than the API
    layer that will eventually catch this and translate it into an
    AuthenticationError). That translation is PHASE-1 wiring (no
    protected route exists yet to do the catching)."""


def _encode(
    *,
    subject: str,
    token_type: TokenType,
    expires_in_minutes: int,
) -> str:
    now = int(time.time())
    payload: dict[str, Any] = {
        "sub": subject,
        "type": token_type,
        "iat": now,
        "exp": now + expires_in_minutes * 60,
    }
    settings = get_settings()
    secret = settings.secret.secret_key.get_secret_value()
    return jwt.encode(payload, secret, algorithm=JWT_ALGORITHM)


def _decode(token: str, *, expected_type: TokenType) -> dict[str, Any]:
    settings = get_settings()
    secret = settings.secret.secret_key.get_secret_value()
    try:
        payload = jwt.decode(token, secret, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError as exc:
        raise TokenError("token has expired") from exc
    except jwt.InvalidTokenError as exc:
        raise TokenError("token is invalid") from exc

    if payload.get("type") != expected_type:
        raise TokenError(f"expected a {expected_type!r} token, got {payload.get('type')!r}")
    return payload


def create_access_token(subject: str) -> str:
    """Issue a short-lived access/session token for `subject`. Expires
    after ACCESS_TOKEN_EXPIRE_MINUTES — docs/07_TECHNICAL_ARCHITECTURE.md
    §53's "session expiration" requirement."""

    return _encode(subject=subject, token_type="access", expires_in_minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


def decode_access_token(token: str) -> str:
    """Verify an access token and return its subject. Raises TokenError
    if expired, malformed, or not an access token. Does NOT check what
    the subject is allowed to do (criterion 4 — PHASE-1 scope)."""

    payload = _decode(token, expected_type="access")
    return str(payload["sub"])


def create_password_reset_token(subject: str) -> str:
    """Issue a short-lived, single-purpose password-reset token for
    `subject`. Satisfies §53's "account recovery" mechanism only — see
    module docstring for what's deliberately not included."""

    return _encode(subject=subject, token_type="password_reset", expires_in_minutes=PASSWORD_RESET_TOKEN_EXPIRE_MINUTES)


def decode_password_reset_token(token: str) -> str:
    """Verify a password-reset token and return its subject. Raises
    TokenError if expired, malformed, or not a password-reset token."""

    payload = _decode(token, expected_type="password_reset")
    return str(payload["sub"])
