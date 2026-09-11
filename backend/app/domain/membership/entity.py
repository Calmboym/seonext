"""The `Membership` domain entity and `Role` enum.

Part of `PHASE-1.3` (Authorization Foundation, .ai/WBS.md §4B). The
WBS's own text leaves "the exact shape [of the membership/role table] as
an implementation-time decision, not decided in this planning session" —
this file is that decision, made and disclosed here (see Observation #10
in `.ai/PROJECT_STATE.md`), not silently assumed.

Placed in `backend/app/domain/membership/`, alongside `user/`,
`workspace/`, `project/` (`PHASE-1.1`) — not directly under
`backend/app/security/`, even though `.ai/WBS.md` §4B's `PHASE-1.3` entry
describes the subtask as populating `backend/app/security/
{authorization,permissions,tenancy}/`. Rationale: a `Membership` (who
belongs to which `Workspace`, at what `Role`) is a domain concept with
its own invariants (a role must be one of a fixed set; a membership
always names exactly one workspace and one user) — structurally no
different from `User`, `Workspace`, or `Project`, all of which got a
domain entity in `PHASE-1.1` rather than living directly in
`backend/app/security/`. `backend/app/security/{tenancy,permissions,
authorization}/` still get populated by this subtask (see those
packages) — they hold the *enforcement* logic that consumes this entity,
which is genuinely a security-layer concern; the entity itself is not.

Deliberately a simple three-role, workspace-scoped model — no
per-project role, no custom/organization-defined roles, no invitation
workflow. `PHASE-1.3`'s own acceptance criterion 3 explicitly defers
resource-level and finer-grained authorization; a three-tier role
hierarchy checked at the workspace level is the simplest model that
satisfies acceptance criterion 1 ("a user cannot read or modify a
workspace/project they are not a member of") without building machinery
nothing in this phase's scope asks for.

Same dependency-direction and immutable-entity conventions as
`backend/app/domain/user/entity.py` — read that module's docstring for
the rationale; not repeated here.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum

from backend.app.domain.common.ids import is_valid_id, new_id


class Role(str, Enum):
    """Three tiers, ordered `MEMBER < ADMIN < OWNER` (the ordering itself
    — used to decide whether one role "meets or exceeds" another for a
    given check — lives in `backend.app.security.permissions.roles`, not
    here: *what the roles are* is a domain fact, *whether one is enough
    for some action* is a security-policy question, and `PHASE-1.3`'s own
    acceptance criterion 3 keeps the latter as coarse as possible for
    now)."""

    OWNER = "owner"
    ADMIN = "admin"
    MEMBER = "member"


class MembershipDomainError(ValueError):
    """Raised when a `Membership` invariant would be violated."""


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True)
class Membership:
    """One user's membership in one workspace, at one role. Uniqueness
    (one membership per (workspace_id, user_id) pair) is a persistence-
    level constraint (see `backend.app.infrastructure.database.models.
    membership.MembershipModel`'s `UniqueConstraint`, docs/06 §55) — this
    entity cannot enforce "no duplicate membership exists" on its own,
    only that *this one instance* is individually well-formed."""

    id: str
    workspace_id: str
    user_id: str
    role: Role
    created_at: datetime = field(default_factory=_utcnow)
    updated_at: datetime = field(default_factory=_utcnow)

    def __post_init__(self) -> None:
        if not is_valid_id(self.id):
            raise MembershipDomainError(f"invalid membership id: {self.id!r}")
        if not is_valid_id(self.workspace_id):
            raise MembershipDomainError(f"invalid workspace_id: {self.workspace_id!r}")
        if not is_valid_id(self.user_id):
            raise MembershipDomainError(f"invalid user_id: {self.user_id!r}")
        if not isinstance(self.role, Role):
            raise MembershipDomainError(f"invalid role: {self.role!r}")

    @classmethod
    def create(cls, *, workspace_id: str, user_id: str, role: Role = Role.MEMBER) -> "Membership":
        now = _utcnow()
        return cls(
            id=new_id(),
            workspace_id=workspace_id,
            user_id=user_id,
            role=role,
            created_at=now,
            updated_at=now,
        )

    def change_role(self, new_role: Role) -> "Membership":
        if not isinstance(new_role, Role):
            raise MembershipDomainError(f"invalid role: {new_role!r}")
        return replace(self, role=new_role, updated_at=_utcnow())

    def belongs_to(self, workspace_id: str) -> bool:
        return self.workspace_id == workspace_id

    def is_held_by(self, user_id: str) -> bool:
        return self.user_id == user_id
