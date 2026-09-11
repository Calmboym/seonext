"""In-memory fakes for testing `backend/app/application/commands/auth/*`
without a real database, bcrypt, or PyJWT installed (none are available
in this sandbox — Risk R9). Not a test module itself (no `test_` prefix,
no `__main__` block) — imported by the test files in this directory that
exercise the auth use cases.

`FakeUserRepository` implements exactly the subset of
`backend.app.infrastructure.repositories.user_repository.UserRepository`'s
interface the `Protocol`s in `backend/app/application/commands/auth/*.py`
require (`get_by_id`, `get_by_email`, `add`, `save`) — structurally, with
no inheritance relationship, exactly like the real repository would
satisfy those same Protocols in production.
"""

from __future__ import annotations

from backend.app.domain.user.entity import User


class FakeUserRepository:
    def __init__(self) -> None:
        self._by_id: dict[str, User] = {}

    async def get_by_id(self, user_id: str) -> User | None:
        return self._by_id.get(user_id)

    async def get_by_email(self, email: str) -> User | None:
        for user in self._by_id.values():
            if user.email == email:
                return user
        return None

    async def add(self, user: User) -> None:
        if any(existing.email == user.email for existing in self._by_id.values()):
            raise AssertionError("FakeUserRepository.add: duplicate email — the use case under test "
                                  "should have checked get_by_email() first and never reached here")
        self._by_id[user.id] = user

    async def save(self, user: User) -> None:
        self._by_id[user.id] = user


def fake_hash_password(plain_password: str) -> str:
    """Deterministic, reversible, and obviously NOT real bcrypt — a fake
    standing in for `backend.app.security.authentication.passwords.
    hash_password`, which cannot be imported in this sandbox (bcrypt not
    installed)."""

    return f"hashed:{plain_password}"


def fake_verify_password(plain_password: str, hashed_password: str) -> bool:
    return hashed_password == fake_hash_password(plain_password)


def fake_issue_access_token(subject: str) -> str:
    return f"access-token:{subject}"


def fake_issue_reset_token(subject: str) -> str:
    return f"reset-token:{subject}"


class FakeTokenError(Exception):
    """Stands in for `backend.app.security.authentication.tokens.
    TokenError` in tests — the real one can't be imported here (tokens.py
    needs `pydantic-settings`, not installed). The use cases under test
    don't reference this type at all (by design — see password_reset.py's
    module docstring), so using a different exception class here than
    production would use is fine: it proves the use case really does
    just propagate whatever the injected decoder raises, unchanged, on
    its own type, not on `TokenError` specifically."""


def fake_decode_reset_token(token: str) -> str:
    if not token.startswith("reset-token:"):
        raise FakeTokenError(f"malformed token: {token!r}")
    return token.removeprefix("reset-token:")
