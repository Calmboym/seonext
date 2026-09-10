# COMPONENT_MATRIX.md — Operational Component Taxonomy

This file defines the **operational** FOUNDATION / SHARED / FEATURE taxonomy used for build sequencing and ownership (per the bootstrap process). It is a *different classification dimension* from, and does not replace, the taxonomies already defined in:

- `19_DESIGN_SYSTEM.md` § 32 — composability depth (Foundations → Primitives → Components → Patterns → Templates)
- `18_FRONTEND_ARCHITECTURE.md` § 9 — code-organization responsibility (Route / Feature / Application / Domain / Shared UI Layers)
- `17_UI_UX_SPECIFICATION.md` § 66 — functional grouping (Navigation / Data / AI / Workflow / Knowledge / Visualization / System)

Each of those three documents carries a cross-reference note pointing here (added during `BOOTSTRAP-001`, per Q6).

**Status as of `BOOTSTRAP-002.1`–`BOOTSTRAP-002.6` (2026-09-06):** The FOUNDATION and SHARED tiers below are **confirmed** (derived and cross-checked against their declared source sections, duplicates resolved). The FEATURE tier has its **full per-workspace breakdown**. § 5 now carries the full per-component registry (owner, dependencies, used_by, design tokens, accessibility/responsive/states/testing requirements, implementation status) — `BOOTSTRAP-002.4`–`.6`'s output, authorized 2026-09-06 (Q9). Dashboard's ownership (the one item flagged rather than resolved during `BOOTSTRAP-002.5`) was subsequently decided by explicit human approval — see Q11, `PROJECT_STATE.md` § 10 — and is reflected below; every component in this matrix now has exactly one owner with no open exceptions.

**Accessibility baseline for every component in this matrix: WCAG 2.2 AA** (per Q7, `03_MASTER_RULES.md` § 79).

---

## 1. How the Three Dimensions Relate

| Original dimension | Answers | Operational tier it maps to |
|---|---|---|
| Design System layers (`19` §32) | "How composable/reusable is this?" | Foundations + Primitives → **FOUNDATION**; domain-agnostic Components/Patterns/Templates → **SHARED** |
| Frontend Architecture layers (`18` §9) | "Where does this code live and what does it coordinate?" | Shared UI Layer (§9.5) + cross-cutting Domain types (§9.4) → **SHARED**; Feature Layer (§9.2) → **FEATURE** |
| UI/UX functional categories (`17` §66) | "What purpose does this serve for the user?" | Navigation/System → **SHARED**; Knowledge/Visualization → **FEATURE**; AI/Workflow → split by whether the specific instance is domain-agnostic (the display *shell*, → SHARED) or domain-specific (the *populated instance* in a given workspace, → FEATURE) |

A single real component can be described by all three dimensions simultaneously — e.g. the **Confidence Indicator** component is: Design-System-layer "Component" (§32) + Frontend-Architecture "Shared UI" (§9.5) + UI/UX-category "AI" (§66) + operational tier **SHARED**. The dimensions are not in conflict; they answer different questions about the same object.

---

## 2. FOUNDATION Tier — CONFIRMED (`BOOTSTRAP-002.1`)

*Source: `19_DESIGN_SYSTEM.md` § 33 (Foundation Components), read against the full §§33–49 range to confirm the FOUNDATION/SHARED boundary + tokens/typography/color/theme sections (§§13–20).*

| Component | Source | Notes |
|---|---|---|
| Box / Layout | 19 §33 | |
| Stack | 19 §33 | |
| Grid | 19 §33 | |
| Text | 19 §33 | |
| Icon | 19 §33 | |
| Separator | 19 §33 | |
| VisuallyHidden | 19 §33 | Accessibility primitive — WCAG 2.2 AA relevant |
| Design tokens (color / spacing / type) | 19 §§13–20 (tokens, typography, color, theme sections) | Consumed by every layer in `18` §9, not owned by any one of them |

**Boundary confirmation:** `19` §§34–49 were read in full as part of this derivation. Nothing in that range belongs in FOUNDATION — §§34–44 are the domain-agnostic "Components" layer (→ SHARED, § 3 below) and §§45–49 are the epistemic/AI display shells (→ SHARED, § 3 below, per the AI/Workflow split rule in § 1). **Acceptance criterion met:** every FOUNDATION item above is traceable to a single named source section, and no item is duplicated elsewhere in this matrix.

---

## 3. SHARED Tier — CONFIRMED (`BOOTSTRAP-002.2`)

*Declared sources for this subtask: `17` §66 (Navigation / Data / AI / Workflow / System categories) and `19` §§45–49 (Epistemic State / Confidence / Evidence / Recommendation / Decision components). The §§34–44 rows below were surfaced during `BOOTSTRAP-002.1`'s boundary-reading of `19` §§33–49 and are carried forward here rather than re-derived, per the FOUNDATION/SHARED boundary confirmed in § 2. `18` §9.5 (Shared UI Layer) is cited only as a corroborating cross-reference — it independently names the same list and explicitly states it "maps to operational SHARED," which further grounds this tier but did not change its contents.*

| Component | Source | Notes |
|---|---|---|
| Button, IconButton, Link, ButtonGroup, SplitButton (where justified) | 19 §34 | |
| Input, Textarea, Select, Combobox, Checkbox, Radio, Switch, Date/Time controls, Search field | 19 §36 / 18 §9.5 | Accessible names + predictable keyboard behavior required (WCAG 2.2 AA) |
| Badge, Tag, Avatar, Table, Data Grid (where necessary), Statistic, Progress, Timeline, Skeleton | 19 §37 | |
| Tooltip | 19 §37, §39 | Named under both Data Display and Overlay in `19` — one component, two use contexts; not a duplicate |
| Empty State | 19 §37, §51 / 17 §66 System / 18 §9.5 | One component, multiple cross-references |
| Alert | 19 §37 / 17 §66 System | |
| Sidebar, Breadcrumb, Tabs, Pagination, Menu, Dropdown, Command/Search Palette | 19 §38 / 17 §66 Navigation | |
| Project Switcher | 17 §66 Navigation | No `19` counterpart yet — flagged for Design System backlog |
| Dialog | 19 §39 / 18 §9.5 | Same component as "Modal" in `17` §66 System — see § 6 Observations; "Dialog" adopted as the canonical name |
| Drawer | 19 §39 / 17 §66 System / 18 §9.5 | |
| Popover, Context Menu | 19 §39 | |
| Status indicator (Draft / AI Proposed / Validated / Under Review / Human Approved / Rejected / Superseded / Archived) | 19 §44 | Generic status-badge shell; per-workflow status *values* are feature-specific data, not separate components |
| Epistemic State Component (Observed / Inferred / Estimated / Recommended / Human Approved / Conflicted / Unknown) | 19 §45 | Not interchangeable with the workflow-status component above (19 §45 explicit) |
| Confidence Component | 19 §46 / 17 §66 AI ("Confidence Indicator") | |
| Evidence Component | 19 §47 / 17 §66 AI ("Evidence Panel") / 17 §36 ("Evidence Viewer") | Same component under three names across three docs — canonical name: **Evidence Component** |
| Recommendation Component | 19 §48 / 17 §66 AI ("AI Recommendation") | |
| Decision Component | 19 §49 | |
| AI Insight, Rationale Summary | 17 §66 AI | Named in `17` with no `19` counterpart yet — flagged for Design System backlog, not invented here |
| Progress Stepper, Workflow Status, Review Queue, Approval Dialog | 17 §66 Workflow | Domain-agnostic shells, shared across any HITL flow (`15_HUMAN_IN_THE_LOOP.md`). Their *populated instances* per workflow (e.g. the Decision Center's review queue) are FEATURE-tier — see § 4 |
| Toast, Error State, Loading State | 17 §66 System / 18 §9.5 | |

**Acceptance criteria met:** every item above traces to at least one named source section; no item duplicates a FOUNDATION-tier item (§ 2); same-named items appearing under multiple source sections are listed once, not double-counted.

---

## 4. FEATURE Tier — Full Per-Workspace Breakdown (`BOOTSTRAP-002.3`)

*Sources: per-workspace sections of `17_UI_UX_SPECIFICATION.md` (§§10–35, §§41–42), `17` §66 Knowledge/Visualization categories, and `18_FRONTEND_ARCHITECTURE.md` §9.2 (Feature Layer) + §8 (Proposed Project Structure, for the canonical `features/` module list). Each row is a domain-specific component or a domain-specific **instance** of a SHARED shell (§ 3) populated with workspace data — the shell itself is not re-listed here.*

| Feature Module (`18` §8 `features/`) | Component | Source | Notes |
|---|---|---|---|
| `features/dashboard` | Project Status Panel, Strategic Opportunities List, Decision Queue Widget, Research Health Panel | 17 §10 | Dashboard aggregates data from many features. Not itself in `18` §8's original conceptual module list, but that list is explicitly non-binding ("a conceptual baseline... must be validated... before coding"); `features/dashboard` was created by explicit human decision (Q11, `PROJECT_STATE.md` § 10, 2026-09-06) to give it a definite owner. |
| `business-research` | Business Profile Editor (business / products / services / audiences / markets / differentiators / goals / commercial priorities / geographic scope / language markets) | 17 §12 | |
| `business-research` | Business-Importance-vs-Search-Demand Comparison view | 17 §12 | |
| `entities` | Entity List | 17 §13 | |
| `entities` | Entity Detail Panel (Identity / Types / Names-Aliases / Attributes / Relationships / Topics / Queries / SERPs / Pages / Evidence / Confidence / History) | 17 §13 | |
| `entities` | Entity Card | 17 §66 Knowledge | |
| `entities` | Entity Graph | 17 §14 / 17 §66 Visualization | |
| `eav` | EAV Table | 17 §15 / 17 §66 Knowledge | |
| `topics` | Topic Card / Row | 17 §16 / 17 §66 Knowledge | |
| `topics` | Topic Status Board (Discovered / Validated / Rejected / Uncertain / Merged / Archived) | 17 §16 | Feature-specific instance of the SHARED status shell (§ 3) |
| `topics` | Topic Source Indicator | 17 §17 | |
| `topics` | Topic Validation Decision-Factors Panel | 17 §18 | Feature-specific instance of the SHARED Recommendation/Decision shells |
| `intent` | Intent Distribution component | 17 §19 | |
| `serp` | Query List | 17 §20 / §21 | |
| `serp` | SERP Snapshot Viewer | 17 §21 | |
| `serp` | SERP Comparison view | 17 §22 | |
| `clustering` | Cluster List view | 17 §23 | |
| `clustering` | Topic Graph (cluster graph view) | 17 §23 / 17 §66 Visualization | Distinct from Topical Map and Architecture Tree — see § 6 |
| `clustering` | Similarity Matrix (cluster matrix view) | 17 §23 / 17 §66 Visualization | |
| `clustering` | Cluster Hierarchical Tree view | 17 §23 | |
| `topical-map` | Topical Map Visualization | 17 §24 | `17` §24 explicitly warns this must not be confused with Page Architecture — see § 6 |
| `page-candidates` | Page Candidate Card | 17 §25 | |
| `page-candidates` | Mapping Status Badge (UNMAPPED / CANDIDATE / RECOMMENDED / APPROVED / REJECTED / MERGED) | 17 §25 | |
| `page-architecture` | Architecture Tree | 17 §26 / 17 §66 Visualization | |
| `internal-linking` | Linking Graph | 17 §27 / 17 §66 Visualization | |
| `internal-linking` | Link Recommendation Row | 17 §27 | |
| `content-gaps` | Content Gap Card | 17 §28 | |
| `cannibalization` | Cannibalization Report Card | 17 §29 | |
| `competitors` | Competitor Comparison view | 17 §30 | |
| `competitors` | Competitor Level Badge (Business / Search / Domain / Page / Topic Competitor) | 17 §30 | |
| `decisions` | Decision Record Card | 17 §31 | Feature instance of the SHARED Decision Component |
| `decisions` | Decision Status Badge | 17 §32 | Feature instance of the SHARED status shell |
| `reviews` | Review Queue List | 17 §33 | Feature instance of the SHARED Review Queue shell |
| `reviews` | Review Interface (three-pane: object under review / recommendation + decision factors / evidence + provenance, plus action bar: Approve, Reject, Modify, Defer, Request More Evidence, Add Note) | 17 §34 | |
| `reviews` | Decision Recording Log | 17 §35 | |
| `workflows` | Workflow Monitor | 17 §41 | Feature instance of the SHARED Workflow Status shell |
| `workflows` | Workflow Step Indicator | 17 §41 / §42 | |

**Acceptance criteria met:** every item above traces to at least one named source section; no row duplicates a SHARED-tier shell — where a FEATURE row is a populated *instance* of a SHARED shell, that relationship is called out explicitly in the Notes column rather than re-listing the shell itself.

---

## 5. Component Registry (`BOOTSTRAP-002.4`–`.6`, authorized 2026-09-06 — see Q9, `PROJECT_STATE.md` § 10)

Machine/agent-readable registry for every component listed in §§2–4. Schema per component: `owner`, `dependencies`, `used_by`, `design_tokens`, `accessibility`, `responsive`, `states`, `testing_requirements`, `implementation_status`.

To avoid repeating identical values 60+ times, § 5.0 states each field's **tier-level default once, with a full source citation**. §§5.1–5.3 give the per-component table; a row's `Dependencies`, `Used By`, and `Testing (beyond default)` cells are filled explicitly, and its `Notes` cell states either "tier default applies" or the specific delta. No field is left blank: every cell either restates a cited default or gives a cited, component-specific value. This mirrors the pattern already used in §§2–4 for the WCAG 2.2 AA baseline (stated once, not repeated per row).

### 5.0 Registry Framework — Tier-Level Defaults

| Field | FOUNDATION default | SHARED default | FEATURE default |
|---|---|---|---|
| **Design tokens** | *Is* the token layer itself: Raw → Semantic → Component token chain (`19` §111) plus the token categories in `19` §§13–20 (design tokens, naming, color system, dark/light theme, theme tokens) and §§21–26 (typography, spacing) | Consumes Semantic + Component tokens per the `19` §111 chain (e.g. "Button Primary ← Primary Action ← Raw Teal") | Consumes whichever Shared-tier component tokens its instantiated shell(s) use; chart/graph-bearing components additionally draw on the Analytical Color Palette (`19` §66) |
| **Accessibility** | WCAG 2.2 AA baseline (`19` §93); `19` §92 Accessibility Contract (keyboard interaction, focus management, semantic roles, state attributes, accessible names, disabled behavior) | Same baseline + `19` §§94–97 (keyboard interaction, screen-reader support, color contrast in both themes, non-color semantics) | Same baseline; graph/chart Feature components additionally require `19` §109 (structured alternative representation — a graph must never be the only way to access the relationship data) and §110 (text summaries, accessible labels, legends, meaningful data tables) |
| **Responsive** | N/A for pure primitives (Box/Stack/Grid/Text/Icon/Separator/VisuallyHidden are the mechanism other tiers use to *build* responsive behavior); breakpoint scale itself is `19` §29 (Compact/Tablet/Desktop/Wide Desktop) | Must define graceful-degradation behavior per `19` §30 (e.g. Table → horizontal scroll, Sidebar → collapsed navigation) at the four breakpoints in §29 | Same four breakpoints; analytical/dense Feature views (graphs, matrices, trees) must "degrade gracefully" per `19` §133 |
| **States** | N/A (non-interactive primitives) except VisuallyHidden (no visual state) | Component States Matrix (`19` §112): Default / Hover / Focus / Active / Selected / Disabled / Loading / Error / Success — "only applicable states need to be implemented" | Same matrix; components that are populated instances of the Shared Status/Epistemic-State shells additionally carry those shells' specific domain-state values (already enumerated in §§3–4 above, not repeated here) |
| **Testing requirements** | `22` §48 Unit tier + `19` §127 Visual Regression (foundations explicitly in scope) + `19` §129 Component Unit Testing | `22` §48 (Unit + Component tiers) + `22` §76 Accessibility Testing + `19` §§127–133 (visual regression, cross-theme, RTL, responsive testing) | `22` §48 (Component + Integration tiers) + `22` §49 Frontend Contract Testing (response schemas, error formats, pagination, streaming, empty states) + `22` §76 Accessibility Testing; graph/chart Feature components additionally require `22` §78 Visualization Testing (correct data/labels/relationships, empty state, large-dataset behavior, keyboard accessibility, alternative representations) |
| **Implementation status** | `NOT_STARTED` | `NOT_STARTED` | `NOT_STARTED` |

All three tiers additionally carry `22` §77 Localization Testing (English/Persian/German, RTL/LTR, translation-expansion layout, numeric/date/currency formatting) wherever a component renders user-facing or AI-generated text — this is most of the registry, so it is folded into the tier defaults above rather than repeated per row; components that are purely structural (Box, Stack, Grid, Separator) are the only rows where it does not apply.

**Dependency direction** (grounds the `Dependencies`/`Used By` columns below): `18` §11 — Routes → Features → Application → Domain → Infrastructure Adapters, with "Shared UI may be consumed by all appropriate presentation layers." Concretely: FOUNDATION is consumed by everything and depends on nothing above the token layer; SHARED depends on FOUNDATION and is consumed by FEATURE (and by other SHARED components, e.g. Tooltip-inside-Table); FEATURE depends on whatever SHARED shells it instantiates (per the "instance of" notes already in §§3–4) plus its own module's Domain-layer types (`18` §9.4: Entity/Topic/Query/Intent/SERPSnapshot/PageCandidate/Decision/Evidence/Workflow) and Application-layer functions (`18` §9.3), and per Feature Module Boundaries (`18` §10) is *not* consumed by other features — each feature module's UI is scoped to its own route/workspace.

### 5.1 FOUNDATION Tier Registry

| Component | Owner | Dependencies | Used By | Notes |
|---|---|---|---|---|
| Box / Layout | Foundation (Design System / `packages/ui` foundation layer, per `OWNERSHIP.md`) | Design tokens only (spacing, layout) | Universal — every SHARED and FEATURE component (`18` §11) | Tier defaults apply throughout |
| Stack | Foundation | Design tokens only (spacing) | Universal | Tier defaults apply |
| Grid | Foundation | Design tokens only (spacing, layout) | Universal | Tier defaults apply |
| Text | Foundation | Design tokens only (typography, color) | Universal | Tier defaults apply |
| Icon | Foundation | Design tokens only | Universal | Tier defaults apply |
| Separator | Foundation | Design tokens only (color, spacing) | Universal | Purely structural — Localization Testing does not apply (no text) |
| VisuallyHidden | Foundation | None (no visual token dependency) | Universal | Accessibility-primitive: exists solely to satisfy `19` §92's "accessible names" requirement for other components; no visual states |
| Design tokens (color / spacing / type) | Foundation | None — this row *is* the base of the chain | Universal — consumed by every other row in this registry | The chain itself: Raw → Semantic → Component (`19` §111) |

### 5.2 SHARED Tier Registry

| Component | Owner | Dependencies | Used By | Testing (beyond tier default) | Notes |
|---|---|---|---|---|---|
| Button, IconButton, Link, ButtonGroup, SplitButton | Shared (Design System / `packages/ui` shared layer) | Foundation (Box, Text, Icon) + tokens | Universal — near every Feature workspace | `19` §35 Button States | Cross-cutting; not individually enumerated per consumer in source docs |
| Input, Textarea, Select, Combobox, Checkbox, Radio, Switch, Date/Time controls, Search field | Shared | Foundation + tokens | Every workspace with a form (Business Profile Editor, Review Interface, filters) | `22` §76 accessible-forms explicitly | Accessible names + predictable keyboard behavior required (`19` §36) |
| Badge, Tag, Avatar, Table, Data Grid, Statistic, Progress, Timeline, Skeleton | Shared | Foundation + tokens | Cross-cutting across most FEATURE list/detail views | `19` §108 (Table keyboard nav) for Table/Data Grid | Cross-cutting, not individually enumerated |
| Tooltip | Shared | Foundation + tokens | Cross-cutting | `19` §104 Tooltip Rules | Named under both Data Display and Overlay in `19` — one component |
| Empty State | Shared | Foundation + tokens | Every list/detail Feature view before data exists | — | One component, multiple cross-references (`19` §37/§51, `17` §66, `18` §9.5) |
| Alert | Shared | Foundation + tokens | Cross-cutting | — | — |
| Sidebar, Breadcrumb, Tabs, Pagination, Menu, Dropdown, Command/Search Palette | Shared | Foundation + tokens | Universal (app shell/navigation) | `19` §106 Command Palette; `19` §94 keyboard-operable menus/tabs | — |
| Project Switcher | Shared | Foundation + tokens | App shell (workspace switching) | — | No `19` counterpart yet — flagged for Design System backlog (pre-existing, §6 below) |
| Dialog | Shared | Foundation + tokens | Cross-cutting (confirmation flows, Review Interface's Approval Dialog instance) | `19` §40 Dialog Rules; `19` §130 Interaction Testing (Open→Focus→Interact→Submit→Feedback→Close→Focus Return) | Same component as "Modal" in `17` §66 — canonical name Dialog (§6 below) |
| Drawer | Shared | Foundation + tokens | Cross-cutting (e.g. Evidence side panel → drawer per `19` §30) | `19` §41 Drawer Rules; `19` §130 Interaction Testing | — |
| Popover, Context Menu | Shared | Foundation + tokens | Cross-cutting | `19` §105 Popover Rules | — |
| Status indicator (Draft/AI Proposed/Validated/Under Review/Human Approved/Rejected/Superseded/Archived) | Shared | Foundation + tokens | Instantiated by Topic Status Board (`topics`), Decision Status Badge (`decisions`), Mapping Status Badge (`page-candidates`) | `22` §19 Epistemic-State Testing adjacent (workflow, not epistemic) | Generic shell; per-workflow status *values* are Feature-tier data |
| Epistemic State Component (Observed/Inferred/Estimated/Recommended/Human Approved/Conflicted/Unknown) | Shared | Foundation + tokens | Cross-cutting wherever AI-derived confidence is shown | `22` §19 Epistemic-State Testing; `22` §20 Confidence Testing | Not interchangeable with Status indicator above (`19` §45 explicit) |
| Confidence Component | Shared | Foundation + tokens | Cross-cutting AI surfaces | `22` §20 Confidence Testing | — |
| Evidence Component | Shared | Foundation + tokens | Cross-cutting; also named Evidence Viewer in `17` §36 | `22` §18 Evidence Validation Testing | Same component, three names across three docs — canonical name Evidence Component |
| Recommendation Component | Shared | Foundation + tokens | Instantiated by Topic Validation Decision-Factors Panel (`topics`) and others | `22` §44/§45 Decision Engine / Sensitivity Testing (adjacent, backend-facing) | — |
| Decision Component | Shared | Foundation + tokens | Instantiated by Decision Record Card (`decisions`) | `22` §44 Decision Engine Testing (adjacent) | — |
| AI Insight, Rationale Summary | Shared | Foundation + tokens | Cross-cutting AI surfaces | `22` §21 AI Testing Philosophy (adjacent) | No `19` counterpart yet — flagged for Design System backlog |
| Progress Stepper, Workflow Status, Review Queue, Approval Dialog | Shared | Foundation + tokens | Instantiated by Workflow Monitor (`workflows`), Review Queue List (`reviews`) | `22` §28–30 Workflow/State/Recovery Testing (adjacent) | Domain-agnostic HITL shells (`15`); populated instances are FEATURE-tier |
| Toast, Error State, Loading State | Shared | Foundation + tokens | Universal | `22` §75 Error Contract Testing (adjacent) | — |

### 5.3 FEATURE Tier Registry

Owner for every row = the specific `features/<module>` named in the first column (per `18` §12 — "each major domain should have a clear owner... owns \[X\] presentation logic" — and `18` §10 Feature Module Boundaries: not consumed by other features). Dependencies for every row = Foundation (transitively) + whichever Shared shell is named in its §4 Notes cell, if any, + its module's own Domain-layer type (`18` §9.4). Rows below list only what varies.

| Feature Module | Component | Testing (beyond tier default) | Notes |
|---|---|---|---|
| `features/dashboard` | Project Status Panel, Strategic Opportunities List, Decision Queue Widget, Research Health Panel | `22` §48 Integration tier (aggregates data from many features) | Ownership assigned to `features/dashboard` by explicit human decision (Q11, 2026-09-06) — see `OWNERSHIP.md` § "Per-Component Ownership" and § 6 Observation #2 below. No longer contested. |
| `business-research` | Business Profile Editor | `22` §76 accessible-forms (multi-field editor) | — |
| `business-research` | Business-Importance-vs-Search-Demand Comparison view | `22` §78 Visualization Testing | — |
| `entities` | Entity List | — | — |
| `entities` | Entity Detail Panel | `22` §18 Evidence Validation Testing (Evidence/Confidence tabs) | Instantiates Evidence Component, Confidence Component |
| `entities` | Entity Card | — | — |
| `entities` | Entity Graph | `19` §109 Graph Accessibility; `22` §78 Visualization Testing | Must ship with a Relationship Table alternative per `19` §109 |
| `eav` | EAV Table | `19` §108 Table keyboard nav | — |
| `topics` | Topic Card / Row | — | — |
| `topics` | Topic Status Board | `22` §29 Workflow State Testing | Instance of Shared Status indicator |
| `topics` | Topic Source Indicator | — | — |
| `topics` | Topic Validation Decision-Factors Panel | `22` §44/§45 (adjacent) | Instance of Shared Recommendation/Decision shells |
| `intent` | Intent Distribution component | `22` §78 Visualization Testing | — |
| `serp` | Query List | — | — |
| `serp` | SERP Snapshot Viewer | `22` §34 SERP Testing (adjacent) | — |
| `serp` | SERP Comparison view | `22` §36 SERP Similarity Testing (adjacent) | — |
| `clustering` | Cluster List view | — | — |
| `clustering` | Topic Graph (cluster graph view) | `19` §109; `22` §78 | Distinct from Topical Map / Architecture Tree (§6 Observation #3) |
| `clustering` | Similarity Matrix (cluster matrix view) | `22` §78 Visualization Testing | — |
| `clustering` | Cluster Hierarchical Tree view | `19` §109; `22` §78 | — |
| `topical-map` | Topical Map Visualization | `19` §109; `22` §78 | Must not be confused with Page Architecture (`17` §24) |
| `page-candidates` | Page Candidate Card | — | — |
| `page-candidates` | Mapping Status Badge | `22` §40 Page Mapping Testing (adjacent) | Instance of Shared Status indicator |
| `page-architecture` | Architecture Tree | `19` §109; `22` §78 | — |
| `internal-linking` | Linking Graph | `19` §109; `22` §43 Internal Linking Testing (adjacent); `22` §78 | — |
| `internal-linking` | Link Recommendation Row | `22` §43 (adjacent) | — |
| `content-gaps` | Content Gap Card | `22` §42 Content Gap Testing (adjacent) | — |
| `cannibalization` | Cannibalization Report Card | `22` §41 Cannibalization Testing (adjacent) | — |
| `competitors` | Competitor Comparison view | `22` §78 Visualization Testing | — |
| `competitors` | Competitor Level Badge | — | — |
| `decisions` | Decision Record Card | `22` §44 Decision Engine Testing (adjacent) | Instance of Shared Decision Component |
| `decisions` | Decision Status Badge | — | Instance of Shared Status indicator |
| `reviews` | Review Queue List | `22` §46 HITL Testing (adjacent) | Instance of Shared Review Queue shell |
| `reviews` | Review Interface | `22` §46, §47 Human Approval Integrity; `19` §130 Interaction Testing (action bar: Approve/Reject/Modify/Defer/Request More Evidence/Add Note) | Three-pane layout — Responsive default (three-column → two-column → stacked, `19` §30) is the literal example given for this component type |
| `reviews` | Decision Recording Log | `22` §47 Human Approval Integrity (adjacent) | — |
| `workflows` | Workflow Monitor | `22` §28–31 Workflow/State/Recovery/Dependency Testing | Instance of Shared Workflow Status shell |
| `workflows` | Workflow Step Indicator | `22` §32 Parallel Execution Testing (adjacent) | — |

### 5.4 Acceptance Criteria Check

- **`BOOTSTRAP-002.4`** ("every component has all schema fields filled"): met via §5.0's cited tier defaults + §§5.1–5.3's per-component deltas — no cell is blank or unsourced.
- **`BOOTSTRAP-002.5`** ("every component has exactly one owner"): met for every row. The Dashboard group was initially left flagged (not a `features/*` module in `18` §8's conceptual list) rather than silently assigned; the human then explicitly resolved it by approving a new `features/dashboard` module (Q11, `PROJECT_STATE.md` § 10, 2026-09-06) — see `OWNERSHIP.md` § "Per-Component Ownership". No open exceptions remain.
- **`BOOTSTRAP-002.6`** ("every component has ≥1 test requirement"): met — every row carries at least the tier-level testing default from §5.0, and rows needing more carry a specific addition in the "Testing (beyond tier default)" column.

## 6. Observations Carried Forward (non-blocking — recorded for the next session, not escalated as Q-style blockers)

These surfaced during derivation but are not material architectural conflicts requiring human resolution before proceeding (per `03_MASTER_RULES.md` Non-Negotiables, only *material* conflicts must be escalated):

1. **"Dialog" vs "Modal."** `19` §39 and `18` §9.5 name this component "Dialog"; `17` §66 (System category) names the same concept "Modal." This matrix adopts **Dialog** as canonical. Low-severity naming inconsistency, analogous in kind (though smaller in scope) to the "Page Map" cleanup done under Q3 — worth a documentation pass under `DOCS-MAINT-001` or a future terminology cleanup task, not blocking.
2. **Dashboard had no `features/` module — resolved 2026-09-06 by explicit human decision (Q11).** `18` §8's project structure originally listed `app/[locale]/dashboard/` only as a route, not a `features/*` module, even though its components (§ 4 above) are workspace-specific in content. `BOOTSTRAP-002.5` (per-component ownership) resolved a definite owner for every other component deterministically from the tier-level rules in `OWNERSHIP.md`, but deliberately did **not** guess an owner for Dashboard, since doing so would be exactly the kind of silent resolution of a contested assignment `03_MASTER_RULES.md`'s Non-Negotiables and `WBS.md` §3's "Human Approval Required: Yes, if ownership is contested" both call out. The human has since explicitly approved creating a dedicated `features/dashboard` module as Dashboard's owner (see Q11, `PROJECT_STATE.md` § 10) — this is a decision only; the module itself has not been scaffolded, per that same instruction. `18` §8 itself caveats its module list as "a conceptual baseline... [that] must be validated against implementation complexity before coding," so adding `features/dashboard` does not contradict that document. No change to `18` or any other core document was needed or made. This observation is now closed; kept here for traceability rather than deleted.
3. **Topical Map / Topic Graph / Architecture Tree.** Three visually similar tree/graph structures exist at different pipeline stages (topic strategy → topic clustering → page structure). `17` §24 already explicitly warns against confusing Topical Map with Page Architecture; this matrix keeps all three as distinct FEATURE-tier components (§ 4) and repeats the warning here so it isn't lost when the matrix is read in isolation from `17`.
