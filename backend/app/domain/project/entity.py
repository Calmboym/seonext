"""The `Project` domain entity.

Part of `PHASE-1.1` (.ai/WBS.md §4B). Grounded in
docs/06_DATA_ARCHITECTURE.md §5 (Organization → Workspace → Project → SEO
Knowledge) and §8 (Business Model). Per this session's decomposition
(`.ai/WBS.md` §4B, "Business Model attributes at the Project level"), the
attributes docs/06 §8 describes for "the organization being analyzed" are
carried directly on `Project` rather than a separate `Business` entity —
each Project analyzes one business, and `docs/20_PROJECT_STRUCTURE.md`
§10's `domain/business/` submodule remains an empty placeholder for a
later phase to use if a Project ever needs to describe *multiple*
businesses (it doesn't today).

Same dependency-direction and immutable-entity conventions as
`backend/app/domain/user/entity.py` and `.../workspace/entity.py` — not
repeated here.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum

from backend.app.domain.common.ids import is_valid_id, new_id


class ProjectStatus(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"


class ProjectDomainError(ValueError):
    """Raised when a `Project` invariant would be violated."""


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


def _require_non_empty(value: str, *, field_name: str) -> str:
    stripped = value.strip()
    if not stripped:
        raise ProjectDomainError(f"{field_name} must not be empty")
    return stripped


def _clean_list(values: list[str] | None) -> tuple[str, ...]:
    """Normalizes an optional list of free-text business attributes
    (markets, products, ...) into a de-duplicated, order-preserving,
    immutable tuple of non-empty stripped strings. A `tuple`, not a
    `list`, so it stays consistent with this being a frozen dataclass —
    a mutable `list` field would let a caller mutate a "frozen" Project
    in place, silently, from outside `replace()`."""

    if not values:
        return ()
    seen: set[str] = set()
    cleaned: list[str] = []
    for raw in values:
        item = raw.strip()
        if item and item not in seen:
            seen.add(item)
            cleaned.append(item)
    return tuple(cleaned)


@dataclass(frozen=True)
class Project:
    """A single business being analyzed within a `Workspace`
    (`backend.app.domain.workspace.entity.Workspace`). `workspace_id` is
    required at construction — there is no such thing as a Project
    without a Workspace in this model (docs/03_MASTER_RULES.md §54,
    Referential Integrity: relationships must reference valid objects;
    the *existence* check against a real Workspace row is the
    repository's job at persistence time, but a Project can't even be
    constructed in memory without a workspace_id string being present).

    The business-attribute fields below (industry, markets, ...) are all
    optional at construction (docs/06 §8 lists them as attributes of the
    business being analyzed, not as things known atomically at project-
    creation time) but are always well-formed once set — see `_clean_list`.
    """

    id: str
    workspace_id: str
    name: str
    description: str = ""
    industry: str | None = None
    markets: tuple[str, ...] = field(default_factory=tuple)
    locations: tuple[str, ...] = field(default_factory=tuple)
    business_model: str | None = None
    products: tuple[str, ...] = field(default_factory=tuple)
    services: tuple[str, ...] = field(default_factory=tuple)
    target_audiences: tuple[str, ...] = field(default_factory=tuple)
    commercial_goals: tuple[str, ...] = field(default_factory=tuple)
    strategic_priorities: tuple[str, ...] = field(default_factory=tuple)
    website: str | None = None
    status: ProjectStatus = ProjectStatus.ACTIVE
    created_at: datetime = field(default_factory=_utcnow)
    updated_at: datetime = field(default_factory=_utcnow)

    def __post_init__(self) -> None:
        if not is_valid_id(self.id):
            raise ProjectDomainError(f"invalid project id: {self.id!r}")
        if not is_valid_id(self.workspace_id):
            raise ProjectDomainError(f"invalid workspace_id: {self.workspace_id!r}")
        object.__setattr__(self, "name", _require_non_empty(self.name, field_name="name"))
        object.__setattr__(self, "markets", _clean_list(list(self.markets)))
        object.__setattr__(self, "locations", _clean_list(list(self.locations)))
        object.__setattr__(self, "products", _clean_list(list(self.products)))
        object.__setattr__(self, "services", _clean_list(list(self.services)))
        object.__setattr__(self, "target_audiences", _clean_list(list(self.target_audiences)))
        object.__setattr__(self, "commercial_goals", _clean_list(list(self.commercial_goals)))
        object.__setattr__(self, "strategic_priorities", _clean_list(list(self.strategic_priorities)))
        if not isinstance(self.status, ProjectStatus):
            raise ProjectDomainError(f"invalid status: {self.status!r}")

    @classmethod
    def create(
        cls,
        *,
        workspace_id: str,
        name: str,
        description: str = "",
        industry: str | None = None,
        markets: list[str] | None = None,
        locations: list[str] | None = None,
        business_model: str | None = None,
        products: list[str] | None = None,
        services: list[str] | None = None,
        target_audiences: list[str] | None = None,
        commercial_goals: list[str] | None = None,
        strategic_priorities: list[str] | None = None,
        website: str | None = None,
    ) -> "Project":
        now = _utcnow()
        return cls(
            id=new_id(),
            workspace_id=workspace_id,
            name=name,
            description=description,
            industry=industry,
            markets=tuple(markets or ()),
            locations=tuple(locations or ()),
            business_model=business_model,
            products=tuple(products or ()),
            services=tuple(services or ()),
            target_audiences=tuple(target_audiences or ()),
            commercial_goals=tuple(commercial_goals or ()),
            strategic_priorities=tuple(strategic_priorities or ()),
            website=website,
            status=ProjectStatus.ACTIVE,
            created_at=now,
            updated_at=now,
        )

    @property
    def is_active(self) -> bool:
        return self.status is ProjectStatus.ACTIVE

    def belongs_to(self, workspace_id: str) -> bool:
        """The one method every project-scoped caller should reach for
        before trusting a `Project` it was handed — see `PHASE-1.1`
        acceptance criterion 4 and `PHASE-1.3`'s authorization layer,
        which calls this in addition to (never instead of) the
        repository-level `WHERE workspace_id = ...` filter."""

        return self.workspace_id == workspace_id

    def rename(self, new_name: str) -> "Project":
        return replace(self, name=_require_non_empty(new_name, field_name="name"), updated_at=_utcnow())

    def update_business_profile(
        self,
        *,
        description: str | None = None,
        industry: str | None = None,
        markets: list[str] | None = None,
        locations: list[str] | None = None,
        business_model: str | None = None,
        products: list[str] | None = None,
        services: list[str] | None = None,
        target_audiences: list[str] | None = None,
        commercial_goals: list[str] | None = None,
        strategic_priorities: list[str] | None = None,
        website: str | None = None,
    ) -> "Project":
        """Partial update: any argument left as `None` keeps the current
        value. To *clear* a list field, pass an empty list explicitly."""

        changes: dict[str, object] = {"updated_at": _utcnow()}
        if description is not None:
            changes["description"] = description
        if industry is not None:
            changes["industry"] = industry
        if markets is not None:
            changes["markets"] = tuple(markets)
        if locations is not None:
            changes["locations"] = tuple(locations)
        if business_model is not None:
            changes["business_model"] = business_model
        if products is not None:
            changes["products"] = tuple(products)
        if services is not None:
            changes["services"] = tuple(services)
        if target_audiences is not None:
            changes["target_audiences"] = tuple(target_audiences)
        if commercial_goals is not None:
            changes["commercial_goals"] = tuple(commercial_goals)
        if strategic_priorities is not None:
            changes["strategic_priorities"] = tuple(strategic_priorities)
        if website is not None:
            changes["website"] = website
        return replace(self, **changes)

    def archive(self) -> "Project":
        if self.status is ProjectStatus.ARCHIVED:
            raise ProjectDomainError("project is already archived")
        return replace(self, status=ProjectStatus.ARCHIVED, updated_at=_utcnow())

    def reactivate(self) -> "Project":
        if self.status is ProjectStatus.ACTIVE:
            raise ProjectDomainError("project is already active")
        return replace(self, status=ProjectStatus.ACTIVE, updated_at=_utcnow())
