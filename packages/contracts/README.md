# packages/contracts

Shared API/output schemas consumed by more than one app (`apps/api`, `apps/web`, and eventually `apps/worker`). See `docs/20_PROJECT_STRUCTURE.md` §32.

Empty at `PHASE-0` — no domain contracts exist yet (see `docs/16_OUTPUT_CONTRACTS.md`). `PHASE-0.4`'s error envelope is defined backend-locally in `backend/app/api/schemas/errors.py` for now, since it is not yet consumed cross-app; it is a candidate to move here once `apps/web` (`PHASE-0.6`) needs the same shape.
