"""API-integration tests: a real (in-process) HTTP round trip through the
FastAPI app, as opposed to unit tests calling functions directly.

API-integration category (.ai/WBS.md §4, PHASE-0.8's third named
category, alongside backend-unit and frontend-unit). Distinguished from
backend/tests/contract/test_response_schemas.py: this file asks "does a
real request to a real route produce the right status/body," the
contract tests ask "does the declared response schema accept/reject the
right shapes," independent of any live route.

NOTE (PHASE-0.8, session 7): requires `fastapi`, `httpx` (FastAPI's
TestClient needs it), and the full application import chain
(`pydantic-settings`, `sqlalchemy`, etc., transitively via
backend/app/main.py) — none installed in this session's sandbox (Risk
R9). Syntax-checked (`ast.parse`) only.
"""

import pytest


@pytest.fixture
def client(monkeypatch):
    """A TestClient around the real `create_app()` factory
    (backend/app/main.py) — not a hand-built minimal app — so this test
    exercises the actual middleware stack (request_id, request logging +
    metrics) and exception handlers, not a stripped-down stand-in that
    could pass while the real wiring is broken."""

    from fastapi.testclient import TestClient

    from backend.app.infrastructure.config.settings import get_settings
    from backend.app.main import create_app

    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://test:test@localhost/test")
    monkeypatch.setenv("SECRET_KEY", "test-only-secret-key-do-not-use-in-production")
    get_settings.cache_clear()

    app = create_app()
    return TestClient(app)


def test_health_endpoint_returns_200_with_the_documented_shape(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_endpoint_response_includes_a_request_id_header(client):
    """backend/app/api/middleware/request_id.py (PHASE-0.4) should attach
    a request ID to every response — this is the one behavior from that
    middleware an API-integration test can observe from outside the
    process, as opposed to unit-testing the middleware function directly."""

    response = client.get("/api/v1/health")

    assert "x-request-id" in {k.lower() for k in response.headers.keys()}


def test_metrics_endpoint_is_reachable_and_unversioned(client):
    """PHASE-0.7 acceptance criterion 2: "a metrics endpoint or exporter
    is reachable." Also protects the deliberate scope decision
    (backend/app/api/routes/metrics.py's docstring) that this endpoint is
    NOT mounted under /api/v1."""

    response = client.get("/metrics")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/plain")


def test_a_nonexistent_route_returns_404():
    """Baseline sanity check that routing itself works — not specific to
    any PHASE-0 acceptance criterion, but the cheapest possible check
    that the app boots and its router is wired at all."""

    from fastapi.testclient import TestClient

    from backend.app.main import app

    client = TestClient(app)
    response = client.get("/api/v1/this-route-does-not-exist")

    assert response.status_code == 404
