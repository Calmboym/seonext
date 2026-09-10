# 06 — DATA ARCHITECTURE

**Project:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document:** Data Architecture
**Filename:** `06_DATA_ARCHITECTURE.md`
**Document Type:** Architectural Specification
**Authority:** Data Architecture
**Status:** `APPROVED AS BASELINE DATA ARCHITECTURE`
**Version:** `1.0.0`

---

# 1. Purpose

This document defines the data architecture of the SEO Research & Strategy Copilot.

Its purpose is to establish how the system represents, stores, relates, validates, versions, retrieves, and governs the information required for SEO research and decision intelligence.

The architecture must support the transition from:

```text
Keyword Database
```

to:

```text
Living SEO Knowledge System
```

The data layer must therefore represent more than keywords.

It must represent:

```text
Business
Entities
Attributes
Values
Relationships
Topics
Keywords
Intent
SERPs
Pages
Competitors
Evidence
Recommendations
Decisions
Human Feedback
Historical State
```

The data architecture must support both:

```text
Structured Data
```

and:

```text
Semantic / Vector Retrieval
```

while preserving authoritative provenance and deterministic system state.

---

# 2. Data Architecture Principles

The data architecture follows these principles:

1. Structured data is the source of operational truth.
2. Semantic representations supplement, but do not replace, structured state.
3. Raw evidence must be distinguishable from derived information.
4. AI inference must be distinguishable from observed facts.
5. Human decisions must be distinguishable from AI recommendations.
6. Historical state should be preserved where strategically valuable.
7. Relationships are first-class data.
8. Provenance must be preserved.
9. Data quality must be validated.
10. External provider data must never be treated as inherently authoritative.
11. Schema evolution must be controlled.
12. Data access must respect tenant/project boundaries.
13. The architecture should support relational, graph-like, and vector retrieval patterns without prematurely requiring a dedicated graph database.
14. Data architecture must remain compatible with the modular-monolith default architecture.

---

# 3. Core Data Philosophy

The system should not model SEO as:

```text
Keyword → Volume → Difficulty → Rank
```

The preferred conceptual model is:

```text
Business
    ↓
Entities
    ↓
Attributes / Values
    ↓
Topics
    ↓
Search Expressions
    ↓
Intent
    ↓
SERP Reality
    ↓
Pages
    ↓
Relationships
    ↓
Evidence
    ↓
Recommendations
    ↓
Human Decisions
    ↓
Outcomes
```

This creates a connected decision model rather than a disconnected metric database.

---

# 4. Data Domains

The data layer is divided into logical domains.

```text
┌──────────────────────────────────────────┐
│ Business Domain                          │
├──────────────────────────────────────────┤
│ Entity / Semantic Domain                 │
├──────────────────────────────────────────┤
│ Topic Domain                             │
├──────────────────────────────────────────┤
│ Search Domain                            │
├──────────────────────────────────────────┤
│ Website Domain                           │
├──────────────────────────────────────────┤
│ Competitive Domain                       │
├──────────────────────────────────────────┤
│ Evidence Domain                           │
├──────────────────────────────────────────┤
│ Decision Domain                            │
├──────────────────────────────────────────┤
│ Workflow / Execution Domain               │
├──────────────────────────────────────────┤
│ Evaluation / Feedback Domain              │
└──────────────────────────────────────────┘
```

These are logical domains and do not necessarily require separate databases.

---

# 5. Tenant / Workspace Boundary

The system should support isolation between independent projects, organizations, or workspaces.

Conceptually:

```text
Organization
    ↓
Workspace
    ↓
Project
    ↓
SEO Knowledge
```

All project-specific entities should be associated with the appropriate project/workspace boundary.

Cross-project data sharing must be explicit.

---

# 6. Core Identity Model

Important objects should have stable identifiers.

Examples:

```text
business_id
entity_id
attribute_id
value_id
topic_id
keyword_id
intent_id
serp_observation_id
page_id
competitor_id
evidence_id
recommendation_id
decision_id
workflow_id
task_id
```

Identifiers should remain stable even when names or descriptions change.

---

# 7. Entity Identity

Entity identity is different from entity naming.

Example:

```text
Entity ID:
entity_123

Canonical Name:
Apple

Type:
Organization
```

Aliases may include:

```text
Apple Inc.
Apple Computer
```

Changing the canonical label must not create a new entity unless identity itself changes.

---

# 8. Business Model

The business model represents the organization being analyzed.

Potential attributes include:

```text
business_id
name
description
industry
markets
locations
business_model
products
services
target_audiences
commercial_goals
strategic_priorities
website
status
created_at
updated_at
```

Business information may originate from:

* user input
* business research
* verified first-party data
* external evidence

Its provenance should be preserved where meaningful.

---

# 9. Entity Model

Entities represent meaningful objects or concepts within the SEO knowledge domain.

Examples:

```text
Product
Service
Brand
Organization
Person
Location
Problem
Concept
Audience
Use Case
Feature
Material
Process
Industry
```

An entity should have:

```text
identity
type
canonical_name
aliases
description
status
evidence
confidence
```

---

# 10. Entity Relationships

Relationships between entities are first-class data.

Examples:

```text
Company
  └── offers → Service

Service
  └── serves → Audience

Product
  └── has_attribute → Attribute

Product
  └── belongs_to → Category
```

A relationship should be represented explicitly rather than encoded only in free-form text.

---

# 11. Relationship Model

A relationship may contain:

```yaml
relationship:
  id:
  subject_entity_id:
  predicate:
  object_entity_id:
  confidence:
  provenance:
  status:
  valid_from:
  valid_to:
  created_at:
  updated_at:
```

The exact schema will be defined in the entity/EAV model document.

---

# 12. Relationship Types

Relationship categories may include:

```text
Hierarchical
Associative
Functional
Causal
Temporal
Commercial
Geographic
Semantic
Competitive
Ownership
Dependency
```

The final controlled vocabulary belongs to the semantic knowledge model.

---

# 13. EAV Model

The system must support Entity–Attribute–Value representation.

Conceptually:

```text
Entity
  ↓
Attribute
  ↓
Value
```

Example:

```text
Entity:
Running Shoes

Attribute:
Water Resistance

Value:
Waterproof
```

EAV allows the system to represent domain-specific properties without requiring every possible attribute to become a physical database column.

---

# 14. EAV vs Relationship

Not every EAV record is merely a string.

Values may be:

```text
Literal
Number
Boolean
Date
Entity Reference
Range
Structured Object
```

Example:

```text
Entity:
Running Shoes

Attribute:
Designed For

Value:
Trail Running Entity
```

This is effectively a semantic relationship and should preserve entity identity.

---

# 15. Topic Model

A topic represents a meaningful subject in the domain.

A topic may be connected to:

```text
Entities
Attributes
Questions
Keywords
Intent
SERPs
Pages
Business Objectives
```

A topic should not be reduced to a keyword string.

---

# 16. Topic Identity

A topic should have a stable identity.

Potential fields:

```text
topic_id
canonical_name
description
topic_type
parent_topic_id
status
confidence
business_relevance
created_at
updated_at
```

Renaming a topic should not necessarily create a new topic.

---

# 17. Topic Relationships

Topics may have:

```text
Parent
Child
Related
Supporting
Alternative
Prerequisite
Adjacent
Contrasting
```

These relationships form the conceptual basis of the topical map.

---

# 18. Keyword Model

Keywords/search expressions are representations of search behavior.

Potential fields:

```text
keyword_id
query
language
locale
country
device
search_engine
topic_id
intent_id
observed_at
source
status
```

Keyword records should be linked to topics where possible.

Multiple keywords may belong to the same topic.

---

# 19. Keyword Canonicalization

The system should distinguish between:

```text
Raw Query
Normalized Query
Canonical Search Expression
```

Normalization may include:

* whitespace normalization
* case normalization
* language handling
* punctuation normalization

Normalization must not destroy meaningful query distinctions.

---

# 20. Search Context

Search observations should preserve relevant context.

Potential dimensions:

```text
Country
Language
Locale
Device
Search Engine
Date
Time
Personalization Context
```

A keyword without search context may be insufficient for some decisions.

---

# 21. Search Volume

Search volume should be represented as an observation, not an eternal property of a keyword.

Conceptually:

```yaml
search_volume:
  keyword_id:
  value:
  period:
  geography:
  source:
  observed_at:
  confidence:
```

Historical observations should remain available where valuable.

---

# 22. Search Metrics

Potential search metrics include:

```text
Search Volume
CPC
Competition
Difficulty
Trend
Impressions
Clicks
CTR
```

These should be treated as distinct measurements.

The system must not assume that metrics from different providers are directly comparable without normalization.

---

# 23. SERP Observation Model

A SERP is an observation of a search environment at a particular point in time.

A SERP observation should conceptually contain:

```text
serp_observation_id
query
location
language
device
search_engine
observed_at
results
features
source
```

---

# 24. SERP Result Model

A result may contain:

```text
rank
url
domain
title
snippet
page_type
result_type
features
observed_at
```

The exact provider-specific fields should be normalized into a canonical representation while retaining raw provider data where necessary.

---

# 25. SERP Features

SERP features may include:

```text
Featured Snippet
People Also Ask
Local Pack
Knowledge Panel
Shopping
Images
Videos
News
Discussions
AI Overview
Other Search Features
```

The taxonomy should remain extensible.

---

# 26. SERP Raw vs Normalized Data

External SERP responses should be separated conceptually into:

```text
Raw Provider Response
        ↓
Normalized SERP Observation
        ↓
Derived SERP Signals
        ↓
AI Interpretation
```

Raw responses provide auditability.

Normalized observations support application logic.

Derived signals support analysis.

AI interpretation supports recommendations.

---

# 27. Intent Model

Intent is a derived semantic/search interpretation.

It should not be stored as though it were an immutable fact.

Potential fields:

```text
intent_id
topic_id
keyword_id
intent_type
confidence
evidence
model_version
observed_at
status
```

---

# 28. Intent History

Intent can change over time.

Therefore the system should be able to represent:

```text
Intent at T1
Intent at T2
Intent at T3
```

rather than overwriting historical values without trace.

---

# 29. Page Model

A page represents an actual or proposed website asset.

Pages may be:

```text
Existing
Planned
Recommended
Archived
Unknown
```

Potential fields:

```text
page_id
url
title
page_type
status
topic_ids
entity_ids
intent
content_role
canonical_url
created_at
updated_at
```

---

# 30. Existing vs Proposed Pages

The data model must distinguish:

```text
Observed Existing Page
```

from:

```text
AI Recommended Page
```

A recommendation must not create the illusion that the page already exists.

---

# 31. Page–Topic Relationship

A page may cover:

* one primary topic
* multiple secondary topics
* several entities
* multiple attributes

The relationship should preserve role.

Example:

```text
Page
 ├── primary_topic
 ├── supporting_topic
 ├── mentioned_entity
 └── target_intent
```

---

# 32. Competitor Model

Competitors should be represented as entities within the competitive domain.

Potential fields:

```text
competitor_id
entity_id
domain
market
competitor_type
source
confidence
status
```

The system should distinguish:

```text
Known Competitor
SERP Competitor
Semantic Competitor
Business Competitor
```

These are not necessarily equivalent.

---

# 33. Evidence Model

Evidence is a first-class data object.

Evidence may originate from:

```text
User Input
Search API
SERP API
SEO API
Website Crawl
Analytics
Business Documentation
External Database
Human Decision
Historical Observation
```

---

# 34. Evidence Structure

Conceptually:

```yaml
evidence:
  id:
  source_type:
  source_identifier:
  captured_at:
  observed_at:
  content_reference:
  raw_data_reference:
  normalized_data_reference:
  reliability:
  freshness:
  provenance:
```

The exact schema will be defined later.

---

# 35. Evidence vs Claim

The system should distinguish:

```text
Evidence
```

from:

```text
Claim
```

Example:

```text
Evidence:
SERP contains 8 informational pages.

Claim:
The query appears primarily informational.
```

The claim should reference the evidence supporting it.

---

# 36. Claim Model

A claim may be:

```text
Observed
Inferred
Estimated
Recommended
Human Approved
```

Claims should preserve:

```text
claim_id
text / structured value
epistemic_status
confidence
evidence
producer
version
created_at
```

---

# 37. Recommendation Model

A recommendation represents an AI/system suggestion.

Examples:

```text
Create Page
Merge Pages
Split Topic
Prioritize Topic
Investigate Intent
Add Internal Link
Improve Existing Page
Create Supporting Content
```

A recommendation must not automatically become a decision.

---

# 38. Decision Model

A decision represents an approved strategic or operational conclusion.

Conceptually:

```text
Recommendation
      ↓
Human Review
      ↓
Decision
```

A decision should preserve:

```text
decision_id
recommendation_id
decision_type
decision_status
decision_author
decision_reason
created_at
```

---

# 39. Decision Status

Possible states:

```text
Pending
Approved
Rejected
Modified
Deferred
Superseded
Implemented
Cancelled
```

The final controlled vocabulary will be defined in the human-in-the-loop specification.

---

# 40. Human Feedback Model

Human feedback should be represented separately from raw decisions.

Examples:

```text
Correct
Incorrect
Useful
Not Useful
Missing Context
Wrong Intent
Wrong Business Priority
Wrong Page Mapping
```

Feedback may later contribute to evaluation datasets.

---

# 41. Historical State

The system should preserve meaningful historical changes.

Potential mechanisms include:

```text
Versioned Records
Event Log
Temporal Fields
Snapshots
Change History
```

The exact implementation may vary by data domain.

---

# 42. Temporal Data

Time-sensitive objects should include appropriate temporal information.

Examples:

```text
observed_at
captured_at
created_at
updated_at
valid_from
valid_to
```

These timestamps have different meanings and must not be conflated.

---

# 43. Timestamp Semantics

The system should distinguish:

```text
created_at
```

from:

```text
observed_at
```

and:

```text
captured_at
```

For example:

```text
SERP observed at:
2026-09-05 10:00

Stored at:
2026-09-05 10:01
```

The difference matters for freshness and auditing.

---

# 44. Data Provenance

Derived objects should reference upstream data.

Example:

```text
SEO Recommendation
    ↓
Intent Classification
    ↓
SERP Signals
    ↓
SERP Observation
    ↓
Provider Response
```

This enables investigation and reprocessing.

---

# 45. Provenance Graph

Conceptually:

```text
Source
  ↓
Evidence
  ↓
Observation
  ↓
Derived Signal
  ↓
Inference
  ↓
Recommendation
  ↓
Human Decision
```

Each layer should preserve references to relevant upstream objects.

---

# 46. Data Classification

The system should distinguish at least:

```text
RAW
NORMALIZED
DERIVED
INFERRED
RECOMMENDED
APPROVED
HISTORICAL
```

These classifications prevent accidental mixing of fundamentally different data types.

---

# 47. Raw Data Storage

Raw provider responses may be stored when useful for:

* auditing
* debugging
* reprocessing
* provider migration
* historical analysis

Raw data should not automatically become the primary application model.

---

# 48. Normalized Data

Normalized data provides a provider-independent representation.

Example:

```text
Provider A SERP format
Provider B SERP format
Provider C SERP format
        ↓
Canonical SERP Model
```

This allows the intelligence layer to operate against a stable internal contract.

---

# 49. Derived Data

Derived data is calculated or transformed from upstream information.

Examples:

```text
Intent Distribution
SERP Similarity
Topic Similarity
Content Coverage
Opportunity Score
Cannibalization Risk
```

Derived data should preserve enough lineage to reproduce or investigate the calculation.

---

# 50. AI-Inferred Data

AI inference includes:

```text
Topic Classification
Intent
Entity Relationship
Semantic Similarity
Potential Cannibalization
Potential Content Gap
```

Inference should preserve:

* model
* version
* confidence
* evidence
* timestamp

where appropriate.

---

# 51. Data Confidence

Confidence is metadata about uncertainty.

It should not replace evidence.

Bad model:

```text
confidence = 0.91
```

with no explanation.

Preferred model:

```text
confidence = 0.91
evidence = [serp_123, topic_456]
model_version = intent_v2
```

---

# 52. Data Quality

Data quality checks should include:

```text
Completeness
Validity
Consistency
Uniqueness
Freshness
Provenance
Referential Integrity
Schema Compliance
```

---

# 53. Data Validation Layers

Validation should occur at multiple levels:

```text
Input Validation
      ↓
Schema Validation
      ↓
Domain Validation
      ↓
Cross-Entity Validation
      ↓
Evidence Validation
      ↓
Persistence Validation
```

---

# 54. Referential Integrity

Relationships should reference valid objects.

Examples:

```text
topic_id → existing topic
entity_id → existing entity
page_id → existing page
evidence_id → existing evidence
```

Broken references must be detected.

---

# 55. Uniqueness

Where identity requires uniqueness, enforce it structurally.

Potential examples:

```text
workspace + canonical_entity_identifier
project + canonical_topic_identifier
provider + external_record_id
```

The exact constraints belong to the implementation/data model.

---

# 56. Soft Deletion

Important historical objects should generally not be physically deleted without considering their impact on:

* evidence
* historical decisions
* auditability
* relationships
* reports

Where appropriate, use states such as:

```text
Active
Archived
Deprecated
Deleted
```

---

# 57. Data Lifecycle

A typical lifecycle is:

```text
Discovered
    ↓
Captured
    ↓
Normalized
    ↓
Validated
    ↓
Stored
    ↓
Enriched
    ↓
Analyzed
    ↓
Used in Decision
    ↓
Historical
    ↓
Archived
```

Not every object must pass through every state.

---

# 58. Database Strategy

The initial implementation should favor a relational database as the system of record.

The recommended conceptual stack is:

```text
PostgreSQL
+
Vector Extension / Vector Store
+
Object / Raw Evidence Storage
```

A dedicated graph database is not required for the initial architecture.

Graph-like relationships can initially be represented through relational tables and relationship records.

---

# 59. Relational Model

PostgreSQL should own:

* identities
* transactional state
* relationships
* workflow state
* approvals
* contracts
* metadata
* normalized records
* audit information

This provides deterministic integrity.

---

# 60. Vector Layer

A vector store or PostgreSQL vector extension may support:

* semantic retrieval
* similarity search
* topic similarity
* entity similarity
* evidence retrieval
* contextual search

Vectors are derived representations.

They are not the canonical source of truth.

---

# 61. Vector Identity

Every vector should reference the source object from which it was generated.

Conceptually:

```yaml
embedding:
  id:
  source_type:
  source_id:
  embedding_model:
  embedding_version:
  created_at:
```

---

# 62. Vector Reproducibility

If embeddings are regenerated using a different model, the system should preserve version information.

Example:

```text
entity_123
embedding_model_v1
embedding_model_v2
```

This supports controlled migration and comparison.

---

# 63. Retrieval Architecture

Semantic retrieval should follow:

```text
User / Agent Task
      ↓
Query Representation
      ↓
Vector / Structured Retrieval
      ↓
Candidate Objects
      ↓
Filtering
      ↓
Ranking
      ↓
Context Assembly
```

Vector similarity alone should not determine final business decisions.

---

# 64. Hybrid Retrieval

The preferred long-term retrieval architecture is hybrid:

```text
Structured Filters
+
Semantic Search
+
Keyword / Lexical Search
+
Relationship Traversal
+
Recency
+
Evidence Quality
```

The exact weighting depends on the task.

---

# 65. Knowledge Graph Representation

The data model should be graph-compatible.

Conceptually:

```text
(Entity)
   │
   ├── has_attribute → (Attribute)
   │                         │
   │                         └── has_value → (Value)
   │
   ├── related_to → (Entity)
   │
   ├── supports → (Topic)
   │
   └── evidenced_by → (Evidence)
```

A graph-compatible model supports future graph retrieval without requiring immediate graph-database adoption.

---

# 66. Entity Resolution

The system should support identifying when multiple records may represent the same real-world entity.

Example:

```text
"Acme Inc."
"Acme"
"ACME Corporation"
```

may represent one entity.

Entity resolution should consider:

* canonical identifiers
* aliases
* domains
* external identifiers
* contextual evidence
* semantic similarity

AI suggestions should be validated before destructive merges.

---

# 67. Entity Merge Safety

Entity merging may have significant downstream impact.

Therefore:

```text
Candidate Match
    ↓
Confidence
    ↓
Evidence
    ↓
Human Approval if Risky
    ↓
Merge
```

should be preferred over automatic irreversible merging.

---

# 68. Topic Deduplication

Topic deduplication should distinguish:

```text
Exact Duplicate
Semantic Duplicate
Related Topic
Distinct Topic
```

Semantic similarity does not automatically imply identity.

---

# 69. Topic Versioning

When a topic changes meaning substantially, the system may need to create a new version or new identity rather than silently modifying the old topic.

This is particularly important when historical decisions depend on the previous definition.

---

# 70. Page Relationship Model

Pages may be connected through:

```text
Supports
Parent
Child
Related
Canonicalizes
Competes With
Links To
Replaces
Redirects To
```

These relationships should be explicit.

---

# 71. Internal Link Data

An internal link should conceptually contain:

```text
source_page_id
target_page_id
anchor_text
context
relationship_type
status
recommendation_source
```

A recommended link must be distinguishable from an existing link.

---

# 72. Cannibalization Data

Cannibalization analysis should not overwrite page state.

Instead, create an analysis/recommendation object containing:

```text
page_a
page_b
overlap_type
signals
confidence
evidence
recommended_action
status
```

---

# 73. Content Gap Data

A content gap should identify:

```text
gap_type
target_topic
target_entity
target_intent
existing_coverage
competitor_evidence
business_value
confidence
recommended_action
```

A gap is an analytical object, not automatically a page.

---

# 74. Opportunity Model

An SEO opportunity should combine multiple signals.

Potential components:

```text
Business Relevance
Search Demand
Intent Fit
SERP Opportunity
Competition
Existing Coverage
Topical Importance
Commercial Value
Strategic Priority
Confidence
```

The exact scoring formula belongs to the SEO Decision Engine specification.

---

# 75. Scoring Data

Scores should preserve their components.

Bad:

```text
opportunity_score = 87
```

Preferred:

```yaml
opportunity:
  score: 87
  components:
    business_relevance: 0.9
    search_demand: 0.7
    intent_fit: 0.95
    coverage_gap: 0.8
    competition: 0.5
```

This improves explainability and debugging.

---

# 76. Data Ownership

Each domain should have a clear ownership boundary.

Conceptually:

```text
Business Service
→ Business Data

Entity Service
→ Entity Data

Topic Service
→ Topic Data

Search Service
→ Search Data

Evidence Service
→ Evidence Data

Decision Service
→ Recommendation / Decision Data
```

No module should casually mutate another domain's internal state.

---

# 77. Data Access Layer

Application components should access persistent data through defined repositories/services where appropriate.

Preferred:

```text
Agent
 ↓
Application Service
 ↓
Domain Service
 ↓
Repository
 ↓
Database
```

rather than:

```text
Agent
 ↓
Raw SQL Everywhere
```

---

# 78. Transaction Boundaries

Operations that require atomic updates should use transactions.

Examples:

```text
Create Decision
+
Update Recommendation Status
+
Create Audit Event
```

should be atomic when the domain requires consistency.

---

# 79. Event Model

The system may use domain events for important state changes.

Examples:

```text
TopicValidated
IntentClassified
SERPObserved
RecommendationCreated
DecisionApproved
PageMapped
```

Events may support:

* audit
* asynchronous workflows
* integrations
* analytics

The initial architecture does not require a distributed event bus.

---

# 80. Event vs State

Events describe:

```text
Something happened.
```

State describes:

```text
What is true now.
```

The system should not confuse these concepts.

---

# 81. Workflow Data

Workflow execution should persist:

```text
workflow_id
task_id
execution_id
status
input_reference
output_reference
attempt_count
started_at
completed_at
error
```

This enables recovery and observability.

---

# 82. Idempotency Data

Operations that may be retried should support idempotency keys where appropriate.

Example:

```text
workflow_id + task_id + input_hash
```

should help identify duplicate executions.

---

# 83. Audit Data

Audit records should capture important actions.

Potential fields:

```text
actor
actor_type
action
resource_type
resource_id
timestamp
before_state
after_state
reason
workflow_id
```

Sensitive data should be minimized.

---

# 84. Security and Data Isolation

Data access must enforce:

```text
Organization Boundary
Workspace Boundary
Project Boundary
Role / Permission Boundary
```

AI agents must receive only the data required for their authorized task.

---

# 85. Secrets

Secrets such as:

* API keys
* provider credentials
* database credentials
* authentication secrets

must not be stored as ordinary domain data.

Secret management belongs to the infrastructure/security layer.

---

# 86. Personal Data

The system should minimize storage and exposure of personal data.

If personal information is unnecessary for SEO strategy, it should not be collected merely because it is available.

---

# 87. External Data Trust

External provider data should carry source metadata.

Example:

```yaml
source:
  provider: example_provider
  external_id: abc123
  retrieved_at:
  observed_at:
```

This allows comparison between providers and historical observations.

---

# 88. Provider Normalization

Provider-specific fields should remain accessible when needed for debugging, while the application should operate primarily against canonical internal structures.

Preferred:

```text
Raw Provider Model
        ↓
Provider Adapter
        ↓
Canonical Data Model
```

---

# 89. Data Freshness

Every time-sensitive observation should have a freshness concept.

Possible states:

```text
Fresh
Aging
Stale
Expired
Unknown
```

Freshness thresholds depend on data type.

A SERP observation and a business description should not share the same freshness policy.

---

# 90. Reprocessing

The architecture should support reprocessing derived information when:

* better models become available
* evidence changes
* taxonomy changes
* algorithms change
* provider data is corrected

Raw evidence should be preserved where feasible to enable reprocessing.

---

# 91. Derived Data Rebuild

A derived object should ideally be rebuildable from:

```text
Source Data
+
Algorithm Version
+
Configuration
```

This improves reproducibility.

---

# 92. Data Migration

Schema changes must be managed through controlled migrations.

Migration planning should consider:

```text
Existing Data
Historical Data
Constraints
Indexes
Backfills
Rollback
Downtime
Compatibility
```

---

# 93. Schema Evolution

The data model is expected to evolve.

Changes may include:

```text
Additive
Non-Breaking
Backwards-Compatible
Breaking
Destructive
```

Breaking/destructive changes require stronger review.

---

# 94. Indexing Strategy

Indexes should support actual access patterns.

Likely indexing dimensions include:

```text
project_id
entity_id
topic_id
keyword_id
page_id
observed_at
status
type
external_id
```

Vector indexes should be optimized separately from relational indexes.

---

# 95. Search Optimization

Search-heavy data should support appropriate indexes for:

* lexical lookup
* filtering
* temporal queries
* relationship lookup
* semantic retrieval

Indexes should be introduced based on measured workload where possible.

---

# 96. Data Retention

Retention policies should distinguish:

```text
Operational Data
Historical Data
Raw Provider Data
Audit Data
Temporary Data
Cached Data
```

Not all data requires the same retention period.

---

# 97. Cache vs Source of Truth

Caches must never silently become authoritative.

Conceptually:

```text
PostgreSQL / Canonical Store
        ↓
Cache
        ↓
Fast Retrieval
```

If the cache conflicts with canonical state, canonical state wins.

---

# 98. Data Export

The system should eventually support exporting important project knowledge.

Potential exports:

```text
Entities
EAV
Topics
Keywords
Intent
SERPs
Pages
Recommendations
Decisions
Evidence
```

Export formats may include structured JSON/CSV and human-readable reports.

---

# 99. Import

Imported data should pass through:

```text
Import
 ↓
Validation
 ↓
Normalization
 ↓
Entity Resolution
 ↓
Conflict Detection
 ↓
Persistence
```

External imports must not bypass domain validation.

---

# 100. Data Conflict Resolution

Conflicts should be represented explicitly.

Example:

```text
Source A:
Entity Type = Product

Source B:
Entity Type = Service
```

The system should preserve:

```text
Conflict Detected
```

until a reliable resolution exists.

---

# 101. Data Lineage

Important derived objects should maintain lineage.

Example:

```text
Recommendation
  ← Decision Factors
  ← Topic
  ← Intent
  ← SERP
  ← Evidence
```

This enables explainability and reprocessing.

---

# 102. Data and AI Context

The knowledge layer should provide AI agents with task-specific context.

The retrieval layer should select:

```text
Relevant Entities
Relevant Topics
Relevant Evidence
Relevant Pages
Relevant Decisions
Relevant History
```

rather than dumping the entire database into the model context.

---

# 103. Knowledge Retrieval Boundary

AI agents should not directly query arbitrary tables unless explicitly authorized.

Prefer controlled retrieval services that enforce:

* project isolation
* permissions
* relevance
* filtering
* provenance
* context limits

---

# 104. Data Access for Agents

Agent context should ideally contain references such as:

```yaml
context:
  task:
  entities:
    - entity_123
  topics:
    - topic_456
  evidence:
    - evidence_789
  pages:
    - page_101
```

The agent can then retrieve details through approved interfaces.

---

# 105. Data Quality Monitoring

The system should eventually monitor:

```text
Missing Provenance
Broken Relationships
Stale Data
Duplicate Entities
Duplicate Topics
Invalid References
Low-Confidence Inference
Provider Conflicts
Schema Violations
```

These should become observable data-quality issues.

---

# 106. Data Governance

Data governance should define:

```text
Ownership
Authority
Provenance
Retention
Access
Versioning
Quality
Deletion
Export
```

The exact operational policies may evolve as the product matures.

---

# 107. Minimum Viable Data Architecture

The MVP should prioritize:

```text
Project / Workspace
Business
Entity
Entity Relationship
EAV
Topic
Keyword
Intent
SERP Observation
Page
Evidence
Recommendation
Decision
Workflow / Task State
```

Advanced historical and evaluation capabilities may be implemented incrementally, but their architectural compatibility should be preserved.

---

# 108. Recommended Initial Persistence Stack

Conceptually:

```text
                    ┌──────────────────────┐
                    │     PostgreSQL       │
                    │                      │
                    │ Canonical State      │
                    │ Relationships        │
                    │ Workflow             │
                    │ Decisions            │
                    │ Evidence Metadata    │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        Vector Layer      Raw Evidence      Cache
        pgvector/Qdrant   Object Storage     Optional
```

The exact technology selection belongs to the technical architecture document.

---

# 109. Data Architecture Anti-Patterns

The following are prohibited or strongly discouraged.

## 109.1 Keyword-Only Database

Do not model the entire product around keywords.

## 109.2 Metrics Without Provenance

Do not store metrics without source and observation context when provenance matters.

## 109.3 AI Output as Truth

Do not write model output directly as authoritative data without validation.

## 109.4 Vector Database as Source of Truth

Vectors are retrieval artifacts, not canonical business state.

## 109.5 Unstructured JSON for Everything

JSON may be useful for flexible payloads, but critical relational invariants should not be hidden inside arbitrary JSON blobs.

## 109.6 Permanent Overwriting

Do not overwrite strategically important historical observations without considering historical integrity.

## 109.7 Cross-Tenant Leakage

Never allow project data to cross isolation boundaries unintentionally.

## 109.8 Unbounded Agent Database Access

Agents must not receive unrestricted database access.

---

# 110. Data Architecture and SEO Decision Engine

The decision engine depends on the data layer to provide:

```text
Business Context
+
Semantic Context
+
Search Context
+
Website Context
+
Competitive Context
+
Evidence
+
Historical Context
```

The decision engine should not have to reconstruct these concepts from raw strings every time.

---

# 111. Data Architecture and Topical Maps

A topical map should be generated from relationships between:

```text
Topics
Entities
Attributes
Questions
Intent
Search Evidence
Business Priorities
```

The map should not be stored merely as a flat list.

---

# 112. Data Architecture and Page Architecture

Page architecture should derive from:

```text
Topic Model
+
Intent
+
SERP Evidence
+
Existing Pages
+
Business Priorities
+
Cannibalization Risk
```

The data layer must therefore preserve these relationships.

---

# 113. Data Architecture and Human Decisions

Human decisions must remain queryable.

The system should eventually answer:

```text
Why was this page recommended?
Who approved it?
What evidence supported the recommendation?
What did the AI originally recommend?
Was the recommendation modified?
What happened afterward?
```

---

# 114. Data Architecture and Learning

The historical data model should support evaluating:

```text
AI Recommendation
→ Human Decision
→ Implementation
→ Outcome
```

This enables future evaluation and model improvement.

---

# 115. Data Architecture and Context Management

The data layer is a major source of persistent context.

The context system should retrieve relevant information from structured knowledge rather than relying on conversation history.

---

# 116. Data Architecture and Skills

Tool/skill outputs that materially affect decisions should be stored as evidence or normalized observations where appropriate.

Example:

```text
SEO API Result
→ Evidence
→ Normalized Search Metric
→ Decision Input
```

Tool output should not disappear after the agent finishes.

---

# 117. Data Architecture and Auditability

The data layer must make it possible to trace:

```text
Decision
↓
Recommendation
↓
Inference
↓
Derived Signal
↓
Observation
↓
Evidence
↓
Source
```

This lineage is one of the core differentiators of the product.

---

# 118. Data Architecture and Security

Data access should follow:

```text
Authentication
    ↓
Authorization
    ↓
Workspace Scope
    ↓
Project Scope
    ↓
Domain Access
    ↓
Data Retrieval
```

Security controls must exist independently of AI prompts.

---

# 119. Data Architecture and Testing

Data architecture must support tests for:

```text
Schema Integrity
Referential Integrity
Transaction Integrity
Entity Resolution
Duplicate Detection
Historical Preservation
Provenance
Isolation
Migration
Retrieval
Vector Mapping
```

---

# 120. Data Architecture Evolution

The initial system should avoid over-engineering.

Start with:

```text
PostgreSQL
+
Relational Knowledge Model
+
Vector Retrieval
+
Raw Evidence Storage
```

Then introduce additional infrastructure only when justified.

Possible future additions include:

```text
Dedicated Graph Database
Event Streaming
Data Warehouse
Specialized Search Index
Feature Store
Knowledge Graph Service
```

These are future options, not MVP requirements.

---

# 121. Canonical Data Flow

The canonical data flow is:

```text
External / User Input
        ↓
Raw Evidence
        ↓
Normalization
        ↓
Validation
        ↓
Canonical Domain Object
        ↓
Knowledge Graph Relationships
        ↓
Derived Intelligence
        ↓
Recommendation
        ↓
Human Decision
        ↓
Outcome
        ↓
Historical Record
```

---

# 122. Data Architecture Success Criteria

The data architecture is successful if it allows the system to:

1. represent entities and relationships
2. represent EAV structures
3. distinguish topics from keywords
4. preserve search observations
5. preserve SERP evidence
6. represent existing and proposed pages
7. preserve provenance
8. distinguish inference from fact
9. preserve human decisions
10. support historical analysis
11. support semantic retrieval
12. support deterministic transactions
13. support tenant/project isolation
14. support reprocessing
15. support future knowledge-graph evolution

---

# 123. Final Data Architecture Model

```text
                           ┌─────────────────┐
                           │     BUSINESS    │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │    ENTITIES     │
                           └────────┬────────┘
                                    │
                     ┌──────────────┼──────────────┐
                     ▼              ▼              ▼
                  EAV / ATTR     RELATIONSHIPS    TOPICS
                     │              │              │
                     └──────────────┼──────────────┘
                                    ▼
                           ┌─────────────────┐
                           │ SEARCH / INTENT │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │      SERP       │
                           └────────┬────────┘
                                    │
                     ┌──────────────┼──────────────┐
                     ▼              ▼              ▼
                  PAGES        COMPETITORS      EVIDENCE
                     │              │              │
                     └──────────────┼──────────────┘
                                    ▼
                           ┌─────────────────┐
                           │   INFERENCES    │
                           └────────┬────────┘
                                    ▼
                           ┌─────────────────┐
                           │ RECOMMENDATIONS │
                           └────────┬────────┘
                                    ▼
                           ┌─────────────────┐
                           │    DECISIONS    │
                           └────────┬────────┘
                                    ▼
                           ┌─────────────────┐
                           │    HISTORY      │
                           └─────────────────┘
```

---

# 124. Governing Data Principle

The data layer must preserve the distinction between:

```text
What was observed
```

```text
What was derived
```

```text
What AI inferred
```

```text
What AI recommended
```

```text
What a human decided
```

This distinction is fundamental.

The system's intelligence is only as trustworthy as its ability to preserve the boundary between evidence, inference, recommendation, and decision.

---

# 125. Status

```yaml
document: 06_DATA_ARCHITECTURE.md
status: APPROVED_AS_BASELINE_DATA_ARCHITECTURE
authority: ARCHITECTURAL
scope:
  - canonical_data
  - knowledge_model
  - evidence
  - search_data
  - semantic_data
  - historical_state
  - recommendations
  - decisions
  - retrieval

primary_store:
  conceptual: relational_database

semantic_layer:
  conceptual:
    - vector_retrieval
    - graph_compatible_relationships

core_principles:
  - provenance
  - temporal_integrity
  - structured_truth
  - semantic_retrieval
  - human_decision_separation
  - project_isolation
  - reproducibility
  - controlled_evolution
```

**End of `06_DATA_ARCHITECTURE.md`**
