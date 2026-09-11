"""Repositories (`PHASE-1.1`; extended `PHASE-1.3` with
`MembershipRepository`). One repository per aggregate root (`User`,
`Workspace`, `Project`, `Membership`) — see docs/20_PROJECT_STRUCTURE.md
§29-30. Each returns domain entities, never ORM rows, and returns `None`
for "not found" rather than raising (translating that into an
HTTP-appropriate error is the API/use-case layer's job — dependency-
direction rule, docs/07_TECHNICAL_ARCHITECTURE.md §14).
`ProjectRepository` and `MembershipRepository` additionally enforce
tenant scoping structurally — see their own module docstrings.

Verification status: `IMPLEMENTED / UNVERIFIED` for all four —
`sqlalchemy` is not installed in this sandbox (Risk R9).
"""

from .membership_repository import MembershipRepository
from .project_repository import ProjectRepository
from .user_repository import UserRepository
from .workspace_repository import WorkspaceRepository

__all__ = ["MembershipRepository", "ProjectRepository", "UserRepository", "WorkspaceRepository"]
