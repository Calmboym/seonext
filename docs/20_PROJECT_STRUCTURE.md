# 20 — Project Structure

**Document:** `20_PROJECT_STRUCTURE.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Repository, Module, Directory & Code Organization Specification
**Status:** `APPROVED_AS_BASELINE_PROJECT_STRUCTURE`
**Authority:** Baseline specification for repository structure, module boundaries, directory organization, dependency direction, naming conventions, ownership, test placement, documentation placement, generated artifacts, and project evolution.

---

## 1. Purpose

This document defines the canonical project structure for the SEO Research & Strategy Copilot / SEO Decision Engine.

Its purpose is to ensure that the implementation:

* reflects the system architecture;
* preserves domain boundaries;
* keeps AI capabilities modular;
* prevents accidental coupling;
* separates deterministic business logic from AI reasoning;
* keeps infrastructure replaceable;
* makes testing predictable;
* makes ownership explicit;
* supports a modular monolith as the default runtime architecture;
* allows future extraction of components into independent services without requiring premature microservice architecture;
* keeps documentation, source code, tests, configuration, migrations, prompts, contracts, and generated artifacts organized consistently.

This document defines **where things belong**.

It does not redefine:

* product requirements;
* SEO domain semantics;
* agent responsibilities;
* API contracts;
* UI behavior;
* database semantics;
* deployment architecture.

Those are governed by their respective documents.

---

# 2. Structural Principles

The project structure MUST follow these principles.

## 2.1 Architecture Must Be Visible in the Repository

The repository structure should make the architecture understandable without requiring the developer to inspect implementation details.

A developer should be able to identify:

* domain logic;
* application orchestration;
* AI capabilities;
* infrastructure;
* integrations;
* API;
* persistence;
* workflows;
* tests;
* frontend;
* documentation.

by directory structure alone.

---

## 2.2 Dependency Direction Must Be Explicit

Dependencies should generally flow inward toward stable domain concepts.

Conceptually:

```text
Presentation
    ↓
API / Application
    ↓
Orchestration
    ↓
Domain / Intelligence
    ↓
Ports / Contracts
    ↓
Infrastructure / Integrations
```

Infrastructure must not become the implicit owner of business rules.

AI providers must not become the owner of application semantics.

Frontend code must not directly depend on database implementation.

---

## 2.3 Modular Monolith First

The initial implementation SHOULD be a modular monolith.

The repository MUST NOT be organized as dozens of independently deployable services merely because the product contains multiple agents.

Logical modules are sufficient.

Future service extraction should be based on measured requirements such as:

* independent scaling;
* independent deployment;
* isolation requirements;
* team ownership;
* runtime characteristics;
* workload differences;
* reliability boundaries;
* security boundaries.

---

## 2.4 Domain Boundaries Over Technical Convenience

Code should be organized primarily around meaningful capabilities and domain boundaries rather than generic technical buckets.

Avoid structures such as:

```text
utils/
helpers/
services/
misc/
ai/
stuff/
```

when those directories become dumping grounds.

Prefer:

```text
topic_modeling/
intent/
serp/
entity/
decision/
```

with internal technical separation where necessary.

---

## 2.5 AI Is a Capability, Not the Architecture

The presence of LLMs must not determine the entire repository structure.

AI-related code belongs within bounded intelligence capabilities.

The system should remain understandable and testable even when:

* an LLM provider changes;
* a model changes;
* an AI call fails;
* an AI feature is disabled;
* deterministic logic performs part of the task.

---

# 3. Canonical Repository Layout

The initial repository SHOULD follow this high-level structure:

```text
seo-decision-engine/
│
├── apps/
│   ├── api/
│   ├── web/
│   └── worker/
│
├── backend/
│   ├── app/
│   └── tests/
│
├── packages/
│   ├── contracts/
│   ├── seo-core/
│   ├── ui/
│   └── config/
│
├── infrastructure/
│   ├── database/
│   ├── redis/
│   ├── vector/
│   ├── object_storage/
│   └── deployment/
│
├── integrations/
│   ├── llm/
│   ├── search/
│   ├── serp/
│   ├── seo/
│   ├── crawling/
│   └── analytics/
│
├── prompts/
│   ├── agents/
│   ├── workflows/
│   └── system/
│
├── tests/
│   ├── fixtures/
│   ├── golden/
│   ├── evaluation/
│   └── e2e/
│
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── operations/
│   └── development/
│
├── scripts/
├── .github/
├── .env.example
├── .gitignore
├── README.md
├── pyproject.toml
├── package.json
└── ...
```

The exact runtime packaging may evolve.

The architectural boundaries MUST remain intact.

---

# 4. Monorepo Strategy

The preferred structure is a monorepo.

The repository contains:

* backend;
* frontend;
* shared contracts;
* shared configuration;
* infrastructure;
* integrations;
* tests;
* documentation.

This provides:

* atomic changes across frontend/backend/contracts;
* consistent versioning;
* easier local development;
* shared CI;
* contract synchronization;
* simpler MVP deployment.

The monorepo MUST NOT mean that all code can import everything else.

Repository-level proximity does not imply architectural permission.

---

# 5. Application Layer

## 5.1 `apps/`

The `apps/` directory contains runnable applications.

Recommended:

```text
apps/
├── api/
├── web/
└── worker/
```

### `apps/api/`

API application entrypoint.

Responsibilities:

* application bootstrapping;
* API server configuration;
* dependency wiring;
* middleware;
* route registration;
* application lifecycle.

It should remain thin.

It MUST NOT contain core SEO reasoning.

---

### `apps/web/`

Frontend application.

Responsibilities:

* routing;
* layouts;
* pages;
* UI composition;
* frontend state;
* API consumption;
* visualization;
* interaction flows.

It MUST NOT directly access:

* PostgreSQL;
* Redis;
* vector database;
* LLM providers;
* search providers.

All backend data access occurs through the API/application boundary.

---

### `apps/worker/`

Background execution entrypoint.

Responsibilities may include:

* workflow execution;
* asynchronous agent tasks;
* crawling jobs;
* SERP collection;
* long-running research;
* scheduled refreshes;
* evaluation jobs.

The worker should reuse application/domain modules rather than duplicate business logic.

---

# 6. Backend Structure

The backend should be organized around bounded modules.

Recommended:

```text
backend/
└── app/
    ├── api/
    ├── application/
    ├── orchestration/
    ├── domain/
    ├── intelligence/
    ├── workflows/
    ├── knowledge/
    ├── contracts/
    ├── infrastructure/
    ├── integrations/
    ├── context/
    ├── security/
    ├── observability/
    └── main.py
```

---

# 7. API Layer

```text
backend/app/api/
├── routes/
├── dependencies/
├── middleware/
├── schemas/
└── errors/
```

## Responsibilities

The API layer handles:

* HTTP;
* authentication boundary;
* authorization checks;
* request parsing;
* request validation;
* response serialization;
* API versioning;
* transport-specific errors;
* rate limiting integration;
* streaming interfaces.

The API layer MUST NOT contain complex SEO reasoning.

---

# 8. Application Layer

```text
backend/app/application/
├── commands/
├── queries/
├── services/
└── use_cases/
```

The application layer coordinates business use cases.

Examples:

```text
CreateProject
StartResearch
ValidateTopic
AnalyzeSERP
BuildTopicalMap
AnalyzeCannibalization
ApproveRecommendation
```

Application services should coordinate domain and infrastructure through defined interfaces.

They should not become generic "service" dumping grounds.

---

# 9. Orchestration Layer

```text
backend/app/orchestration/
├── orchestrator/
├── planners/
├── execution/
├── scheduling/
├── checkpoints/
├── policies/
└── state/
```

Responsibilities:

* workflow planning;
* task decomposition;
* agent selection;
* execution sequencing;
* parallelization;
* conditional branching;
* retries;
* checkpoints;
* resume;
* human-review pauses;
* authorization gates;
* workflow state transitions.

The orchestrator MUST NOT implement the specialized reasoning of every agent.

---

# 10. Domain Layer

The domain layer contains stable business and SEO concepts.

Recommended:

```text
backend/app/domain/
├── business/
├── entity/
├── eav/
├── topic/
├── keyword/
├── intent/
├── search/
├── serp/
├── page/
├── competitor/
├── content_gap/
├── cannibalization/
├── internal_linking/
├── topical_map/
├── decision/
├── evidence/
├── provenance/
├── workflow/
└── common/
```

Domain modules contain:

* entities;
* value objects;
* domain rules;
* invariants;
* domain events where appropriate;
* deterministic calculations;
* domain-specific validation.

Domain code should not directly import an LLM SDK.

---

# 11. Intelligence Layer

The intelligence layer contains AI-enabled and analytical capabilities.

Recommended:

```text
backend/app/intelligence/
├── agents/
│   ├── business_research/
│   ├── entity/
│   ├── eav/
│   ├── topic_discovery/
│   ├── topic_validation/
│   ├── intent/
│   ├── serp/
│   ├── topic_clustering/
│   ├── page_mapping/
│   ├── page_architecture/
│   ├── internal_linking/
│   ├── content_gap/
│   ├── cannibalization/
│   ├── competitor/
│   └── decision_support/
│
├── reasoning/
├── retrieval/
├── extraction/
├── classification/
├── clustering/
├── ranking/
├── scoring/
├── validation/
└── registry/
```

Each agent module should preferably contain:

```text
topic_discovery/
├── agent.py
├── input.py
├── output.py
├── rules.py
├── prompts.py
├── validators.py
└── tests/
```

Not every agent needs every file.

Only create files when they represent meaningful boundaries.

---

# 12. Agent Module Rules

Every agent module MUST have:

1. explicit responsibility;
2. explicit input contract;
3. explicit output contract;
4. defined evidence requirements;
5. defined tool permissions;
6. defined confidence semantics;
7. defined failure behavior;
8. defined human-review behavior where applicable.

Agent modules MUST NOT:

* directly call unrelated agents;
* modify arbitrary database tables;
* bypass output validation;
* bypass authorization;
* write unvalidated AI output into canonical state;
* contain hidden global state.

Inter-agent communication should occur through orchestrator-managed contracts.

---

# 13. Workflow Structure

```text
backend/app/workflows/
├── research/
├── topic/
├── serp/
├── mapping/
├── auditing/
├── decision/
└── shared/
```

A workflow represents an executable process.

It is distinct from an agent.

Example:

```text
ResearchWorkflow
    ↓
BusinessResearch
    ↓
EntityModeling
    ↓
EAVEnrichment
    ↓
TopicDiscovery
    ↓
TopicValidation
    ↓
QueryDiscovery
    ↓
IntentAnalysis
    ↓
SERPAnalysis
    ↓
Clustering
    ↓
PageCandidates
    ↓
DecisionReview
```

Workflow definitions should reference capabilities rather than duplicate their implementations.

---

# 14. Knowledge Layer

Recommended:

```text
backend/app/knowledge/
├── repositories/
├── retrieval/
├── graph/
├── evidence/
├── provenance/
├── snapshots/
├── freshness/
└── indexing/
```

Responsibilities:

* retrieving structured knowledge;
* retrieving semantic knowledge;
* evidence retrieval;
* provenance traversal;
* entity relationships;
* knowledge snapshots;
* freshness management;
* indexing.

Knowledge access should occur through defined interfaces.

---

# 15. Context Layer

```text
backend/app/context/
├── assembly/
├── retrieval/
├── ranking/
├── compression/
├── budgeting/
├── policies/
└── state/
```

Responsibilities:

* task-specific context;
* context retrieval;
* context ranking;
* context compression;
* token budgeting;
* context freshness;
* context provenance;
* context isolation.

The context layer MUST NOT simply dump the entire project database into an LLM prompt.

---

# 16. Contracts

Shared contracts should have a dedicated location.

```text
backend/app/contracts/
├── agents/
├── workflows/
├── api/
├── decisions/
├── evidence/
├── context/
└── common/
```

Where contracts need to be shared with the frontend, they should also be represented in:

```text
packages/contracts/
```

The exact synchronization strategy may use:

* OpenAPI;
* generated TypeScript types;
* JSON Schema;
* Pydantic models;
* explicit versioned schemas.

The canonical contract ownership must remain explicit.

---

# 17. Infrastructure Layer

```text
backend/app/infrastructure/
├── database/
├── cache/
├── vector/
├── storage/
├── queues/
├── repositories/
├── transactions/
└── configuration/
```

Infrastructure implements technical concerns.

Examples:

* PostgreSQL repositories;
* Redis cache;
* pgvector/Qdrant adapters;
* object storage;
* queue implementations;
* database transactions.

Infrastructure MUST NOT redefine domain semantics.

---

# 18. Integration Layer

External systems should be isolated behind adapters.

```text
backend/app/integrations/
├── llm/
├── search/
├── serp/
├── seo/
├── crawling/
├── analytics/
└── external_data/
```

Each provider should ideally follow:

```text
integration/
├── interface.py
├── models.py
├── provider_a.py
├── provider_b.py
├── normalization.py
├── errors.py
└── tests/
```

Application code should depend on interfaces rather than vendor SDKs.

---

# 19. LLM Integration Structure

Recommended:

```text
integrations/llm/
├── interface.py
├── providers/
├── model_router.py
├── structured_output.py
├── tool_calling.py
├── errors.py
└── telemetry.py
```

LLM provider-specific code must remain isolated.

For example:

```text
OpenAI
Anthropic
Google
Local Model
```

should not leak provider-specific response objects throughout the domain.

---

# 20. Search and SERP Integration

Recommended:

```text
integrations/
├── search/
│   ├── interface.py
│   ├── providers/
│   ├── normalization.py
│   └── errors.py
│
└── serp/
    ├── interface.py
    ├── providers/
    ├── normalization.py
    ├── classifiers.py
    └── errors.py
```

Provider responses should be normalized into application-level contracts.

Raw provider payloads should be retained where evidence requirements justify them.

---

# 21. SEO Provider Integrations

SEO APIs should be isolated:

```text
integrations/seo/
├── interface.py
├── providers/
├── normalization.py
├── metrics.py
└── errors.py
```

Provider metrics MUST preserve:

* source;
* timestamp;
* search context;
* provider;
* metric definition;
* estimated/observed state;
* freshness.

---

# 22. Crawling

Crawler functionality should remain independent of SEO reasoning.

```text
integrations/crawling/
├── interface.py
├── fetchers/
├── parsers/
├── robots/
├── canonicalization/
├── extraction/
└── errors.py
```

Crawler output should become evidence/data.

The crawler must not directly decide:

> "Create a new page."

That decision belongs to the appropriate intelligence/decision layers.

---

# 23. Security Structure

```text
backend/app/security/
├── authentication/
├── authorization/
├── permissions/
├── tenancy/
├── secrets/
├── audit/
└── policies/
```

Security-sensitive logic must not be scattered across unrelated feature modules.

Authorization should be enforced server-side.

Frontend visibility is not authorization.

---

# 24. Observability Structure

```text
backend/app/observability/
├── logging/
├── metrics/
├── tracing/
├── audit/
└── events/
```

AI execution should additionally track:

* model;
* provider;
* model version where available;
* prompt version;
* token usage;
* latency;
* tool calls;
* validation result;
* output status;
* cost estimate;
* workflow/task identifiers.

---

# 25. Frontend Structure

The frontend should follow feature/domain-oriented organization.

Recommended:

```text
apps/web/
├── app/
├── components/
├── features/
├── lib/
├── hooks/
├── stores/
├── services/
├── types/
├── styles/
└── tests/
```

---

# 26. Frontend Feature Organization

Recommended:

```text
features/
├── business/
├── entities/
├── eav/
├── topics/
├── intent/
├── serp/
├── clustering/
├── topical-map/
├── pages/
├── internal-linking/
├── content-gap/
├── cannibalization/
├── competitors/
├── decisions/
├── workflows/
├── evidence/
├── context/
└── settings/
```

Each feature should contain only what is specific to that feature.

Example:

```text
features/topics/
├── components/
├── hooks/
├── api/
├── schemas/
├── types/
├── utils/
└── tests/
```

Shared UI belongs elsewhere.

---

# 27. Shared Frontend Components

Shared components belong in:

```text
packages/ui/
```

or an equivalent design-system package.

They should include:

* buttons;
* inputs;
* dialogs;
* tables;
* cards;
* badges;
* charts;
* graph primitives;
* evidence indicators;
* confidence indicators;
* state indicators.

Feature-specific components should not be promoted to shared components merely because they are used twice.

---

# 28. State Management

Frontend state should be separated conceptually.

```text
Server State
UI State
Session State
Workflow State
Form State
Derived View State
```

Do not create one global store containing all application state.

Server state should be managed through the appropriate data-fetching/cache layer.

UI state should remain local where possible.

---

# 29. Database Structure

Database migrations should be separated from application code.

Recommended:

```text
infrastructure/database/
├── migrations/
├── seeds/
├── fixtures/
├── scripts/
└── README.md
```

Migration files MUST be:

* ordered;
* deterministic;
* versioned;
* reviewable;
* reversible where practical.

Database schema changes must not be hidden inside application startup code.

---

# 30. Repository Pattern

Repositories should exist where they provide meaningful persistence abstraction.

Example:

```text
backend/app/infrastructure/repositories/
├── project_repository.py
├── entity_repository.py
├── topic_repository.py
├── serp_repository.py
├── page_repository.py
├── decision_repository.py
└── evidence_repository.py
```

Repositories should not become business-logic containers.

A repository answers questions such as:

> Retrieve topics for project X.

It should not answer:

> Should these topics become separate pages?

That belongs to domain/intelligence/decision logic.

---

# 31. Prompt Management

Prompts are versioned artifacts.

Recommended:

```text
prompts/
├── system/
├── agents/
│   ├── business_research/
│   ├── entity/
│   ├── topic_discovery/
│   ├── intent/
│   └── ...
└── workflows/
```

Prompts should include metadata such as:

```yaml
id: topic_discovery_v1
version: 1
agent: topic_discovery
purpose: discover candidate topics
input_contract: topic_discovery_input_v1
output_contract: topic_discovery_output_v1
status: active
```

Prompts MUST NOT become the only location where business rules exist.

Critical rules belong in code/contracts/domain policies.

---

# 32. Shared Packages

The `packages/` directory may contain reusable cross-application modules.

Recommended:

```text
packages/
├── contracts/
├── seo-core/
├── ui/
└── config/
```

## `contracts`

Shared API/output schemas.

## `seo-core`

Only genuinely reusable, stable SEO primitives.

## `ui`

Shared frontend design-system components.

## `config`

Shared configuration primitives where necessary.

Packages should have clear ownership and dependency boundaries.

---

# 33. Tests

Tests should exist at multiple levels.

Recommended:

```text
tests/
├── unit/
├── integration/
├── data/
├── ai/
├── agents/
├── workflows/
├── api/
├── e2e/
├── evaluation/
├── regression/
├── security/
├── fixtures/
└── golden/
```

Feature-local tests may also live beside implementation.

Example:

```text
topic_discovery/
├── agent.py
├── validators.py
└── tests/
    ├── test_agent.py
    └── test_validation.py
```

Large cross-module suites belong in the root test structure.

---

# 34. Golden Datasets

AI evaluation datasets should be explicit.

```text
tests/golden/
├── entities/
├── topics/
├── intents/
├── serp/
├── clustering/
├── page_mapping/
├── decisions/
└── workflows/
```

Golden datasets should support:

* regression;
* evaluation;
* quality comparison;
* model migration;
* prompt migration.

Golden outputs MUST NOT be treated as immutable truth.

They represent expected or reviewed behavior under defined conditions.

---

# 35. Evaluation Structure

AI evaluations should be separated from ordinary unit tests.

```text
tests/evaluation/
├── agents/
├── workflows/
├── retrieval/
├── ranking/
├── clustering/
└── decision_support/
```

Evaluation may measure:

* precision;
* recall;
* classification agreement;
* cluster quality;
* evidence coverage;
* schema validity;
* recommendation quality;
* calibration;
* consistency;
* business relevance.

---

# 36. Fixtures

Fixtures should be reusable and deterministic.

```text
tests/fixtures/
├── business/
├── entities/
├── topics/
├── keywords/
├── serp/
├── pages/
├── competitors/
├── decisions/
└── providers/
```

Provider fixtures should enable testing without external network calls.

---

# 37. Mock Providers

Every major external integration should have a mock/fake implementation suitable for tests.

Examples:

```text
FakeLLMProvider
FakeSearchProvider
FakeSERPProvider
FakeSEOProvider
FakeCrawler
```

This is required for:

* deterministic tests;
* failure testing;
* offline development;
* provider-independent testing;
* CI reliability.

---

# 38. Documentation Structure

The fixed 26-document architecture is authoritative.

Those documents should live under:

```text
docs/
├── 01_PRD.md
├── 02_PRODUCT_VISION.md
├── ...
└── 26_SKILLS_AND_TOOLING_POLICY.md
```

No additional "replacement" architecture documents should be created merely because a developer finds the existing documents inconvenient.

Supporting documentation may exist under:

```text
docs/
├── architecture/
├── decisions/
├── operations/
└── development/
```

but must not contradict the 26 baseline documents.

---

# 39. Architecture Decision Records

Architecture decisions should be stored under:

```text
docs/decisions/
├── ADR-001-...
├── ADR-002-...
└── ...
```

ADRs should document significant decisions such as:

* choosing PostgreSQL;
* choosing pgvector/Qdrant;
* choosing modular monolith;
* changing provider;
* extracting a service;
* changing workflow architecture;
* changing contract versioning strategy.

An ADR does not silently override baseline architecture.

A change to a baseline document must be explicit.

---

# 40. Scripts

```text
scripts/
├── development/
├── database/
├── testing/
├── evaluation/
├── migration/
└── maintenance/
```

Scripts should be:

* deterministic;
* documented;
* safe;
* appropriately scoped.

Destructive scripts MUST require explicit confirmation or a safe execution mode.

---

# 41. Configuration

Configuration should be environment-driven.

Recommended:

```text
config/
├── development/
├── test/
├── staging/
└── production/
```

Secrets MUST NOT be committed.

Use:

```text
.env.example
```

for required environment variable documentation.

Never commit:

```text
.env
```

or production secrets.

---

# 42. Generated Artifacts

Generated files should be clearly separated.

Possible:

```text
generated/
├── api/
├── contracts/
├── types/
└── documentation/
```

Generated files MUST NOT be manually edited unless explicitly designated as editable.

Generated artifacts should include provenance where practical:

* generator;
* source;
* version;
* timestamp.

---

# 43. Raw Evidence and Data

Raw external data should not be mixed with source code.

Runtime evidence should be stored through the configured storage system.

Local development fixtures may exist under:

```text
tests/fixtures/
```

Raw production evidence must not be committed to Git.

---

# 44. Dependency Rules

The following dependency direction is preferred:

```text
API
 ↓
Application
 ↓
Orchestration
 ↓
Domain / Intelligence
 ↓
Contracts / Ports
 ↓
Infrastructure / Integrations
```

The following patterns are prohibited:

```text
Domain → API
Domain → FastAPI
Domain → React
Domain → PostgreSQL SDK
Domain → LLM SDK
```

Similarly:

```text
Frontend → PostgreSQL
Frontend → LLM provider
Frontend → SERP provider
```

is prohibited.

---

# 45. Import Boundary Rules

Modules should depend only on explicitly allowed layers.

Example:

```text
domain
    ↓
common domain primitives

intelligence
    ↓
domain + contracts + retrieval/tool interfaces

application
    ↓
domain + intelligence + contracts

orchestration
    ↓
application + intelligence + workflow contracts

infrastructure
    ↓
contracts + domain persistence interfaces

api
    ↓
application + contracts

frontend
    ↓
API contracts + UI package
```

Circular dependencies MUST be treated as architectural defects unless explicitly justified.

---

# 46. Naming Conventions

Use predictable names.

Python:

```text
snake_case
```

Classes:

```text
PascalCase
```

Constants:

```text
UPPER_SNAKE_CASE
```

TypeScript:

```text
camelCase
PascalCase for types/components
```

Directories should generally use:

```text
kebab-case
```

for frontend routes and feature folders where appropriate.

Backend Python modules should use:

```text
snake_case
```

---

# 47. Naming Semantic Objects

Names must preserve domain distinctions.

Do not use:

```text
Keyword
```

when the object actually represents:

```text
Topic
Query
SearchExpression
PageCandidate
```

Do not use generic names such as:

```text
Data
Item
Object
Result
Info
Record
```

when a domain-specific name exists.

Names are part of architecture.

---

# 48. Avoid Generic Utility Directories

A directory such as:

```text
utils/
```

should not become a dumping ground.

Prefer:

```text
topic/canonicalization.py
entity/resolution.py
serp/classification.py
evidence/validation.py
```

If a utility is truly cross-domain, its placement should be justified.

---

# 49. Error Structure

Errors should be categorized.

Recommended:

```text
backend/app/
├── errors/
│   ├── domain.py
│   ├── application.py
│   ├── integration.py
│   ├── validation.py
│   ├── authorization.py
│   └── workflow.py
```

Errors should preserve:

* category;
* code;
* message;
* retryability;
* source;
* correlation ID;
* task/workflow context where appropriate.

---

# 50. Event Structure

If domain/application events are used:

```text
backend/app/
└── events/
    ├── domain/
    ├── application/
    └── integration/
```

Events should not become a hidden replacement for explicit function calls.

Use events when they provide meaningful decoupling or asynchronous behavior.

---

# 51. API Versioning

API contracts should be versioned intentionally.

Example:

```text
api/
└── routes/
    ├── v1/
    └── v2/
```

Do not create API versions merely because internal implementation changes.

A version boundary should represent a compatibility boundary.

---

# 52. Feature Ownership

Every major capability should have an identifiable owner.

Example:

| Capability          | Primary Module                                   |
| ------------------- | ------------------------------------------------ |
| Entity modeling     | `domain/entity`                                  |
| Entity intelligence | `intelligence/agents/entity`                     |
| Topic modeling      | `domain/topic` + `intelligence/topic_*`          |
| Intent              | `domain/intent` + `intelligence/agents/intent`   |
| SERP                | `domain/serp` + `integrations/serp` + SERP agent |
| Page mapping        | `domain/page` + mapping agent                    |
| Cannibalization     | `domain/cannibalization` + agent                 |
| Content gaps        | `domain/content_gap` + agent                     |
| Decisions           | `domain/decision` + decision support             |
| Workflow            | `workflows` + orchestration                      |
| Evidence            | `domain/evidence` + knowledge                    |
| Context             | `context`                                        |
| Human review        | application/orchestration + HITL UI              |

Ownership prevents duplicated implementations.

---

# 53. Shared Code Criteria

Code may become shared only when:

1. it has a stable semantic meaning;
2. multiple modules genuinely need it;
3. sharing reduces duplication without creating coupling;
4. its API is sufficiently stable;
5. its ownership is clear.

"Used twice" is not enough justification.

---

# 54. Frontend/Backend Contract Boundary

The frontend should consume typed contracts.

Preferred flow:

```text
Backend Domain
    ↓
Application
    ↓
Output Contract
    ↓
API
    ↓
Generated/Shared Client Types
    ↓
Frontend Feature
```

Frontend code must not reconstruct backend domain semantics independently.

---

# 55. AI Contract Boundary

AI outputs must follow:

```text
LLM
 ↓
Structured Output
 ↓
Schema Validation
 ↓
Semantic Validation
 ↓
Evidence Validation
 ↓
Domain Validation
 ↓
Policy Validation
 ↓
Canonical State
```

No directory structure should allow an agent to bypass this sequence.

---

# 56. Human Decision Boundary

Human decisions should be represented explicitly.

Recommended:

```text
domain/decision/
├── models.py
├── policies.py
├── lifecycle.py
├── validation.py
└── history.py
```

Human approval is not represented merely by:

```text
approved = true
```

without:

* actor;
* timestamp;
* scope;
* decision type;
* evidence/context;
* version;
* audit information.

---

# 57. Context and Documentation Boundary

The system should not load every repository file into every AI context.

Context should be assembled from:

* task requirements;
* relevant documentation;
* current workflow state;
* relevant domain objects;
* evidence;
* prior decisions;
* applicable contracts;
* applicable policies.

The repository structure must support targeted retrieval.

This directly supports `25_CONTEXT_MANAGEMENT.md`.

---

# 58. Skills and Tooling Boundary

Skills and tools should be registered and governed.

Tool-specific code belongs under appropriate integration/capability modules.

Tool installation metadata and policy belong to:

```text
26_SKILLS_AND_TOOLING_POLICY.md
```

The project MUST NOT allow arbitrary tool installation to silently modify production behavior.

---

# 59. Environment Structure

The system should support:

```text
Development
Test
Staging
Production
```

Environment-specific behavior should be controlled by configuration.

Do not fork business logic by environment.

Prefer:

```text
configuration → behavior
```

over:

```text
if production:
    ...
else:
    ...
```

unless the distinction is genuinely architectural.

---

# 60. Local Development

Local development should support minimal infrastructure required for meaningful work.

Potential local dependencies:

```text
PostgreSQL
Redis
Vector Store
Object Storage / Local equivalent
```

External providers should have mocks where practical.

A developer should be able to run core domain and workflow tests without external API credentials.

---

# 61. CI Structure

CI should conceptually execute:

```text
Formatting
    ↓
Linting
    ↓
Type Checking
    ↓
Unit Tests
    ↓
Integration Tests
    ↓
Contract Tests
    ↓
AI Evaluation
    ↓
Security Tests
    ↓
Build
    ↓
E2E
```

Exact ordering may be optimized for execution time.

Fast deterministic checks should fail early.

---

# 62. Repository Hygiene

Git MUST NOT contain:

* secrets;
* production credentials;
* temporary debugging artifacts;
* local databases;
* large raw SERP datasets;
* generated caches;
* model caches;
* unnecessary binaries;
* personal development files.

`.gitignore` must explicitly cover expected local artifacts.

---

# 63. Temporary Code

Temporary implementation MUST be marked clearly.

Use:

```text
TODO
FIXME
TECH-DEBT
EXPERIMENT
```

where appropriate.

Temporary code must not silently become production architecture.

High-risk temporary implementations should include an issue or ADR reference.

---

# 64. Experimental Work

Experiments should be isolated.

Recommended:

```text
experiments/
├── prompts/
├── models/
├── clustering/
├── retrieval/
└── evaluation/
```

Experimental code MUST NOT become a dependency of production modules without explicit validation and promotion.

---

# 65. Migration Strategy

When moving functionality:

```text
Old
 ↓
Compatibility Layer
 ↓
New
 ↓
Validation
 ↓
Migration
 ↓
Removal
```

Do not simultaneously rewrite unrelated modules.

Migrations should be incremental and reversible where practical.

---

# 66. Service Extraction Readiness

A module is a candidate for future extraction when it has:

* clear ownership;
* explicit API;
* explicit contracts;
* limited dependencies;
* independent scaling characteristics;
* independent deployment value;
* observable runtime behavior;
* isolated persistence requirements where necessary.

The repository should make extraction possible without designing for microservices prematurely.

---

# 67. Anti-Patterns

The following structures are prohibited or strongly discouraged.

### God Service

```text
services/seo_service.py
```

containing the entire product.

### God Agent

```text
agents/seo_agent.py
```

doing business research, entities, topics, SERP, mapping, and decisions.

### Generic AI Folder

```text
ai/
└── everything.py
```

### Generic Utility Dump

```text
utils/
└── 200 files
```

### Provider Leakage

```text
domain/topic/
    openai_client.py
```

### Database Leakage

```text
intelligence/topic/
    sqlalchemy_queries.py
```

### Frontend Database Access

```text
React → PostgreSQL
```

### Prompt-as-Architecture

```text
A giant prompt contains the entire product logic.
```

### Contract Bypass

```text
LLM → database
```

### Hidden State

Global mutable state shared between agents/workflows is prohibited unless explicitly designed and controlled.

---

# 68. Minimal MVP Structure

The MVP does not need every directory immediately.

A valid initial structure may be:

```text
seo-decision-engine/
├── apps/
│   ├── api/
│   └── web/
│
├── backend/
│   └── app/
│       ├── api/
│       ├── application/
│       ├── domain/
│       ├── intelligence/
│       ├── orchestration/
│       ├── knowledge/
│       ├── contracts/
│       ├── infrastructure/
│       ├── integrations/
│       ├── context/
│       └── security/
│
├── packages/
│   ├── contracts/
│   └── ui/
│
├── infrastructure/
│   └── database/
│
├── prompts/
├── tests/
├── docs/
└── scripts/
```

Empty directories should not be created merely to satisfy this document.

Create structural boundaries when implementation requires them.

---

# 69. Implementation Sequence

The project structure should be established progressively.

Recommended conceptual sequence:

```text
Repository Bootstrap
    ↓
Configuration
    ↓
Core Domain
    ↓
Contracts
    ↓
Persistence
    ↓
Application Layer
    ↓
Intelligence Capabilities
    ↓
Orchestration
    ↓
API
    ↓
Frontend
    ↓
Integrations
    ↓
Workers
    ↓
Evaluation / Observability / Operations
```

The actual implementation order must be derived from the dependency graph established during project control and task planning.

This document does not authorize implementation by itself.

---

# 70. Documentation-to-Code Mapping

Each major architectural concept should map to implementation.

| Concept                | Primary Documentation                    | Implementation Boundary       |
| ---------------------- | ---------------------------------------- | ----------------------------- |
| Product                | `01_PRD.md`                              | Entire system                 |
| Vision                 | `02_PRODUCT_VISION.md`                   | Product direction             |
| Rules                  | `03_MASTER_RULES.md`                     | All modules                   |
| System architecture    | `04_SYSTEM_ARCHITECTURE.md`              | Backend/runtime boundaries    |
| Agent architecture     | `05_AI_AGENT_ARCHITECTURE.md`            | `intelligence/`               |
| Data                   | `06_DATA_ARCHITECTURE.md`                | `domain/` + persistence       |
| Technical architecture | `07_TECHNICAL_ARCHITECTURE.md`           | Runtime/infrastructure        |
| SEO knowledge          | `08_SEO_KNOWLEDGE_MODEL.md`              | `knowledge/` + domain         |
| Entity/EAV             | `09_ENTITY_EAV_MODEL.md`                 | `domain/entity`, `domain/eav` |
| Topic modeling         | `10_TOPIC_MODELING_AND_CLUSTERING.md`    | topic/clustering modules      |
| Search/SERP            | `11_SEARCH_AND_SERP_INTELLIGENCE.md`     | search/serp                   |
| Decision engine        | `12_SEO_DECISION_ENGINE.md`              | decision/application          |
| Agents                 | `13_AGENT_SPECIFICATIONS.md`             | `intelligence/agents`         |
| Workflows              | `14_AGENT_WORKFLOW.md`                   | `workflows/` + orchestration  |
| HITL                   | `15_HUMAN_IN_THE_LOOP.md`                | decisions/workflows/UI        |
| Contracts              | `16_OUTPUT_CONTRACTS.md`                 | `contracts/`                  |
| UX                     | `17_UI_UX_SPECIFICATION.md`              | frontend                      |
| Frontend               | `18_FRONTEND_ARCHITECTURE.md`            | `apps/web`                    |
| Design system          | `19_DESIGN_SYSTEM.md`                    | `packages/ui`                 |
| Project structure      | `20_PROJECT_STRUCTURE.md`                | repository                    |
| Development/debug      | `21_DEVELOPMENT_AND_DEBUG.md`            | engineering process           |
| Testing                | `22_TESTING_AND_VALIDATION.md`           | `tests/`                      |
| Project control        | `23_PROJECT_CONTROL_CENTER.md`           | state/task governance         |
| Index/roadmap          | `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md` | project planning              |
| Context                | `25_CONTEXT_MANAGEMENT.md`               | `context/`                    |
| Skills/tooling         | `26_SKILLS_AND_TOOLING_POLICY.md`        | tooling/integrations          |

---

# 71. Change Management

Structural changes require evaluation of:

1. affected modules;
2. dependency direction;
3. contracts;
4. tests;
5. documentation;
6. context requirements;
7. deployment implications;
8. security implications;
9. migration requirements.

A directory move is not automatically harmless.

It may alter:

* imports;
* ownership;
* dependency boundaries;
* test discovery;
* build behavior;
* generated code;
* deployment packaging.

---

# 72. Definition of Done for Structural Changes

A project-structure change is complete only when:

* the new location is architecturally justified;
* dependency direction remains valid;
* imports are updated;
* tests pass;
* no circular dependency was introduced;
* contracts remain valid;
* documentation is updated if necessary;
* obsolete files are removed;
* generated artifacts are handled correctly;
* CI passes;
* runtime behavior is verified where relevant;
* project state is updated.

---

# 73. Structural Validation Checklist

Before accepting a new module, ask:

```text
Does this belong to a clear domain?
Does it have a clear owner?
Does it have a stable responsibility?
Does it depend on the correct layer?
Does it expose an explicit contract?
Can it be tested independently?
Does it introduce a circular dependency?
Does it duplicate existing functionality?
Does it leak provider-specific behavior?
Does it bypass validation?
Does it bypass authorization?
Does it create unnecessary global state?
Does it belong in shared code?
Does the documentation need updating?
```

If these questions cannot be answered, the module should not be accepted as production architecture.

---

# 74. Architectural Integrity Rules

The repository structure must preserve these distinctions:

```text
Entity ≠ Topic
Topic ≠ Keyword
Keyword ≠ Query
Query ≠ SERP
SERP ≠ Intent
Topic ≠ Page
Topical Map ≠ Page Candidate Mapping
Page Candidate Mapping ≠ Information Architecture
Recommendation ≠ Decision
Decision ≠ Action
Agent ≠ Workflow
Workflow ≠ Orchestrator
Evidence ≠ Inference
Confidence ≠ Truth
AI Output ≠ Canonical State
```

The directory structure must not collapse these concepts merely for implementation convenience.

---

# 75. Final Project Structure Model

The intended architectural relationship is:

```text
                         ┌───────────────────────┐
                         │       Frontend        │
                         │       apps/web        │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │       API Layer       │
                         │       apps/api        │
                         └───────────┬───────────┘
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   Application Layer   │
                         └───────────┬───────────┘
                                     │
                   ┌─────────────────┴─────────────────┐
                   ▼                                   ▼
        ┌─────────────────────┐             ┌─────────────────────┐
        │    Orchestrator     │             │       Domain        │
        │    + Workflows      │             │ Business / SEO      │
        └──────────┬──────────┘             └──────────┬──────────┘
                   │                                   │
                   ▼                                   ▼
        ┌─────────────────────┐             ┌─────────────────────┐
        │    Intelligence     │             │     Knowledge       │
        │ Agents / Analysis   │             │ Evidence / Graph    │
        └──────────┬──────────┘             └──────────┬──────────┘
                   │                                   │
                   └─────────────────┬─────────────────┘
                                     ▼
                         ┌───────────────────────┐
                         │ Contracts / Ports     │
                         └───────────┬───────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
          ┌─────────────────────┐           ┌─────────────────────┐
          │    Infrastructure   │           │     Integrations    │
          │ DB / Cache / Vector │           │ LLM / SERP / SEO    │
          └─────────────────────┘           └─────────────────────┘
```

The repository should mirror this architecture as closely as practical.

---

# 76. Non-Negotiable Rules

1. The project uses a modular-monolith structure by default.
2. Repository organization must reflect architectural boundaries.
3. Domain logic must remain independent from infrastructure providers.
4. AI agents must remain modular capabilities.
5. Agents must not bypass contracts and validation.
6. External providers must be isolated behind adapters.
7. Frontend must not directly access backend infrastructure.
8. Shared code must have explicit ownership.
9. Generic dumping-ground directories must be avoided.
10. Tests must reflect architectural boundaries.
11. Prompts must be versioned artifacts, not hidden architecture.
12. Human decisions must remain explicit and auditable.
13. Context must be assembled selectively.
14. Generated artifacts must be distinguishable from source.
15. Structural changes require dependency and regression validation.
16. The fixed 26-document architecture remains authoritative.
17. This document defines project organization; it does not authorize implementation.
18. No structural change may silently redefine the system architecture.
19. No directory structure may collapse important domain distinctions.
20. Simplicity is preferred until complexity is justified by actual requirements.

---

# 77. Relationship to Other Documents

This document depends on:

* `03_MASTER_RULES.md`
* `04_SYSTEM_ARCHITECTURE.md`
* `05_AI_AGENT_ARCHITECTURE.md`
* `06_DATA_ARCHITECTURE.md`
* `07_TECHNICAL_ARCHITECTURE.md`
* `13_AGENT_SPECIFICATIONS.md`
* `14_AGENT_WORKFLOW.md`
* `16_OUTPUT_CONTRACTS.md`
* `18_FRONTEND_ARCHITECTURE.md`
* `19_DESIGN_SYSTEM.md`

It is directly related to:

* `21_DEVELOPMENT_AND_DEBUG.md`
* `22_TESTING_AND_VALIDATION.md`
* `23_PROJECT_CONTROL_CENTER.md`
* `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md`
* `25_CONTEXT_MANAGEMENT.md`
* `26_SKILLS_AND_TOOLING_POLICY.md`

The final dependency graph and implementation order must be derived by auditing the complete 26-document system.

---

# 78. Document Control

```yaml
document:
  id: "20"
  filename: "20_PROJECT_STRUCTURE.md"
  status: "APPROVED_AS_BASELINE_PROJECT_STRUCTURE"
  authority: "baseline_repository_and_code_organization"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

architecture:
  repository: "monorepo"
  runtime_default: "modular_monolith"
  service_extraction: "evidence_based"
  dependency_direction: "inward_toward_domain_and_contracts"

primary_layers:
  - "presentation"
  - "api"
  - "application"
  - "orchestration"
  - "intelligence"
  - "domain"
  - "knowledge"
  - "contracts"
  - "infrastructure"
  - "integrations"

primary_applications:
  - "api"
  - "web"
  - "worker"

core_backend_boundaries:
  - "api"
  - "application"
  - "orchestration"
  - "domain"
  - "intelligence"
  - "workflows"
  - "knowledge"
  - "context"
  - "contracts"
  - "infrastructure"
  - "integrations"
  - "security"
  - "observability"

core_frontend_boundaries:
  - "features"
  - "components"
  - "services"
  - "state"
  - "types"
  - "visualization"
  - "tests"

external_provider_policy:
  isolation: true
  adapter_pattern: true
  provider_specific_types_leakage: false

ai_architecture:
  agents_are_modules: true
  direct_agent_to_agent_calls: false
  structured_contracts: true
  validated_outputs_required: true
  direct_unvalidated_ai_to_canonical_state: false

testing:
  unit: true
  integration: true
  contract: true
  workflow: true
  ai_evaluation: true
  regression: true
  security: true
  e2e: true
  mock_providers: true
  golden_datasets: true

documentation:
  baseline_documents: 26
  architecture_documents_are_authoritative: true
  adr_supported: true

security:
  secrets_in_git: false
  server_side_authorization: true
  tenant_isolation_required: true

structural_principles:
  domain_first: true
  explicit_boundaries: true
  minimal_shared_code: true
  no_generic_dumping_grounds: true
  no_premature_microservices: true
  no_hidden_global_state: true

next_dependency:
  document: "21_DEVELOPMENT_AND_DEBUG.md"
  purpose: "development_workflow_debugging_and_engineering_process"
```

---

**End of `20_PROJECT_STRUCTURE.md`**
