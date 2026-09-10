"""SQLAlchemy ORM models (`PHASE-1.1`). Importing this package (or any
module in it) registers every model class's table with
`backend.app.infrastructure.database.base.Base.metadata` — this is why
`infrastructure/database/migrations/env.py` (`PHASE-0.3`) must import this
package before it can autogenerate against `Base.metadata`, and why the
hand-written migration in
`infrastructure/database/migrations/versions/` for these three tables
does *not* rely on autogenerate (docs/07_TECHNICAL_ARCHITECTURE.md §30 —
migrations should be explicit and reviewable) but is still kept in sync
with these definitions by hand.

Verification status: `IMPLEMENTED / UNVERIFIED` — `sqlalchemy` is not
installed in this sandbox (Risk R9). See user.py / workspace.py /
project.py for the per-model rationale.
"""

from .project import ProjectModel
from .user import UserModel
from .workspace import WorkspaceModel

__all__ = ["ProjectModel", "UserModel", "WorkspaceModel"]
