"""Repository for the `memberships` table (`PHASE-1.3`).

Mirrors `backend.app.infrastructure.repositories.project_repository.
ProjectRepository`'s tenant-scoping pattern deliberately:
`get_for_workspace_and_user()` requires both `workspace_id` and
`user_id` as non-optional parameters — exactly the shape
`backend.app.security.authorization`'s checks need to answer "does this
specific user have a membership in this specific workspace", which is
the core question `PHASE-1.3` acceptance criterion 1 depends on being
impossible to get wrong by construction.

See `user_repository.py`'s module docstring for the other shared
conventions (`None` not exceptions, domain entities not ORM rows,
`IMPLEMENTED / UNVERIFIED`) — identical here.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.domain.membership.entity import Membership
from backend.app.infrastructure.database.models.membership import MembershipModel


class MembershipRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_for_workspace_and_user(self, *, workspace_id: str, user_id: str) -> Membership | None:
        """The one lookup `backend.app.security.authorization` actually
        needs: "is `user_id` a member of `workspace_id`, and if so at
        what role". Both parameters required, no `get_by_id(membership_id)`
        shortcut exists — see module docstring."""

        statement = select(MembershipModel).where(
            MembershipModel.workspace_id == workspace_id,
            MembershipModel.user_id == user_id,
        )
        result = await self._session.execute(statement)
        row = result.scalar_one_or_none()
        return row.to_domain() if row else None

    async def list_for_workspace(self, *, workspace_id: str) -> list[Membership]:
        statement = select(MembershipModel).where(MembershipModel.workspace_id == workspace_id)
        result = await self._session.execute(statement)
        return [row.to_domain() for row in result.scalars().all()]

    async def add(self, membership: Membership) -> None:
        """Raises whatever the underlying driver raises on a
        unique-constraint violation (the user already has a membership in
        this workspace) — the caller (a future `PHASE-1.6`-or-later
        "invite member" use case) is expected to check
        `get_for_workspace_and_user()` first, same pattern as
        `UserRepository.add()`."""

        self._session.add(MembershipModel.from_domain(membership))
        await self._session.flush()

    async def save(self, membership: Membership) -> None:
        await self._session.merge(MembershipModel.from_domain(membership))
        await self._session.flush()
