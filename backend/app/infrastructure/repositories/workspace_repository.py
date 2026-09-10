"""Repository for the `workspaces` table. See
`backend/app/infrastructure/repositories/user_repository.py`'s module
docstring for the "returns domain entities, returns `None` not an
exception, `ast.parse`-checked only" conventions — identical here.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.domain.workspace.entity import Workspace
from backend.app.infrastructure.database.models.workspace import WorkspaceModel


class WorkspaceRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, workspace_id: str) -> Workspace | None:
        row = await self._session.get(WorkspaceModel, workspace_id)
        return row.to_domain() if row else None

    async def list_for_owner(self, owner_user_id: str) -> list[Workspace]:
        statement = select(WorkspaceModel).where(WorkspaceModel.owner_user_id == owner_user_id)
        result = await self._session.execute(statement)
        return [row.to_domain() for row in result.scalars().all()]

    async def add(self, workspace: Workspace) -> None:
        self._session.add(WorkspaceModel.from_domain(workspace))
        await self._session.flush()

    async def save(self, workspace: Workspace) -> None:
        await self._session.merge(WorkspaceModel.from_domain(workspace))
        await self._session.flush()
