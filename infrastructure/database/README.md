# infrastructure/database/

PostgreSQL migrations and operational database concerns, separated from application code per `docs/20_PROJECT_STRUCTURE.md` §29.

```text
infrastructure/database/
├── migrations/     Alembic migration environment + version history
├── seeds/          Not yet populated — no domain data to seed until entities exist
├── fixtures/        Not yet populated — same reason
├── scripts/        check_connection.py (below)
└── README.md       this file
```

## Running migrations

Requires `DATABASE_URL` set (see `.env.example`) and the `dev` dependency group installed (`pip install -e ".[dev]"` from repo root, or equivalent).

```bash
alembic upgrade head      # apply all migrations
alembic downgrade base    # revert all migrations
alembic revision --autogenerate -m "description"   # once domain models exist
```

`alembic.ini` lives at the repo root; `script_location` points here. The connection string is resolved once, from `backend/app/infrastructure/config/settings.py`'s `SecretSettings.database_url` — it is not duplicated into `alembic.ini`.

## Verification status (PHASE-0.3, session 6)

**Not runtime-verified.** This session's sandbox had no network access (could not install `alembic`/`asyncpg`/`sqlalchemy`) and no local PostgreSQL server. The migration framework, session/engine code, and initial migration have been written and syntax-checked (`ast.parse`) but never executed against a real database. Before this is marked `RUNTIME_VERIFIED`, a session with package-install and database access must confirm:

1. `alembic upgrade head` succeeds against a clean local Postgres instance.
2. `alembic downgrade base` cleanly reverts it.
3. `scripts/check_connection.py` reports success.

See `.ai/PROJECT_STATE.md` § 14 (Verification Log, Session 6) and Risk R9.
