"""Role ranking (`PHASE-1.3`).

`backend.app.domain.membership.entity.Role` defines *what the roles
are* (a domain fact — see that module's docstring for why). This module
defines *whether one role is enough for a given check* — a security-
policy question, kept as coarse as possible on purpose:
`role_meets_minimum(role, minimum)` is the only thing this module
exports, answering "does `role` outrank or equal `minimum` in the fixed
`OWNER > ADMIN > MEMBER` hierarchy". There is no per-action permission
table (`CAN_INVITE_MEMBER`, `CAN_DELETE_PROJECT`, ...) — `PHASE-1.3`
acceptance criterion 3 explicitly defers tool/action-level authorization
(see Observation #9), and this file does not quietly build that anyway
under a different name.

Populates `backend/app/security/permissions/`, per `.ai/WBS.md` §4B's
`PHASE-1.3` entry — this is "one layer more granular than
`authorization/`" (that package's own placeholder docstring, `PHASE-0.5`)
in exactly the sense that `authorization/` calls into this module to
decide the coarse-grained yes/no, rather than hardcoding role comparisons
itself in more than one place.
"""

from __future__ import annotations

from backend.app.domain.membership.entity import Role

# Higher number outranks lower. A plain dict, not an IntEnum on Role
# itself, because Role is a domain type (backend/app/domain/membership/
# entity.py) and domain types must not encode security-policy ordering —
# see this module's own docstring for why that split matters.
_ROLE_RANK: dict[Role, int] = {
    Role.MEMBER: 0,
    Role.ADMIN: 1,
    Role.OWNER: 2,
}


def role_meets_minimum(role: Role, minimum: Role) -> bool:
    """True if `role` outranks or equals `minimum` in the
    `OWNER > ADMIN > MEMBER` hierarchy. Both arguments must be `Role`
    members — this function does not coerce strings, on purpose (a
    caller passing a raw string instead of a `Role` almost always means
    a client-supplied value slipped in somewhere it shouldn't have,
    which docs/03 §109 says never to trust in the first place; failing
    loudly here is the safer default)."""

    return _ROLE_RANK[role] >= _ROLE_RANK[minimum]
