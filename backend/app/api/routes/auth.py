"""`/api/v1/auth` routes (`PHASE-1.2`).

This is the composition root for the auth use cases
(`backend/app/application/commands/auth/`): the one place their injected
`Protocol` dependencies are bound to real implementations
(`backend.app.security.authentication.passwords`/`tokens`,
`backend.app.infrastructure.repositories.user_repository.UserRepository`)
and the one place their plain application-layer exceptions
(`backend/app/application/errors.py`) are translated into HTTP-appropriate
`AppError` subclasses (`backend/app/api/errors/exceptions.py`) — see
those two modules' docstrings for why neither layer does this itself.

Request/response shapes come from `backend/app/contracts/api/auth.py`
(`PHASE-1.4`), written before this file, per `docs/03_MASTER_RULES.md`
§ 97.

NOTE (PHASE-1.2, session 9): `ast.parse`-checked only —
`fastapi`/`pydantic`/`sqlalchemy` are not installed in this sandbox (Risk
R9). The use cases this file calls into are, unlike this file, genuinely
unit-tested (zero third-party deps — see backend/tests/unit/
test_{register,login,logout}_user_use_case.py and
test_password_reset_use_cases.py). Verification status for this file:
`IMPLEMENTED / UNVERIFIED`.
"""

from __future__ import annotations

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.api.dependencies.auth import get_current_user
from backend.app.api.dependencies.db import get_db_session
from backend.app.api.errors.exceptions import AuthenticationError, ConflictAppError, ValidationAppError
from backend.app.api.middleware.request_id import get_request_id
from backend.app.application.commands.auth.login import login_user
from backend.app.application.commands.auth.logout import logout_user
from backend.app.application.commands.auth.password_reset import (
    confirm_password_reset,
    request_password_reset,
)
from backend.app.application.commands.auth.register import register_user
from backend.app.application.errors import (
    AccountDisabledError,
    EmailAlreadyRegisteredError,
    InvalidCredentialsError,
    InvalidOrExpiredResetTokenError,
)
from backend.app.contracts.api.auth import (
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
from backend.app.domain.user.entity import User, UserDomainError
from backend.app.infrastructure.repositories.user_repository import UserRepository
from backend.app.observability.logging.core import get_logger
from backend.app.security.authentication.passwords import hash_password, verify_password
from backend.app.security.authentication.tokens import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    TokenError,
    create_access_token,
    create_password_reset_token,
    decode_password_reset_token,
)

router = APIRouter(prefix="/auth", tags=["auth"])
logger = get_logger(__name__)


@router.post("/register", response_model=RegisterResponse, status_code=status.HTTP_201_CREATED)
async def register(
    body: RegisterRequest,
    session: AsyncSession = Depends(get_db_session),
) -> RegisterResponse:
    users = UserRepository(session)
    try:
        user = await register_user(
            email=body.email,
            password=body.password,
            display_name=body.display_name,
            users=users,
            hash_password=hash_password,
        )
    except EmailAlreadyRegisteredError as exc:
        raise ConflictAppError(str(exc), details={"field": "email"}) from exc
    except UserDomainError as exc:
        raise ValidationAppError(str(exc)) from exc

    return RegisterResponse(
        data=RegisterData(
            id=user.id, email=user.email, display_name=user.display_name, created_at=user.created_at
        ),
        request_id=get_request_id(),
    )


@router.post("/login", response_model=LoginResponse)
async def login(
    body: LoginRequest,
    session: AsyncSession = Depends(get_db_session),
) -> LoginResponse:
    users = UserRepository(session)
    try:
        result = await login_user(
            email=body.email,
            password=body.password,
            users=users,
            user_writer=users,
            verify_password=verify_password,
            issue_access_token=create_access_token,
            access_token_expire_minutes=ACCESS_TOKEN_EXPIRE_MINUTES,
        )
    except (InvalidCredentialsError, AccountDisabledError) as exc:
        # Deliberately the same AuthenticationError either way — see
        # backend/app/application/errors.py's InvalidCredentialsError
        # docstring on why a disabled account isn't distinguished from a
        # wrong password at this boundary either.
        raise AuthenticationError("invalid email or password") from exc

    return LoginResponse(
        data=LoginData(
            access_token=result.access_token,
            expires_in_minutes=result.expires_in_minutes,
        ),
        request_id=get_request_id(),
    )


@router.post("/logout", response_model=LogoutResponse)
async def logout(current_user: User = Depends(get_current_user)) -> LogoutResponse:
    logout_user(user_id=current_user.id)
    return LogoutResponse(data=LogoutData(), request_id=get_request_id())


@router.post("/password-reset/request", response_model=PasswordResetRequestResponse)
async def password_reset_request(
    body: PasswordResetRequestRequest,
    session: AsyncSession = Depends(get_db_session),
) -> PasswordResetRequestResponse:
    users = UserRepository(session)
    token = await request_password_reset(
        email=body.email, users=users, issue_reset_token=create_password_reset_token
    )
    if token is not None:
        # No notification/email-delivery subsystem exists yet
        # (integrations/ is empty by design — see password_reset.py's
        # module docstring for the full rationale). Logging the token
        # server-side is this phase's honest, minimal stand-in for a
        # real delivery flow: never put in the HTTP response, never
        # conditioned on in a way that would change what the client
        # sees (the response below is identical whether or not `token`
        # is None).
        logger.info(
            "Password reset token issued (no delivery channel wired yet — PHASE-1.2)",
            extra={"request_id": get_request_id()},
        )
    # Deliberately identical response regardless of `token`'s value —
    # see request_password_reset's own docstring (account-enumeration
    # safety).
    return PasswordResetRequestResponse(data=PasswordResetRequestData(), request_id=get_request_id())


@router.post("/password-reset/confirm", response_model=PasswordResetConfirmResponse)
async def password_reset_confirm(
    body: PasswordResetConfirmRequest,
    session: AsyncSession = Depends(get_db_session),
) -> PasswordResetConfirmResponse:
    users = UserRepository(session)
    try:
        await confirm_password_reset(
            reset_token=body.reset_token,
            new_password=body.new_password,
            decode_reset_token=decode_password_reset_token,
            users=users,
            user_writer=users,
            hash_password=hash_password,
        )
    except (TokenError, InvalidOrExpiredResetTokenError) as exc:
        raise AuthenticationError("invalid or expired password reset token") from exc

    return PasswordResetConfirmResponse(
        data=PasswordResetConfirmData(), request_id=get_request_id()
    )
