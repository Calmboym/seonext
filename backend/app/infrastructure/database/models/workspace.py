"""SQLAlchemy ORM model for the `workspaces` table.

Infrastructure-layer persistence mapping for
`backend.app.domain.workspace.entity.Workspace` (`PHASE-1.1`). See
`backend/app/infrastructure/database/models/user.py`'s module docstring
for the dependency-direction rationale and the `IMPLEMENTED / UNVERIFIED`
verification status — identical here.

`owner_user_id` is a foreign key to `users.id`: referential integrity is
enforced at the database level (docs/06_DATA_ARCHITECTURE.md §54), not
just by the domain entity's `is_valid_id` format check.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.domain.workspace.entity import Workspace, WorkspaceStatus
from backend.app.infrastructure.database.base import Base


class WorkspaceModel(Base):
    """Persistence row for a `Workspace`. See `UserModel`'s docstring for
    the "models carry no business rules" convention this follows too."""

    __tablename__ = "workspaces"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    owner_user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    status: Mapped[str] = mapped_column(String(20), nullable=False, default=WorkspaceStatus.ACTIVE.value)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def to_domain(self) -> Workspace:
        return Workspace(
            id=self.id,
            name=self.name,
            owner_user_id=self.owner_user_id,
            status=WorkspaceStatus(self.status),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, workspace: Workspace) -> "WorkspaceModel":
        return cls(
            id=workspace.id,
            name=workspace.name,
            owner_user_id=workspace.owner_user_id,
            status=workspace.status.value,
            created_at=workspace.created_at,
            updated_at=workspace.updated_at,
        )
