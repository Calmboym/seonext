"""Request/response contracts for the `/api/v1/projects` group (docs/07
§15), for `PHASE-1.5`'s create/read/update/list endpoints — written now,
ahead of `PHASE-1.5` (not authorized or started this session), per
`PHASE-1.4`'s own expected output ("present in both the backend contract
location and the shared frontend-visible package" for "project
create/read/update/list (`PHASE-1.5`)") and docs/03 §97 (contracts before
implementation). `PHASE-1.5` is `BACKLOG`/not authorized; nothing here
implies its endpoints exist yet.

Field set mirrors `backend.app.domain.project.entity.Project` exactly
(`PHASE-1.1`) — this is the request-validation boundary
(docs/07 §17) that entity's own docstring said would own full validation
(min/max lengths, etc.), one layer above the domain entity's lighter
invariant checks.

See `envelope.py` and `auth.py`'s module docstrings for the shared
`SuccessEnvelope` / verification-status conventions — identical here
(`IMPLEMENTED / UNVERIFIED`, `ast.parse`-checked only, Risk R9).
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from backend.app.contracts.api.envelope import SuccessEnvelope

_MAX_LIST_ITEMS = 50  # docs/07 §17: length limits are part of request validation


class ProjectCreateRequest(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: str = Field(default="", max_length=2000)
    industry: str | None = Field(default=None, max_length=200)
    markets: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    locations: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    business_model: str | None = Field(default=None, max_length=500)
    products: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    services: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    target_audiences: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    commercial_goals: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    strategic_priorities: list[str] = Field(default_factory=list, max_length=_MAX_LIST_ITEMS)
    website: str | None = Field(default=None, max_length=500)


class ProjectUpdateRequest(BaseModel):
    """Every field optional: `None` means "leave unchanged", matching
    `backend.app.domain.project.entity.Project.update_business_profile`'s
    own partial-update semantics exactly, so this schema can be passed
    straight through to that method's keyword arguments without a
    translation layer. To clear a list field, send an empty list `[]`
    explicitly — not `null`."""

    name: str | None = Field(default=None, min_length=1, max_length=200)
    description: str | None = Field(default=None, max_length=2000)
    industry: str | None = Field(default=None, max_length=200)
    markets: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    locations: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    business_model: str | None = Field(default=None, max_length=500)
    products: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    services: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    target_audiences: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    commercial_goals: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    strategic_priorities: list[str] | None = Field(default=None, max_length=_MAX_LIST_ITEMS)
    website: str | None = Field(default=None, max_length=500)


class ProjectData(BaseModel):
    id: str
    workspace_id: str
    name: str
    description: str
    industry: str | None
    markets: list[str]
    locations: list[str]
    business_model: str | None
    products: list[str]
    services: list[str]
    target_audiences: list[str]
    commercial_goals: list[str]
    strategic_priorities: list[str]
    website: str | None
    status: str
    created_at: datetime
    updated_at: datetime


class ProjectResponse(SuccessEnvelope[ProjectData]):
    contract_id: str = "projects.item.response"


class ProjectListData(BaseModel):
    items: list[ProjectData]
    total: int


class ProjectListResponse(SuccessEnvelope[ProjectListData]):
    contract_id: str = "projects.list.response"
