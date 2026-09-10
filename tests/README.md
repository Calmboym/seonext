# tests/

Cross-cutting, large-suite test root (as opposed to feature-local tests that live beside implementation). See `docs/20_PROJECT_STRUCTURE.md` §33.

**Layout established `PHASE-0.8` (session 7):** `fixtures/`, `golden/`, `evaluation/`, `e2e/` each exist with a `README.md` explaining why they're still empty — none has content yet because nothing in this repository produces AI output, runs a workflow, or has a deployed environment to test against. `.github/workflows/ci.yml` is the actual CI pipeline (`docs/20_PROJECT_STRUCTURE.md` §61's stage order); `backend/tests/` and `apps/web/tests/` hold the test suites that currently exist (backend-unit, API-integration, contract, frontend-unit) — nothing lives directly under this directory yet since no suite so far is genuinely cross-cutting between backend and frontend.
