# 07_TECHNICAL_ARCHITECTURE.md

**Document:** `07_TECHNICAL_ARCHITECTURE.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Technical Architecture Specification
**Status:** `APPROVED_AS_BASELINE_TECHNICAL_ARCHITECTURE`
**Depends On:** `01_PRD.md`, `02_PRODUCT_VISION.md`, `03_MASTER_RULES.md`, `04_SYSTEM_ARCHITECTURE.md`, `05_AI_AGENT_ARCHITECTURE.md`, `06_DATA_ARCHITECTURE.md`

---

# 1. Purpose

This document translates the product, system, AI, and data architecture into a concrete technical architecture.

It defines:

* runtime technologies
* backend architecture
* frontend architecture boundaries
* API architecture
* AI runtime
* orchestration runtime
* persistence
* vector retrieval
* background processing
* external integrations
* configuration
* observability
* security boundaries
* deployment
* environments
* scalability
* reliability
* testing infrastructure
* technical evolution

This document intentionally defines **technical direction and boundaries**, not every implementation detail.

Concrete implementation tasks belong to the project planning and task documents.

---

# 2. Technical Architecture Goals

The technical architecture must support:

1. modular development
2. reliable AI execution
3. persistent SEO intelligence
4. evidence preservation
5. human-in-the-loop workflows
6. asynchronous research
7. structured AI outputs
8. provider independence
9. strong project isolation
10. testability
11. observability
12. controlled scaling
13. predictable development
14. future extensibility

The system must remain technically simpler than the problem it solves.

---

# 3. Primary Technology Direction

The baseline technical stack is:

```yaml
backend:
  language: Python
  framework: FastAPI

database:
  primary: PostgreSQL

semantic_retrieval:
  vector_store: pgvector_or_Qdrant

ai:
  provider: provider_agnostic_LLM_interface

search:
  provider_agnostic_search_and_SERP_adapters

frontend:
  architecture: modern_web_application
  framework: Next.js_or_equivalent_approved_web_framework

background_processing:
  workers: Python_based
  queue: Redis_backed_or_equivalent

cache:
  Redis

object_storage:
  S3_compatible_or_equivalent

observability:
  structured_logging
  metrics
  tracing

deployment:
  initial: modular_monolith
  future: selectively_distributed
```

The exact provider selections may evolve without changing the domain architecture.

---

# 4. Technology Selection Principles

Technology decisions must optimize for:

* correctness
* maintainability
* ecosystem maturity
* developer productivity
* testability
* security
* observability
* interoperability
* reasonable operating cost

Technology must not be selected because it is merely fashionable.

---

# 5. Backend

The backend uses Python as the primary implementation language.

FastAPI is the baseline HTTP/API framework.

The backend owns:

* application APIs
* authentication/authorization integration
* workflow execution
* orchestration
* domain services
* AI services
* tool adapters
* persistence access
* background jobs
* validation
* observability

---

# 6. Backend Architectural Boundary

The backend should be organized around logical modules rather than a purely technical folder hierarchy.

Conceptually:

```text
backend/
├── api/
├── application/
├── orchestration/
├── intelligence/
├── domain/
├── knowledge/
├── integrations/
├── infrastructure/
└── workers/
```

The final project structure is governed by:

`20_PROJECT_STRUCTURE.md`

---

# 7. Application Layer

The application layer coordinates user-facing use cases.

Responsibilities:

* request validation
* authorization checks
* use-case invocation
* transaction boundaries
* workflow creation
* response mapping

It should not contain large amounts of SEO reasoning.

---

# 8. Domain Layer

The domain layer contains business and SEO domain rules.

Examples:

* topic rules
* entity relationships
* decision states
* recommendation rules
* workflow domain rules
* page relationships
* validation rules

Domain logic must remain independent of:

* HTTP
* LLM providers
* specific search providers
* frontend frameworks
* infrastructure details

---

# 9. Intelligence Layer

The intelligence layer contains:

* AI services
* specialized agents
* inference pipelines
* semantic classification
* clustering
* reasoning components
* model adapters

It must communicate with the domain and knowledge layers through defined interfaces.

---

# 10. Orchestration Layer

The orchestration layer manages:

* workflow planning
* capability selection
* task dependencies
* agent execution
* retries
* timeouts
* human review
* workflow state
* execution budgets

The orchestrator must not become the owner of every domain rule.

---

# 11. Knowledge Layer

The knowledge layer provides access to:

* entities
* EAV
* topics
* keywords
* intents
* SERPs
* pages
* competitors
* evidence
* recommendations
* decisions
* history

It abstracts persistence from intelligence modules.

---

# 12. Integration Layer

The integration layer contains adapters for:

* LLM providers
* search providers
* SERP providers
* SEO APIs
* web crawlers
* analytics
* external websites
* storage services
* third-party tools

External providers must not leak provider-specific models throughout the domain.

---

# 13. Infrastructure Layer

Infrastructure manages:

* PostgreSQL connections
* Redis
* queues
* object storage
* HTTP clients
* configuration
* secrets
* logging
* metrics
* tracing
* task execution

Infrastructure is replaceable where practical.

---

# 14. Dependency Direction

The preferred dependency direction is:

```text
API
 ↓
Application
 ↓
Orchestration
 ↓
Domain / Intelligence
 ↓
Knowledge Interfaces
 ↓
Infrastructure / Integrations
```

Infrastructure implementations may satisfy interfaces defined by inner layers.

Core domain rules must not depend directly on infrastructure implementations.

---

# 15. API Architecture

The API should expose explicit application capabilities.

Conceptual groups:

```text
/auth
/projects
/business
/entities
/eav
/topics
/keywords
/intents
/serps
/pages
/competitors
/evidence
/recommendations
/decisions
/workflows
/agents
/evaluations
```

Exact endpoints belong to API implementation specifications.

---

# 16. API Versioning

Public or externally consumed APIs should support explicit versioning when compatibility requires it.

Example:

```text
/api/v1/...
```

Internal interfaces may use different versioning strategies where appropriate.

API versioning must not be introduced merely for appearance.

---

# 17. Request Validation

All externally supplied input must be validated before entering domain logic.

Validation should include:

* type validation
* required fields
* length limits
* enum validation
* ownership
* authorization
* domain constraints

Malformed input must fail explicitly.

---

# 18. Response Contracts

API responses must use explicit schemas.

Responses should distinguish:

* success
* validation failure
* authorization failure
* not found
* conflict
* provider failure
* workflow failure
* partial result

The API must not return arbitrary LLM prose as the only structured interface.

---

# 19. Error Architecture

Errors should be represented through a consistent application error model.

Conceptually:

```yaml
error:
  code: TOPIC_VALIDATION_FAILED
  message: Human-readable description
  details: structured_context
  request_id: req_123
  retryable: false
```

Internal stack traces must not be exposed to end users.

---

# 20. HTTP Error Semantics

The API should use appropriate HTTP semantics.

Examples:

```text
400 → malformed request
401 → unauthenticated
403 → unauthorized
404 → resource unavailable
409 → state/conflict
422 → validation failure
429 → rate limited
500 → internal failure
502/503 → external dependency failure
504 → timeout
```

Exact mapping should remain consistent across the system.

---

# 21. Synchronous vs Asynchronous Execution

Short operations may execute synchronously.

Examples:

* retrieve topic
* validate small payload
* update metadata
* fetch cached result

Long operations should execute asynchronously.

Examples:

* large-scale keyword research
* SERP collection
* competitor crawling
* clustering
* topical map generation
* full-site analysis

---

# 22. Background Worker Architecture

Long-running workflows should use background workers.

Conceptually:

```text
API
 ↓
Create Workflow
 ↓
Queue
 ↓
Worker
 ↓
Orchestrator
 ↓
Agents / Tools
 ↓
Knowledge Layer
```

The API process must not be responsible for maintaining long-running research operations.

---

# 23. Queue Architecture

The queue should support:

* delayed execution
* retries
* job state
* concurrency control
* failure handling
* deduplication where required

Redis may be used initially for queue/cache infrastructure.

The queue implementation must remain abstracted enough to allow replacement.

---

# 24. Workflow Persistence

Every meaningful asynchronous workflow should have persistent state.

Example:

```yaml
workflow:
  id: wf_123
  type: topical_map_generation
  project_id: project_456
  status: RUNNING
  current_step: serp_analysis
  started_at: ...
  updated_at: ...
```

This state must survive worker restarts.

---

# 25. Workflow Resume

A failed or interrupted workflow should be resumable where practical.

The system should persist sufficient state to identify:

* completed steps
* failed step
* inputs
* outputs
* retry attempts
* human decisions
* remaining work

---

# 26. PostgreSQL

PostgreSQL is the primary system of record.

It stores authoritative structured information including:

* projects
* users
* business information
* entities
* relationships
* EAV
* topics
* keywords
* intents
* search observations
* SERPs
* pages
* competitors
* evidence
* recommendations
* decisions
* workflow state
* audit records

---

# 27. Database Access

The backend should use a clear persistence abstraction.

Possible implementation technologies include:

* SQLAlchemy
* SQLModel
* async PostgreSQL drivers

The final selection must follow project implementation requirements.

Database access must not be scattered arbitrarily throughout application code.

---

# 28. Transactions

Transactions must be used for operations that require atomicity.

Examples:

* creating related domain records
* approving a decision
* updating workflow state
* persisting derived results
* state transitions

Transaction boundaries should follow domain/use-case requirements.

---

# 29. Database Constraints

Important invariants should be enforced at database level where practical.

Examples:

* uniqueness
* foreign-key integrity
* non-null constraints
* ownership
* valid state combinations

Application validation remains necessary but must not be the only protection.

---

# 30. Migrations

Database schema changes must use version-controlled migrations.

A migration must define:

* schema change
* forward operation
* rollback strategy where practical
* data migration requirements
* compatibility impact

Production schema changes must not be performed manually without a controlled process.

---

# 31. Vector Retrieval

The system requires semantic retrieval for:

* entity similarity
* topic similarity
* evidence retrieval
* document retrieval
* semantic clustering
* contextual retrieval

The vector layer is supplementary.

It is not the authoritative system of record.

---

# 32. pgvector vs Dedicated Vector Store

The initial system may use:

* PostgreSQL + pgvector

or:

* PostgreSQL + Qdrant

The choice should be driven by:

* dataset size
* query complexity
* operational simplicity
* filtering requirements
* latency
* scaling requirements

The architecture must keep vector retrieval behind an abstraction.

---

# 33. Hybrid Retrieval

Semantic retrieval should generally be combined with structured filtering.

Conceptually:

```text
Query
 ↓
Structured Filters
 +
Semantic Retrieval
 +
Authority / Freshness
 ↓
Ranked Context
```

Pure vector similarity is insufficient for many SEO intelligence tasks.

---

# 34. Retrieval Metadata

Every vectorized object should retain enough metadata to identify:

* source entity
* object type
* object ID
* project
* version
* timestamp
* source
* content scope

This allows retrieval results to be traced back to authoritative data.

---

# 35. Embedding Versioning

Embeddings must be versioned where reproducibility matters.

Example:

```yaml
embedding:
  provider: example-provider
  model: embedding-model-x
  version: 2
```

A change in embedding model may require re-indexing.

---

# 36. Raw Evidence Storage

Raw external evidence should be retained where required.

Examples:

* SERP payloads
* API responses
* crawled documents
* search snapshots
* source documents

Raw evidence should be immutable or versioned where appropriate.

---

# 37. Object Storage

Large raw artifacts should not necessarily be stored directly inside PostgreSQL.

Object storage may be used for:

* HTML snapshots
* large documents
* crawl results
* raw provider payloads
* exported reports

PostgreSQL stores metadata and references.

---

# 38. Redis

Redis may support:

* caching
* rate limiting
* temporary workflow state
* queues
* distributed locks where required
* short-lived context

Redis must not replace PostgreSQL as the authoritative source of durable project knowledge.

---

# 39. Cache Policy

Cache entries should define:

* key
* scope
* TTL
* source
* freshness
* invalidation

Caching must never make stale information appear authoritative.

---

# 40. Distributed Locks

Locks may be used where concurrent operations could corrupt state.

Examples:

* duplicate workflow execution
* repeated expensive research
* concurrent decision approval
* unique ingestion operations

Locks must have:

* owner
* expiration
* recovery behavior

---

# 41. LLM Architecture

All LLM interaction should occur through an internal abstraction.

Conceptually:

```text
Agent
 ↓
AI Runtime Interface
 ↓
Model Router
 ↓
Provider Adapter
 ↓
LLM Provider
```

Agents should not embed direct provider-specific API calls.

---

# 42. Model Router

The model router may select models based on:

* task
* complexity
* latency requirement
* cost budget
* structured-output capability
* context size
* language support
* provider health

The router must remain observable.

---

# 43. AI Runtime

The AI runtime is responsible for:

* prompt construction
* model invocation
* structured output handling
* token/cost tracking
* timeout
* retries
* provider errors
* model metadata
* response normalization

It must not contain SEO business logic.

---

# 44. Prompt Management

Prompts should be:

* versioned
* identifiable
* testable
* reviewable

Prompt changes should be treated as behavior changes.

---

# 45. Structured AI Output

Where an AI result is consumed programmatically:

```text
LLM
 ↓
Parser
 ↓
Schema Validator
 ↓
Semantic Validator
 ↓
Domain Validator
 ↓
Persistence
```

No direct persistence of arbitrary model text into authoritative fields.

---

# 46. Tool Calling

AI tool calls should pass through a controlled runtime.

Conceptually:

```text
Agent
 ↓
Tool Selection
 ↓
Permission Check
 ↓
Input Validation
 ↓
Tool Execution
 ↓
Output Validation
 ↓
Evidence / Result
```

---

# 47. Search Integration

Search integration should be provider-independent.

Conceptually:

```text
Search Service
     ↓
Provider Adapter
     ↓
Search Provider
```

The internal system should receive a normalized search representation.

---

# 48. SERP Integration

SERP providers may return different:

* schemas
* ranking structures
* feature labels
* pagination
* localization
* device contexts

Provider-specific formats must be normalized before entering the domain model.

---

# 49. Search Context

Search observations should preserve context such as:

* query
* locale
* country
* language
* device
* timestamp
* provider
* result position
* SERP features

Search results without context may be misleading.

---

# 50. Website Crawling

Website crawling should be treated as an external data acquisition capability.

The crawler must support:

* robots-aware behavior where applicable
* rate limiting
* timeout
* retries
* content extraction
* URL canonicalization
* crawl metadata
* raw evidence retention

The crawler must not become coupled to the topic model.

---

# 51. Competitor Research

Competitor data must preserve:

* source
* observation time
* competitor identity
* observed pages
* topics
* search evidence
* extracted attributes

Competitor information must not be treated as permanent truth.

---

# 52. External Analytics

Future integrations may include:

* Google Search Console
* Google Analytics
* rank tracking
* backlink providers
* SEO data providers

Each integration must use an adapter.

No provider-specific data structure should become the universal domain model.

---

# 53. Authentication

Authentication should be handled at the application/security boundary.

The architecture should support:

* session or token-based authentication
* secure password storage where passwords exist
* OAuth where approved
* session expiration
* account recovery

Exact authentication implementation is outside this document.

---

# 54. Authorization

Authorization must operate at:

* user level
* workspace level
* project level
* resource level where necessary
* tool/action level where necessary

Agents inherit controlled permissions.

AI output must never grant permissions.

---

# 55. Multi-Tenancy

The system should logically isolate:

```text
Organization
   ↓
Workspace
   ↓
Project
   ↓
Data
   ↓
Workflow
```

Every query involving project-scoped data must enforce ownership boundaries.

---

# 56. Tenant Isolation

Cross-project data retrieval must be impossible through normal application pathways unless explicitly authorized.

This includes:

* SQL queries
* vector retrieval
* cache
* object storage
* search indexes
* workflow state

---

# 57. Secrets Management

Secrets should be supplied through:

* environment configuration
* secret manager
* deployment platform secret storage

They must never be committed to source control.

---

# 58. Configuration

Configuration should be separated into:

### Application Configuration

Examples:

* feature flags
* timeouts
* limits
* environment behavior

### Secret Configuration

Examples:

* API keys
* database credentials
* signing secrets

### Runtime Configuration

Examples:

* model routing
* provider availability
* queue concurrency

Configuration should be typed and validated at startup.

---

# 59. Environment Model

At minimum:

```text
development
testing
staging
production
```

Each environment should have clearly defined:

* database
* credentials
* external providers
* logging level
* feature flags
* data policy

---

# 60. Development Environment

Development should optimize for:

* fast iteration
* reproducibility
* local debugging
* safe mock providers
* isolated test data

External services should be replaceable by mocks where appropriate.

---

# 61. Testing Environment

The testing environment must not depend on uncontrolled production services.

Use:

* deterministic fixtures
* mock providers
* controlled AI responses
* isolated databases
* test-specific credentials

External integration tests may run separately when required.

---

# 62. Staging Environment

Staging should approximate production behavior.

It should validate:

* deployment
* migrations
* external integrations
* background jobs
* workflow execution
* observability
* security configuration

---

# 63. Production Environment

Production must use:

* managed secrets
* secure database access
* backups
* monitoring
* alerting
* controlled migrations
* rate limiting
* audit logging
* rollback strategy

Production readiness must be verified, not assumed.

---

# 64. Deployment Architecture

Initial deployment:

```text
                    Internet
                       │
                       ▼
                Reverse Proxy
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
         Frontend             Backend
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
          PostgreSQL         Redis          Object Store
              │
              ▼
         Vector Layer
```

Background workers may run as separate processes while remaining part of the same logical modular application.

---

# 65. Worker Deployment

Workers should be independently scalable when necessary.

However, worker separation does not automatically imply microservice architecture.

The workers may remain part of the same codebase and share domain modules.

---

# 66. Horizontal Scaling

Stateless API instances should be horizontally scalable.

State must reside in:

* PostgreSQL
* Redis
* object storage
* workflow persistence

not only in process memory.

---

# 67. Worker Scaling

Worker concurrency should be controlled based on:

* CPU
* memory
* provider rate limits
* LLM concurrency
* database capacity
* queue depth
* cost budgets

---

# 68. AI Concurrency

AI calls must respect provider limits.

The system should support:

* concurrency limits
* per-provider quotas
* exponential backoff
* request cancellation
* budget enforcement

---

# 69. Rate Limiting

Rate limiting should exist for:

* public API
* expensive workflows
* search providers
* SERP providers
* LLM providers
* crawling

Rate limits should be configurable.

---

# 70. Observability

The system should implement:

```text
Logs
+
Metrics
+
Traces
+
Audit Events
```

Together these provide operational visibility.

---

# 71. Structured Logging

Logs should be structured rather than arbitrary text.

Example:

```yaml
timestamp: ...
level: ERROR
service: orchestrator
workflow_id: wf_123
task_id: task_456
agent_id: serp_agent
error_code: PROVIDER_TIMEOUT
retryable: true
```

Secrets and sensitive information must be excluded.

---

# 72. Distributed Tracing

Even in the modular monolith, execution IDs should be propagated.

Example:

```text
request_id
  ↓
workflow_id
  ↓
task_id
  ↓
agent_execution_id
  ↓
tool_execution_id
```

This makes future distributed extraction easier.

---

# 73. Metrics

Useful metrics include:

### Application

* request latency
* error rate
* throughput

### Workflow

* completion rate
* failure rate
* queue latency
* execution duration

### AI

* model latency
* token usage
* cost
* schema failure
* retry rate

### SEO

* evidence freshness
* data coverage
* human acceptance
* recommendation quality

---

# 74. Health Checks

Services should expose appropriate health information.

Distinguish:

* process health
* dependency health
* readiness
* liveness

A running process does not necessarily mean the system is ready.

---

# 75. Backups

Production PostgreSQL data must have a backup strategy.

Important object-storage data should also have appropriate retention and recovery controls.

Backup restoration must be tested periodically.

A backup that has never been restored is not sufficient evidence of recoverability.

---

# 76. Disaster Recovery

The architecture should eventually define:

* RPO
* RTO
* backup frequency
* restore procedure
* dependency recovery
* failure communication

Requirements may differ by deployment tier.

---

# 77. Data Export

Projects should be exportable where practical.

Export should preserve:

* structured data
* evidence references
* decisions
* important metadata
* version information

The system should avoid unnecessary vendor lock-in.

---

# 78. Data Import

Imports must pass:

* schema validation
* ownership validation
* referential validation
* provenance requirements
* conflict handling

Imported data must be identifiable as imported data.

---

# 79. Concurrency

Concurrent operations must account for:

* optimistic locking
* database transactions
* workflow locks
* duplicate execution
* stale state

High-impact decisions should not be silently overwritten by concurrent updates.

---

# 80. Event Architecture

The system may use internal domain events for loosely coupled reactions.

Examples:

```text
TopicValidated
EntityUpdated
SERPObserved
DecisionApproved
PageCandidateCreated
```

Events should represent meaningful domain occurrences.

They should not be created for every trivial function call.

---

# 81. Event Handling

Event consumers must be:

* idempotent
* observable
* failure-aware

Failed event handling must not silently lose important state.

---

# 82. Eventual Consistency

Some derived intelligence may be eventually consistent.

For example:

```text
Entity Updated
   ↓
Topic Recalculation
   ↓
Clustering Update
   ↓
Recommendation Update
```

The UI should make asynchronous state understandable.

---

# 83. Strong Consistency

Strong consistency should be used where correctness requires it.

Examples:

* authorization
* decision approval
* ownership
* critical state transitions
* financial/billing state if later introduced

---

# 84. Frontend Technical Boundary

The frontend should consume backend APIs and workflow state.

It must not independently implement authoritative SEO business logic.

The frontend may provide:

* visualization
* filtering
* editing
* review
* navigation
* workflow monitoring
* human approval

---

# 85. Frontend and AI Boundary

The frontend must not directly call privileged AI tools using unrestricted credentials.

Preferred:

```text
Frontend
 ↓
Backend
 ↓
Authorization
 ↓
Orchestrator
 ↓
AI / Tools
```

---

# 86. Real-Time Workflow Updates

Long-running workflows should support real-time or near-real-time updates.

Potential technologies:

* Server-Sent Events
* WebSockets
* polling

The choice depends on workflow characteristics.

---

# 87. Cancellation

Users should be able to cancel long-running workflows where safe.

Cancellation must propagate to:

* queued jobs
* workers
* tool calls where supported
* downstream workflow steps

Cancellation must not corrupt persistent state.

---

# 88. Timeouts

Every external dependency should have an explicit timeout.

Examples:

* HTTP request
* LLM request
* SERP query
* crawler request
* database operation
* queue job

No external operation should be allowed to hang indefinitely.

---

# 89. Retry Policy

Retries should be configured by operation.

Examples:

```text
Transient provider timeout → retry
Authentication failure → do not retry
Invalid request → do not retry
Rate limit → retry with backoff
Malformed AI output → controlled retry/revalidation
```

---

# 90. Circuit Breaking

Circuit-breaking may be introduced for unstable external providers.

The goal is to prevent one failing dependency from consuming all system capacity.

This should be added when actual operational need justifies it.

---

# 91. Resource Budgets

Workflows should support budgets for:

* time
* tokens
* provider requests
* crawl pages
* search calls
* database operations where appropriate

Budget exhaustion should produce an explicit state.

---

# 92. Cost Attribution

AI and external-provider costs should be attributable to:

* project
* workflow
* task
* agent
* provider
* model

This allows future product-level cost analysis.

---

# 93. Performance Architecture

Performance optimization should follow evidence.

The preferred sequence:

```text
Measure
 ↓
Identify Bottleneck
 ↓
Optimize
 ↓
Benchmark
 ↓
Verify
```

Premature optimization is discouraged.

---

# 94. Database Performance

Performance considerations include:

* appropriate indexes
* query plans
* pagination
* connection pooling
* batching
* avoiding N+1 queries
* appropriate denormalization where justified

Database optimization must preserve domain integrity.

---

# 95. Retrieval Performance

Vector/search retrieval should use:

* metadata filtering
* appropriate indexes
* bounded result sets
* caching where useful
* hybrid retrieval

Do not retrieve thousands of semantically similar records when a smaller evidence set is sufficient.

---

# 96. AI Performance

AI latency may be reduced through:

* smaller models for simple tasks
* parallel independent calls
* caching
* prompt compression
* context selection
* batching where supported

Quality must not be sacrificed merely to reduce latency.

---

# 97. Security Architecture

The security model should include:

```text
Identity
 ↓
Authentication
 ↓
Authorization
 ↓
Project Isolation
 ↓
Tool Permission
 ↓
Data Access
 ↓
Audit
```

Each layer is independent.

---

# 98. Input Security

Inputs from users, websites, documents, and APIs are untrusted.

The system must protect against:

* injection
* malicious payloads
* oversized requests
* unsafe URLs
* prompt injection
* SSRF where relevant
* malicious files
* unauthorized resource access

---

# 99. AI Security

AI-specific security must include:

* prompt-injection resistance
* output validation
* tool authorization
* data minimization
* model-provider controls
* sensitive-data handling

Security must exist outside the model.

---

# 100. Supply Chain Security

Dependencies and external tools should be reviewed for:

* known vulnerabilities
* licensing
* maintenance
* provenance
* permissions

Lockfiles should be maintained.

---

# 101. CI/CD

The project should eventually automate:

```text
Commit
 ↓
Lint
 ↓
Type Check
 ↓
Unit Tests
 ↓
Integration Tests
 ↓
Security Checks
 ↓
Build
 ↓
Migration Validation
 ↓
Deployment
 ↓
Smoke Tests
```

Production deployment should not depend on undocumented manual steps.

---

# 102. Build Reproducibility

Builds should use:

* pinned/controlled dependencies
* reproducible configuration
* versioned migrations
* versioned prompts
* versioned model configuration where relevant

---

# 103. Feature Flags

Feature flags may control:

* experimental agents
* new models
* new providers
* UI experiments
* staged workflows

Feature flags must not become permanent undocumented architecture.

---

# 104. Technical Debt

Technical debt must be explicit.

A temporary workaround should include:

* reason
* impact
* owner
* follow-up task
* removal condition

Otherwise temporary architecture tends to become permanent architecture.

---

# 105. Migration Strategy

When replacing a component:

```text
Current
  ↓
Compatibility Layer
  ↓
New Implementation
  ↓
Validation
  ↓
Migration
  ↓
Old Implementation Removal
```

Do not perform destructive replacement without a recovery strategy.

---

# 106. Provider Migration

Switching providers should affect primarily:

* provider adapter
* configuration
* integration tests
* capability mapping

It should not require rewriting:

* domain model
* SEO reasoning
* orchestration contracts

---

# 107. Model Migration

A model change must trigger evaluation of:

* output quality
* schema compliance
* latency
* cost
* safety
* regression cases

A new model is not automatically a better model.

---

# 108. AI Runtime Fallbacks

Fallback models/providers may be used when explicitly configured.

Fallback behavior must preserve:

* output contracts
* provenance
* model metadata
* confidence handling
* observability

---

# 109. Technical Documentation

Technical implementation decisions must remain documented.

Documentation should describe:

* architecture
* interfaces
* deployment
* configuration
* operational procedures
* known limitations

Documentation must be updated when technical reality changes materially.

---

# 110. Local Development

Local development should allow developers to run the core system without requiring every external provider.

Recommended local strategy:

```text
PostgreSQL
Redis
Backend
Worker
Frontend
Mock External Providers
```

Optional integrations can be enabled separately.

---

# 111. Mock Providers

Mock providers should implement the same internal interfaces as real providers.

Example:

```text
SearchProvider
├── RealSearchProvider
└── MockSearchProvider
```

Mocks must be clearly identified.

They must never silently execute in production.

---

# 112. Test Fixtures

Fixtures should cover:

* realistic business data
* entities
* EAV
* topics
* keywords
* intents
* SERPs
* pages
* evidence
* decisions
* failures

Fixtures should include ambiguous and adversarial cases.

---

# 113. Contract Testing

Contract tests should verify:

* agent outputs
* provider adapters
* API schemas
* module interfaces
* event payloads

This is especially important when multiple modules depend on the same contract.

---

# 114. Architecture Testing

Where practical, automated checks should enforce:

* dependency direction
* module boundaries
* forbidden imports
* ownership boundaries
* API contracts

Architecture should be enforceable, not merely documented.

---

# 115. Technical Anti-Patterns

Avoid:

* direct LLM calls throughout the codebase
* direct provider calls inside domain logic
* shared mutable global state
* unrestricted database access
* arbitrary cross-module imports
* agent access to all tools
* frontend-owned business logic
* Redis as permanent source of truth
* vector database as authoritative database
* undocumented background jobs
* unbounded AI workflows
* hard-coded secrets
* manual production schema changes

---

# 116. Initial Runtime Architecture

The first implementation should remain operationally simple:

```text
┌──────────────────────────────────────────┐
│                Frontend                  │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│              FastAPI Backend             │
│                                          │
│  API                                     │
│   ↓                                      │
│  Application                             │
│   ↓                                      │
│  Orchestrator                            │
│   ↓                                      │
│  AI / Domain / Knowledge Modules         │
│   ↓                                      │
│  Integration Adapters                    │
└───────────┬─────────────┬────────────────┘
            │             │
            ▼             ▼
      PostgreSQL         Redis
            │
            ▼
       Vector Layer
            │
            ▼
      Object Storage

             +
        Background Workers
```

---

# 117. Future Runtime Architecture

Only when justified:

```text
Frontend
   │
API Gateway
   │
Orchestrator
   │
   ├── Research Service
   ├── Semantic Intelligence
   ├── Search Intelligence
   ├── Decision Intelligence
   └── Content Intelligence
          │
          ▼
      Shared/Domain Data
```

Extraction must follow proven boundaries.

---

# 118. Technical Evolution Criteria

A module becomes a candidate for independent deployment when:

* load differs significantly
* independent scaling is required
* deployment cadence differs
* failure isolation is valuable
* security isolation is required
* ownership becomes independent
* technology requirements differ materially

Architecture should evolve from evidence.

---

# 119. Technical Architecture Decision Principles

When evaluating a technical change, ask:

1. Does it solve a demonstrated problem?
2. Does it simplify or complicate operations?
3. Does it preserve domain boundaries?
4. Does it preserve provider independence?
5. Does it improve testability?
6. Does it improve observability?
7. Does it introduce a new failure mode?
8. Does it increase cost?
9. Does it require migration?
10. Is the change reversible?
11. Does it require human approval?
12. Which documents must change?

---

# 120. Technical Definition of Done

A technical component is complete only when applicable:

* implementation exists
* interfaces are defined
* validation exists
* tests pass
* error handling exists
* observability exists
* security is addressed
* documentation is updated
* deployment behavior is known
* external dependencies are verified or explicitly marked unverified

---

# 121. Relationship to Other Documents

This document provides the technical foundation for:

* `08_SEO_KNOWLEDGE_MODEL.md`
* `09_ENTITY_EAV_MODEL.md`
* `10_TOPIC_MODELING_AND_CLUSTERING.md`
* `11_SEARCH_AND_SERP_INTELLIGENCE.md`
* `12_SEO_DECISION_ENGINE.md`
* `13_AGENT_SPECIFICATIONS.md`
* `14_AGENT_WORKFLOW.md`
* `16_OUTPUT_CONTRACTS.md`
* `17_UI_UX_SPECIFICATION.md`
* `18_FRONTEND_ARCHITECTURE.md`
* `19_DESIGN_SYSTEM.md`
* `20_PROJECT_STRUCTURE.md`
* `21_DEVELOPMENT_AND_DEBUG.md`
* `22_TESTING_AND_VALIDATION.md`
* `23_PROJECT_CONTROL_CENTER.md`
* `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md`
* `25_CONTEXT_MANAGEMENT.md`
* `26_SKILLS_AND_TOOLING_POLICY.md`

---

# 122. Final Technical Architecture Principles

The technical system must remain:

### Modular

Capabilities have explicit boundaries.

### Observable

Important execution is traceable.

### Testable

Modules can be validated independently.

### Persistent

Important state survives process failure.

### Provider-independent

External vendors remain behind adapters.

### AI-safe

Model outputs are validated before trust.

### Evidence-driven

Important decisions retain provenance.

### Human-controlled

High-impact decisions remain governed.

### Operationally simple

Complexity is introduced only when justified.

### Evolution-ready

Clear boundaries make future extraction possible.

---

# 123. Final Status

```yaml
document: 07_TECHNICAL_ARCHITECTURE.md
status: APPROVED_AS_BASELINE_TECHNICAL_ARCHITECTURE

backend:
  language: Python
  framework: FastAPI

primary_database:
  PostgreSQL: true

semantic_retrieval:
  vector_layer: required
  implementation: pgvector_or_Qdrant

cache:
  Redis: true

ai:
  provider_abstraction: required
  structured_outputs: required
  prompt_versioning: required
  model_versioning: required_where_applicable

architecture:
  deployment_default: modular_monolith
  workers: asynchronous
  provider_adapters: required
  domain_infrastructure_separation: required

security:
  authentication: required
  authorization: required
  project_isolation: required
  secret_management: required
  tool_permissions: required

observability:
  structured_logs: required
  metrics: required
  tracing: required
  audit_events: required_where_applicable

reliability:
  timeouts: required
  retry_policy: required
  idempotency: required_where_applicable
  workflow_persistence: required
  recovery: required_where_applicable

testing:
  unit: required_where_applicable
  integration: required
  contract: required_where_applicable
  workflow: required
  regression: required_for_material_changes

future:
  independent_services: conditional
  microservices: not_default
  provider_migration: supported
  model_migration: supported
```

---

# 124. Final Principle

> **The technical architecture must make the intelligent system easier to control, verify, evolve, and trust—not merely easier to build.**
