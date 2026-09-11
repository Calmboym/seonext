"""Workspace-level authorization (`PHASE-1.3`).

`require_workspace_access` is the one function every workspace-scoped
route (or another authorization check, e.g. `project.py` below) should
call before doing anything with a `workspace_id` a client supplied — it
never trusts that ID on its own (docs/03 §109): it always looks up a
real `Membership` row server-side via the injected `MembershipReader`
(`backend.app.security.tenancy.membership`, itself backed by
`backend.app.infrastructure.repositories.membership_repository.
MembershipRepository` in production) before deciding anything.

Same `Protocol`-injection, zero-third-party-dependency, genuinely-
testable-with-fakes design as `backend/app/application/commands/auth/`
— see `register.py`'s module docstring there for the full rationale;
identical reasoning applies here (`sqlalchemy` is not installed — Risk
R9 — so a hard import of the concrete repository would make this module
untestable in this sandbox).
"""

from __future__ import annotations

from backend.app.domain.membership.entity import Role
from backend.app.security.authorization.errors import AuthorizationDeniedError
from backend.app.security.permissions.roles import role_meets_minimum
from backend.app.security.tenancy.membership import MembershipReader, get_role


async def require_workspace_access(
    *,
    user_id: str,
    workspace_id: str,
    memberships: MembershipReader,
    minimum_role: Role = Role.MEMBER,
) -> Role:
    """Raises `AuthorizationDeniedError` if `user_id` has no membership
    in `workspace_id` at all, or has one but it does not meet
    `minimum_role`. Returns the caller's actual `Role` on success, so a
    route can use it for further decisions (e.g. showing an "invite
    member" button only to `ADMIN`/`OWNER`) without a second lookup.

    Deliberately raises the *same* exception, with the *same* message,
    whether `workspace_id` doesn't exist at all or the user simply isn't
    a member of a workspace that does exist — `PHASE-1.3` acceptance
    criterion 1 ("a user cannot read or modify a workspace/project they
    are not a member of") does not require distinguishing "doesn't
    exist" from "exists but you can't see it", and not distinguishing
    them is the more cautious default (the same account-enumeration-style
    reasoning already applied to login/password-reset in `PHASE-1.2` —
    see `backend.app.application.errors.InvalidCredentialsError`'s
    docstring for the general pattern). Whether a future route maps this
    to a 403 or a 404 is that route's decision, not this function's —
    see `backend/app/security/authorization/errors.py`'s module
    docstring."""

    role = await get_role(memberships=memberships, workspace_id=workspace_id, user_id=user_id)
    if role is None or not role_meets_minimum(role, minimum_role):
        raise AuthorizationDeniedError(
            f"user {user_id!r} does not have sufficient access to workspace {workspace_id!r}"
        )
    return role
