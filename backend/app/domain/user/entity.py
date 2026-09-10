"""The `User` domain entity.

Part of `PHASE-1.1` (Core Domain Model & Persistence — .ai/WBS.md §4B),
grounded in docs/06_DATA_ARCHITECTURE.md §6 (Core Identity Model — stable
IDs) and §8 (read for the sibling `Project` entity's business attributes,
not this one). Per docs/07_TECHNICAL_ARCHITECTURE.md §14 (Dependency
Direction), this module imports nothing from `backend.app.infrastructure`,
`backend.app.api`, or any third-party persistence/web library — it is
plain Python, deliberately, so it can be constructed and tested without a
database, an HTTP framework, or any installed dependency at all. See
backend/tests/unit/test_domain_user.py, which does exactly that.

This entity stores `hashed_password` — an opaque string produced by
`backend.app.security.authentication.passwords.hash_password` (PHASE-0.5)
— never a plaintext password. Hashing itself is the security layer's
concern (already implemented); this module only holds the resulting
string and never inspects, logs, or compares it directly (`verify_password`
is called by `PHASE-1.2`'s login use case, not by this entity).

Scope note: email format validation here is a light domain-level
sanity check only (non-empty, contains "@"), not full RFC 5322 validation
— that belongs to the request-validation boundary
(docs/07_TECHNICAL_ARCHITECTURE.md §17), which `PHASE-1.4`'s Pydantic
schemas own.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum

from backend.app.domain.common.ids import is_valid_id, new_id


class UserStatus(str, Enum):
    """Lifecycle state of a User account."""

    ACTIVE = "active"
    DISABLED = "disabled"


class UserDomainError(ValueError):
    """Raised when a `User` invariant would be violated. A plain
    `ValueError` subclass, not an `backend.app.api.errors.exceptions.AppError`
    subclass — this module must not import from `api/` (dependency-direction
    rule, docs/07_TECHNICAL_ARCHITECTURE.md §14). Translating this into an
    HTTP-appropriate `AppError` is the application/API layer's job."""


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _normalize_email(email: str) -> str:
    normalized = email.strip().lower()
    if not normalized or "@" not in normalized:
        raise UserDomainError(f"invalid email address: {email!r}")
    return normalized


def _require_non_empty(value: str, *, field_name: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise UserDomainError(f"{field_name} must not be empty")
    return stripped


@dataclass(frozen=True)
class User:
    """A registered account. Immutable (frozen dataclass) — every mutating
    method below (`rename`, `deactivate`, ...) returns a *new* `User`
    instance via `dataclasses.replace` rather than mutating in place, so a
    caller holding a reference never sees it silently change underneath
    them (docs/03_MASTER_RULES.md §145: persistence must reflect domain
    state explicitly, not implicitly)."""

    id: str
    email: str
    hashed_password: str
    display_name: str
    status: UserStatus = UserStatus.ACTIVE
    last_login_at: datetime | None = None
    created_at: datetime = field(default_factory=_utcnow)
    updated_at: datetime = field(default_factory=_utcnow)

    def __post_init__(self) -> None:
        if not is_valid_id(self.id):
            raise UserDomainError(f"invalid user id: {self.id!r}")
        # Re-validate even on direct construction (not just `.register()`),
        # so a repository hydrating a row from the database can't silently
        # produce an invariant-violating User either.
        object.__setattr__(self, "email", _normalize_email(self.email))
        object.__setattr__(self, "display_name", _require_non_empty(self.display_name, field_name="display_name"))
        if not self.hashed_password:
            raise UserDomainError("hashed_password must not be empty")

    @classmethod
    def register(cls, *, email: str, hashed_password: str, display_name: str) -> "User":
        """Factory for a brand-new User. `hashed_password` must already be
        a hash (see module docstring) — this factory never hashes a
        plaintext password itself."""

        now = _utcnow()
        return cls(
            id=new_id(),
            email=email,
            hashed_password=hashed_password,
            display_name=display_name,
            status=UserStatus.ACTIVE,
            last_login_at=None,
            created_at=now,
            updated_at=now,
        )

    @property
    def is_active(self) -> bool:
        return self.status is UserStatus.ACTIVE

    def record_login(self, *, at: datetime | None = None) -> "User":
        """Returns a new `User` with `last_login_at` (and `updated_at`)
        advanced to `at` (defaults to now). Raises if the account is
        disabled — a disabled account cannot record a successful login by
        construction, independent of whatever check the API layer also
        performs."""

        if not self.is_active:
            raise UserDomainError(f"cannot record login for a {self.status.value} user")
        timestamp = at or _utcnow()
        return replace(self, last_login_at=timestamp, updated_at=timestamp)

    def rename(self, new_display_name: str) -> "User":
        return replace(
            self,
            display_name=_require_non_empty(new_display_name, field_name="display_name"),
            updated_at=_utcnow(),
        )

    def change_password_hash(self, new_hashed_password: str) -> "User":
        if not new_hashed_password:
            raise UserDomainError("hashed_password must not be empty")
        return replace(self, hashed_password=new_hashed_password, updated_at=_utcnow())

    def deactivate(self) -> "User":
        if self.status is UserStatus.DISABLED:
            raise UserDomainError("user is already disabled")
        return replace(self, status=UserStatus.DISABLED, updated_at=_utcnow())

    def reactivate(self) -> "User":
        if self.status is UserStatus.ACTIVE:
            raise UserDomainError("user is already active")
        return replace(self, status=UserStatus.ACTIVE, updated_at=_utcnow())
