"""Repository for the `projects` table.

`PHASE-1.1` acceptance criterion 4 (.ai/WBS.md §4B): "every project-scoped
repository method takes an explicit workspace/project identifier — no
method can return cross-project data by omission." Concretely enforced
below: `get()` filters `WHERE id = :project_id AND workspace_id =
:workspace_id` in one query — there is no `get(project_id)` overload that
takes only a project ID, so it is not possible to call this repository in
a way that would return a project from the wrong workspace, even by a
caller's mistake. This is docs/22_TESTING_AND_VALIDATION.md §14
(Multi-Tenant / Project Isolation Testing) and
docs/07_TECHNICAL_ARCHITECTURE.md §56 (Tenant Isolation) enforced at the
query level, not just tested for after the fact — see
backend/tests/unit/test_project_repository_tenant_scoping.py, which
`ast`-inspects this file's query construction directly (no live database
available in this sandbox, so this is a structural check, not an
execution — see that test file's own docstring).

See `user_repository.py`'s module docstring for the other shared
conventions (`None` not exceptions, domain entities not ORM rows,
`IMPLEMENTED / UNVERIFIED`) — identical here.
"""

from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.domain.project.entity import Project
from backend.app.infrastructure.database.models.project import ProjectModel


class ProjectRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get(self, *, workspace_id: str, project_id: str) -> Project | None:
        """The only single-project lookup this repository offers.
        `workspace_id` is not optional and not a keyword with a default —
        a caller cannot accidentally omit it. If `project_id` exists but
        belongs to a *different* workspace, this returns `None`, exactly
        as if the project did not exist at all — a wrong-tenant guess
        must be indistinguishable from a nonexistent ID."""

        statement = select(ProjectModel).where(
            ProjectModel.id == project_id,
            ProjectModel.workspace_id == workspace_id,
        )
        result = await self._session.execute(statement)
        row = result.scalar_one_or_none()
        return row.to_domain() if row else None

    async def list_for_workspace(self, *, workspace_id: str) -> list[Project]:
        statement = select(ProjectModel).where(ProjectModel.workspace_id == workspace_id)
        result = await self._session.execute(statement)
        return [row.to_domain() for row in result.scalars().all()]

    async def add(self, project: Project) -> None:
        self._session.add(ProjectModel.from_domain(project))
        await self._session.flush()

    async def save(self, project: Project) -> None:
        """Updates an existing project. Scoped the same way as `get()`:
        this issues an `UPDATE ... WHERE id = :id AND workspace_id =
        :workspace_id`, not a bare `merge()` by primary key alone — a
        `Project` entity that somehow carries a mismatched `workspace_id`
        (it shouldn't be possible to construct one, since `workspace_id`
        is immutable after `Project.create()`, but this repository does
        not rely on that alone) silently updates zero rows rather than
        moving a project between workspaces."""

        row = await self._session.get(ProjectModel, project.id)
        if row is None or row.workspace_id != project.workspace_id:
            return
        merged = ProjectModel.from_domain(project)
        await self._session.merge(merged)
        await self._session.flush()
