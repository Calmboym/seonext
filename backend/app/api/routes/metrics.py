"""Metrics scrape endpoint.

Deliberately NOT mounted under the versioned `/api/v1` prefix (see
backend/app/main.py). docs/07_TECHNICAL_ARCHITECTURE.md §16/§51 scope API
versioning to "public or externally consumed APIs"; `/metrics` is an
internal operational endpoint scraped by infrastructure tooling (e.g.
Prometheus), not a contract consumed by API clients — matching common
practice (Prometheus's own exporters, Kubernetes, etc. all expose
unversioned `/metrics`). This is a scope decision made and recorded here,
not silently assumed — revisit if a future session disagrees.
"""

from fastapi import APIRouter
from starlette.responses import Response

from backend.app.observability.metrics import CONTENT_TYPE_LATEST, render_prometheus_text

router = APIRouter(tags=["observability"])


@router.get("/metrics")
async def metrics() -> Response:
    """Prometheus-text-format scrape endpoint. See backend/app/
    observability/metrics/registry.py for what's currently collected —
    only the PHASE-0.7 foundation-level HTTP request metrics; domain/AI
    metrics are added by the phases that introduce them."""

    return Response(content=render_prometheus_text(), media_type=CONTENT_TYPE_LATEST)
