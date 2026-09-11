"""Permission definitions and checks, one layer more granular than
authorization/ (docs/20_PROJECT_STRUCTURE.md §23 lists them separately).

Populated (`PHASE-1.3`, session 9): `roles.py` — the `OWNER > ADMIN >
MEMBER` role-ranking check `backend.app.security.authorization` calls
into. Deliberately does not define per-action/per-resource permissions
(`CAN_DELETE_PROJECT`, etc.) — `PHASE-1.3` acceptance criterion 3
explicitly defers that (Observation #9); populate this further only when
a phase actually needs finer granularity than "is this role enough".
"""

from .roles import role_meets_minimum

__all__ = ["role_meets_minimum"]
