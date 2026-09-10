"""Project domain module (`PHASE-1.1`). See entity.py for the `Project`
entity, its business-profile attributes, and the disclosed
Business-attributes-on-Project scope decision. docs/06_DATA_ARCHITECTURE.md
§5, §8.
"""

from .entity import Project, ProjectDomainError, ProjectStatus

__all__ = ["Project", "ProjectDomainError", "ProjectStatus"]
