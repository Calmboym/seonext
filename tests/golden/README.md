# tests/golden/

Golden datasets: known-correct expected outputs for AI/agent workflows, used to detect regressions in non-deterministic output quality. See `docs/20_PROJECT_STRUCTURE.md` §33/§34.

Empty at `PHASE-0.8` — no AI runtime, agent, or workflow exists yet to have a golden output (`backend/app/intelligence/`, `backend/app/orchestration/` are both empty placeholders). Referenced as a "no-op, nothing to evaluate yet" stage in `.github/workflows/ci.yml`'s `ai-evaluation` job.
