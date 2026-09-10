"""The `Workspace` domain entity.

Part of `PHASE-1.1` (.ai/WBS.md §4B). Grounded in
docs/06_DATA_ARCHITECTURE.md §5 (Organization → Workspace → Project → SEO
Knowledge) and §6 (Core Identity Model).

Scope simplification (disclosed, not silently assumed — see
.ai/PROJECT_STATE.md §10, Observation #9 for this session): docs/06 §5's
chain names "Organization" as the level above Workspace, but no document
in this project's baseline (docs/24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md
§18's PHASE-1 capability list included) describes Organization as a
capability with its own data or lifecycle — only "user/workspace/project
model" is named. For `PHASE-1`, `Workspace` is therefore treated as the
top-level tenant boundary in its own right (each Workspace has exactly one
owning `User`, identified by `owner_user_id`), and "Organization" is not
modeled as a separate entity. If a later phase needs one Organization to
own several Workspaces (e.g. a company with multiple regional workspaces),
that is a genuine new capability to decompose and authorize then, not a
retrofit of this file.

Same dependency-direction and mutability conventions as
`backend/app/domain/user/entity.py` — read that module's docstring for the
rationale; not repeated here.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum

from backend.app.domain.common.ids import is_valid_id, new_id


class WorkspaceStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"


class WorkspaceDomainError(ValueError):
    """Raised when a `Workspace` invariant would be violated. See
    `backend.app.domain.user.entity.UserDomainError` for why this is a
    plain `ValueError`, not an API-layer exception."""


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _require_non_empty(value: str, *, field_name: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise WorkspaceDomainError(f"{field_name} must not be empty")
    return stripped


@dataclass(frozen=True)
class Workspace:
    """A tenant boundary. Every `Project` (see
    `backend.app.domain.project.entity.Project`) belongs to exactly one
    Workspace, and — per `PHASE-1.3`'s membership model, not this file —
    every access check to a Project's data is scoped through its
    Workspace. This entity itself does not enforce access control; it
    only enforces that it is well-formed (docs/03_MASTER_RULES.md §108:
    authentication/identity ≠ authorization, and this is neither — it is
    just data)."""

    id: str
    name: str
    owner_user_id: str
    status: WorkspaceStatus = WorkspaceStatus.ACTIVE
    created_at: datetime = field(default_factory=_utcnow)
    updated_at: datetime = field(default_factory=_utcnow)

    def __post_init__(self) -> None:
        if not is_valid_id(self.id):
            raise WorkspaceDomainError(f"invalid workspace id: {self.id!r}")
        if not is_valid_id(self.owner_user_id):
            raise WorkspaceDomainError(f"invalid owner_user_id: {self.owner_user_id!r}")
        object.__setattr__(self, "name", _require_non_empty(self.name, field_name="name"))

    @classmethod
    def create(cls, *, name: str, owner_user_id: str) -> "Workspace":
        now = _utcnow()
        return cls(
            id=new_id(),
            name=name,
            owner_user_id=owner_user_id,
            status=WorkspaceStatus.ACTIVE,
            created_at=now,
            updated_at=now,
        )

    @property
    def is_active(self) -> bool:
        return self.status is WorkspaceStatus.ACTIVE

    def rename(self, new_name: str) -> "Workspace":
        return replace(self, name=_require_non_empty(new_name, field_name="name"), updated_at=_utcnow())

    def archive(self) -> "Workspace":
        if self.status is WorkspaceStatus.ARCHIVED:
            raise WorkspaceDomainError("workspace is already archived")
        return replace(self, status=WorkspaceStatus.ARCHIVED, updated_at=_utcnow())

    def reactivate(self) -> "Workspace":
        if self.status is WorkspaceStatus.ACTIVE:
            raise WorkspaceDomainError("workspace is already active")
        return replace(self, status=WorkspaceStatus.ACTIVE, updated_at=_utcnow())

    def is_owned_by(self, user_id: str) -> bool:
        return self.owner_user_id == user_id
