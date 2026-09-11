"""The logout use case (`PHASE-1.2`).

This project's access tokens are stateless JWTs
(`backend.app.security.authentication.tokens`, `PHASE-0.5`) — there is no
server-side session row to delete and no token-revocation/blocklist store
(building one would be a new capability, outside `PHASE-1.2`'s authorized
scope — nothing in `.ai/WBS.md` §4B's `PHASE-1.2` entry asks for one).
"Logging out" therefore has exactly one honest meaning at this phase: the
client discards the token, and the server's only remaining job is to
confirm the caller was actually authenticated when they asked to log out
(`backend/app/api/dependencies/auth.py`'s `get_current_user`, checked by
the route before this function is even called — not by this function)
and acknowledge the request.

This is a real, correct implementation of "logout" for a stateless-JWT
architecture — not a stub standing in for a missing feature — but it is
worth being explicit about what it does *not* do: it does not invalidate
the token server-side. A token issued before logout remains valid until
it naturally expires (`ACCESS_TOKEN_EXPIRE_MINUTES = 30`, `tokens.py`). A
future phase that needs immediate server-side revocation (e.g. "log out
of all devices", or responding to a compromised account) would add a
token-blocklist repository and check it from `get_current_user` — a new,
separately authorized capability, not a retrofit of this file.
"""

from __future__ import annotations


def logout_user(*, user_id: str) -> None:
    """`user_id` is accepted, and currently unused beyond documenting
    intent, so this function's signature is the seam a future
    token-revocation feature would extend (e.g. writing `user_id` plus
    the token's `jti` to a blocklist) without changing
    `backend/app/api/routes/auth.py`'s call site or this function's
    contract with its caller."""

    return None
