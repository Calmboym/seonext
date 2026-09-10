# 04_SYSTEM_ARCHITECTURE.md

# System Architecture

## 1. Document Purpose

This document defines the system-level architecture of the **SEO Research & Strategy Copilot**.

It establishes:

* The major architectural layers
* Core system components
* Component responsibilities
* System boundaries
* Data flow
* AI orchestration
* Knowledge management
* External integrations
* Persistence boundaries
* Human interaction boundaries
* Execution boundaries
* Reliability boundaries
* Security boundaries
* Extensibility principles
* Deployment direction

This document intentionally operates above implementation details.

It defines **how the system is organized**, not the exact code structure of every module.

Detailed responsibilities of individual AI agents belong to:

`05_AI_AGENT_ARCHITECTURE.md`

Detailed data modeling belongs to:

`06_DATA_ARCHITECTURE.md`

Detailed technology decisions belong to:

`07_TECHNICAL_ARCHITECTURE.md`

---

# 2. Architectural Objective

The system must transform heterogeneous SEO and business information into structured, explainable, actionable SEO decisions.

The fundamental architecture is:

```text
Business Context
+
Website Context
+
Search Data
+
Semantic Knowledge
+
Historical Decisions
+
AI Reasoning
+
Human Judgment
        ↓
SEO Intelligence
        ↓
SEO Decisions
```

The architecture must therefore support both:

```text
Information Processing
```

and:

```text
Decision Support
```

The system is not merely a data pipeline.

It is an intelligent decision-support platform.

---

# 3. Core Architectural Model

The preferred system architecture is:

```text
                         USER
                          │
                          ↓
                  PRESENTATION LAYER
                          │
                          ↓
                  APPLICATION LAYER
                          │
                          ↓
                    ORCHESTRATOR
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
      AI MODULES       DOMAIN LOGIC     WORKFLOWS
          │               │               │
          └───────────────┼───────────────┘
                          ↓
                    KNOWLEDGE LAYER
                          │
          ┌───────────────┼───────────────┐
          ↓               ↓               ↓
      STRUCTURED       SEMANTIC        EVIDENCE
        DATA            DATA             DATA
          │               │               │
          └───────────────┼───────────────┘
                          ↓
                   INTEGRATION LAYER
                          │
       ┌──────────────────┼──────────────────┐
       ↓                  ↓                  ↓
   SEARCH APIs        WEB/CRAWLER       LLM PROVIDERS
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ↓
                    EXTERNAL WORLD
```

This is the conceptual architecture.

The exact technology used to implement each layer is defined separately.

---

# 4. Architectural Principles

The system architecture must follow these principles.

## 4.1 Modularity

Major capabilities must be independently understandable and replaceable.

---

## 4.2 Separation of Concerns

Presentation, application orchestration, domain logic, AI reasoning, persistence, and external integrations must remain clearly separated.

---

## 4.3 Explicit Boundaries

Every major module must have a defined responsibility and interface.

---

## 4.4 Evidence Preservation

External observations and derived intelligence must remain distinguishable.

---

## 4.5 Human Control

High-impact strategic decisions must remain subject to appropriate human authorization.

---

## 4.6 Provider Independence

LLM, search, crawling, embedding, and other external providers should remain replaceable where practical.

---

## 4.7 Testability

Architectural boundaries must allow components to be tested independently.

---

## 4.8 Observability

Important workflows must be traceable across layers.

---

## 4.9 Progressive Autonomy

The architecture must allow increasing automation without requiring a complete redesign.

---

## 4.10 Simplicity

The architecture should use the minimum complexity necessary to satisfy actual requirements.

---

# 5. System Boundary

The system consists of several logical areas.

## Inside the Core System

```text
Project Management
Business Knowledge
Entity Model
EAV Model
Topic Model
Intent Model
Search Intelligence
SERP Analysis
Clustering
Page Architecture
Internal Linking
Content Gap Analysis
Cannibalization Analysis
SEO Decision Engine
Human Review
Decision History
AI Orchestration
```

## Outside the Core System

Potential external systems include:

```text
LLM Providers
Search Providers
SERP Providers
SEO Data Providers
Websites
Crawlers
Analytics Platforms
Search Engines
Third-Party APIs
Future Integrations
```

The integration layer isolates the core system from these external dependencies.

---

# 6. Architectural Layers

The system is conceptually divided into the following layers:

```text
1. Presentation Layer
2. API / Application Layer
3. Orchestration Layer
4. Intelligence Layer
5. Domain Layer
6. Knowledge Layer
7. Integration Layer
8. Infrastructure Layer
```

These are logical boundaries.

They do not necessarily imply separate deployable services.

---

# 7. Presentation Layer

The Presentation Layer is responsible for user interaction.

It includes:

* Dashboard
* Research Workspace
* Entity Views
* Topic Views
* Intent Views
* SERP Views
* Topic Maps
* Page Architecture Views
* Internal Linking Views
* Content Gap Views
* Cannibalization Views
* Decision Review
* Project State
* Reports

The Presentation Layer must not own core SEO logic.

---

# 8. Presentation Layer Responsibilities

The Presentation Layer may:

* Display data
* Collect user input
* Display recommendations
* Display evidence
* Display confidence
* Request actions
* Submit approvals
* Submit modifications
* Display errors
* Display workflow state

It must not independently determine strategic SEO truth.

---

# 9. API / Application Layer

The Application Layer exposes use cases to the frontend and other authorized consumers.

Examples:

```text
Create Project
Get Project
Start Research
Run Topic Discovery
Analyze SERP
Generate Topic Clusters
Review Recommendation
Approve Decision
Reject Decision
Update Entity
Refresh Search Data
Get Page Architecture
Get Content Gaps
```

The Application Layer translates external requests into application operations.

---

# 10. API Layer Must Remain Thin

API handlers should not contain complex domain reasoning.

Avoid:

```text
HTTP Request
↓
500 lines of SEO logic
```

Prefer:

```text
HTTP Request
↓
Application Service
↓
Domain / Intelligence
↓
Result
```

The API layer should primarily handle:

* Request validation
* Authentication
* Authorization
* Routing
* Response serialization
* Error mapping

---

# 11. Orchestration Layer

The Orchestration Layer coordinates complex workflows.

The central component is the:

> **SEO Orchestrator**

Its responsibility is to coordinate capabilities, not perform every specialized reasoning task itself.

Conceptually:

```text
User Goal
↓
Orchestrator
↓
Determine Required Steps
↓
Retrieve Required Context
↓
Execute Modules
↓
Validate Outputs
↓
Persist Results
↓
Generate Decision State
↓
Return Result
```

---

# 12. Orchestrator Responsibilities

The Orchestrator may:

* Interpret the requested workflow
* Determine required modules
* Resolve dependencies
* Retrieve context
* Select tools
* Execute AI modules
* Execute deterministic services
* Manage retries
* Validate outputs
* Handle failures
* Persist state
* Trigger human review
* Resume workflows
* Produce workflow status

It must not become an unbounded "God Object."

---

# 13. Orchestrator Does Not Own Domain Truth

The Orchestrator coordinates.

It should not become the permanent owner of:

* Entity logic
* Topic logic
* Intent logic
* Clustering logic
* Page architecture logic
* Search interpretation logic

Those responsibilities belong to their appropriate domain or intelligence modules.

---

# 14. Workflow Execution Model

A workflow should conceptually follow:

```text
REQUEST
  ↓
PLAN
  ↓
CONTEXT RETRIEVAL
  ↓
DATA COLLECTION
  ↓
ANALYSIS
  ↓
VALIDATION
  ↓
DECISION
  ↓
HUMAN REVIEW
  ↓
PERSISTENCE
  ↓
OUTPUT
```

Not every workflow requires every step.

The Orchestrator should construct the appropriate execution path.

---

# 15. Intelligence Layer

The Intelligence Layer contains AI-powered and algorithmic reasoning capabilities.

Examples:

```text
Business Research
Entity Extraction
Entity Resolution
EAV Extraction
Topic Discovery
Topic Validation
Intent Classification
SERP Analysis
Topic Clustering
Page Candidate Analysis
Page Architecture
Internal Linking Analysis
Content Gap Analysis
Cannibalization Detection
Opportunity Scoring
SEO Decision Analysis
```

These modules consume structured context and evidence.

---

# 16. Intelligence Modules

Intelligence modules should be:

* Focused
* Bounded
* Testable
* Schema-driven
* Observable
* Replaceable

Each module should define:

```text
Input
Output
Dependencies
Tools
Rules
Validation
Failure Modes
Confidence
```

Detailed specifications belong in:

`13_AGENT_SPECIFICATIONS.md`

---

# 17. AI and Deterministic Logic

The system should use a hybrid architecture.

```text
                    INTELLIGENCE
                         │
             ┌───────────┴───────────┐
             ↓                       ↓
        DETERMINISTIC              AI
          LOGIC                  REASONING
             │                       │
             └───────────┬───────────┘
                         ↓
                    VALIDATION
```

Use deterministic logic for:

* Schema validation
* Arithmetic
* Filtering
* Sorting
* Rule enforcement
* State transitions
* Referential integrity
* Exact comparisons

Use AI for:

* Semantic interpretation
* Classification
* Ambiguous relationships
* Qualitative analysis
* Reasoning over heterogeneous evidence
* Recommendation generation

---

# 18. Domain Layer

The Domain Layer represents the core concepts and business rules of the product.

Core domain concepts include:

```text
Project
Business
Entity
Attribute
Value
Relationship
Topic
Keyword
Intent
SERP
Page
Content
Link
Competitor
Opportunity
Recommendation
Decision
Evidence
```

The Domain Layer should not depend directly on:

* UI frameworks
* HTTP
* Specific LLM providers
* Specific search APIs
* Database implementation details

---

# 19. Domain Rules

Domain rules should define:

* Valid relationships
* Valid state transitions
* Business constraints
* SEO conceptual constraints
* Decision rules
* Data integrity rules

Examples:

```text
Keyword ≠ Topic
Topic ≠ Page
Recommendation ≠ Decision
Decision ≠ Execution
Evidence ≠ Interpretation
```

---

# 20. Knowledge Layer

The Knowledge Layer is the persistent intelligence foundation of the system.

It stores and exposes:

```text
Business Knowledge
Entity Knowledge
EAV
Topics
Keywords
Intents
SERPs
Pages
Content
Relationships
Evidence
Recommendations
Decisions
Historical State
```

The Knowledge Layer is not merely a database abstraction.

It is the persistent state of the SEO intelligence system.

---

# 21. Structured Knowledge

Structured knowledge should represent explicit relationships.

Examples:

```text
Entity → hasAttribute → Attribute
Entity → relatedTo → Entity
Topic → relatedTo → Topic
Topic → associatedWith → Entity
Keyword → represents → Topic
Page → targets → Topic
Page → serves → Intent
Page → linksTo → Page
Decision → concerns → Topic
Evidence → supports → Recommendation
```

The exact schema is defined in:

`06_DATA_ARCHITECTURE.md`

and:

`09_ENTITY_EAV_MODEL.md`

---

# 22. Semantic Knowledge

The system may also maintain semantic representations such as:

* Embeddings
* Semantic similarity
* Vector indexes
* Retrieval representations
* Topic representations
* Entity representations

However:

> Semantic retrieval must not replace structured domain knowledge.

The system should use:

```text
Structured Knowledge
+
Semantic Retrieval
```

rather than relying exclusively on embeddings.

---

# 23. Evidence Layer

Evidence should be treated as a first-class architectural concept.

Evidence may originate from:

```text
Business Input
Website
Crawler
Search API
SERP API
SEO Data Provider
Analytics
Human Decision
Historical System State
```

Evidence should retain provenance wherever practical.

---

# 24. Evidence Pipeline

The preferred evidence flow is:

```text
External Source
↓
Raw Evidence
↓
Normalization
↓
Validation
↓
Structured Observation
↓
AI Interpretation
↓
Recommendation
↓
Human Decision
```

Each stage should remain conceptually distinguishable.

---

# 25. Raw Evidence vs Derived Knowledge

The system should distinguish:

```text
RAW
OBSERVED
DERIVED
INFERRED
RECOMMENDED
APPROVED
```

Example:

```text
Raw SERP Response
↓
Observed SERP Features
↓
Detected Search Intent
↓
Recommended Page Type
↓
Human Approved Page Strategy
```

This separation is essential for auditing.

---

# 26. Integration Layer

The Integration Layer isolates external systems.

Potential integrations include:

```text
LLM
Search
SERP
SEO Metrics
Website Crawling
Analytics
Keyword Data
Trend Data
Future External APIs
```

Each provider should ideally implement a stable internal interface.

---

# 27. Provider Adapter Pattern

Conceptually:

```text
Core System
     ↓
Internal Provider Interface
     ↓
Adapter
     ↓
External Provider
```

Example:

```text
SERPService
    ↓
SERPProvider Interface
    ↓
GoogleSERPAdapter
```

The core system should not depend directly on provider-specific response formats.

---

# 28. External Provider Failure

External integrations are inherently unreliable.

Possible failures include:

```text
Timeout
Rate Limit
Authentication Failure
Invalid Response
Partial Response
Service Unavailable
Malformed Data
Quota Exhaustion
```

The system must explicitly model these failures.

---

# 29. No Fake External Data

If an external provider fails, the system must never substitute fabricated equivalent data.

Valid outcomes include:

```text
Provider Failed
Partial Data
Stale Data
Insufficient Data
Retry Required
Human Review Required
```

Never:

```text
Provider Failed
↓
AI Invents Missing SERP
```

---

# 30. Integration Isolation

External API calls should not leak provider-specific details throughout the application.

Bad:

```text
Domain Logic
↓
Specific Provider SDK
```

Preferred:

```text
Domain/Application
↓
Internal Interface
↓
Provider Adapter
↓
SDK/API
```

---

# 31. Infrastructure Layer

The Infrastructure Layer provides technical capabilities such as:

* Database
* Cache
* Queues
* Object storage
* Vector storage
* Logging
* Metrics
* Configuration
* Secrets
* Scheduling
* Background execution

Infrastructure should support the domain rather than define it.

---

# 32. Persistence Architecture

Persistent state should be divided conceptually into:

```text
Authoritative Structured State
+
Semantic Indexes
+
Cached State
+
Raw Evidence
+
Operational State
```

Each category has different lifecycle requirements.

---

# 33. Authoritative State

Authoritative state includes information that the system treats as canonical.

Examples:

```text
Projects
Entities
Topics
Pages
Decisions
Human Approvals
Relationships
```

This state must have strong integrity guarantees.

---

# 34. Semantic Indexes

Semantic indexes may contain:

```text
Embeddings
Vector Representations
Semantic Search Metadata
```

They are derived representations.

If necessary, they should be rebuildable from authoritative data.

---

# 35. Cache

Cache exists to improve:

* Performance
* Cost
* Latency

Cache must not become the authoritative source for critical domain state.

---

# 36. Raw Evidence Storage

Raw evidence may include:

* Search responses
* SERP snapshots
* Crawled pages
* API responses
* Source metadata

Where practical, raw evidence should be retained long enough to support:

* Auditing
* Reprocessing
* Debugging
* Historical comparison

---

# 37. Workflow State

Long-running AI workflows may require persistent workflow state.

Conceptually:

```text
Workflow
↓
Pending
↓
Running
↓
Waiting For Review
↓
Approved
↓
Continuing
↓
Completed
```

Failure states must also be explicit.

---

# 38. Asynchronous Work

Long-running operations should not unnecessarily block user requests.

Potential asynchronous operations include:

* Large website crawls
* SERP collection
* Bulk keyword processing
* Large-scale clustering
* Embedding generation
* Deep analysis
* Report generation

The architecture should support background execution.

---

# 39. Synchronous Work

Fast operations may remain synchronous.

Examples:

* Reading project state
* Reading an entity
* Loading a topic
* Approving a recommendation
* Updating simple metadata

The distinction should be based on actual latency and workload characteristics.

---

# 40. Event-Driven Extensions

The architecture should leave room for event-driven workflows.

Examples:

```text
EntityUpdated
TopicApproved
SERPRefreshed
PageCreated
DecisionRejected
ProjectStateChanged
```

Events may trigger downstream processing.

However, event-driven architecture should not be introduced where direct synchronous orchestration is simpler.

---

# 41. Human Interaction Boundary

Human review is a formal system boundary.

The system must be able to pause:

```text
AI Workflow
↓
Human Review
↓
Decision
↓
Resume Workflow
```

Human decisions should return to the knowledge layer.

---

# 42. Human Review States

Recommended conceptual states:

```text
NOT_REVIEWED
IN_REVIEW
APPROVED
REJECTED
MODIFIED
DEFERRED
SUPERSEDED
```

These states should be explicit.

---

# 43. Decision Lifecycle

A strategic recommendation should follow a lifecycle such as:

```text
Generated
↓
Validated
↓
Presented
↓
Reviewed
├── Approved
├── Modified
├── Rejected
└── Deferred
```

A recommendation must not silently become an approved decision.

---

# 44. Context Retrieval Architecture

AI modules should not receive the entire project by default.

Instead:

```text
Task
↓
Determine Required Context
↓
Retrieve Relevant Knowledge
↓
Retrieve Required Evidence
↓
Build Working Context
↓
Execute AI Module
```

This protects:

* Token budget
* Latency
* Cost
* Relevance
* Reliability

---

# 45. Context Sources

Relevant context may come from:

```text
Project State
Business Profile
Entity Graph
Topic Graph
Existing Pages
Historical Decisions
Evidence Store
Search Data
Previous Workflow Results
User Input
```

Context selection should be task-specific.

---

# 46. Context Priority

When context is limited, prioritize:

```text
Current Task Requirements
↓
Relevant Canonical Knowledge
↓
Recent Evidence
↓
Relevant Historical Decisions
↓
Supporting Context
↓
Low-Relevance Background
```

Irrelevant context should not be loaded merely because it exists.

---

# 47. AI Execution Boundary

The system should isolate AI execution from the rest of the application.

Conceptually:

```text
Application
↓
AI Task Definition
↓
Context Builder
↓
LLM / AI Module
↓
Structured Output
↓
Validator
↓
Application
```

The AI should not directly mutate arbitrary persistent state.

---

# 48. AI Output Safety Boundary

AI output should pass through validation before becoming authoritative state.

```text
AI Output
↓
Schema Validation
↓
Semantic / Domain Validation
↓
Business Rules
↓
Persistence
```

Invalid outputs must be rejected or repaired through controlled mechanisms.

---

# 49. AI Does Not Get Direct Database Authority

AI modules should not be allowed to arbitrarily execute database mutations.

Prefer:

```text
AI
↓
Structured Proposal
↓
Application / Domain Validation
↓
Authorized Mutation
```

This creates a clear control boundary.

---

# 50. Tool Execution Boundary

AI may require tools such as:

* Search
* Crawling
* Database retrieval
* Semantic search
* External APIs

Tool calls should pass through controlled interfaces.

The system should know:

```text
Which Tool
Why
Input
Output
Permission
Result
Failure
```

---

# 51. Tool Permissions

Tools should have explicit permission boundaries.

For example:

```text
Read-only Search Tool
```

should not automatically have:

```text
Write Database Permission
```

A tool's capabilities should match its required purpose.

---

# 52. Skill Installation Boundary

The architecture may support dynamic skill installation when permitted by project policy.

The installation flow should be:

```text
Capability Required
↓
Capability Discovery
↓
Suitability Check
↓
Permission Check
↓
Installation
↓
Validation
↓
Registration
↓
Usage
```

Installed skills should not automatically gain unrestricted system access.

---

# 53. Security Architecture

Security must exist across all layers.

Conceptually:

```text
Identity
↓
Authentication
↓
Authorization
↓
Capability Permissions
↓
Data Access
↓
Tool Access
↓
Audit
```

No layer should assume that another layer has already enforced every security requirement.

---

# 54. Authentication

Authentication establishes who is interacting with the system.

It does not determine what that user can do.

---

# 55. Authorization

Authorization must control access to:

* Projects
* Data
* Decisions
* Administrative functions
* Tools
* Integrations
* Sensitive operations

---

# 56. Data Isolation

Project data must remain isolated according to authorization boundaries.

One project must not accidentally retrieve another project's:

* Entities
* Topics
* Pages
* Evidence
* Decisions
* Credentials

---

# 57. AI Data Isolation

AI context retrieval must respect the same authorization boundaries as ordinary application access.

The fact that information is being sent to an LLM does not bypass project isolation.

---

# 58. External Data Security

External content should be treated as untrusted.

The system must protect against:

* Prompt injection
* Malicious content
* Unexpected payloads
* Oversized inputs
* Malformed responses
* Data exfiltration attempts

---

# 59. Observability Architecture

The system should produce structured operational information.

Important events should be traceable through:

```text
Request ID
↓
Workflow ID
↓
Task ID
↓
Module / Agent
↓
Tool Calls
↓
Evidence
↓
Output
↓
Validation
↓
Persistence
```

This enables debugging and auditing.

---

# 60. Logging

Logs should help answer:

```text
What happened?
When?
Where?
Why?
Which component?
Which workflow?
Which external dependency?
What failed?
```

Logs must not expose secrets or unnecessary sensitive data.

---

# 61. Metrics

Useful system metrics may include:

```text
Workflow Duration
LLM Latency
LLM Token Usage
Tool Latency
API Error Rate
Validation Failure Rate
Retry Rate
Workflow Failure Rate
Human Review Rate
Cache Hit Rate
```

Metrics should serve operational decisions rather than become vanity dashboards.

---

# 62. Tracing

Distributed tracing may become useful as the system grows.

However, tracing complexity should remain proportional to actual architecture.

Do not introduce distributed tracing infrastructure merely because it is fashionable.

---

# 63. Error Architecture

Errors should have explicit categories.

```text
ValidationError
DomainError
AuthorizationError
AuthenticationError
ProviderError
ToolError
AIOutputError
DataError
ConfigurationError
InfrastructureError
WorkflowError
```

Errors should preserve enough context for diagnosis.

---

# 64. Error Propagation

Errors should be translated at appropriate architectural boundaries.

For example:

```text
Provider Exception
↓
Provider Adapter Error
↓
Application Error
↓
API Error
↓
User-Friendly Message
```

Raw provider exceptions should not leak directly into the UI.

---

# 65. Retry Architecture

Retryable operations should define:

```text
Retryable?
Maximum Attempts
Backoff
Timeout
Idempotency
Fallback
Final Failure State
```

Not every error should be retried.

---

# 66. Idempotency

Operations that may execute more than once should be designed to prevent unintended duplicate effects.

This is especially important for:

* Background jobs
* External API mutations
* Data imports
* Persistence
* Workflow resumption

---

# 67. Failure Isolation

Failure in one external provider should not unnecessarily corrupt unrelated system state.

For example:

```text
SERP Provider Failure
```

should not invalidate:

```text
Existing Entity Model
```

or:

```text
Existing Human Decisions
```

---

# 68. Graceful Degradation

When possible, the system should degrade gracefully.

Examples:

```text
Search Provider Down
↓
Use Existing Cached Evidence
↓
Mark Data As Stale
```

rather than:

```text
Search Provider Down
↓
Pretend Current Data Exists
```

---

# 69. Architecture for Reprocessing

The system should support reprocessing where practical.

For example:

```text
Raw SERP Data
↓
New Intent Classifier
↓
Recompute Intent
↓
Recompute Clustering
```

This is easier when raw evidence and derived state remain separate.

---

# 70. Versioned Intelligence

AI modules may evolve.

The architecture should allow important outputs to be associated with:

```text
Model
Prompt Version
Module Version
Configuration
Input Snapshot
```

This supports reproducibility and debugging.

---

# 71. Model Routing

The system may eventually select different models based on task requirements.

Conceptually:

```text
Task
↓
Complexity
↓
Required Capability
↓
Model Selection
```

Possible factors:

* Reasoning complexity
* Latency
* Cost
* Context size
* Structured output capability
* Reliability

Model routing must remain behind an abstraction.

---

# 72. Cost Control Architecture

The system should support:

```text
Caching
Batching
Model Selection
Context Reduction
Deduplication
Request Reuse
```

Cost optimization must not compromise strategic correctness.

---

# 73. Concurrency

Independent tasks may execute concurrently.

Dependent tasks must preserve dependency order.

The Orchestrator should understand workflow dependencies before parallel execution.

---

# 74. Dependency Graph

A workflow should be represented conceptually as a directed graph.

Example:

```text
Business Research
       ↓
Entity Model
       ↓
EAV
       ↓
Topic Discovery
       ↓
Topic Validation
       ↓
Intent
       ↓
SERP
       ↓
Clustering
       ↓
Page Architecture
       ↓
Internal Linking
```

Some branches may execute independently.

For example:

```text
                 Entity Model
                      │
             ┌────────┴────────┐
             ↓                 ↓
       Topic Discovery     Competitor Research
             │                 │
             └────────┬────────┘
                      ↓
                  Analysis
```

The actual dependency graph must be derived from the detailed module specifications.

---

# 75. System State Machine

The project itself should maintain explicit state.

Conceptually:

```text
INITIALIZED
    ↓
RESEARCHING
    ↓
MODELING
    ↓
ANALYZING
    ↓
RECOMMENDING
    ↓
AWAITING_REVIEW
    ↓
APPROVED
    ↓
EXECUTING
    ↓
MEASURING
    ↓
LEARNING
    ↓
UPDATED
```

Not every project must follow this exact linear sequence.

The state machine is conceptual.

---

# 76. Architecture Must Support Iteration

SEO research is not necessarily linear.

New evidence may require revisiting earlier assumptions.

For example:

```text
New SERP Evidence
↓
Intent Changes
↓
Topic Cluster Changes
↓
Page Architecture Changes
```

Therefore the architecture must support controlled recomputation.

---

# 77. No Destructive Recalculation

Recomputing derived intelligence should not automatically destroy valuable historical state.

Prefer:

```text
Previous Result
+
New Result
+
Version / Timestamp
```

where historical comparison matters.

---

# 78. Source of Truth Hierarchy

Different information categories may have different authoritative sources.

For example:

```text
User-Approved Business Information
        ↓
Authoritative Project Knowledge

Raw Search Data
        ↓
Evidence Source

Derived Topic Classification
        ↓
AI / Domain Derived State

Human Decision
        ↓
Authoritative Strategic Decision
```

The architecture must define which layer is authoritative for each class of information.

---

# 79. Code vs Documentation

The architecture documentation describes intended system architecture.

The actual implementation and infrastructure definitions establish the deployed reality.

When architecture documentation and implementation diverge, the discrepancy must be resolved rather than ignored.

The project should prefer mechanisms that reduce documentation drift, including generated diagrams or machine-readable contracts where practical.

---

# 80. Architectural Views

The system should be understood through multiple architectural views.

At minimum:

```text
Context View
Container / System View
Component View
Data View
Workflow View
Deployment View
Security View
```

Different views answer different questions.

A single diagram should not be expected to explain the entire architecture.

---

# 81. Context View

The Context View answers:

> What systems and actors interact with the SEO platform?

Conceptually:

```text
                         USER
                          │
                          ↓
                SEO INTELLIGENCE SYSTEM
                  /       |       \
                 /        |        \
                ↓         ↓         ↓
             SEARCH     WEBSITE    LLM
             PROVIDERS  / CRAWLER  PROVIDERS
                │         │         │
                └─────────┼─────────┘
                          ↓
                    EXTERNAL DATA
```

---

# 82. Container View

The major logical containers are:

```text
Web Application
API
Workflow / Orchestrator
AI Intelligence Modules
Domain Services
Knowledge Store
Evidence Store
Semantic Index
Cache
Integration Adapters
Background Workers
Observability
```

These may be deployed together or separately depending on scale.

---

# 83. Component View

Within the Intelligence Layer, components may include:

```text
Business Research
Entity Intelligence
EAV Intelligence
Topic Intelligence
Intent Intelligence
SERP Intelligence
Clustering Intelligence
Page Intelligence
Link Intelligence
Gap Intelligence
Cannibalization Intelligence
Decision Intelligence
```

Detailed component boundaries are defined elsewhere.

---

# 84. Data View

The data architecture should conceptually connect:

```text
Business
↓
Entities
↓
Relationships
↓
Attributes
↓
Topics
↓
Keywords
↓
Intents
↓
SERPs
↓
Pages
↓
Links
↓
Decisions
```

Evidence and provenance cross-cut these objects.

---

# 85. Workflow View

A typical strategic workflow may look like:

```text
User Defines Business
        ↓
Business Research
        ↓
Entity Modeling
        ↓
EAV Modeling
        ↓
Topic Discovery
        ↓
Topic Validation
        ↓
Intent Analysis
        ↓
SERP Research
        ↓
Topic Clustering
        ↓
Page Candidate Analysis
        ↓
Page Architecture
        ↓
Internal Linking
        ↓
Human Review
        ↓
Approved SEO Strategy
```

This is a representative workflow, not a rigid universal pipeline.

---

# 86. Deployment View

The initial system should favor a simple deployment architecture.

Conceptually:

```text
                   USER
                    │
                    ↓
              WEB APPLICATION
                    │
                    ↓
                  API
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
   ORCHESTRATOR  DOMAIN      WORKERS
        │           │           │
        └───────────┼───────────┘
                    ↓
               DATA LAYER
          ┌─────────┼─────────┐
          ↓         ↓         ↓
       SQL DB     VECTOR     CACHE
                    │
                    ↓
              EXTERNAL APIS
```

This does not require microservices.

---

# 87. Modular Monolith as Default

Unless actual requirements justify distributed deployment, the preferred initial architecture is a **modular monolith**.

This provides:

* Clear boundaries
* Lower operational complexity
* Easier local development
* Easier debugging
* Shared transactions where useful
* Simpler deployment

Modules should be designed so that future extraction remains possible if justified.

---

# 88. When to Extract a Service

A module should not become a separate service merely because it is conceptually independent.

Extraction may become justified by:

* Independent scaling requirements
* Independent deployment requirements
* Strong fault isolation requirements
* Infrastructure constraints
* Security isolation
* Clear ownership boundaries
* Measured performance requirements

---

# 89. No Microservice-by-Default Architecture

The project must avoid:

```text
10 Agents
↓
10 Microservices
↓
10 Databases
↓
20 Queues
```

unless real requirements justify that complexity.

Agent modularity and deployment modularity are separate decisions.

---

# 90. Future Distributed Architecture

If scale eventually requires distributed deployment, the conceptual architecture should support:

```text
API Service
Workflow Service
Research Workers
AI Workers
Search Workers
Data Services
Knowledge Services
```

However, this is a future evolution, not an MVP requirement.

---

# 91. Background Worker Architecture

Background workers may execute expensive or asynchronous operations.

Examples:

```text
Crawler Worker
SERP Worker
Embedding Worker
Clustering Worker
Analysis Worker
Report Worker
```

Workers should consume explicit jobs rather than arbitrary shared state.

---

# 92. Queue Semantics

If queues are introduced, jobs should define:

```text
Job ID
Type
Payload
Priority
Status
Attempt
Created At
Started At
Completed At
Error
```

Long-running jobs should be observable.

---

# 93. Job Idempotency

A retried job must not accidentally:

```text
Duplicate Entities
Duplicate Topics
Duplicate Decisions
Duplicate External Mutations
```

Idempotency keys or equivalent mechanisms should be used where required.

---

# 94. Data Consistency

The system should distinguish:

```text
Strongly Consistent State
```

from:

```text
Eventually Consistent Derived State
```

For example:

```text
Human Approval
→ Strong authoritative state
```

while:

```text
Vector Index
→ Rebuildable derived state
```

---

# 95. Transaction Boundaries

Operations that require atomic state changes should use appropriate transactional boundaries.

Examples:

```text
Human Approval
+
Decision Status Update
+
Audit Record
```

should not leave the system in a half-updated state.

---

# 96. Cache Invalidation

Cached information should have explicit freshness rules.

The system should be able to identify:

```text
Fresh
Stale
Expired
Unavailable
```

A stale cache should not masquerade as current external evidence.

---

# 97. Configuration Architecture

Configuration should be separated from application logic.

Configuration may include:

```text
Provider Selection
Model Selection
Timeouts
Thresholds
Feature Flags
Environment Settings
```

Secrets must be managed separately from ordinary configuration.

---

# 98. Feature Flags

Feature flags may be used for:

* Experimental AI modules
* Gradual rollout
* Provider migration
* UI experiments
* Risk-controlled automation

Feature flags should not become a substitute for proper architecture.

---

# 99. Extensibility

The architecture should allow adding:

```text
New LLM
New Search Provider
New SERP Provider
New SEO Data Provider
New AI Module
New Tool
New Visualization
New Analysis Method
```

without requiring a rewrite of unrelated core systems.

---

# 100. Plugin-Like Intelligence Modules

Future intelligence modules should ideally register through defined interfaces.

Conceptually:

```text
Module Registry
    │
    ├── Intent Module
    ├── SERP Module
    ├── Clustering Module
    ├── Gap Module
    └── Future Module
```

Registration should include capability metadata.

---

# 101. Capability Metadata

An intelligence capability may define:

```text
Name
Version
Purpose
Inputs
Outputs
Required Tools
Required Context
Permissions
Cost Profile
Latency Profile
Validation
```

This supports intelligent orchestration.

---

# 102. Architecture and Context Management

Context management must be treated as an architectural concern.

The system should not rely on increasingly large prompts.

Instead:

```text
Persistent Knowledge
↓
Context Retrieval
↓
Task-Specific Context
↓
AI Execution
```

The detailed policy is defined in:

`25_CONTEXT_MANAGEMENT.md`

---

# 103. Architecture and Skills

Skills and tools are external capabilities connected to the architecture through controlled integration boundaries.

The system should support:

```text
Capability Discovery
↓
Permission
↓
Installation
↓
Validation
↓
Registration
↓
Execution
```

Detailed policy belongs to:

`26_SKILLS_AND_TOOLING_POLICY.md`

---

# 104. Architecture and Testing

Every major architectural boundary should be testable.

Testing should occur at multiple levels:

```text
Unit
Integration
Contract
Workflow
Data
AI Module
API
E2E
Regression
```

Detailed testing strategy belongs to:

`22_TESTING_AND_VALIDATION.md`

---

# 105. Architecture and Debugging

The architecture must make failures traceable across boundaries.

A useful diagnostic path is:

```text
User Request
↓
Workflow
↓
Module
↓
Context
↓
Tool
↓
External Provider
↓
Output
↓
Validation
↓
Persistence
```

The system should make it possible to determine where the failure occurred.

---

# 106. Architecture Decision Records

Material architectural decisions should be recorded.

Examples:

```text
Why modular monolith?
Why central orchestrator?
Why structured knowledge?
Why vector search?
Why a particular search provider?
Why a particular LLM abstraction?
Why asynchronous workers?
```

The exact ADR mechanism may be established by project governance.

---

# 107. Architecture Evolution

Architecture must evolve based on evidence.

The preferred process is:

```text
Observe Problem
↓
Collect Evidence
↓
Identify Constraint
↓
Evaluate Alternatives
↓
Make Decision
↓
Document Decision
↓
Implement
↓
Measure
```

Do not redesign the system based solely on theoretical concerns.

---

# 108. Migration Strategy

Major architectural changes should support incremental migration where practical.

Avoid:

```text
Old Architecture
↓
Complete Rewrite
↓
Hope It Works
```

Prefer:

```text
Existing System
↓
Introduce Boundary
↓
Migrate Component
↓
Validate
↓
Remove Legacy
```

---

# 109. Backward Compatibility

Where existing consumers or persisted data exist, architectural changes should consider compatibility.

Breaking changes must be intentional.

---

# 110. Architecture Health Indicators

The project should periodically assess:

```text
Module Coupling
Boundary Violations
Duplicate Logic
Provider Lock-In
Testability
Observability
Data Integrity
Documentation Drift
AI Failure Rate
Workflow Complexity
Operational Complexity
```

Architecture should be improved when measurable problems justify it.

---

# 111. Architectural Anti-Patterns

The following should be treated as warning signs.

## God Orchestrator

One component owns every decision.

## God Agent

One agent performs unrelated reasoning.

## God Database

Every module directly accesses every table.

## AI Direct Mutation

LLM output directly changes authoritative state.

## Provider Leakage

External SDK types spread throughout the domain.

## Prompt-as-Architecture

Critical business rules exist only inside prompts.

## JSON Dump Architecture

The database becomes an unstructured collection of AI outputs.

## Hidden Workflow

The execution sequence exists only inside undocumented code.

## Context Dumping

Every AI call receives the entire project.

## Autonomous Sprawl

Every module becomes an independent autonomous agent.

---

# 112. Architectural Quality Model

The system architecture should optimize for:

```text
Correctness
+
Clarity
+
Modularity
+
Testability
+
Observability
+
Security
+
Extensibility
+
Operational Simplicity
```

These qualities should be balanced against:

```text
Cost
Latency
Complexity
Development Speed
```

No single quality should automatically dominate every architectural decision.

---

# 113. System-Level Golden Path

The preferred end-to-end path is:

```text
USER
 ↓
APPLICATION REQUEST
 ↓
ORCHESTRATOR
 ↓
CONTEXT BUILDER
 ↓
INTELLIGENCE MODULE
 ↓
TOOLS / EXTERNAL DATA
 ↓
STRUCTURED AI OUTPUT
 ↓
VALIDATION
 ↓
DOMAIN DECISION
 ↓
HUMAN REVIEW WHEN REQUIRED
 ↓
PERSISTENT KNOWLEDGE
 ↓
USER OUTPUT
```

This is the core architectural loop.

---

# 114. Example: Topic-to-Page Workflow

A simplified execution might be:

```text
User:
"Analyze opportunities around running shoes."

        ↓

Orchestrator

        ↓

Retrieve:
Business Context
Entity Model
Existing Topics
Existing Pages
Historical Decisions

        ↓

Topic Discovery

        ↓

Topic Validation

        ↓

Intent Analysis

        ↓

SERP Collection

        ↓

SERP Analysis

        ↓

Topic Clustering

        ↓

Page Candidate Analysis

        ↓

Strategic Scoring

        ↓

Recommendation

        ↓

Human Review

        ↓

Approved Page Strategy

        ↓

Knowledge Update
```

Each step should have explicit inputs and outputs.

---

# 115. Example: New Business Entity Workflow

```text
User Adds New Product

        ↓

Entity Created

        ↓

Entity Validation

        ↓

Attribute Extraction

        ↓

Relationship Discovery

        ↓

Topic Opportunity Analysis

        ↓

Search Intelligence

        ↓

Page Opportunity Analysis

        ↓

Recommendation

        ↓

Human Review

        ↓

Knowledge Update
```

The architecture should support such feedback loops.

---

# 116. Example: SERP Change Workflow

```text
Scheduled SERP Refresh

        ↓

SERP Provider

        ↓

Raw Snapshot

        ↓

Change Detection

        ↓

Intent Re-evaluation

        ↓

Topic / Page Impact Analysis

        ↓

Strategic Alert

        ↓

Human Review

        ↓

Decision Update
```

This illustrates the future living-intelligence capability.

---

# 117. Architectural Contract Between Layers

The major layer contract is:

```text
Presentation
→ Requests application capabilities

Application
→ Coordinates use cases

Orchestrator
→ Coordinates workflows

Intelligence
→ Produces structured analysis

Domain
→ Enforces conceptual and business rules

Knowledge
→ Persists authoritative state

Integration
→ Communicates with external systems

Infrastructure
→ Provides technical execution capabilities
```

No layer should casually bypass these boundaries.

---

# 118. Dependency Direction

The preferred dependency direction is:

```text
Presentation
        ↓
Application
        ↓
Orchestration
        ↓
Domain
        ↓
Abstractions
        ↓
Infrastructure
```

AI and integration implementations should depend on appropriate abstractions rather than forcing the domain to depend on vendors.

---

# 119. Dependency Inversion

Core domain behavior should not depend directly on volatile external implementations.

Conceptually:

```text
Domain
  ↓
Interface
  ↑
Provider Adapter
```

This makes external dependencies replaceable.

---

# 120. Boundary Violation Policy

A boundary violation should be treated as an architectural issue.

Examples:

```text
UI directly queries internal database tables
Agent directly mutates database
Domain imports provider SDK
API implements clustering algorithm
Search adapter modifies human decisions
```

Such violations require explicit justification.

---

# 121. Architectural Invariants

The following must remain true:

```text
1. Human-approved decisions are authoritative strategic state.

2. AI output is not automatically authoritative.

3. External data is untrusted.

4. Structured knowledge remains distinct from semantic retrieval.

5. Keywords, topics, intents, entities, and pages remain distinct.

6. Provider-specific implementations remain behind integration boundaries.

7. Critical state transitions are validated.

8. Invalid critical AI output cannot silently persist.

9. High-risk actions require authorization.

10. Project state must not depend solely on chat history.
```

---

# 122. MVP Architectural Scope

The MVP should prioritize:

```text
Core Web Application
Core API
Central Orchestrator
Core Domain Model
Structured Knowledge Store
Evidence Store
Core AI Modules
LLM Integration Abstraction
Search / SERP Integration Abstraction
Human Review
Decision Persistence
Basic Background Processing
Validation
Testing
Observability
```

The MVP should not require:

```text
Full Microservice Architecture
Large Agent Network
Complex Event Mesh
Multi-Region Infrastructure
Autonomous Publishing
Fully Automated SEO Execution
```

unless later evidence makes them necessary.

---

# 123. Future Architectural Expansion

Future versions may introduce:

```text
Distributed Workers
Event Bus
Advanced Scheduling
Continuous Monitoring
Multi-Provider AI Routing
Advanced Knowledge Graph
Real-Time Search Monitoring
Autonomous Low-Risk Operations
Multi-Project Intelligence
Enterprise Permissions
Advanced Analytics
```

These are extensions of the architecture, not prerequisites for the initial system.

---

# 124. Architectural Success Criteria

The architecture is successful when:

* Major components have clear responsibilities.
* Domain logic is separated from infrastructure.
* AI modules are independently testable.
* External providers can be replaced.
* Human decisions remain authoritative.
* Evidence remains traceable.
* Context can be retrieved selectively.
* Workflows can pause and resume.
* Failures are observable.
* Critical state transitions are validated.
* The system can evolve without repeated rewrites.
* Complexity remains proportional to actual requirements.

---

# 125. Final Architectural Model

The entire system can be summarized as:

```text
                         USER
                          │
                          ↓
                    WEB / UI
                          │
                          ↓
                    APPLICATION
                          │
                          ↓
                    ORCHESTRATOR
                          │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
        WORKFLOWS      AI MODULES    DOMAIN
            │             │             │
            └─────────────┼─────────────┘
                          ↓
                    CONTEXT LAYER
                          │
                          ↓
                   KNOWLEDGE LAYER
              ┌───────────┼───────────┐
              ↓           ↓           ↓
          STRUCTURED   SEMANTIC     EVIDENCE
             DATA       INDEXES       DATA
              │           │           │
              └───────────┼───────────┘
                          ↓
                  INTEGRATION LAYER
             ┌────────────┼────────────┐
             ↓            ↓            ↓
          SEARCH        WEB/SEO       LLM
          PROVIDERS     PROVIDERS   PROVIDERS
             │            │            │
             └────────────┼────────────┘
                          ↓
                    EXTERNAL WORLD
```

The central architectural philosophy is:

```text
Simple Core
+
Modular Intelligence
+
Controlled Orchestration
+
Persistent Knowledge
+
Evidence
+
Human Authority
+
Replaceable Integrations
+
Validated AI
```

---

# 126. Relationship to Other Documents

This document establishes system-level architecture.

It should be read together with:

```text
01_PRD.md
02_PRODUCT_VISION.md
03_MASTER_RULES.md
```

The following documents refine specific architectural areas:

```text
05_AI_AGENT_ARCHITECTURE.md
06_DATA_ARCHITECTURE.md
07_TECHNICAL_ARCHITECTURE.md
08_SEO_KNOWLEDGE_MODEL.md
09_ENTITY_EAV_MODEL.md
10_TOPIC_MODELING_AND_CLUSTERING.md
11_SEARCH_AND_SERP_INTELLIGENCE.md
12_SEO_DECISION_ENGINE.md
13_AGENT_SPECIFICATIONS.md
14_AGENT_WORKFLOW.md
15_HUMAN_IN_THE_LOOP.md
16_OUTPUT_CONTRACTS.md
17_UI_UX_SPECIFICATION.md
18_FRONTEND_ARCHITECTURE.md
19_DESIGN_SYSTEM.md
20_PROJECT_STRUCTURE.md
21_DEVELOPMENT_AND_DEBUG.md
22_TESTING_AND_VALIDATION.md
23_PROJECT_CONTROL_CENTER.md
24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md
25_CONTEXT_MANAGEMENT.md
26_SKILLS_AND_TOOLING_POLICY.md
```

These references identify architectural relationships; they do not prescribe the final execution order.

The definitive dependency and reading order must be established through the project documentation audit.

---

# 127. Document Status

**Document:** `04_SYSTEM_ARCHITECTURE.md`

**Role:** System-Level Architecture

**Authority Level:** Architectural

**Depends On:**

* `01_PRD.md`
* `02_PRODUCT_VISION.md`
* `03_MASTER_RULES.md`

**Defines:**

* System boundaries
* Architectural layers
* Major components
* Orchestration model
* Knowledge architecture
* Integration boundaries
* AI execution boundaries
* Human interaction boundaries
* Security boundaries
* Deployment direction
* Architectural invariants

**Status:** APPROVED AS BASELINE SYSTEM ARCHITECTURE

**Core Architectural Principle:**

> Build a modular, evidence-driven intelligence system around a central orchestrator, persistent structured knowledge, controlled AI reasoning, replaceable external integrations, and explicit human decision authority — while keeping the initial implementation as simple as the real requirements allow.
