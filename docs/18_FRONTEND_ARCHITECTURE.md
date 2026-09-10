# 18 — Frontend Architecture

**Document:** `18_FRONTEND_ARCHITECTURE.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Frontend Architecture Specification
**Status:** `APPROVED_AS_BASELINE_FRONTEND_ARCHITECTURE`
**Authority:** Baseline specification for frontend structure, application composition, feature boundaries, state management, data access, rendering, visualization architecture, AI interaction, frontend security boundaries, testing, performance, localization, and frontend evolution.

---

# 1. Purpose

This document defines the technical architecture of the frontend application.

The frontend is responsible for:

* presenting the SEO knowledge model;
* enabling research workflows;
* visualizing search intelligence;
* presenting AI analysis and recommendations;
* supporting human review and decision-making;
* monitoring workflows;
* interacting with backend APIs;
* maintaining responsive and accessible interfaces;
* preserving domain and output-contract semantics.

The frontend is **not** responsible for:

* authoritative business rules;
* authorization enforcement;
* AI reasoning;
* canonical data validation;
* direct database access;
* provider-specific SEO logic;
* security-critical decisions.

The backend remains the source of truth for canonical state.

---

# 2. Architectural Objective

The frontend must support a complex analytical application without becoming a collection of tightly coupled pages and UI components.

The architecture should provide:

* clear domain boundaries;
* reusable UI primitives;
* predictable state management;
* typed API contracts;
* isolated feature modules;
* testability;
* scalable visualization;
* contextual AI interaction;
* localization;
* accessibility;
* controlled data fetching;
* explicit loading/error/partial states;
* compatibility with the backend output contracts.

---

# 3. Core Architecture Principle

The frontend follows:

```text
Pages / Routes
        ↓
Feature Modules
        ↓
Application / Use Cases
        ↓
Domain Models
        ↓
API / Data Access
        ↓
Backend
```

Shared UI flows horizontally across the system:

```text
Design System
     ↓
Shared Components
     ↓
Feature Components
     ↓
Pages
```

The architecture must prevent feature components from bypassing domain and API boundaries unnecessarily.

---

# 4. Frontend Architectural Model

The conceptual architecture is:

```text
┌──────────────────────────────────────────────┐
│                 Application                  │
│                                              │
│  Routes / Pages / Layouts                    │
│                 ↓                            │
│  Feature Modules                             │
│                 ↓                            │
│  Application Services / Use Cases            │
│                 ↓                            │
│  Domain Models / View Models                 │
│                 ↓                            │
│  API Client / Query Layer                    │
└──────────────────────┬───────────────────────┘
                       ↓
              Backend API / SSE
                       ↓
                 Backend System
```

Shared infrastructure:

```text
Design System
Localization
Auth Session
Error Handling
Observability
Analytics
Configuration
Feature Flags
```

---

# 5. Technology Direction

The baseline frontend technology should support:

* React-based application architecture;
* Next.js or an equivalent React framework;
* TypeScript;
* server/client rendering where appropriate;
* typed API communication;
* streaming AI responses;
* interactive visualization;
* internationalization;
* RTL/LTR;
* accessible component primitives.

The exact framework version must be selected and pinned during implementation.

Technology decisions must not be changed casually.

---

# 6. Recommended Frontend Stack

Baseline direction:

```text
Framework:
Next.js

Language:
TypeScript

UI:
React

Styling:
CSS architecture compatible with Design System

Components:
Reusable design-system components

Forms:
Typed schema-driven form system

Data Fetching:
Server/client query abstraction

State:
Server state + local UI state + explicit application state

Validation:
Shared contract/schema validation

Visualization:
Dedicated visualization layer

Testing:
Unit + component + integration + E2E
```

Specific libraries should be selected only after validating:

* maintenance;
* compatibility;
* accessibility;
* bundle impact;
* license;
* security;
* project requirements.

---

# 7. Frontend Directory Philosophy

The project structure should be organized primarily around product capabilities rather than technical artifact type.

Avoid:

```text
components/
  Button/
  Table/
  Topic/
  Entity/
  Page/
```

as the entire application architecture.

Prefer:

```text
features/
  topics/
  entities/
  serp/
  decisions/
  workflows/
  pages/
```

with shared components separated from domain-specific components.

---

# 8. Proposed Project Structure

A conceptual structure:

```text
src/
├── app/
│   ├── [locale]/
│   │   ├── dashboard/
│   │   ├── research/
│   │   ├── knowledge/
│   │   ├── search/
│   │   ├── topics/
│   │   ├── pages/
│   │   ├── opportunities/
│   │   ├── decisions/
│   │   └── workflows/
│   │
│   └── api/
│
├── features/
│   ├── business-research/
│   ├── entities/
│   ├── eav/
│   ├── topics/
│   ├── intent/
│   ├── serp/
│   ├── clustering/
│   ├── topical-map/
│   ├── page-candidates/
│   ├── page-architecture/
│   ├── internal-linking/
│   ├── content-gaps/
│   ├── cannibalization/
│   ├── competitors/
│   ├── decisions/
│   ├── reviews/
│   └── workflows/
│
├── components/
│   ├── ui/
│   ├── layout/
│   ├── data-display/
│   ├── feedback/
│   └── visualization/
│
├── domain/
│   ├── entities/
│   ├── topics/
│   ├── search/
│   ├── pages/
│   ├── decisions/
│   └── workflows/
│
├── lib/
│   ├── api/
│   ├── auth/
│   ├── i18n/
│   ├── validation/
│   ├── telemetry/
│   └── utilities/
│
├── hooks/
├── providers/
├── config/
└── types/
```

This is a conceptual baseline.

The final directory structure must be validated against implementation complexity before coding.

---

# 9. Layer Responsibilities

## 9.1 Route Layer

Responsible for:

* URL structure;
* route parameters;
* page composition;
* layouts;
* metadata;
* access boundaries;
* loading/error boundaries.

It should not contain large amounts of domain logic.

---

## 9.2 Feature Layer

Responsible for:

* feature-specific UI;
* feature workflows;
* feature state;
* feature-level API interactions;
* domain-specific presentation logic.

Examples:

```text
features/topics
features/entities
features/serp
features/decisions
```

---

## 9.3 Application Layer

Responsible for frontend-level use cases.

Examples:

```text
validateTopic()
approveRecommendation()
refreshSerp()
createPageCandidate()
requestMoreEvidence()
```

These functions coordinate UI behavior and API calls.

They must not become a second backend business-logic layer.

---

## 9.4 Domain Layer

Responsible for frontend representations of domain concepts.

Examples:

```text
Entity
Topic
Query
Intent
SERPSnapshot
PageCandidate
Decision
Evidence
Workflow
```

Domain types should reflect canonical backend contracts.

---

## 9.5 Shared UI Layer

Responsible for reusable visual primitives.

Examples:

* Button
* Input
* Select
* Dialog
* Drawer
* Table
* Badge
* Tabs
* Tooltip
* EmptyState
* ErrorState
* LoadingState

Shared components must remain domain-agnostic whenever possible.

**Relationship to the operational component taxonomy:** the five layers above (§ 9.1–9.5) describe *code-organization* responsibility, not build sequencing. The project separately maintains an operational FOUNDATION / SHARED / FEATURE taxonomy in `.ai/COMPONENT_MATRIX.md` for build-order and ownership purposes. These are different classification dimensions, not competing ones: the Shared UI Layer (§ 9.5), together with cross-cutting Domain Layer types (§ 9.4), maps to operational SHARED; the Feature Layer (§ 9.2) maps to operational FEATURE; operational FOUNDATION corresponds to the design tokens and primitives (`19_DESIGN_SYSTEM.md` § 32–33) that all layers here consume rather than to a layer of its own. See `.ai/COMPONENT_MATRIX.md` for the authoritative mapping.

---

# 10. Feature Module Boundaries

Each feature should have an explicit boundary.

Example:

```text
features/topics/
├── components/
├── hooks/
├── api/
├── state/
├── schemas/
├── types/
├── utils/
└── index.ts
```

Feature modules should expose only intentional public APIs.

Internal implementation details should not be imported freely by unrelated modules.

---

# 11. Dependency Direction

Preferred dependency direction:

```text
Routes
  ↓
Features
  ↓
Application
  ↓
Domain
  ↓
Infrastructure Adapters
```

Shared UI may be consumed by all appropriate presentation layers.

Avoid:

```text
Topic Feature
   ↔
SERP Feature
   ↔
Page Feature
```

with arbitrary circular imports.

Cross-feature interaction should occur through:

* shared domain contracts;
* application services;
* explicit APIs;
* orchestrated state;
* URL state where appropriate.

---

# 12. Domain Ownership

Each major domain should have a clear owner.

Example:

```text
topics/
    owns topic presentation logic

entities/
    owns entity presentation logic

serp/
    owns SERP presentation logic

decisions/
    owns decision presentation logic
```

A feature should not mutate another feature's internal state directly.

---

# 13. State Management Model

The frontend should distinguish:

### Server State

Data originating from backend systems.

Examples:

* topics;
* entities;
* SERPs;
* decisions;
* workflows.

### UI State

Temporary interface state.

Examples:

* modal open;
* selected row;
* active tab;
* panel width.

### URL State

State that should be shareable/bookmarkable.

Examples:

* filters;
* selected topic;
* current view;
* pagination;
* search query.

### Session State

Examples:

* authentication;
* active workspace;
* active project;
* user preferences.

### Application State

Only for genuinely cross-feature state that cannot be derived from server, URL, or local UI state.

---

# 14. Server State Principle

Server data should not be duplicated unnecessarily into global client state.

Preferred model:

```text
Backend
   ↓
Query/Data Layer
   ↓
Feature
   ↓
UI
```

Avoid:

```text
Backend
 ↓
Query
 ↓
Global Store
 ↓
Local Store
 ↓
Component State
```

unless there is a demonstrated requirement.

---

# 15. Cache Strategy

Caching should be explicit.

Potential categories:

### Highly dynamic

* workflow state;
* review queue;
* live AI stream;
* current SERP job status.

### Moderately dynamic

* topics;
* entities;
* decisions.

### Relatively stable

* project configuration;
* taxonomy;
* static metadata.

Cache invalidation must follow backend state transitions.

The frontend must not assume that a cached recommendation is still current indefinitely.

---

# 16. Optimistic Updates

Optimistic updates may be used for low-risk reversible UI interactions.

They should not be used casually for consequential actions.

For example:

```text
Changing a local filter
→ optimistic

Approving a strategic SEO recommendation
→ server confirmation required
```

The UI must not show a human approval as completed until the backend confirms it.

---

# 17. API Client Architecture

All backend communication should pass through a centralized API abstraction.

Avoid scattered direct `fetch()` calls throughout components.

Preferred:

```text
Feature
   ↓
Feature API Function
   ↓
Shared API Client
   ↓
Backend
```

The API layer should handle:

* base URL;
* authentication;
* headers;
* serialization;
* errors;
* retries where appropriate;
* request IDs;
* timeouts;
* response validation.

---

# 18. Typed API Contracts

API responses must be strongly typed.

The frontend should consume contracts derived from:

`16_OUTPUT_CONTRACTS.md`

Where possible, API schemas should be generated or shared from a canonical schema source rather than manually recreated.

Manual duplication creates drift.

---

# 19. Runtime Validation

TypeScript types alone are insufficient for untrusted runtime data.

External API responses should be validated at runtime where appropriate.

Pipeline:

```text
HTTP Response
     ↓
Runtime Schema Validation
     ↓
Typed Domain Data
     ↓
Feature
     ↓
UI
```

Invalid responses should produce explicit errors rather than silently coercing malformed data.

---

# 20. API Error Model

The frontend should normalize backend errors into a predictable structure.

Conceptually:

```text
ApiError
├── code
├── message
├── category
├── retryable
├── requestId
├── fieldErrors
└── details
```

The UI should use error categories to determine presentation.

---

# 21. Error Boundaries

Error handling should exist at multiple levels:

```text
Application Error Boundary
        ↓
Route Error Boundary
        ↓
Feature Error Boundary
        ↓
Component-Level Error State
```

A failure in a visualization should not necessarily crash the entire application.

---

# 22. Loading Architecture

Loading behavior should be intentional.

Use:

* route-level loading;
* feature-level loading;
* skeletons;
* progressive rendering;
* streaming;
* background refresh.

Avoid replacing the entire application with a generic loading spinner when only one panel is updating.

---

# 23. Partial Data

The frontend must understand partial output states.

Example:

```text
SERP Analysis

38 / 50 queries complete

Status: PARTIAL
```

Partial data should carry enough metadata to explain what is missing.

---

# 24. AI Streaming

AI text generation may use streaming mechanisms such as SSE.

Conceptual architecture:

```text
AI Request
    ↓
API
    ↓
SSE Stream
    ↓
Stream Adapter
    ↓
AI UI State
    ↓
Rendered Output
```

Streaming infrastructure should be separated from ordinary REST query logic.

---

# 25. AI Artifact Boundary

Generated text and canonical artifacts are different.

Example:

```text
AI streamed recommendation
        ↓
Validation
        ↓
Structured artifact
        ↓
Persisted state
```

The frontend must not assume that streamed text is automatically persisted.

---

# 26. AI Assistant Context

The AI Assistant should receive contextual identifiers rather than arbitrary duplicated page content.

Context may include:

```text
workspaceId
projectId
route
selectedEntityIds
selectedTopicIds
selectedPageIds
workflowId
decisionId
```

The backend remains responsible for authoritative context retrieval.

The frontend should not construct hidden "truth" from local state.

---

# 27. AI Assistant UI State

The assistant should distinguish:

```text
Idle
Thinking / Processing
Streaming
Completed
Requires Review
Failed
Cancelled
```

The interface should support:

* cancel;
* retry;
* inspect evidence;
* create artifact;
* ask follow-up.

---

# 28. Human Review Architecture

Review UI should consume structured decision contracts.

Conceptually:

```text
Decision API
   ↓
Decision View Model
   ↓
Review Panel
   ├── Recommendation
   ├── Factors
   ├── Evidence
   ├── Confidence
   ├── Conflicts
   └── Actions
```

Approval actions must use dedicated API mutations.

---

# 29. Decision Mutation Flow

Example:

```text
User clicks Approve
        ↓
Confirmation if required
        ↓
POST decision approval
        ↓
Backend authorization
        ↓
Backend state transition
        ↓
Audit event
        ↓
API response
        ↓
Cache invalidation
        ↓
UI update
```

The frontend must never directly mutate decision status locally as authoritative state.

---

# 30. Workflow Architecture

Workflow screens should consume workflow state from the backend.

Possible implementation:

```text
Workflow Query
      ↓
Workflow View
      ↓
Step Components
      ↓
Evidence / Output Panels
```

For long-running workflows:

* polling;
* SSE;
* WebSocket;

may be used depending on requirements.

The transport must remain abstracted from feature components.

---

# 31. Visualization Architecture

Visualization should be treated as a specialized subsystem.

Recommended structure:

```text
Visualization Data
       ↓
View Model
       ↓
Visualization Adapter
       ↓
Graph / Chart Library
       ↓
Interaction Events
       ↓
Domain Selection
```

Visualization libraries must not become the source of domain truth.

---

# 32. Entity Graph Architecture

The entity graph should consume normalized relationship data.

Example:

```text
Entity[]
Relationship[]
    ↓
Graph View Model
    ↓
Graph Renderer
```

Graph interactions should return stable entity IDs.

Do not use visual node indices as domain identifiers.

---

# 33. Topic Graph Architecture

The same principle applies to topic graphs.

```text
Topics
Relationships
Clusters
Evidence
    ↓
Topic Graph View Model
    ↓
Renderer
```

The graph should support filtering without mutating canonical topic relationships.

---

# 34. Page Architecture Visualization

Page architecture should use a hierarchical tree representation.

```text
PageNode
├── id
├── parentId
├── label
├── status
├── topicIds
└── children
```

Drag-and-drop operations should create explicit proposed changes.

The backend must validate and persist approved changes.

---

# 35. Internal Linking Visualization

Internal linking may use:

* directed graphs;
* page relationship tables;
* link opportunity lists.

The visualization should remain usable with large page sets.

Progressive expansion should be preferred over rendering thousands of nodes simultaneously.

---

# 36. Large Dataset Strategy

The application must assume professional SEO datasets may become large.

Use:

* pagination;
* virtualization;
* server-side filtering;
* server-side sorting;
* incremental graph loading;
* debounced search;
* selective rendering.

Do not fetch the entire project into the browser by default.

---

# 37. URL and Routing Architecture

Routes should reflect conceptual product structure.

Example:

```text
/[locale]/dashboard

/[locale]/projects/[projectId]/research

/[locale]/projects/[projectId]/entities

/[locale]/projects/[projectId]/topics

/[locale]/projects/[projectId]/search

/[locale]/projects/[projectId]/pages

/[locale]/projects/[projectId]/decisions

/[locale]/projects/[projectId]/workflows
```

Exact route naming should be finalized during implementation.

---

# 38. URL State

Filters and views should be encoded into URLs when useful.

Example:

```text
/topics?
status=validated
intent=commercial
cluster=cluster_123
```

This allows:

* bookmarking;
* sharing;
* browser navigation;
* reproducibility.

Sensitive data must never be encoded into URLs.

---

# 39. Authentication Architecture

Authentication state should be centralized.

The frontend should know:

* whether the user is authenticated;
* current user;
* current workspace/project;
* session status.

It should not independently implement authentication rules.

The backend remains authoritative.

---

# 40. Authorization Architecture

Frontend authorization is for UX.

For example:

```text
User cannot approve
→ hide or disable Approve button
```

But:

```text
Backend
→ independently verifies authorization
```

Never rely on:

```text
if (isAdmin) {
    allowAction()
}
```

as a security boundary.

---

# 41. Project Isolation

Every project-scoped request should carry sufficient project/workspace context.

The frontend must not assume that route-level isolation alone provides security.

Backend authorization must verify ownership/access.

---

# 42. Security Requirements

The frontend must:

* avoid storing sensitive secrets;
* avoid exposing provider API keys;
* avoid placing credentials in client bundles;
* sanitize untrusted rendered content;
* protect against XSS;
* handle CSRF according to authentication architecture;
* avoid leaking private project information;
* avoid logging sensitive data;
* avoid exposing internal prompts or system configuration.

---

# 43. AI Prompt Security

User-generated content may contain prompt injection attempts.

The frontend should treat imported text, website content, SERP snippets, and external data as untrusted content.

It must not:

* execute instructions found in external content;
* treat external text as system instructions;
* expose privileged actions merely because content requests them.

Primary prompt-injection defense belongs to the backend AI architecture.

---

# 44. Rendering Untrusted Content

Content such as:

* page titles;
* snippets;
* crawled text;
* competitor content;
* AI-generated Markdown;

must be handled safely.

HTML rendering should be sanitized through an approved mechanism.

Do not use unrestricted raw HTML rendering.

---

# 45. Forms

Forms should be:

* schema-driven;
* typed;
* accessible;
* validated;
* explicit about required fields;
* resilient to server validation errors.

Validation should exist at:

```text
UI validation
      +
Server validation
```

Frontend validation improves UX.

Backend validation protects correctness.

---

# 46. Forms and AI Suggestions

AI-generated form values must be treated as proposals.

Example:

```text
AI suggested topic name
[Use suggestion]
[Edit]
```

Do not silently populate consequential fields and submit them automatically.

---

# 47. Design System Integration

The frontend must consume `19_DESIGN_SYSTEM.md`.

Components should not independently invent:

* spacing;
* colors;
* typography;
* radius;
* shadows;
* status styles.

The Design System is the visual source of truth.

---

# 48. Shared Component Architecture

Shared components should be divided into:

### Primitive

* Button
* Input
* Text
* Icon

### Composite

* SearchBar
* FilterBar
* DataTable
* EvidencePanel

### Domain-Aware

* TopicStatus
* ConfidenceIndicator
* DecisionCard
* WorkflowStepper

Domain-aware components should live in feature/domain areas rather than pretending to be universal primitives.

---

# 49. Accessibility Architecture

Accessibility must be embedded into component design.

Requirements include:

* semantic markup;
* keyboard support;
* focus management;
* accessible dialogs;
* accessible tables;
* screen-reader labels;
* reduced motion;
* accessible charts;
* non-color status indicators.

Accessibility should be tested at component and feature level.

---

# 50. Internationalization Architecture

All user-facing strings must be localized.

Avoid:

```typescript
<h1>Topic Validation</h1>
```

Prefer translation keys.

Conceptually:

```text
topics.validation.title
```

Localization must cover:

* navigation;
* forms;
* errors;
* status labels;
* AI UI;
* dates;
* numbers;
* units;
* empty states.

---

# 51. RTL/LTR Architecture

The application must support direction dynamically.

The direction should be derived from active locale.

Components must avoid hard-coded assumptions such as:

```css
left: 0;
right: 0;
```

when logical properties can be used.

Prefer logical CSS properties where appropriate.

---

# 52. Theme Architecture

Theme state should be centralized.

Potential themes:

* light;
* dark;
* system.

Components should consume semantic design tokens rather than hard-coded colors.

---

# 53. State Synchronization

The frontend may need to synchronize:

* workflow state;
* review state;
* decision state;
* notifications.

Use explicit synchronization strategies.

Potential methods:

* query invalidation;
* polling;
* SSE;
* WebSocket;
* event-driven refresh.

Do not create uncontrolled background polling across every page.

---

# 54. Real-Time Architecture

Real-time communication should be introduced where it provides clear value.

Good candidates:

* AI streaming;
* long-running workflow progress;
* live review queue;
* workflow completion.

Not every CRUD operation requires real-time transport.

---

# 55. Notifications Architecture

Notifications should have:

```text
Notification
├── id
├── type
├── severity
├── message
├── createdAt
├── readAt
└── target
```

The frontend should render notifications based on structured data.

---

# 56. Analytics and Telemetry

Frontend telemetry should capture meaningful product events.

Examples:

* research started;
* topic validated;
* recommendation reviewed;
* workflow completed;
* feature used.

Avoid logging:

* sensitive project content;
* credentials;
* private AI prompts;
* confidential data.

Analytics events should have stable names and documented schemas.

---

# 57. Observability

Frontend errors should provide enough context for debugging.

Potential metadata:

* route;
* feature;
* project identifier where safe;
* request ID;
* correlation ID;
* application version;
* locale.

Do not include sensitive user content by default.

---

# 58. Performance Architecture

Performance priorities:

1. fast initial navigation;
2. responsive interaction;
3. efficient data fetching;
4. efficient rendering;
5. controlled JavaScript payload;
6. scalable visualizations.

Potential techniques:

* server rendering;
* code splitting;
* lazy loading;
* dynamic imports;
* virtualization;
* memoization where justified;
* caching;
* image optimization;
* incremental data loading.

Optimization should be evidence-driven.

---

# 59. Bundle Management

Large visualization and AI-related libraries should not necessarily load on every route.

Use route/feature-level code splitting where appropriate.

Example:

```text
Dashboard
→ no graph engine required

Entity Graph
→ graph engine loaded

Topic Matrix
→ matrix visualization module loaded
```

---

# 60. Frontend Configuration

Configuration should distinguish:

### Public configuration

Safe for browser exposure.

Examples:

* public API base URL;
* feature flags intended for clients;
* locale configuration.

### Private configuration

Server-only.

Examples:

* API secrets;
* provider keys;
* signing secrets.

Private values must never enter client bundles.

---

# 61. Feature Flags

Feature flags may control:

* experimental visualizations;
* new workflows;
* beta AI capabilities;
* progressive rollout.

Flags must not be used as a substitute for authorization.

---

# 62. Offline Behavior

The primary product is online-first.

Offline editing of canonical SEO decisions is not an MVP requirement.

The frontend may preserve temporary drafts locally where useful, but offline state must not be mistaken for canonical server state.

---

# 63. Data Freshness

The frontend should communicate freshness metadata.

For example:

```text
Last updated:
4 minutes ago
```

or:

```text
Data may be stale.
Last SERP observation:
21 days ago
```

Freshness decisions belong to backend/data specifications.

---

# 64. Frontend Caching and Staleness

The frontend should support:

```text
Fresh
Stale
Refreshing
Failed Refresh
Unavailable
```

The user should be able to trigger refresh where permitted.

---

# 65. Search and Filtering Architecture

Filtering should be implemented close to the data source.

For large datasets:

```text
User Filter
    ↓
API Query
    ↓
Server Filtering
    ↓
Reduced Dataset
    ↓
UI
```

Local filtering is acceptable for small already-loaded datasets.

---

# 66. Table Architecture

Data tables should support:

* typed columns;
* server-side sorting;
* server-side filtering;
* pagination;
* row selection;
* bulk actions;
* column visibility;
* responsive behavior.

Table components should remain reusable while allowing feature-specific columns.

---

# 67. Selection Model

Selections should use stable IDs.

Example:

```text
selectedTopicIds: string[]
```

not:

```text
selectedRows: number[]
```

Visual order may change.

Domain IDs must not.

---

# 68. Modal and Drawer Architecture

Use:

### Modal

For:

* confirmation;
* focused decisions;
* short forms.

### Drawer

For:

* evidence;
* object details;
* contextual inspection.

### Full page

For:

* complex workflows;
* deep analysis;
* architecture design;
* large datasets.

---

# 69. Navigation Between Related Objects

Users should be able to move naturally between relationships.

Example:

```text
Topic
 ↓
Intent
 ↓
Query
 ↓
SERP
 ↓
Page
 ↓
Cannibalization
```

Navigation should preserve project context and allow return to the previous analysis state.

---

# 70. Breadcrumbs

Breadcrumbs should reflect conceptual hierarchy.

Example:

```text
Project
→ Topics
→ Cluster
→ Topic
```

Avoid technical URL-based breadcrumbs that expose implementation details.

---

# 71. Deep Linking

Important objects should have stable URLs.

Examples:

```text
/projects/{projectId}/topics/{topicId}

/projects/{projectId}/entities/{entityId}

/projects/{projectId}/decisions/{decisionId}
```

Deep links must respect authorization.

---

# 72. Frontend Domain Models

Frontend models should preserve conceptual distinctions.

Minimum models:

```text
Business
Workspace
Project
Entity
Attribute
EAVFact
Topic
Keyword
Query
Intent
SearchContext
SERPSnapshot
SERPResult
Cluster
PageCandidate
Page
Decision
Evidence
Recommendation
Workflow
WorkflowStep
HumanDecision
```

A frontend model must not merge these merely for convenience.

---

# 73. View Models

UI-specific transformations should use view models.

Example:

```text
Domain Topic
    ↓
TopicViewModel
    ↓
TopicTableRow
```

View models may combine information for presentation but must retain references to canonical IDs.

---

# 74. Avoiding Data Duplication

Do not create multiple independent versions of the same domain object in unrelated feature states.

Preferred:

```text
Canonical API Data
      ↓
Feature Query
      ↓
View Model
```

rather than:

```text
EntityStore
TopicStore
PageStore
DecisionStore
```

each containing duplicate copies of shared objects without synchronization.

---

# 75. Cross-Feature Data

When a feature needs data owned by another feature:

```text
Feature A
   ↓
Shared Domain Contract / API
   ↓
Feature B
```

Do not import private implementation state.

---

# 76. Frontend Workflow Composition

The frontend may visually compose workflows but must not become the workflow engine.

For example:

```text
Research UI
→ starts backend workflow

Workflow UI
→ monitors backend workflow

Review UI
→ handles human decision

Decision UI
→ displays resulting state
```

Workflow orchestration belongs to the backend.

---

# 77. Frontend Authorization UX

The frontend should provide appropriate UX based on permissions:

* hidden actions;
* disabled actions;
* read-only views;
* explanation of missing permission.

However, every mutation must be re-authorized by the backend.

---

# 78. Destructive Action UX

Destructive actions should require:

* explicit action;
* confirmation where appropriate;
* clear consequences;
* server confirmation;
* error recovery where possible.

Example:

```text
Archive 12 topics?

They will no longer appear in active topic views.

[Cancel]
[Archive]
```

---

# 79. Human Approval UX

Approval should be explicit.

Avoid:

```text
clicking next = approval
```

Prefer:

```text
Review
→ Inspect
→ Approve
```

The user must know when they are making a consequential decision.

---

# 80. Frontend Testing Architecture

Testing should exist at several layers.

### Unit

* utilities;
* transformations;
* validation helpers;
* view-model logic.

### Component

* states;
* interactions;
* accessibility.

### Feature

* topic validation;
* decision review;
* workflow monitoring.

### Integration

* API interactions;
* authentication;
* state synchronization.

### E2E

* complete user journeys.

---

# 81. Visual Regression

Visual regression should be considered for:

* design-system components;
* complex tables;
* graphs;
* responsive layouts;
* RTL/LTR;
* dark/light themes.

The goal is to detect unintended visual changes.

---

# 82. Accessibility Testing

Automated accessibility testing should be supplemented with manual keyboard and screen-reader testing for critical flows.

Critical flows include:

* authentication;
* topic validation;
* decision approval;
* workflow monitoring;
* navigation.

---

# 83. API Contract Testing

Frontend integration should validate that backend responses conform to expected contracts.

Important cases:

* valid output;
* partial output;
* validation error;
* conflict;
* unauthorized action;
* stale data;
* provider failure.

---

# 84. E2E Critical Paths

At minimum:

```text
Login
 ↓
Create/Open Project
 ↓
Research
 ↓
Discover Topics
 ↓
Validate Topics
 ↓
Inspect SERP
 ↓
Review Recommendation
 ↓
Approve/Reject
 ↓
Verify State
```

Additional paths should cover:

* failure;
* retry;
* partial results;
* localization;
* RTL.

---

# 85. Testing AI UX

AI interfaces should be tested for:

* streaming behavior;
* cancellation;
* malformed output;
* delayed output;
* empty output;
* partial output;
* tool failure;
* evidence display;
* confidence display;
* recommendation/decision distinction.

---

# 86. Testing State Transitions

Critical state transitions should be tested explicitly.

Example:

```text
AI_PROPOSED
   ↓
REQUIRES_REVIEW
   ↓
HUMAN_APPROVED
```

and:

```text
AI_PROPOSED
   ↓
REJECTED
```

The frontend should correctly reflect each backend-confirmed state.

---

# 87. Error Recovery Testing

Test:

* network timeout;
* authentication expiry;
* authorization failure;
* validation error;
* server error;
* provider error;
* malformed response;
* stream interruption.

The UI should recover without corrupting local state.

---

# 88. Development Workflow

Frontend implementation follows:

```text
Read Documentation
      ↓
Understand Authorized Task
      ↓
Inspect Existing Implementation
      ↓
Plan Minimal Change
      ↓
Implement
      ↓
Run Targeted Tests
      ↓
Run Regression Tests
      ↓
Verify UI
      ↓
Update Project State
```

No feature should be implemented merely because it appears useful.

---

# 89. Documentation-First Constraint

Before implementing a frontend feature, the developer/agent should inspect relevant documents.

At minimum:

* `03_MASTER_RULES.md`
* `04_SYSTEM_ARCHITECTURE.md`
* `16_OUTPUT_CONTRACTS.md`
* `17_UI_UX_SPECIFICATION.md`
* this document
* relevant domain specifications
* relevant testing/debugging documentation.

The final reading order must be derived by project orchestration rather than permanently hard-coded here.

---

# 90. No Silent Architecture Drift

Frontend implementation must not silently introduce:

* a second state architecture;
* a second API layer;
* a new design system;
* duplicated domain models;
* a new authentication mechanism;
* an incompatible routing strategy.

If implementation requires architectural change, it must be documented and authorized.

---

# 91. Dependency Management

New frontend dependencies must be evaluated for:

* necessity;
* security;
* maintenance;
* bundle size;
* accessibility;
* compatibility;
* licensing;
* duplication.

Do not install libraries merely because they simplify a small component.

Skills/tooling requirements are governed by:

`26_SKILLS_AND_TOOLING_POLICY.md`.

---

# 92. Provider Independence

Frontend code must not depend directly on:

* a specific LLM provider;
* a specific SERP provider;
* a specific SEO data provider.

For example, avoid:

```text
components/serp/
    directly importing ProviderX SDK
```

Prefer:

```text
Frontend
   ↓
Backend API Contract
   ↓
Provider Adapter
```

Provider abstraction belongs primarily to the backend.

---

# 93. Backend as Source of Truth

The frontend must never become the canonical store for:

* entities;
* topics;
* decisions;
* approvals;
* SERP observations;
* workflow state.

Local state is temporary unless explicitly defined otherwise.

---

# 94. Persistence Boundaries

The frontend may persist:

* UI preferences;
* temporary drafts;
* non-sensitive local state;
* cached data according to policy.

It should not persist sensitive credentials or canonical strategic decisions independently of the backend.

---

# 95. Browser Storage

Browser storage should be used carefully.

Avoid storing:

* access tokens unless explicitly required by the approved auth design;
* refresh tokens in unsafe client storage;
* provider secrets;
* sensitive project datasets unnecessarily.

Storage strategy must follow the security architecture.

---

# 96. Contextual AI and Frontend State

The frontend should provide identifiers and UI context.

The backend should resolve authoritative semantic context.

Example:

```text
Frontend:
selectedTopicId = topic_123

Backend:
loads topic_123
loads related entities
loads evidence
loads relevant decisions
loads project context
```

This reduces token waste and prevents the frontend from becoming a context-management engine.

---

# 97. Progressive Enhancement

The product should remain usable if advanced visualizations fail.

For example:

```text
Entity Graph unavailable
        ↓
Entity Relationship Table remains available
```

A graph should enhance analysis, not become the only way to access information.

---

# 98. Accessibility Alternative for Visualization

Every important visualization should have a structured alternative.

Example:

```text
Entity Graph
    ↓
Relationship Table
```

or:

```text
Topic Graph
    ↓
Hierarchical Topic List
```

This is required for accessibility and operational resilience.

---

# 99. Frontend Architecture Anti-Patterns

Prohibited patterns include:

### 99.1 God Components

One page/component containing:

* data fetching;
* business logic;
* visualization;
* mutations;
* formatting;
* authorization logic.

---

### 99.2 Global Store Everything

Putting every server response into a global store.

---

### 99.3 Direct API Calls Everywhere

Scattered raw requests inside UI components.

---

### 99.4 Domain Logic in JSX

Complex decision logic embedded directly inside rendering.

---

### 99.5 Backend Logic Reimplemented in Frontend

The frontend must not become a second decision engine.

---

### 99.6 Unbounded Client Fetching

Loading entire projects into browser memory.

---

### 99.7 Hidden State Mutation

Changing important state locally without server confirmation.

---

### 99.8 Design-System Bypass

Creating one-off visual styles instead of using shared tokens/components.

---

### 99.9 Visualization as Source of Truth

Graph state must not become canonical domain state.

---

### 99.10 AI Response as Canonical Data

Streaming output must not automatically become persisted state.

---

# 100. MVP Frontend Architecture

The MVP should remain a modular monolith.

Conceptually:

```text
Next.js / React Application
│
├── Application Shell
├── Authentication
├── Project Context
│
├── Research
├── Knowledge
├── Topics
├── Search Intelligence
├── Pages
├── Decisions
├── Reviews
└── Workflows
```

All feature modules share:

```text
Design System
API Client
Auth
Localization
Validation
Telemetry
Error Handling
```

---

# 101. MVP Rendering Strategy

Use a hybrid rendering strategy.

### Server rendering

For:

* route-level project information;
* stable metadata;
* initial page data where useful.

### Client rendering

For:

* interactive tables;
* filters;
* graphs;
* drag-and-drop;
* AI streaming;
* live workflow state.

The rendering strategy should be chosen based on actual feature requirements.

---

# 102. MVP Data Flow

```text
User Interaction
      ↓
Feature UI
      ↓
Application Action
      ↓
API Client
      ↓
Backend
      ↓
Validated Contract
      ↓
Query / State Update
      ↓
View Model
      ↓
UI
```

---

# 103. MVP Required Frontend Capabilities

The initial frontend must support:

* authentication;
* workspace/project selection;
* application shell;
* dashboard;
* business research;
* entity exploration;
* EAV;
* topic universe;
* topic validation;
* intent;
* SERP intelligence;
* clustering;
* page candidates;
* decision center;
* human review;
* evidence inspection;
* workflow monitoring;
* AI assistant;
* localization;
* RTL/LTR;
* accessible core components.

---

# 104. Future Frontend Evolution

Future architecture may introduce:

* micro-frontends only if justified;
* separate visualization packages;
* collaborative real-time editing;
* advanced offline capabilities;
* richer graph engine;
* plugin-driven feature modules;
* workspace customization;
* advanced analytics;
* strategy simulations.

None should be introduced merely because the product has many features.

---

# 105. Criteria for Frontend Extraction

A feature should become a separately deployed frontend package/application only when justified by measurable requirements such as:

* independent deployment needs;
* team ownership boundaries;
* significant build isolation;
* runtime isolation;
* independently scaled workloads.

Feature count alone is not sufficient.

---

# 106. Frontend Versioning

Frontend releases should be traceable to:

* application version;
* API compatibility;
* contract versions;
* design-system version;
* feature flags.

Breaking API changes must be coordinated with backend deployment strategy.

---

# 107. Backward Compatibility

The frontend should tolerate compatible API evolution.

For example:

```text
Backend adds optional field
→ existing frontend continues working
```

For breaking changes:

```text
Contract Version N
        ↓
Migration / compatibility layer
        ↓
Contract Version N+1
```

Do not silently reinterpret changed semantics.

---

# 108. Feature Deprecation

When removing a frontend feature:

1. identify consumers;
2. inspect API dependencies;
3. identify saved URLs;
4. communicate deprecation where needed;
5. migrate users;
6. remove feature;
7. remove dead dependencies;
8. update documentation.

---

# 109. Frontend Documentation

Each complex feature should document:

* purpose;
* owner;
* domain;
* API dependencies;
* state model;
* major components;
* important user flows;
* testing strategy;
* known limitations.

This prevents the frontend from becoming an undocumented implementation maze.

---

# 110. Frontend Debugging

When a frontend defect occurs, follow:

```text
Detect
  ↓
Reproduce
  ↓
Capture Evidence
  ↓
Classify
  ↓
Identify Root Cause
  ↓
Implement Minimal Fix
  ↓
Targeted Test
  ↓
Regression Test
  ↓
Verify
  ↓
Document
```

Never declare a frontend issue fixed merely because the error disappeared locally.

---

# 111. Frontend Failure Classification

Common categories:

```text
Rendering
State
API
Contract
Authentication
Authorization
Localization
Accessibility
Performance
Visualization
Concurrency
Streaming
Browser Compatibility
```

Correct classification should precede remediation.

---

# 112. Contract Failure Handling

If the frontend receives malformed contract data:

```text
Invalid Response
      ↓
Validation Failure
      ↓
Safe Error State
      ↓
Request ID / Diagnostics
```

Do not:

* silently repair arbitrary fields;
* invent defaults;
* display malformed data as trustworthy.

Bounded compatibility transformations may be used only when explicitly defined.

---

# 113. Race Conditions

The frontend must account for concurrent updates.

Example:

```text
User A approves decision
        ↓
User B viewing same decision
```

The frontend should refresh or reconcile state after server-confirmed changes.

Stale local state must not overwrite newer canonical state.

---

# 114. Concurrent Workflow Views

Multiple tabs/windows may display the same project.

The system should tolerate:

* stale tabs;
* duplicated requests;
* simultaneous review;
* workflow completion while viewing;
* permission changes.

Server state remains authoritative.

---

# 115. Security Monitoring

Frontend security monitoring should detect:

* runtime exceptions;
* suspicious client errors;
* failed authentication patterns where observable;
* dependency vulnerabilities;
* unexpected bundle changes.

Security-sensitive incidents must be handled according to project security procedures.

---

# 116. Frontend Build Quality

A production build must verify:

* TypeScript correctness;
* linting;
* tests;
* route generation;
* localization completeness;
* asset loading;
* environment configuration;
* bundle integrity.

Warnings should be reviewed rather than automatically ignored.

---

# 117. CI/CD Frontend Pipeline

Conceptual pipeline:

```text
Install
 ↓
Dependency Validation
 ↓
Type Check
 ↓
Lint
 ↓
Unit Tests
 ↓
Component Tests
 ↓
Build
 ↓
Contract Tests
 ↓
E2E
 ↓
Visual / Accessibility Checks
 ↓
Artifact
 ↓
Deploy
```

Exact pipeline belongs to deployment infrastructure and project controls.

---

# 118. Definition of Done

A frontend feature is complete when:

1. Its user goal is defined.
2. Its domain boundary is defined.
3. Its route is defined where required.
4. Its API contract is defined.
5. Its loading state exists.
6. Its empty state exists.
7. Its error state exists.
8. Its partial state exists where relevant.
9. Its stale/conflict state exists where relevant.
10. Its accessibility behavior is implemented.
11. Its localization behavior is implemented.
12. RTL/LTR behavior is verified.
13. Authorization UX is implemented.
14. Consequential actions require server confirmation.
15. Tests exist.
16. Relevant E2E coverage exists.
17. No architecture boundary is violated.
18. No duplicated source of truth is introduced.
19. Documentation is updated where necessary.
20. Project state is updated.

---

# 119. Final Frontend Architecture Model

The frontend should ultimately operate as:

```text
                       USER
                         │
                         ↓
                ┌────────────────┐
                │ Application UI │
                └───────┬────────┘
                        ↓
                ┌────────────────┐
                │ Feature Modules │
                └───────┬────────┘
                        ↓
              ┌─────────────────────┐
              │ Application Actions │
              └──────────┬──────────┘
                         ↓
              ┌─────────────────────┐
              │ Typed API / Streams │
              └──────────┬──────────┘
                         ↓
                 ┌──────────────┐
                 │ Backend APIs │
                 └──────┬───────┘
                        ↓
        ┌────────────────────────────────┐
        │ Domain + Decision + AI System  │
        └────────────────────────────────┘
```

With shared infrastructure:

```text
Design System
Localization
Authentication
Validation
Telemetry
Error Handling
Configuration
```

The frontend is therefore a **decision interface and application layer**, not the source of SEO intelligence or business truth.

---

# 120. Non-Negotiable Frontend Principles

1. **Backend state is canonical.**
2. **Frontend state is not authoritative.**
3. **Domain concepts must remain distinct.**
4. **API contracts must be typed and validated.**
5. **AI output must not bypass contract validation.**
6. **Human approvals require server confirmation.**
7. **Authorization must be enforced by the backend.**
8. **Feature boundaries must remain explicit.**
9. **Shared components must remain reusable and controlled.**
10. **Design System is the visual source of truth.**
11. **Large datasets require scalable rendering strategies.**
12. **Graphs are views, not sources of truth.**
13. **URL state should be used for shareable analytical state.**
14. **Loading, error, empty, partial, stale, and conflict states are first-class.**
15. **AI streaming is separate from canonical persistence.**
16. **Context identifiers should be passed to the backend rather than rebuilding semantic context in the browser.**
17. **Accessibility is mandatory.**
18. **RTL/LTR is a structural requirement.**
19. **Localization must be built into the architecture.**
20. **New dependencies require justification.**
21. **No silent architecture drift.**
22. **No frontend duplication of backend decision logic.**
23. **No sensitive secrets in client code or browser storage.**
24. **Visualization failure must not make underlying data inaccessible.**
25. **Every consequential UX action must have an explicit state transition.**
26. **Testing is part of implementation, not post-implementation cleanup.**
27. **Frontend complexity must remain proportional to measured product requirements.**
28. **The application must optimize for reliable SEO decision-making, not merely visual richness.**

---

# 121. Document Control

```yaml
document:
  id: "18"
  filename: "18_FRONTEND_ARCHITECTURE.md"
  status: "APPROVED_AS_BASELINE_FRONTEND_ARCHITECTURE"
  product: "SEO Research & Strategy Copilot / SEO Decision Engine"
  authority: "baseline_frontend_architecture"

architecture:
  pattern: "modular_frontend_application"
  primary_framework: "React_based_framework"
  recommended_framework: "Next.js"
  language: "TypeScript"
  rendering: "hybrid_server_and_client"
  deployment_model: "modular_application"
  frontend_is_source_of_truth: false
  backend_is_source_of_truth: true

layers:
  - routes
  - feature_modules
  - application_actions
  - domain_models
  - api_data_access
  - backend

core_features:
  - business_research
  - entities
  - eav
  - topics
  - intent
  - serp
  - clustering
  - topical_map
  - page_candidates
  - page_architecture
  - internal_linking
  - content_gaps
  - cannibalization
  - competitors
  - decisions
  - reviews
  - workflows

state_model:
  server_state: canonical_backend_data
  ui_state: local_interface_state
  url_state: shareable_navigation_and_filters
  session_state: authentication_and_project_context
  application_state: minimal_cross_feature_state

data:
  typed_api_contracts: true
  runtime_validation: true
  direct_database_access: false
  direct_provider_access: false
  canonical_state_in_browser: false

ai:
  streaming_supported: true
  streaming_equals_persistence: false
  contextual_assistant: true
  frontend_resolves_authoritative_semantic_context: false
  backend_resolves_authoritative_context: true

security:
  frontend_is_security_boundary: false
  backend_authorization_required: true
  secrets_in_client: false
  provider_keys_in_browser: false
  untrusted_content_sanitized: true

localization:
  multilingual: true
  rtl: true
  ltr: true
  initial_languages:
    - en
    - fa
    - de

accessibility:
  required: true
  keyboard_navigation: true
  screen_reader_support: true
  non_color_semantics: true
  reduced_motion: true
  visualization_alternatives: true

visualization:
  specialized_subsystem: true
  graph_is_source_of_truth: false
  progressive_loading: true
  large_dataset_support: true
  accessible_alternative_required: true

testing:
  unit: true
  component: true
  feature: true
  integration: true
  e2e: true
  accessibility: true
  visual_regression: true
  contract_testing: true
  regression: true

performance:
  virtualization: true
  pagination: true
  code_splitting: true
  lazy_loading: true
  server_side_filtering: true
  server_side_sorting: true
  evidence_driven_optimization: true

architecture_rules:
  direct_fetch_in_components: discouraged
  global_store_for_all_server_state: prohibited
  backend_logic_reimplementation: prohibited
  silent_state_mutation: prohibited
  design_system_bypass: prohibited
  uncontrolled_cross_feature_state_access: prohibited
  silent_architecture_drift: prohibited

mvp:
  architecture: "modular_monolith_frontend"
  priority: "research_and_decision_experience"
  advanced_visualizations: "incremental"
  mobile_priority: "secondary_to_desktop"

dependencies:
  primary:
    - "16_OUTPUT_CONTRACTS.md"
    - "17_UI_UX_SPECIFICATION.md"
    - "19_DESIGN_SYSTEM.md"
  domain:
    - "08_SEO_KNOWLEDGE_MODEL.md"
    - "09_ENTITY_EAV_MODEL.md"
    - "10_TOPIC_MODELING_AND_CLUSTERING.md"
    - "11_SEARCH_AND_SERP_INTELLIGENCE.md"
    - "12_SEO_DECISION_ENGINE.md"
  workflow:
    - "14_AGENT_WORKFLOW.md"
    - "15_HUMAN_IN_THE_LOOP.md"
  implementation:
    - "20_PROJECT_STRUCTURE.md"
    - "21_DEVELOPMENT_AND_DEBUG.md"
    - "22_TESTING_AND_VALIDATION.md"
    - "25_CONTEXT_MANAGEMENT.md"
    - "26_SKILLS_AND_TOOLING_POLICY.md"

primary_rule:
  statement: "The frontend presents and coordinates domain state through validated contracts; it does not become the source of truth or a second decision engine."

next_dependency:
  document: "19_DESIGN_SYSTEM.md"
```
