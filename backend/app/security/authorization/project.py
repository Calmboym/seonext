"""Project-level authorization (`PHASE-1.3`).

`require_project_access` is the check `PHASE-1.5`'s (not authorized or
built this session) project routes are expected to call. It composes two
guarantees that already each hold independently:

1. `require_workspace_access` (this package) — the caller is a
   sufficiently-privileged member of `workspace_id`, checked server-side,
   never trusting a client-supplied claim (docs/03 §109).
2. `ProjectRepository.get(workspace_id=..., project_id=...)`
   (`PHASE-1.1`) — a project lookup that is *already* impossible to get
   to return cross-workspace data, by construction (see that
   repository's own module docstring).

**Order matters and is deliberate**: membership is checked *first*,
*before* any project lookup happens at all. A caller who is not a member
of `workspace_id` never causes a project query to run — this is a
stronger tenant-isolation guarantee than "the query would have returned
nothing anyway" (`PHASE-1.1`'s guarantee): it means no project data for a
workspace a caller isn't in is ever touched on their behalf, for any
reason, not even to decide a 403 vs 404. This ordering is exactly what
`backend/tests/unit/test_authorization_checks.py`'s privilege-escalation
and cross-project-leakage tests (`PHASE-1.3` acceptance criterion 4)
verify — including that a *member* of workspace A cannot use a project ID
that actually belongs to workspace B to read or modify it, by supplying
A's workspace_id alongside B's project_id.
"""

from __future__ import annotations

from typing import Protocol

from backend.app.domain.membership.entity import Role
from backend.app.domain.project.entity import Project
from backend.app.security.authorization.errors import ProjectNotFoundError
from backend.app.security.authorization.workspace import require_workspace_access
from backend.app.security.tenancy.membership import MembershipReader


class ProjectReader(Protocol):
    async def get(self, *, workspace_id: str, project_id: str) -> Project | None: ...


async def require_project_access(
    *,
    user_id: str,
    workspace_id: str,
    project_id: str,
    projects: ProjectReader,
    memberships: MembershipReader,
    minimum_role: Role = Role.MEMBER,
) -> tuple[Project, Role]:
    """Raises `AuthorizationDeniedError` (from `require_workspace_access`)
    if `user_id` is not a sufficiently-privileged member of
    `workspace_id` — checked before anything else, see module docstring.
    Raises `ProjectNotFoundError` if the caller *is* a sufficient member
    but no project with `project_id` exists in `workspace_id` (a genuine
    404, not a 403 — see that exception's own docstring). Returns the
    `Project` and the caller's `Role` on success."""

    role = await require_workspace_access(
        user_id=user_id, workspace_id=workspace_id, memberships=memberships, minimum_role=minimum_role
    )

    project = await projects.get(workspace_id=workspace_id, project_id=project_id)
    if project is None:
        raise ProjectNotFoundError(f"no project {project_id!r} in workspace {workspace_id!r}")

    return project, role
