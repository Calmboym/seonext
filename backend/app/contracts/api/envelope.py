"""The canonical success-response envelope — the counterpart to
`backend.app.api.schemas.errors.ErrorResponse` (16 §12's error half,
already established in `PHASE-0.4` and reused here unchanged, not
reinvented, per `PHASE-1.4` acceptance criterion 2).

docs/16_OUTPUT_CONTRACTS.md §12 defines a single conceptual envelope with
categories spanning both plain application responses and AI-agent
outputs (`execution.workflow_run_id`, `evidence`, `confidence`,
`epistemic_state`, `conflicts`, `recommendations`, ...). §12 itself says:
"The exact implementation schema may differ, but these semantic
categories must remain available where applicable" (emphasis added).
`Auth` and `Projects` (this session's two contract domains) are ordinary
CRUD — no AI agent, workflow, or model produces any of their responses —
so `SuccessEnvelope` below carries only the categories that are always
applicable to *any* response (`status`, `data`, `created_at`, plus
`request_id`/`contract_id`/`contract_version` for traceability and
versioning, §8-9): it does not fabricate always-null `evidence`/
`confidence`/`epistemic_state`/etc. fields just to look complete. The
first endpoint whose response genuinely comes from an AI agent (a later
phase) should define its own envelope that extends this one with those
fields, rather than this file guessing their shape ahead of that need
(docs/03_MASTER_RULES.md §97: no implementation before specification —
applies to speculative fields exactly as much as speculative endpoints).

NOTE (PHASE-1.4, session 9): `pydantic` is declared in `pyproject.toml`
but not installed in this sandbox (no network access — Risk R9). This
file is `ast.parse`-checked and structurally reviewed against the
Pydantic v2 generic-model API, not executed. Verification status:
`IMPLEMENTED / UNVERIFIED`.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Generic, Literal, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class SuccessEnvelope(BaseModel, Generic[DataT]):
    """Top-level response body for every 2xx response from a plain
    application (non-agent) endpoint. `contract_id`/`contract_version`
    identify *this response shape* (docs/16 §8: "Contracts must be
    versioned", e.g. `contract_id="auth.register.response"`,
    `contract_version="1.0"`) independently of the URL-path API version
    (`/api/v1/...`, docs/07 §16) — the two answer different questions:
    the URL version is "which generation of the whole API is this",
    the contract version is "which shape is this one response type,
    which can evolve on its own schedule". Every endpoint that returns a
    `SuccessEnvelope` sets both fields to fixed per-endpoint literals
    when constructing it (see `auth.py`/`projects.py`), not to this
    class's defaults, which exist only because Pydantic requires a
    default or an explicit value at every construction site.
    """

    contract_id: str = Field(..., description="e.g. 'auth.register.response'. See docs/16 §8.")
    contract_version: str = Field(default="1.0", description="Semantic-ish version of this contract shape.")
    status: Literal["success"] = "success"
    data: DataT
    request_id: str = Field(..., description="Correlates this response with server-side logs — matches ErrorBody.request_id's convention.")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
