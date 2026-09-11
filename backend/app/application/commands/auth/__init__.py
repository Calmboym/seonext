"""Write-side auth use cases (`PHASE-1.2`): register, login, logout,
password-reset request/confirm. See docs/20_PROJECT_STRUCTURE.md §8.

Every use case here takes its dependencies (repository, password
hasher/verifier, token issuer/decoder) as explicit `Protocol`-typed
parameters rather than importing concrete implementations — see
`register.py`'s module docstring for why. `backend/app/api/routes/
auth.py` is the composition root that wires the real implementations in.
"""

from .login import AccessTokenIssuer, LoginResult, PasswordVerifier, login_user
from .logout import logout_user
from .password_reset import confirm_password_reset, request_password_reset
from .register import PasswordHasher, register_user

__all__ = [
    "AccessTokenIssuer",
    "LoginResult",
    "PasswordHasher",
    "PasswordVerifier",
    "confirm_password_reset",
    "login_user",
    "logout_user",
    "register_user",
    "request_password_reset",
]
