"""Repositories (`PHASE-1.1`). One repository per aggregate root (`User`,
`Workspace`, `Project`) — see docs/20_PROJECT_STRUCTURE.md §29-30. Each
returns domain entities, never ORM rows, and returns `None` for "not
found" rather than raising (translating that into an HTTP-appropriate
error is the API/use-case layer's job — dependency-direction rule,
docs/07_TECHNICAL_ARCHITECTURE.md §14). `ProjectRepository` additionally
enforces tenant scoping structurally — see its own module docstring.

Verification status: `IMPLEMENTED / UNVERIFIED` for all three —
`sqlalchemy` is not installed in this sandbox (Risk R9).
"""

from .project_repository import ProjectRepository
from .user_repository import UserRepository
from .workspace_repository import WorkspaceRepository

__all__ = ["ProjectRepository", "UserRepository", "WorkspaceRepository"]
