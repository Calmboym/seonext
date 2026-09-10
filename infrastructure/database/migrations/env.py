"""Alembic environment script.

Wired to this project's own async engine/config rather than a duplicated
connection string, per docs/07_TECHNICAL_ARCHITECTURE.md §30 (a migration
must define schema change, forward operation, rollback strategy, data
migration requirements, compatibility impact — and per §27, database access
must not be scattered arbitrarily; this file is the one place migrations
resolve their connection).

Async support follows Alembic's standard recipe for async engines:
`run_sync()` bridges Alembic's synchronous migration API onto our
`AsyncEngine`. See https://alembic.sqlalchemy.org/en/latest/cookbook.html
#using-asyncio-with-alembic (not fetched in this session — written from
established Alembic async-engine pattern, not from that page's exact text).

NOTE (PHASE-0.3, session 6): this file is syntax-checked (ast.parse) only.
Alembic is not installed in this sandbox (no network access), so it has
never actually been imported or executed — see
backend/app/infrastructure/database/session.py's note and
.ai/PROJECT_STATE.md Risk R9.
"""

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import Connection
from sqlalchemy.ext.asyncio import AsyncEngine

from backend.app.infrastructure.config import get_settings
from backend.app.infrastructure.database.base import Base
from backend.app.infrastructure.database.session import get_engine

# Importing this package registers every ORM model's table with
# Base.metadata as a side effect (see backend/app/infrastructure/database/
# models/__init__.py's own docstring). Required here so `target_metadata`
# below actually reflects PHASE-1.1's users/workspaces/projects tables —
# without this import, Base.metadata would stay empty regardless of how
# many model modules exist elsewhere in the codebase, and autogenerate
# would (incorrectly) propose dropping all three tables.
from backend.app.infrastructure.database import models  # noqa: F401

# Alembic Config object, providing access to values in alembic.ini.
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for 'autogenerate' support. As of PHASE-1.1 this
# reflects the three core domain tables (users, workspaces, projects);
# it was empty through PHASE-0 (Base had no domain models registered yet).
target_metadata = Base.metadata


def get_url() -> str:
    """Single source of truth for the DB URL: our own validated settings,
    not a duplicated value in alembic.ini. See backend/app/infrastructure/
    config/settings.py's SecretSettings.database_url."""

    return get_settings().secret.database_url.get_secret_value()


def run_migrations_offline() -> None:
    """Run migrations without a live DB connection (emits SQL to stdout)."""

    context.configure(
        url=get_url(),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Run migrations against the real async engine (docs/07_TECHNICAL_
    ARCHITECTURE.md §26, PostgreSQL as primary system of record)."""

    connectable: AsyncEngine = get_engine()

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
