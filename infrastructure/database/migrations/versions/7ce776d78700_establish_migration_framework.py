"""establish migration framework

Revision ID: 7ce776d78700
Revises:
Create Date: 2026-09-07

This migration deliberately defines no domain schema. Per
.ai/WBS.md §4 (PHASE-0.3): "an initial migration establishing the migration
framework itself — not domain schema, which belongs to later phases once
entities exist." Its only job is to prove the migration mechanism itself
works end to end (forward + rollback) against a real database, per
docs/07_TECHNICAL_ARCHITECTURE.md §30.

Running `alembic upgrade head` from a clean database against this
revision should succeed and create Alembic's own `alembic_version`
bookkeeping table (Alembic's built-in behavior — no application table is
created here). `alembic downgrade base` should then cleanly return to the
pre-migration state.

NOTE (PHASE-0.3, session 6): this revision has been written and
syntax-checked (ast.parse) but has NOT been executed against a real
PostgreSQL database — no network access and no local Postgres server were
available in this session's sandbox. See .ai/PROJECT_STATE.md Risk R9.
A future session must run this (and its downgrade) against a live
database before the PHASE-0.3 acceptance criterion "at least one
migration applies and reverts cleanly" can be marked RUNTIME_VERIFIED.
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "7ce776d78700"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Intentionally a no-op beyond Alembic's own bookkeeping. Domain schema
    # begins in the first migration of the phase that introduces entities.
    pass


def downgrade() -> None:
    # Symmetric no-op — see upgrade().
    pass
