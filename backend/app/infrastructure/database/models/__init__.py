"""SQLAlchemy ORM models (`PHASE-1.1`; extended `PHASE-1.3` with
`MembershipModel`). Importing this package (or any module in it)
registers every model class's table with
`backend.app.infrastructure.database.base.Base.metadata` — this is why
`infrastructure/database/migrations/env.py` (`PHASE-0.3`) must import this
package before it can autogenerate against `Base.metadata`, and why the
hand-written migrations in
`infrastructure/database/migrations/versions/` do *not* rely on
autogenerate (docs/07_TECHNICAL_ARCHITECTURE.md §30 — migrations should
be explicit and reviewable) but are still kept in sync with these
definitions by hand.

Verification status: `IMPLEMENTED / UNVERIFIED` — `sqlalchemy` is not
installed in this sandbox (Risk R9). See user.py / workspace.py /
project.py / membership.py for the per-model rationale.
"""

from .membership import MembershipModel
from .project import ProjectModel
from .user import UserModel
from .workspace import WorkspaceModel

__all__ = ["MembershipModel", "ProjectModel", "UserModel", "WorkspaceModel"]
