"""Request/response contracts for the `/api/v1/auth` group (docs/07 §15),
for `PHASE-1.2`'s register/login/logout/password-recovery endpoints.
Written *before* `PHASE-1.2`'s endpoints (`PHASE-1.4` acceptance
criterion 1, docs/03 §97) — `PHASE-1.2` implements against these shapes,
not the other way around.

See `envelope.py`'s module docstring for the `SuccessEnvelope` design
rationale (shared here); error responses reuse
`backend.app.api.schemas.errors.ErrorResponse` unchanged (acceptance
criterion 2 — not reinvented).

A password is never echoed back in any response body, and no response
here ever includes a `hashed_password` field — matches `PHASE-1.2`
acceptance criterion 3 ("credentials still never stored/returned in
plaintext") one layer up, at the contract level, so a route
implementation would have to actively fight this schema to leak one.

Password-reset request/response deliberately does not reveal whether the
given email actually has an account (`PasswordResetRequestResponse`'s
message is the same either way) — a standard mitigation against
account-enumeration via the recovery flow (docs/07 §52, Security Testing:
"privilege escalation" / info-disclosure adjacent concerns), not
explicitly named in the WBS acceptance criteria but a reasonable,
low-risk default per docs/03 §98.

NOTE (PHASE-1.4, session 9): `ast.parse`-checked only — `pydantic` is not
installed in this sandbox (Risk R9). Verification status: `IMPLEMENTED /
UNVERIFIED`.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, EmailStr, Field

from backend.app.contracts.api.envelope import SuccessEnvelope

# ---------------------------------------------------------------------------
# Register
# ---------------------------------------------------------------------------


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=200)
    display_name: str = Field(..., min_length=1, max_length=200)


class RegisterData(BaseModel):
    id: str
    email: EmailStr
    display_name: str
    created_at: datetime


class RegisterResponse(SuccessEnvelope[RegisterData]):
    contract_id: str = "auth.register.response"


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=1, max_length=200)


class LoginData(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int


class LoginResponse(SuccessEnvelope[LoginData]):
    contract_id: str = "auth.login.response"


# ---------------------------------------------------------------------------
# Logout
# ---------------------------------------------------------------------------


class LogoutData(BaseModel):
    """Deliberately empty (no fields) rather than omitted: logout has no
    natural payload with this project's stateless-JWT design (there is no
    server-side session row to report on), but the envelope's `status`/
    `request_id`/`created_at` are still meaningful, so `data` stays
    present as an empty object rather than the endpoint returning no
    envelope at all (docs/07 §18: "API responses must use explicit
    schemas" — including the empty ones)."""


class LogoutResponse(SuccessEnvelope[LogoutData]):
    contract_id: str = "auth.logout.response"


# ---------------------------------------------------------------------------
# Password recovery (docs/07 §53's "account recovery" requirement)
# ---------------------------------------------------------------------------


class PasswordResetRequestRequest(BaseModel):
    email: EmailStr


class PasswordResetRequestData(BaseModel):
    message: str = "If an account exists for that email, a password reset link has been sent."


class PasswordResetRequestResponse(SuccessEnvelope[PasswordResetRequestData]):
    contract_id: str = "auth.password_reset_request.response"


class PasswordResetConfirmRequest(BaseModel):
    reset_token: str
    new_password: str = Field(..., min_length=8, max_length=200)


class PasswordResetConfirmData(BaseModel):
    message: str = "Password updated successfully."


class PasswordResetConfirmResponse(SuccessEnvelope[PasswordResetConfirmData]):
    contract_id: str = "auth.password_reset_confirm.response"
