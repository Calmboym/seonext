"""Membership domain module (`PHASE-1.3`). See entity.py for the
`Membership` entity, the `Role` enum, and the disclosed placement
rationale (why this lives in `domain/`, not directly in `security/`).
docs/07_TECHNICAL_ARCHITECTURE.md §54; docs/06_DATA_ARCHITECTURE.md §55.
"""

from .entity import Membership, MembershipDomainError, Role

__all__ = ["Membership", "MembershipDomainError", "Role"]
