"""SQLAlchemy ORM model for the `projects` table.

Infrastructure-layer persistence mapping for
`backend.app.domain.project.entity.Project` (`PHASE-1.1`). See
`backend/app/infrastructure/database/models/user.py`'s module docstring
for the dependency-direction rationale and the `IMPLEMENTED / UNVERIFIED`
verification status — identical here.

`workspace_id` is a foreign key to `workspaces.id` (`ondelete="CASCADE"`:
deleting a Workspace deletes its Projects — a disclosed, reasonable
implementation-time default per docs/03_MASTER_RULES.md §98; archiving
rather than deleting is the expected normal path per each entity's
`status` field, so `CASCADE` is a safety net for the genuine-deletion
case, not the everyday one). `UniqueConstraint("workspace_id", "name")`
enforces docs/06_DATA_ARCHITECTURE.md §55 (Uniqueness: "where identity
requires uniqueness, enforce it structurally") — two Projects in the same
Workspace cannot share a name; the same name is fine across different
Workspaces.

The free-text business-attribute list fields (`markets`, `products`, ...)
are stored as native JSON columns rather than a normalized child table:
they are unordered-ish, small, always read/written as a whole alongside
their Project, and never queried or filtered on independently anywhere in
this project's baseline docs — a normalized table would add join
complexity docs/03_MASTER_RULES.md §97 gives no evidence is needed yet.
"""

from __future__ import annotations

from datetime import datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.domain.project.entity import Project, ProjectStatus
from backend.app.infrastructure.database.base import Base


class ProjectModel(Base):
    """Persistence row for a `Project`. See `UserModel`'s docstring for
    the "models carry no business rules" convention this follows too."""

    __tablename__ = "projects"
    __table_args__ = (UniqueConstraint("workspace_id", "name", name="uq_projects_workspace_id_name"),)

    id: Mapped[str] = mapped_column(String(36), primary_key=True)
    workspace_id: Mapped[str] = mapped_column(
        String(36), ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False, default="")
    industry: Mapped[str | None] = mapped_column(String(200), nullable=True)
    markets: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    locations: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    business_model: Mapped[str | None] = mapped_column(String(500), nullable=True)
    products: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    services: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    target_audiences: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    commercial_goals: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    strategic_priorities: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    website: Mapped[str | None] = mapped_column(String(500), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default=ProjectStatus.ACTIVE.value)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    def to_domain(self) -> Project:
        return Project(
            id=self.id,
            workspace_id=self.workspace_id,
            name=self.name,
            description=self.description,
            industry=self.industry,
            markets=tuple(self.markets or ()),
            locations=tuple(self.locations or ()),
            business_model=self.business_model,
            products=tuple(self.products or ()),
            services=tuple(self.services or ()),
            target_audiences=tuple(self.target_audiences or ()),
            commercial_goals=tuple(self.commercial_goals or ()),
            strategic_priorities=tuple(self.strategic_priorities or ()),
            website=self.website,
            status=ProjectStatus(self.status),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @classmethod
    def from_domain(cls, project: Project) -> "ProjectModel":
        return cls(
            id=project.id,
            workspace_id=project.workspace_id,
            name=project.name,
            description=project.description,
            industry=project.industry,
            markets=list(project.markets),
            locations=list(project.locations),
            business_model=project.business_model,
            products=list(project.products),
            services=list(project.services),
            target_audiences=list(project.target_audiences),
            commercial_goals=list(project.commercial_goals),
            strategic_priorities=list(project.strategic_priorities),
            website=project.website,
            status=project.status.value,
            created_at=project.created_at,
            updated_at=project.updated_at,
        )
