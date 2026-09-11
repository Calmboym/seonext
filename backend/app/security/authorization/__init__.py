"""Authorization: user/workspace/project/resource/tool-action level
permission checks (docs/07_TECHNICAL_ARCHITECTURE.md §54).

Populated (`PHASE-1.3`, session 9) at the user/workspace/project level
only: `workspace.py` (`require_workspace_access`) and `project.py`
(`require_project_access`), backed by `backend.app.security.tenancy` and
`backend.app.security.permissions`. Resource-level and tool/action-level
authorization remain explicitly out of scope by construction — see
Observation #9 (`.ai/PROJECT_STATE.md`) and `.ai/WBS.md` §4B's
`PHASE-1.3` acceptance criterion 3 — not populated here, not silently
approximated under a different name.
"""

from .errors import AuthorizationDeniedError, ProjectNotFoundError
from .project import ProjectReader, require_project_access
from .workspace import require_workspace_access

__all__ = [
    "AuthorizationDeniedError",
    "ProjectNotFoundError",
    "ProjectReader",
    "require_project_access",
    "require_workspace_access",
]
