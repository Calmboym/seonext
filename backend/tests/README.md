# backend/tests/

Backend test suite root. See `docs/20_PROJECT_STRUCTURE.md` §33.

**Wired starting `PHASE-0.8` (session 7):** pytest (`pyproject.toml`'s `[tool.pytest.ini_options]`, already pointed at this directory since `PHASE-0.1`). Three subdirectories exist, matching `.ai/WBS.md` §4's named categories:
- `unit/` — `test_error_hierarchy.py` (zero third-party dependencies — **actually executed** in session 7's sandbox, including a deliberately-broken-build round trip; see its own docstring and `.ai/PROJECT_STATE.md` § 14) and `test_authentication_tokens.py` (needs `pydantic-settings`/`bcrypt`, not installed this session — `IMPLEMENTED`/`UNVERIFIED`).
- `api/` — `test_health_endpoint.py`, a real (in-process) HTTP round trip via FastAPI's `TestClient`. Needs `fastapi`/`httpx` — `UNVERIFIED`.
- `contract/` — `test_response_schemas.py`, validating `HealthResponse`/`ErrorResponse` directly. Needs `pydantic` — `UNVERIFIED`.

Nothing in `PHASE-0.1`–`.7` claims a `TESTED` or `RUNTIME_VERIFIED` status beyond the one file named above. See `.ai/PROJECT_STATE.md` § 14 for the full record of what was actually checked, and Risk R9 for what a future session needs to close the gap for everything else.
