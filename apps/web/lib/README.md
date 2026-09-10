# apps/web/lib/

Cross-feature utilities and framework glue — not specific to one `features/*` module, not a React hook (see `hooks/`), and not a component (see `components/`). See `docs/20_PROJECT_STRUCTURE.md` §25.

Empty at `PHASE-0.6`. `services/health.ts` (this subtask's API client) lives in `services/`, not here, since it is a data-fetching service per §25's own directory split, not a generic utility.
