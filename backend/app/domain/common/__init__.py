"""Cross-cutting domain code shared by every domain module (User, Workspace,
Project, and whatever a later phase adds) — not specific to any one SEO or
platform concept. See docs/20_PROJECT_STRUCTURE.md §10, which reserves
`domain/common/` for exactly this. Currently: stable-ID generation (`ids.py`,
docs/06_DATA_ARCHITECTURE.md §6).
"""

from .ids import is_valid_id, new_id

__all__ = ["is_valid_id", "new_id"]
