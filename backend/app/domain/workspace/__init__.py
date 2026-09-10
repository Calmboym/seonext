"""Workspace domain module (`PHASE-1.1`). See entity.py for the
`Workspace` entity, its invariants, and the disclosed Organization-vs-
Workspace scope simplification. docs/06_DATA_ARCHITECTURE.md §5, §6.
"""

from .entity import Workspace, WorkspaceDomainError, WorkspaceStatus

__all__ = ["Workspace", "WorkspaceDomainError", "WorkspaceStatus"]
