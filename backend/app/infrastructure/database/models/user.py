"""SQLAlchemy ORM model for the `users` table.

Infrastructure-layer persistence mapping for
`backend.app.domain.user.entity.User` (`PHASE-1.1`). Per
docs/07_TECHNICAL_ARCHITECTURE.md §14 (Dependency Direction),
infrastructure may depend on domain — never the reverse — so this module
imports the domain entity to convert to/from it, but
`backend/app/domain/user/entity.py` imports nothing from here.

NOTE (session 9): `sqlalchemy` is declared in `pyproject.toml` but not
installed in this sandbox (no network access — Risk R9,
`.ai/PROJECT_STATE.md` §9, the same limitation already recorded for every
`PHASE-0` infrastructure module, e.g. `backend/app/infrastructure/database/
{base,session}.py`). This file is `ast.parse`-checked and structurally
reviewed against the SQLAlchemy 2.0 declarative-mapping API, not executed.
Verification status: `IMPLEMENTED / UNVERIFIED`.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.domain.user.entity import User, UserStatus
from backend.app.infrastructure.database.base import Base


class UserModel(Base):
    """Persistence row for a `User`. Carries no business rules of its own
    (docs/20_PROJECT_STRUCTURE.md §29-30: models/repositories answer "what
    is stored", not "what is allowed" — that's the domain entity's job).
    `to_domain()`/`from_domain()` are the only two places this row shape
    and the `User` dataclass shape are allowed to know about each other.
    """

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    email: Mapped[str] = mapped_column(String(320), nullable=False, unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    display_name: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default=UserStatus.ACTIVE.value)
    last_login_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def to_domain(self) -> User:
        return User(
            id=self.id,
            email=self.email,
            hashed_password=self.hashed_password,
            display_name=self.display_name,
            status=UserStatus(self.status),
            last_login_at=self.last_login_at,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, user: User) -> "UserModel":
        return cls(
            id=user.id,
            email=user.email,
            hashed_password=user.hashed_password,
            display_name=user.display_name,
            status=user.status.value,
            last_login_at=user.last_login_at,
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
