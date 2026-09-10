"""User domain module (`PHASE-1.1`). See entity.py for the `User` entity
and its invariants. docs/06_DATA_ARCHITECTURE.md §6, §55 (identity,
uniqueness); docs/07_TECHNICAL_ARCHITECTURE.md §14 (dependency direction —
this package imports no infrastructure).
"""

from .entity import User, UserDomainError, UserStatus

__all__ = ["User", "UserDomainError", "UserStatus"]
