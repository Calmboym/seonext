"""establish core domain tables: users, workspaces, projects

Revision ID: 91ae40b03721
Revises: 7ce776d78700
Create Date: 2026-09-10

`PHASE-1.1` (.ai/WBS.md §4B): the first migration to define actual domain
schema, on top of `7ce776d78700`'s empty migration-framework-only
revision (`PHASE-0.3`). Mirrors
backend/app/infrastructure/database/models/{user,workspace,project}.py
exactly — column types, nullability, defaults, indexes, and constraints
here must match those ORM model definitions; if the two ever drift,
Alembic autogenerate (once actually runnable — Risk R9) would surface the
diff, but until then keeping them in sync is a manual discipline this
migration follows deliberately rather than relying on autogenerate for
(docs/07_TECHNICAL_ARCHITECTURE.md §30: migrations should be explicit and
reviewable).

Referential integrity (docs/06_DATA_ARCHITECTURE.md §54): `workspaces.
owner_user_id` → `users.id` (`RESTRICT` — a user who owns a workspace
cannot be deleted out from under it); `projects.workspace_id` →
`workspaces.id` (`CASCADE` — deleting a workspace deletes its projects).
Uniqueness (docs/06 §55): `(workspace_id, name)` on `projects` — two
projects in the same workspace cannot share a name.

Reversibility: `downgrade()` drops the three tables in exact reverse
creation order (`projects` → `workspaces` → `users`), the mirror image of
`upgrade()`'s creation order, respecting FK dependency direction in both
directions. This structural symmetry was confirmed by inspection this
session (`.ai/PROJECT_STATE.md` §14) — every `op.create_table` /
`op.create_index` in `upgrade()` has a matching `op.drop_table` /
`op.drop_index` in `downgrade()`.

NOTE (PHASE-1.1, session 9): written and `ast.parse`-checked only.
`alembic`/`sqlalchemy`/`asyncpg` are not installed and no Postgres server
is reachable in this sandbox (no network access — Risk R9, the same
limitation `7ce776d78700` already recorded). This migration has NOT been
run against a real database. Verification status: `IMPLEMENTED /
UNVERIFIED`. A future session with package-install and Postgres access
must run `alembic upgrade head` then `alembic downgrade -1` against a
real database before this can be marked `RUNTIME_VERIFIED`.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "91ae40b03721"
down_revision: Union[str, None] = "7ce776d78700"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("display_name", sa.String(length=200), nullable=False),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="active"),
        sa.Column("last_login_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "workspaces",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column(
            "owner_user_id",
            sa.String(length=36),
            sa.ForeignKey("users.id", ondelete="RESTRICT"),
            nullable=False,
        ),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_workspaces_owner_user_id", "workspaces", ["owner_user_id"])

    op.create_table(
        "projects",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column(
            "workspace_id",
            sa.String(length=36),
            sa.ForeignKey("workspaces.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=2000), nullable=False, server_default=""),
        sa.Column("industry", sa.String(length=200), nullable=True),
        sa.Column("markets", sa.JSON(), nullable=False),
        sa.Column("locations", sa.JSON(), nullable=False),
        sa.Column("business_model", sa.String(length=500), nullable=True),
        sa.Column("products", sa.JSON(), nullable=False),
        sa.Column("services", sa.JSON(), nullable=False),
        sa.Column("target_audiences", sa.JSON(), nullable=False),
        sa.Column("commercial_goals", sa.JSON(), nullable=False),
        sa.Column("strategic_priorities", sa.JSON(), nullable=False),
        sa.Column("website", sa.String(length=500), nullable=True),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("workspace_id", "name", name="uq_projects_workspace_id_name"),
    )
    op.create_index("ix_projects_workspace_id", "projects", ["workspace_id"])


def downgrade() -> None:
    op.drop_index("ix_projects_workspace_id", table_name="projects")
    op.drop_table("projects")

    op.drop_index("ix_workspaces_owner_user_id", table_name="workspaces")
    op.drop_table("workspaces")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
