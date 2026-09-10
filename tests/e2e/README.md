# tests/e2e/

End-to-end tests exercising the deployed frontend + backend + database together through a real (or realistically simulated) user journey, via browser automation (e.g. Playwright).

Empty at `PHASE-0.8`. `.ai/WBS.md` §4's `PHASE-0.8` Expected Output names exactly three test categories to populate now (backend-unit, frontend-unit, API-integration) — basic E2E is listed as mandatory in `docs/22_TESTING_AND_VALIDATION.md` §120's overall mandatory set, but that same `WBS.md` entry doesn't scope it as "reachable at foundation level" yet: there is no deployed environment, no browser-automation tooling installed, and no user journey to test (no auth UI, no domain UI — `apps/web/features/` is empty). `.github/workflows/ci.yml`'s `e2e` job is a documented no-op for the same reason. Populate once there is an actual journey worth automating.
