"""establish memberships table (user/workspace role)

Revision ID: 6dca5a60eeea
Revises: 91ae40b03721
Create Date: 2026-09-10

`PHASE-1.3` (.ai/WBS.md §4B): the membership/role table whose exact shape
the WBS explicitly left as "an implementation-time decision" for this
subtask. Mirrors
backend/app/infrastructure/database/models/membership.py exactly — see
that file's docstring for the column/constraint rationale (in particular,
the `UniqueConstraint("workspace_id", "user_id")` enforcing "one
membership per user per workspace" structurally, docs/06 §55).

Reversibility: `downgrade()` drops `memberships` and both its indexes —
confirmed structurally symmetric with `upgrade()` this session via
`test_migration_structural_reversibility.py` (extended to cover this
migration too), same AST-based approach as `91ae40b03721`'s own
docstring explains in full.

NOTE (PHASE-1.3, session 9): written and `ast.parse`-checked only —
`alembic`/`sqlalchemy`/`asyncpg` are not installed and no Postgres server
is reachable in this sandbox (Risk R9). Verification status:
`IMPLEMENTED / UNVERIFIED` for actual database application/reversal.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "6dca5a60eeea"
down_revision: Union[str, None] = "91ae40b03721"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "memberships",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column(
            "workspace_id",
            sa.String(length=36),
            sa.ForeignKey("workspaces.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "user_id",
            sa.String(length=36),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("role", sa.String(length=20), nullable=False, server_default="member"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.UniqueConstraint("workspace_id", "user_id", name="uq_memberships_workspace_id_user_id"),
    )
    op.create_index("ix_memberships_workspace_id", "memberships", ["workspace_id"])
    op.create_index("ix_memberships_user_id", "memberships", ["user_id"])


def downgrade() -> None:
    op.drop_index("ix_memberships_user_id", table_name="memberships")
    op.drop_index("ix_memberships_workspace_id", table_name="memberships")
    op.drop_table("memberships")
