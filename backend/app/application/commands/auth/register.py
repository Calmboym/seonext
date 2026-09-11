"""The register-a-new-user use case (`PHASE-1.2`, .ai/WBS.md §4B).

Every dependency (the repository, the password hasher) is accepted as an
explicit parameter, typed as a `Protocol` — this module imports nothing
from `backend.app.infrastructure` or
`backend.app.security.authentication.passwords` at all, let alone at
module level. Two reasons, not one:

1. Dependency direction (docs/07 §14) is satisfied trivially either way
   here (Application is allowed to depend on Infrastructure), but
   Protocol-typing keeps this module honestly decoupled rather than
   relying on that allowance.
2. Practically, `passwords.py` does `import bcrypt` at module level, and
   `bcrypt` is not installed in this sandbox (Risk R9) — a hard import of
   `passwords.py` here would make this file itself fail to import,
   which would make it impossible to unit-test the orchestration logic
   below at all. With the hasher injected, this module has zero
   third-party imports and was genuinely unit-tested this session with a
   fake hasher and a fake in-memory repository — see
   backend/tests/unit/test_register_user_use_case.py.

`PHASE-1.2` acceptance criterion 1 ("registration creates a real `User`
record via `PHASE-0.5`'s existing `bcrypt`-backed hashing — not
reimplemented") is satisfied at the composition root
(`backend/app/api/routes/auth.py`), which is the one place that actually
passes `backend.app.security.authentication.passwords.hash_password` in
as `hash_password` below — this module never reimplements hashing itself,
it just doesn't hard-import the real implementation.
"""

from __future__ import annotations

from typing import Protocol

from backend.app.application.errors import EmailAlreadyRegisteredError
from backend.app.domain.user.entity import User


class PasswordHasher(Protocol):
    def __call__(self, plain_password: str) -> str: ...


class UserWriter(Protocol):
    """The subset of `backend.app.infrastructure.repositories.
    user_repository.UserRepository`'s interface this use case needs — a
    real `UserRepository` instance satisfies this structurally, with no
    inheritance relationship required."""

    async def get_by_email(self, email: str) -> User | None: ...

    async def add(self, user: User) -> None: ...


async def register_user(
    *,
    email: str,
    password: str,
    display_name: str,
    users: UserWriter,
    hash_password: PasswordHasher,
) -> User:
    """Registers a new user. Raises `EmailAlreadyRegisteredError` if the
    (normalized) email is already taken, or `UserDomainError` if `email`/
    `display_name` fail `User`'s own invariants (e.g. empty display
    name) — both are plain exceptions the caller (an API route) is
    expected to catch and translate; see `backend/app/application/
    errors.py`'s module docstring for why."""

    normalized_email = email.strip().lower()
    existing = await users.get_by_email(normalized_email)
    if existing is not None:
        raise EmailAlreadyRegisteredError(f"an account already exists for {normalized_email!r}")

    # User.register() requires a hash to construct the entity at all (it
    # has no separate "validate first, hash later" step), so hashing
    # happens before domain validation can run. If User.register then
    # rejects the email/display_name, the computed hash is simply
    # discarded — a wasted bcrypt call on an error path, not a
    # correctness or security concern.
    hashed_password = hash_password(password)
    user = User.register(email=email, hashed_password=hashed_password, display_name=display_name)

    await users.add(user)
    return user
