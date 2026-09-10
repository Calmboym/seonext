"""Stable identifier generation for domain entities.

docs/06_DATA_ARCHITECTURE.md §6 (Core Identity Model): "Important objects
should have stable identifiers... Identifiers should remain stable even
when names or descriptions change." This module is the single place a new
domain-entity ID is minted, so every entity (User, Workspace, Project, and
whatever a later phase adds) gets the same identifier shape rather than
each domain module inventing its own.

Uses `uuid.uuid4()` (stdlib, zero third-party dependencies) rather than a
sequential integer: a predictable/sequential ID would let a caller guess
neighboring IDs, which docs/07_TECHNICAL_ARCHITECTURE.md §97 (Security
Architecture) and §98 (Input Security) treat as the kind of thing to avoid
by construction, not by convention. A UUIDv7 (time-ordered) would give
better database index locality than uuid4's fully random ordering, but
Python 3.12's stdlib `uuid` module has no `uuid7()` (added in 3.14) and no
third-party backport is installed in this sandbox (Risk R9, `.ai/
PROJECT_STATE.md` § 9) — uuid4 is the correct, dependency-free default
for now; revisit once a session can install a uuid7 backport or upgrade
the Python baseline.

Lives in `domain/common/` per docs/20_PROJECT_STRUCTURE.md §10's own
domain-submodule list, which already reserves `common/` for exactly this
kind of cross-cutting, non-SEO-domain-specific code.
"""

from __future__ import annotations

import uuid


def new_id() -> str:
    """Mint a new stable identifier: the canonical (lowercase, hyphenated)
    string form of a random UUID4. Every domain entity factory in this
    package (`User.register`, `Workspace.create`, `Project.create`) calls
    this exactly once, at construction, and never again for that entity's
    lifetime."""

    return str(uuid.uuid4())


def is_valid_id(value: str) -> bool:
    """True if `value` is a syntactically valid ID minted by `new_id()`
    (or any RFC 4122 UUID string). Used at domain-entity construction
    boundaries to reject a malformed/foreign identifier early, rather
    than letting it reach a database constraint violation first."""

    try:
        uuid.UUID(value)
    except (ValueError, AttributeError, TypeError):
        return False
    return True
