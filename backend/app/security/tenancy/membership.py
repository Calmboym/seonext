"""Tenant-membership lookups (`PHASE-1.3`).

Answers "is user X part of workspace Y, and at what role" — the
containment-chain question docs/07 §§55-56 (Multi-Tenancy, Tenant
Isolation) describe. Deliberately thin: `Membership` itself
(`backend.app.domain.membership.entity.Membership`) already carries the
`role`; this module's only job is looking one up without every caller
re-writing the same "call the repository, handle None" shape, and
without hard-importing the concrete `MembershipRepository`
(`sqlalchemy` is not installed in this sandbox — Risk R9 — so, same
reasoning as every use case in `backend/app/application/commands/auth/`,
a `Protocol` keeps this module's own zero-third-party-dependency
property, and genuinely testable with a fake).

`backend.app.security.authorization` is the only intended caller of
this module — routes should go through `authorization/`'s checks, not
call `is_member`/`get_role` directly, so the actual *decision* ("is this
enough to proceed") stays in exactly one place.
"""

from __future__ import annotations

from typing import Protocol

from backend.app.domain.membership.entity import Membership, Role


class MembershipReader(Protocol):
    async def get_for_workspace_and_user(self, *, workspace_id: str, user_id: str) -> Membership | None: ...


async def get_role(*, memberships: MembershipReader, workspace_id: str, user_id: str) -> Role | None:
    """Returns the caller's role in `workspace_id`, or `None` if they
    have no membership there at all (not distinguished from "workspace
    doesn't exist" — see `backend.app.security.authorization.workspace`'s
    module docstring for why that's the correct behavior, not an
    oversight)."""

    membership = await memberships.get_for_workspace_and_user(workspace_id=workspace_id, user_id=user_id)
    return membership.role if membership else None


async def is_member(*, memberships: MembershipReader, workspace_id: str, user_id: str) -> bool:
    return await get_role(memberships=memberships, workspace_id=workspace_id, user_id=user_id) is not None
