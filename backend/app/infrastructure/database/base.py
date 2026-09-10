"""Declarative base for all ORM models.

No domain models are defined at PHASE-0 — this module exists purely so the
migration framework (infrastructure/database/migrations/) has a real
`Base.metadata` to autogenerate against once a later phase adds entities.
See docs/07_TECHNICAL_ARCHITECTURE.md §30 (Migrations) and
docs/20_PROJECT_STRUCTURE.md §29-30 (Database Structure, Repository Pattern).
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Shared declarative base. Domain-specific models (later phases) should
    subclass this rather than defining their own `DeclarativeBase`, so that
    a single `Base.metadata` covers the whole schema for migrations."""
