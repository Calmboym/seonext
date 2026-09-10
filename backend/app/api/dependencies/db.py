"""Dependency-injection wiring for the API layer.

Re-exports the infrastructure-layer session dependency at the API
boundary, since "dependency wiring" is an explicit `apps/api`/API-layer
responsibility (docs/20_PROJECT_STRUCTURE.md §5.1, §7). No route currently
uses this (the health check is dependency-free by design, see
backend/app/api/routes/health.py) — it exists so the first route that
needs a DB session in a later phase has a ready `Depends(get_db_session)`
import point at the API layer, rather than importing across layers ad hoc.
"""

from backend.app.infrastructure.database.session import get_db_session

__all__ = ["get_db_session"]
