"""Async PostgreSQL connectivity.

Implements docs/07_TECHNICAL_ARCHITECTURE.md §27 (Database Access): a clear
persistence abstraction, not scattered ad hoc connections. All access goes
through `get_db_session()` — no module outside this file opens a raw
connection or constructs a raw SQL string. See docs/20_PROJECT_STRUCTURE.md
§29-30 for where this fits (infrastructure layer; repositories, added by a
later phase once domain entities exist, will depend on this module — this
module must not depend on them).

NOTE (PHASE-0.3, session 6): SQLAlchemy/asyncpg are declared in
pyproject.toml but were NOT installed, and no PostgreSQL server was
reachable, in the sandbox this file was written in (no network access).
This module is syntax-checked (ast.parse) only. The acceptance criteria
"DB reachable from the app locally" and "at least one migration applies
and reverts cleanly" (.ai/WBS.md §4, PHASE-0.3) are therefore IMPLEMENTED
but UNVERIFIED at runtime — see .ai/PROJECT_STATE.md § 14 and Risk R9.
A future session with package-install + local Postgres access must run
`alembic upgrade head` / `alembic downgrade base` against a real database
before this can be marked RUNTIME_VERIFIED.
"""

from collections.abc import AsyncGenerator
from functools import lru_cache

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from backend.app.infrastructure.config import get_settings


@lru_cache
def get_engine() -> AsyncEngine:
    """Process-wide async engine, built once from validated settings.
    Cached so the connection pool is shared, not re-created per call."""

    settings = get_settings()
    return create_async_engine(
        settings.secret.database_url.get_secret_value(),
        pool_pre_ping=True,
        echo=settings.app.debug,
    )


@lru_cache
def get_session_factory() -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=get_engine(), expire_on_commit=False, autoflush=False)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """FastAPI-compatible dependency: `session = Depends(get_db_session)`.

    Yields one session per request/call, committing on clean exit and
    rolling back on exception — callers must not manage the transaction
    boundary themselves for the common case (docs/07_TECHNICAL_ARCHITECTURE.md
    §28, Transactions)."""

    session_factory = get_session_factory()
    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
