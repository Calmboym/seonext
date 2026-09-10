# Seonex — SEO Research & Strategy Copilot / SEO Decision Engine

`PHASE-0` (Foundation) is complete — all 8 subtasks `DONE`. `PHASE-1` (Core Platform) has been decomposed into 8 subtasks (`.ai/WBS.md` § 4B) but **none is authorized or implemented**. See `.ai/PROJECT_STATE.md` for the authoritative current state; do not rely on this file for status.

## Project layout

This is a monorepo. See `docs/20_PROJECT_STRUCTURE.md` for the canonical layout and rationale. At a glance:

```text
apps/           Runnable applications (api, web, worker*)
backend/        Python/FastAPI backend, organized by architectural layer
                (includes security/authentication — session/token auth)
packages/       Shared cross-app packages (ui; contracts*, seo-core*, config*)
infrastructure/ Operational infrastructure (database, redis*, vector*, ...)
integrations/   External provider adapters*
prompts/        Agent/workflow prompt templates*
tests/          Cross-cutting test placeholders (fixtures*, golden*, evaluation*, e2e*)
docs/           26 approved baseline documents (authoritative specification)
.ai/            Project control system (state, task board, WBS, component matrix, ownership)
scripts/        Developer/operational utility scripts
.github/        CI pipeline (.github/workflows/ci.yml)
```

`*` = directory exists as a documented placeholder only; not yet populated (see that directory's own `README.md` for why).

## Governance

This project follows a documentation-first, authorization-gated development methodology. **No code is written or modified without an explicit, named human authorization recorded in `.ai/TASK_BOARD.md`.** Before touching anything, read `.ai/SESSION_PROMPT.md`.

## Stack (baseline, per `docs/07_TECHNICAL_ARCHITECTURE.md` §3)

- Backend: Python + FastAPI
- Database: PostgreSQL (SQLAlchemy async + Alembic)
- Auth: session/token mechanism (PyJWT + bcrypt) — bare mechanism only; full authorization/tenancy is `PHASE-1`
- Frontend: Next.js (App Router) — scaffolded, no features/components implemented yet
- Observability: structured JSON logging, `prometheus_client`-backed metrics, lightweight in-process tracing
- Testing/CI: pytest (backend) + Vitest (frontend), ten-stage CI pipeline (`.github/workflows/ci.yml`)
- Cache/queue: Redis (not yet in scope)

## Local development

Not yet runnable end-to-end — no session so far has had network access to install dependencies (`pip`/`npm`), so nothing has been runtime-verified beyond one dependency-free test file (see `.ai/PROJECT_STATE.md` Risk R9). Once dependencies are installable:

```text
# Backend (from repo root)
pip install -e ".[dev]"
uvicorn apps.api.main:app --reload
pytest backend/tests/

# Frontend (from repo root)
npm install
npm run dev --workspace=apps/web
npm run test --workspace=apps/web
```

All 8 `PHASE-0` subtasks (`.1` Repository Bootstrap, `.2` Environment & Configuration, `.3` Database & Migrations, `.4` API Foundation, `.5` Authentication Foundation, `.6` Frontend Foundation, `.7` Observability Foundation, `.8` Testing Foundation & CI) are `DONE`. `PHASE-1` (Core Platform) has been broken into 8 subtasks — `PHASE-1.1` Core Domain Model & Persistence, `.2` Authentication: Real User Binding, `.3` Authorization Foundation, `.4` API Contract Layer, `.5` Project Lifecycle, `.6` Dashboard Shell, `.7` Basic AI Runtime Foundation, `.8` Context Foundation — none authorized or implemented. See `.ai/TASK_BOARD.md` for verification-status detail per subtask and `.ai/PROJECT_STATE.md` § 12 for what comes next (authorizing a `PHASE-1` subtask, or a runtime-verification session for `PHASE-0`).
