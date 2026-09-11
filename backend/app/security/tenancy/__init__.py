"""Multi-tenancy and tenant isolation (docs/07_TECHNICAL_ARCHITECTURE.md
§§55-56): the Organization → Workspace → Project → Data → Workflow
containment chain, and enforcement that cross-project data retrieval is
impossible through normal application pathways.

Populated (`PHASE-1.3`, session 9): `membership.py` — "is user X part of
workspace Y, and at what role" lookups, consumed by
`backend.app.security.authorization`. The other half of tenant
isolation — "a project lookup scoped to the wrong workspace returns
nothing, structurally" — was already built at the repository level in
`PHASE-1.1` (`backend.app.infrastructure.repositories.project_repository.
ProjectRepository`); this module does not duplicate that, it composes
with it (see `authorization/project.py`).
"""

from .membership import MembershipReader, get_role, is_member

__all__ = ["MembershipReader", "get_role", "is_member"]
