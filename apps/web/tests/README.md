# apps/web/tests/

Frontend test suite root. See `docs/20_PROJECT_STRUCTURE.md` §33.

**Wired starting `PHASE-0.8` (session 7):** Vitest (`apps/web/vitest.config.ts`), run via `npm run test --workspace=apps/web`. `unit/health.test.ts` is the frontend-unit category's test (`.ai/WBS.md` §4) — it covers `services/health.ts`'s three response branches (success, HTTP error, network failure). Add `integration/` or `component/` subdirectories here as apps/web grows actual features to test; nothing beyond `unit/` exists yet since nothing beyond `services/health.ts` exists yet to test at another level.
