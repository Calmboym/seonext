"""API application entrypoint.

Deliberately thin (docs/20_PROJECT_STRUCTURE.md §5.1: "It should remain
thin. It MUST NOT contain core SEO reasoning.") — all actual assembly
(routes, middleware, exception handlers) lives in backend/app/main.py.
This module only re-exports `app` for an ASGI server to find, and gives a
`python -m apps.api.main` convenience path for local development.

Run locally (once dependencies are installed, see pyproject.toml, and
DATABASE_URL/SECRET_KEY are set, see .env.example):

    uvicorn apps.api.main:app --reload --host 0.0.0.0 --port 8000

or:

    python -m apps.api.main
"""

from backend.app.main import app

__all__ = ["app"]


if __name__ == "__main__":
    import uvicorn

    from backend.app.infrastructure.config import get_settings

    settings = get_settings()
    uvicorn.run(
        "apps.api.main:app",
        host=settings.app.api_host,
        port=settings.app.api_port,
        reload=settings.app.environment.value == "development",
    )
