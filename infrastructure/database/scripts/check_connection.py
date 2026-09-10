#!/usr/bin/env python3
"""Standalone DB connectivity check.

Usage:
    python infrastructure/database/scripts/check_connection.py

Exits 0 and prints "OK" if a connection + trivial query succeeds; exits 1
with the error otherwise. Intended for local/CI smoke-testing — NOT a
substitute for the migration acceptance criteria (applies/reverts cleanly),
which alembic itself must confirm.

NOTE (PHASE-0.3, session 6): written and syntax-checked only; never
executed, since this sandbox has neither `sqlalchemy`/`asyncpg` installed
nor a reachable PostgreSQL server. See infrastructure/database/README.md.
"""

import asyncio
import sys
from pathlib import Path

# Allow running this script directly (`python infrastructure/database/
# scripts/check_connection.py`) without the package being pip-installed.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from sqlalchemy import text  # noqa: E402

from backend.app.infrastructure.database.session import get_engine  # noqa: E402


async def main() -> int:
    engine = get_engine()
    try:
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            row = result.scalar_one()
            if row != 1:
                print(f"Unexpected result from SELECT 1: {row!r}", file=sys.stderr)
                return 1
        print("OK — database reachable.")
        return 0
    except Exception as exc:  # noqa: BLE001 - this is a diagnostic script
        print(f"FAILED — could not reach database: {exc}", file=sys.stderr)
        return 1
    finally:
        await engine.dispose()


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
