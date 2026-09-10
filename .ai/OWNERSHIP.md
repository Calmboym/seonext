# OWNERSHIP.md — Ownership Boundaries

No individuals or teams exist yet (pre-implementation), so "owner" below means **which document is the binding source of truth and which future subsystem is responsible** — not a named person. Update with real owner names once the project has contributors. Ownership exists to prevent duplicate components, conflicting implementations, unclear responsibility, circular dependencies, and feature logic leaking into shared infrastructure.

| Domain | Governing Document(s) | Responsible Subsystem (once built) | Notes |
|---|---|---|---|
| Foundation (components) | `19_DESIGN_SYSTEM.md` §§32–33 | `packages/ui` (foundation layer) | Changes require Design System sign-off; nothing else may redefine a token or primitive |
| Shared (components) | `19` §§34–49, `.ai/COMPONENT_MATRIX.md` § 3 | `packages/ui` (shared layer) | A feature team may propose a new shared component but cannot unilaterally merge one — must land in `19`/Component Matrix first |
| Feature (components) | `17_UI_UX_SPECIFICATION.md` (per-workspace sections), `18_FRONTEND_ARCHITECTURE.md` §9.2 | `apps/web/features/*` | Feature components must not be imported cross-feature; promote to Shared instead |
| Backend | `07_TECHNICAL_ARCHITECTURE.md` | Backend service(s) (Python/FastAPI per `07` §3) | See Known Risk R1 in `PROJECT_STATE.md` re: `.gitignore` |
| Domain (SEO knowledge model) | `08_SEO_KNOWLEDGE_MODEL.md`, `09_ENTITY_EAV_MODEL.md`, `10_TOPIC_MODELING_AND_CLUSTERING.md`, `11_SEARCH_AND_SERP_INTELLIGENCE.md` | Domain/knowledge layer | Terminology precision (Topic/Keyword/Entity/Page/Page Candidate Mapping) is binding — see Q3 resolution |
| AI / Agents | `05_AI_AGENT_ARCHITECTURE.md`, `13_AGENT_SPECIFICATIONS.md` | Agent runtime | Agent-level dependency declarations should be corrected under `DOCS-MAINT-001` |
| Workflows | `14_AGENT_WORKFLOW.md`, `15_HUMAN_IN_THE_LOOP.md` | Orchestration layer | |
| Decision Engine | `12_SEO_DECISION_ENGINE.md` | Decision layer | Recommendation ≠ Decision ≠ Action must be preserved (`24` §96) |
| Data | `06_DATA_ARCHITECTURE.md` | Data layer / persistence | `06` currently has no explicit self-declared "Depends On" — tracked under `DOCS-MAINT-001` |
| Integrations / Output Contracts | `16_OUTPUT_CONTRACTS.md` | Contract layer | |
| Infrastructure | `07_TECHNICAL_ARCHITECTURE.md`, `20_PROJECT_STRUCTURE.md` | Infra/DevOps | |
| Testing | `22_TESTING_AND_VALIDATION.md` | QA / CI | WCAG 2.2 AA conformance testing belongs here for all UI components |
| Design System | `19_DESIGN_SYSTEM.md` | Design System maintainers | Final authority on Foundation/Shared visual and interaction rules |
| Project Control (this `.ai/` system) | This directory | Whoever runs each session | Update `PROJECT_STATE.md` and `TASK_BOARD.md` at the end of every meaningful task (see `SESSION_PROMPT.md`) |

## Ownership Rules

1. A component/subsystem has exactly one governing document and one responsible subsystem. If two documents appear to claim the same responsibility, that is a contradiction to raise, not something to resolve by picking one silently.
2. Feature-specific logic must not leak into Foundation or Shared — see the anti-duplication rule in `.ai/COMPONENT_MATRIX.md` § 4.
3. This table is itself owned by whoever maintains `.ai/` — update it whenever `WBS.md` or `COMPONENT_MATRIX.md` changes in a way that shifts responsibility.

## Per-Component Ownership (`BOOTSTRAP-002.5`, authorized 2026-09-06 — see Q9, `PROJECT_STATE.md` § 10)

Assigns a single owner to every component in `.ai/COMPONENT_MATRIX.md` §§2–4, deriving deterministically from the tier-level rows above (Foundation/Shared/Feature) rather than introducing a new ownership dimension. Full dependency/testing detail for each component lives in `COMPONENT_MATRIX.md` § 5; this table exists to satisfy `WBS.md` §3's acceptance criterion for `BOOTSTRAP-002.5` ("every component has exactly one owner") in one place.

| Tier | Owner | Applies to |
|---|---|---|
| FOUNDATION | Design System maintainers / `packages/ui` (foundation layer) | Every row in `COMPONENT_MATRIX.md` § 2 (Box, Stack, Grid, Text, Icon, Separator, VisuallyHidden, design tokens) |
| SHARED | Design System maintainers / `packages/ui` (shared layer) | Every row in `COMPONENT_MATRIX.md` § 3 — a Feature team may propose additions but cannot unilaterally merge one (pre-existing rule, row 2 above) |
| FEATURE | The specific `features/<module>` named in `COMPONENT_MATRIX.md` § 4's first column (per `18_FRONTEND_ARCHITECTURE.md` §12 — "each major domain should have a clear owner... owns \[its\] presentation logic") | Every row in § 4, with no exceptions — see resolution note below |

**Dashboard, resolved by explicit human decision (Q11, `PROJECT_STATE.md` § 10, 2026-09-06):** the Dashboard-group components (Project Status Panel, Strategic Opportunities List, Decision Queue Widget, Research Health Panel) initially had no owning `features/*` module — `18` §8 lists `dashboard/` as a route, not a feature, in its (explicitly non-binding, "conceptual baseline") module list. Per this document's own Rule 1 and `WBS.md` §3's "Human Approval Required: Yes, if ownership is contested," `BOOTSTRAP-002.5` left this unassigned rather than guessing, and surfaced it to the human. The human has since explicitly approved a dedicated `features/dashboard` module as the owner of Dashboard and its Dashboard-specific components. That module is an ownership assignment only — it has not been scaffolded or implemented; no `PHASE-0` or implementation work has been authorized. Every component in `COMPONENT_MATRIX.md` §§2–4 now has exactly one owner with no open exceptions.
