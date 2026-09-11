"""SQLAlchemy ORM model for the `memberships` table.

Infrastructure-layer persistence mapping for
`backend.app.domain.membership.entity.Membership` (`PHASE-1.3`). See
`backend/app/infrastructure/database/models/user.py`'s module docstring
for the dependency-direction rationale and the `IMPLEMENTED / UNVERIFIED`
verification status — identical here.

`UniqueConstraint("workspace_id", "user_id")` enforces "one membership
per user per workspace" structurally (docs/06 §55) — a user cannot hold
two different roles in the same workspace simultaneously. Both
`workspace_id` and `user_id` are foreign keys with `ondelete="CASCADE"`:
deleting a Workspace or a User removes their membership rows (there is
nothing meaningful for an orphaned membership row to reference).
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.domain.membership.entity import Membership, Role
from backend.app.infrastructure.database.base import Base


class MembershipModel(Base):
    __tablename__ = "memberships"
    __table_args__ = (
        UniqueConstraint("workspace_id", "user_id", name="uq_memberships_workspace_id_user_id"),
    )

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    workspace_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True
    )
    user_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    role: Mapped[str] = mapped_column(String(20), nullable=False, default=Role.MEMBER.value)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def to_domain(self) -> Membership:
        return Membership(
            id=self.id,
            workspace_id=self.workspace_id,
            user_id=self.user_id,
            role=Role(self.role),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, membership: Membership) -> "MembershipModel":
        return cls(
            id=membership.id,
            workspace_id=membership.workspace_id,
            user_id=membership.user_id,
            role=membership.role.value,
            created_at=membership.created_at,
            updated_at=membership.updated_at,
        )
