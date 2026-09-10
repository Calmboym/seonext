"""API routes, aggregated by version.

docs/07_TECHNICAL_ARCHITECTURE.md §16: "Public or externally consumed APIs
should support explicit versioning when compatibility requires it" —
example given is `/api/v1/...`. `v1_router` is mounted under that prefix in
backend/app/main.py. Adding a new domain router in a later phase means
`include_router`-ing it here, not inventing a second mounting point.
"""

from fastapi import APIRouter

from .health import router as health_router

v1_router = APIRouter()
v1_router.include_router(health_router)

__all__ = ["v1_router"]
