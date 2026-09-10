# apps/web/types/

Cross-feature TypeScript types not specific to one `features/*` module and not already covered by `packages/contracts` (shared API/output schemas consumed by more than one app, `docs/20_PROJECT_STRUCTURE.md` §32).

Empty at `PHASE-0.6`. `services/health.ts`'s `HealthResponse` type is currently local to that file since it has exactly one consumer (`app/page.tsx`) — promote it here (or to `packages/contracts`, if `apps/api` needs the identical shape) once a second consumer exists.
