"""Repository for the `users` table.

`PHASE-1.1` (.ai/WBS.md §4B). Per docs/07_TECHNICAL_ARCHITECTURE.md §14
(Dependency Direction) and docs/20_PROJECT_STRUCTURE.md §29-30, a
repository is the *only* place SQL/ORM queries for its table live, and it
returns domain entities (`backend.app.domain.user.entity.User`), never
`UserModel` rows, to its callers.

Deliberately returns `None` on a missing row rather than raising —
translating "not found" into an HTTP-appropriate error
(`backend.app.api.errors.exceptions.NotFoundAppError` or
`AuthenticationError`, depending on context) is the calling use case's
job, not this layer's: this module must not import from `backend.app.api`
(that would invert the dependency direction — infrastructure would depend
on the API layer, which depends on infrastructure).

Verification status: `IMPLEMENTED / UNVERIFIED` — `sqlalchemy` is not
installed in this sandbox (Risk R9); this file is `ast.parse`-checked and
structurally reviewed against the SQLAlchemy 2.0 async API, not executed.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.domain.user.entity import User
from backend.app.infrastructure.database.models.user import UserModel


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, user_id: str) -> User | None:
        row = await self._session.get(UserModel, user_id)
        return row.to_domain() if row else None

    async def get_by_email(self, email: str) -> User | None:
        """`email` is matched exactly as given — the caller (the
        register/login use cases, `PHASE-1.2`) is responsible for
        normalizing case before calling this, matching the normalization
        `backend.app.domain.user.entity.User.__post_init__` already
        applies, so a lookup and a freshly-constructed `User` agree on
        what "the same email" means."""

        statement = select(UserModel).where(UserModel.email == email)
        result = await self._session.execute(statement)
        row = result.scalar_one_or_none()
        return row.to_domain() if row else None

    async def add(self, user: User) -> None:
        """Inserts a brand-new user. Raises whatever the underlying
        driver raises on a unique-constraint violation (duplicate email)
        — the register use case is expected to catch that and translate
        it into a `ConflictAppError`/`ValidationAppError`, not this
        method (dependency-direction rule, see module docstring)."""

        self._session.add(UserModel.from_domain(user))
        await self._session.flush()

    async def save(self, user: User) -> None:
        """Persists an update to an existing user (e.g. after
        `user.record_login()` or `user.rename()`). Merges by primary key;
        if no row with this `id` exists, this creates one — callers that
        need "must already exist" semantics should `get_by_id` first."""

        await self._session.merge(UserModel.from_domain(user))
        await self._session.flush()
