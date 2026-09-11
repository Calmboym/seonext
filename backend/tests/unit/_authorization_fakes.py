"""In-memory fakes for testing `backend/app/security/{authorization,
tenancy}` without a real database (`sqlalchemy` not installed — Risk R9).
Not a test module itself — imported by test_authorization_checks.py.

Structurally satisfies `backend.app.security.tenancy.membership.
MembershipReader` and `backend.app.security.authorization.project.
ProjectReader` — no inheritance relationship, same as every other fake
in this test suite (`_auth_fakes.py`).
"""

from __future__ import annotations

from backend.app.domain.membership.entity import Membership
from backend.app.domain.project.entity import Project


class FakeMembershipRepository:
    def __init__(self) -> None:
        self._rows: dict[tuple[str, str], Membership] = {}

    async def get_for_workspace_and_user(self, *, workspace_id: str, user_id: str) -> Membership | None:
        return self._rows.get((workspace_id, user_id))

    async def add(self, membership: Membership) -> None:
        self._rows[(membership.workspace_id, membership.user_id)] = membership


class FakeProjectRepository:
    """Deliberately mirrors `backend.app.infrastructure.repositories.
    project_repository.ProjectRepository`'s tenant-scoping behavior
    exactly: `get()` returns `None` for a project ID that exists but
    belongs to a *different* workspace_id, not just for one that doesn't
    exist at all — this is the exact property
    `test_authorization_checks.py`'s cross-project-leakage test relies
    on to prove `require_project_access` composes correctly with it."""

    def __init__(self) -> None:
        self._rows: dict[str, Project] = {}  # keyed by project.id only

    async def get(self, *, workspace_id: str, project_id: str) -> Project | None:
        project = self._rows.get(project_id)
        if project is None or project.workspace_id != workspace_id:
            return None
        return project

    async def add(self, project: Project) -> None:
        self._rows[project.id] = project
