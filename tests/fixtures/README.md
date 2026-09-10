# tests/fixtures/

Shared, cross-cutting test fixtures (sample API responses, sample SERP data, sample entity records) reusable across multiple test suites — as opposed to fixtures local to one test file. See `docs/20_PROJECT_STRUCTURE.md` §33.

Empty at `PHASE-0.8` — no test suite yet needs a fixture shared across more than one file. `backend/tests/unit/test_authentication_tokens.py`'s `_configured_settings` fixture, for example, is local to that one file since nothing else needs it yet.
