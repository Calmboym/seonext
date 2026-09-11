"""Versioned request/response contracts for `/api/v1/auth`
(`PHASE-1.2`) and `/api/v1/projects` (`PHASE-1.5`). See `envelope.py` for
the shared `SuccessEnvelope`. Written ahead of both subtasks' endpoints
per docs/03 §97 (`PHASE-1.4` acceptance criterion 1).

`packages/contracts/src/` mirrors these as TypeScript types for
`apps/web` — see that package's README for the manual-sync statement
required by `PHASE-1.4` acceptance criterion 3.
"""

from .auth import (
    LoginData,
    LoginRequest,
    LoginResponse,
    LogoutData,
    LogoutResponse,
    PasswordResetConfirmData,
    PasswordResetConfirmRequest,
    PasswordResetConfirmResponse,
    PasswordResetRequestData,
    PasswordResetRequestRequest,
    PasswordResetRequestResponse,
    RegisterData,
    RegisterRequest,
    RegisterResponse,
)
from .envelope import SuccessEnvelope
from .projects import (
    ProjectCreateRequest,
    ProjectData,
    ProjectListData,
    ProjectListResponse,
    ProjectResponse,
    ProjectUpdateRequest,
)

__all__ = [
    "LoginData",
    "LoginRequest",
    "LoginResponse",
    "LogoutData",
    "LogoutResponse",
    "PasswordResetConfirmData",
    "PasswordResetConfirmRequest",
    "PasswordResetConfirmResponse",
    "PasswordResetRequestData",
    "PasswordResetRequestRequest",
    "PasswordResetRequestResponse",
    "ProjectCreateRequest",
    "ProjectData",
    "ProjectListData",
    "ProjectListResponse",
    "ProjectResponse",
    "ProjectUpdateRequest",
    "RegisterData",
    "RegisterRequest",
    "RegisterResponse",
    "SuccessEnvelope",
]
