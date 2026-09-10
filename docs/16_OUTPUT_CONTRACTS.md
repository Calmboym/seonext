# 16 — Output Contracts

**Document:** `16_OUTPUT_CONTRACTS.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** AI Output, Agent Contract & Workflow Data Specification
**Status:** `APPROVED_AS_BASELINE_OUTPUT_CONTRACTS`
**Authority:** Baseline specification for structured outputs, agent-to-workflow contracts, validation, provenance, confidence, errors, versioning, compatibility, and downstream consumption.

---

# 1. Purpose

This document defines the contract system used between:

* AI agents
* deterministic services
* workflows
* the Central Orchestrator
* the shared knowledge layer
* the SEO Decision Engine
* human review
* UI/API consumers
* external integrations

The purpose is to prevent AI-generated information from becoming ambiguous, unvalidated, or structurally incompatible with downstream systems.

The fundamental principle is:

> **An AI output is a typed, versioned, evidence-aware proposal that must pass validation before it becomes trusted system state.**

Structured output improves machine interoperability, but schema validity alone does not establish semantic correctness, truth, authorization, or safety. Therefore output validation must operate at multiple levels.

---

# 2. Core Principle

The output pipeline is:

```text
AI / Service
    ↓
Structured Output
    ↓
Schema Validation
    ↓
Semantic Validation
    ↓
Evidence Validation
    ↓
Business / Domain Validation
    ↓
Policy Validation
    ↓
Confidence / Epistemic State
    ↓
Persisted Artifact
    ↓
Downstream Consumer
```

A syntactically valid JSON object is therefore **not automatically a valid SEO decision**.

---

# 3. Why Output Contracts Exist

Without output contracts, agents may return:

```text
Different field names
Different structures
Missing evidence
Unsupported claims
Inconsistent enums
Different confidence semantics
Unclear failure states
Unversioned outputs
```

This creates downstream ambiguity.

Output contracts provide:

* predictable structure
* type safety
* explicit semantics
* validation
* interoperability
* versioning
* provenance
* observability
* testability
* reproducibility

Schema-based structured outputs are commonly used to make agent results directly consumable by application logic rather than requiring fragile free-form parsing.

---

# 4. Contract Definition

An output contract defines the expected shape and semantics of an output produced by a capability.

Conceptually:

```yaml
contract:
  id:
  version:
  purpose:
  producer:
  consumers:
  input_requirements:
  output_schema:
  semantic_rules:
  evidence_requirements:
  confidence_requirements:
  validation_rules:
  failure_states:
  compatibility:
```

---

# 5. Contract Layers

Contracts exist at several levels.

```text
Capability Contract
        ↓
Agent Contract
        ↓
Step Contract
        ↓
Artifact Contract
        ↓
API Contract
        ↓
UI Consumption Contract
```

These contracts should be related but not unnecessarily duplicated.

---

# 6. Producer vs Consumer

Every contract should identify:

### Producer

The system component creating the output.

Examples:

* Topic Discovery Agent
* SERP Intelligence Agent
* Decision Engine

### Consumer

The component using the output.

Examples:

* next workflow step
* database persistence
* human review
* UI
* another deterministic service

This creates an explicit producer-consumer boundary.

---

# 7. Contract Ownership

Every contract must have an owner.

Conceptually:

```text
contract.owner:
  type:
  component:
```

The owner is responsible for:

* semantic correctness
* versioning
* compatibility
* validation rules
* migration strategy
* documentation
* test coverage

---

# 8. Contract Versioning

Contracts must be versioned.

Example:

```text
topic.discovery.output@1.0
topic.discovery.output@1.1
topic.discovery.output@2.0
```

Versioning prevents downstream consumers from silently breaking when an output changes.

---

# 9. Versioning Rules

A change may be considered backward-compatible when it does not invalidate existing consumers.

Examples may include:

* adding optional metadata
* adding non-breaking provenance fields
* adding optional diagnostic information

Potentially breaking changes include:

* renaming required fields
* changing field types
* changing enum semantics
* removing required fields
* changing meaning of an existing field

Breaking changes should require a new major contract version.

---

# 10. Schema vs Semantics

A contract must distinguish:

```text
Schema Validity
```

from:

```text
Semantic Validity
```

Example:

```json
{
  "topic": "best shoes",
  "business_relevance": "high"
}
```

may be schema-valid while still being semantically incorrect for the project.

Therefore:

```text
Schema Validation ≠ Truth Validation
```

Structured-output systems similarly distinguish schema validation from application-level validation.

---

# 11. Three Core Validation Gates

The minimum validation architecture is:

```text
Gate 1 — Shape
Gate 2 — Meaning
Gate 3 — Persistence / Action
```

## Gate 1 — Shape

Does the output conform to the schema?

## Gate 2 — Meaning

Does it satisfy domain, evidence, identity, and business rules?

## Gate 3 — Persistence / Action

Is the system authorized and able to safely store or execute it?

A schema-valid output must not bypass Gates 2 and 3.

---

# 12. Canonical Output Envelope

All major agent outputs should use a common conceptual envelope.

```yaml
output:
  contract:
    id:
    version:

  execution:
    workflow_run_id:
    step_id:
    agent_id:
    agent_version:
    model:
    prompt_version:

  status:

  data:

  evidence:

  confidence:

  epistemic_state:

  assumptions:

  warnings:

  conflicts:

  validation:

  provenance:

  recommendations:

  created_at:
```

The exact implementation schema may differ, but these semantic categories must remain available where applicable.

---

# 13. Output Status

Output status represents execution/result state.

Recommended values:

```text
SUCCESS
PARTIAL
INCOMPLETE
REQUIRES_REVIEW
FAILED
REJECTED
CONFLICTED
```

Status must not be confused with epistemic state.

---

# 14. Epistemic State

The system uses:

```text
OBSERVED
INFERRED
ESTIMATED
RECOMMENDED
HUMAN_APPROVED
CONFLICTED
UNKNOWN
```

Examples:

```text
SERP contains product pages
→ OBSERVED

Intent is likely commercial
→ INFERRED

Search demand estimate
→ ESTIMATED

Create dedicated page
→ RECOMMENDED

Human accepts recommendation
→ HUMAN_APPROVED
```

---

# 15. Confidence

Confidence expresses uncertainty in an analytical result.

Example:

```yaml
confidence:
  score: 0.84
  level: HIGH
  basis:
    - strong_serp_signal
    - consistent_entity_relationship
```

Confidence must never imply authority.

```text
confidence = 0.99
```

does not mean:

```text
human approval = true
```

---

# 16. Confidence Semantics

Confidence should be:

* bounded
* consistently interpreted
* versioned
* explainable
* evaluated against outcomes

The system should avoid false precision.

For example:

```text
0.873421
```

may suggest more certainty than the evidence supports.

Where appropriate, use:

```text
LOW
MEDIUM
HIGH
```

alongside or instead of numerical scores.

---

# 17. Confidence Calibration

Confidence values should eventually be evaluated against actual outcomes.

Example:

```text
AI confidence = 0.90
Actual correctness = low
```

indicates calibration problems.

The system should therefore monitor:

* confidence vs correctness
* confidence vs human approval
* confidence vs downstream outcome

---

# 18. Evidence Contract

Important claims should reference evidence.

Conceptual structure:

```yaml
evidence:
  - id:
    type:
    source:
    source_reference:
    observed_at:
    freshness:
    excerpt_or_fact:
    reliability:
```

Evidence may originate from:

* SERP
* search provider
* website
* database
* analytics
* business input
* human input
* external source
* previously validated project knowledge

---

# 19. Evidence Reference vs Evidence Copy

Outputs should generally reference canonical evidence rather than duplicate large evidence payloads.

Example:

```yaml
evidence_refs:
  - evidence_123
  - evidence_456
```

The canonical evidence remains in the shared knowledge/evidence layer.

---

# 20. Provenance

Every derived output should preserve its origin.

Conceptually:

```text
Source
 ↓
Observation
 ↓
Normalization
 ↓
Inference
 ↓
Recommendation
 ↓
Human Decision
```

A recommendation should therefore be traceable to upstream observations.

---

# 21. Provenance Contract

```yaml
provenance:
  sources:
    - id:
  derived_from:
    - artifact_id:
  generated_by:
    component:
    version:
  generated_at:
  transformations:
    - type:
      version:
```

---

# 22. Assumptions

When an output depends on assumptions, they should be explicit.

Example:

```yaml
assumptions:
  - id: A1
    statement: >
      The supplied domain represents the primary business website.
    confidence: medium
```

Assumptions must not be presented as observed facts.

---

# 23. Warnings

Warnings communicate non-blocking concerns.

Examples:

```text
STALE_SERP_DATA
LIMITED_QUERY_SAMPLE
LOW_ENTITY_CONFIDENCE
PARTIAL_PROVIDER_DATA
MISSING_OPTIONAL_CONTEXT
```

Warnings should remain visible to downstream consumers where relevant.

---

# 24. Conflicts

Conflicts must be represented explicitly.

Example:

```yaml
conflicts:
  - id:
    type: intent_conflict
    sources:
      - source_a
      - source_b
    description:
    resolution_status:
```

The system must not silently choose one interpretation when conflict materially affects the result.

---

# 25. Validation Result

Validation should be structured.

```yaml
validation:
  status:
  schema:
    passed:
  semantic:
    passed:
  evidence:
    passed:
  domain:
    passed:
  policy:
    passed:
  errors:
  warnings:
```

---

# 26. Validation States

Recommended states:

```text
NOT_VALIDATED
VALIDATING
VALID
INVALID
PARTIALLY_VALID
REQUIRES_REVIEW
```

---

# 27. Validation Errors

Validation errors should identify:

* contract
* field
* rule
* severity
* message
* remediation

Example:

```yaml
error:
  code: INVALID_ENTITY_REFERENCE
  field: entity_id
  severity: BLOCKING
  message: >
    Referenced entity does not exist in the current project.
```

---

# 28. Error Contract

Failures should be machine-readable.

Conceptual structure:

```yaml
error:
  code:
  category:
  message:
  retryable:
  severity:
  step_id:
  contract_id:
  details:
  recovery:
```

---

# 29. Error Categories

Recommended categories:

```text
SCHEMA_ERROR
SEMANTIC_ERROR
EVIDENCE_ERROR
AUTHORIZATION_ERROR
DEPENDENCY_ERROR
PROVIDER_ERROR
TIMEOUT
RATE_LIMIT
DATA_CONFLICT
LOW_CONFIDENCE
POLICY_VIOLATION
SYSTEM_ERROR
UNKNOWN_ERROR
```

---

# 30. Retryability

Every failure should indicate whether retrying is appropriate.

```yaml
retry:
  retryable: true
  max_attempts:
  strategy:
```

Not every invalid AI output should trigger unlimited retries.

---

# 31. Structured Refusal

An agent must be able to explicitly decline to produce a substantive result.

Example:

```yaml
status: INCOMPLETE

reason:
  code: INSUFFICIENT_EVIDENCE

message:
  "Available evidence is insufficient to determine dominant intent."
```

This is preferable to inventing an answer.

---

# 32. Partial Output

Some workflows may produce partial results.

Example:

```yaml
status: PARTIAL

data:
  analyzed_topics: 82
  pending_topics: 18
```

Partial output must clearly identify:

* completed portion
* missing portion
* reason
* downstream limitations

---

# 33. Empty Output

An empty result is not necessarily a failure.

Examples:

```text
No valid topics discovered.
No SERP results available.
No cannibalization detected.
No content gap detected.
```

The contract should distinguish:

```text
VALID_EMPTY_RESULT
```

from:

```text
FAILED_TO_PRODUCE_RESULT
```

---

# 34. Null Semantics

Null values must have defined meaning.

For example:

```text
null = unknown
```

must not automatically mean:

```text
false
```

or:

```text
not applicable
```

Where semantic distinctions matter, explicit enums should be used.

---

# 35. Enum Discipline

Controlled fields should use defined enums.

Example:

```yaml
epistemic_state:
  enum:
    - OBSERVED
    - INFERRED
    - ESTIMATED
    - RECOMMENDED
    - HUMAN_APPROVED
    - CONFLICTED
    - UNKNOWN
```

Free-form strings should not replace controlled states where downstream logic depends on them.

---

# 36. IDs

All major objects should use stable identifiers.

Examples:

```text
entity_id
topic_id
keyword_id
query_id
serp_snapshot_id
page_id
cluster_id
decision_id
evidence_id
workflow_run_id
artifact_id
```

IDs should remain stable across non-destructive updates.

---

# 37. References

Outputs should reference canonical objects.

Example:

```yaml
topic_refs:
  - topic_123
  - topic_456

entity_refs:
  - entity_abc

page_refs:
  - page_789
```

Consumers should not have to infer identity from names.

---

# 38. Localization

Outputs must support multilingual projects.

Where applicable, distinguish:

```text
canonical concept
localized label
localized query
language
market
search context
```

A translated string must not automatically be treated as the same search query or same intent.

---

# 39. Search Context Contract

Search-related outputs should preserve:

```yaml
search_context:
  language:
  country:
  region:
  device:
  search_engine:
  market:
  observed_at:
```

This is essential because the same query may have different SERPs and intent distributions across contexts.

---

# 40. Entity Output Contract

Example conceptual output:

```yaml
entity_result:
  entity:
    id:
    canonical_name:
    type:
    aliases:

  relationships:
    - source_entity_id:
      relation:
      target_entity_id:
      confidence:

  evidence_refs:
    - evidence_id

  confidence:
    score:

  epistemic_state:
```

---

# 41. EAV Output Contract

```yaml
eav_result:
  facts:
    - entity_id:
      attribute:
      value:
      value_type:
      confidence:
      epistemic_state:
      evidence_refs:
```

The contract must preserve whether a value is:

* observed
* inferred
* estimated
* human-approved

---

# 42. Topic Discovery Output Contract

```yaml
topic_discovery_result:
  topics:
    - topic_id:
      canonical_topic:
      description:
      entities:
      attributes:
      user_need:
      business_relevance:
      evidence_refs:
      confidence:
      epistemic_state:
```

A discovered topic is not automatically approved.

---

# 43. Topic Validation Output Contract

```yaml
topic_validation_result:
  topic_id:
  status:
  validation_factors:
    business_relevance:
    semantic_validity:
    search_evidence:
    serp_evidence:
    existing_coverage:
  confidence:
  evidence_refs:
  recommendation:
```

---

# 44. Query Discovery Output Contract

```yaml
query_discovery_result:
  queries:
    - query_id:
      raw_query:
      normalized_query:
      canonical_query:
      language:
      search_context:
      source:
      source_type:
      validation_state:
      evidence_refs:
```

AI-generated queries must be distinguishable from observed queries.

---

# 45. Intent Output Contract

```yaml
intent_result:
  query_id:
  intents:
    - type:
      probability:
  dominant_intent:
  intent_distribution:
  evidence_refs:
  confidence:
  epistemic_state:
  conflicts:
```

Intent must not be represented as an unexplained single label when the evidence indicates mixed intent.

---

# 46. SERP Output Contract

```yaml
serp_result:
  snapshot_id:
  query_id:
  search_context:
  captured_at:

  results:
    - position:
      result_type:
      url:
      domain:
      title:
      page_type:
      content_format:

  features:
    - type:
      position:
      evidence_ref:

  intent_signals:
  competitor_signals:
  similarity_features:

  evidence_refs:
  confidence:
```

---

# 47. Topic Clustering Output Contract

```yaml
clustering_result:
  clusters:
    - cluster_id:
      label:
      topic_refs:
      query_refs:
      similarity:
      intent_alignment:
      serp_similarity:
      entity_overlap:
      cluster_confidence:
      cluster_status:

  unclustered:
    - topic_id

  evidence_refs:
```

The contract must support unclustered items.

---

# 48. Page Candidate Output Contract

```yaml
page_candidate_result:
  candidates:
    - page_candidate_id:
      topic_refs:
      query_refs:
      intent:
      recommended_page_type:
      existing_page_refs:
      rationale:
      confidence:
      evidence_refs:
      status:
```

This output is a recommendation, not an approved page architecture.

---

# 49. Page Architecture Output Contract

```yaml
page_architecture_result:
  architecture:
    - page_id:
      page_type:
      parent_page_id:
      topic_refs:
      intent:
      purpose:
      relationships:

  risks:
  alternatives:
  evidence_refs:
  confidence:
  recommendation_status:
```

Human approval may be required before the architecture becomes authoritative.

---

# 50. Internal Linking Output Contract

```yaml
internal_linking_result:
  recommendations:
    - source_page_id:
      target_page_id:
      anchor_concept:
      relationship_type:
      rationale:
      confidence:
      evidence_refs:
      risk_level:
```

---

# 51. Content Gap Output Contract

```yaml
content_gap_result:
  gaps:
    - gap_id:
      topic_refs:
      missing_page_type:
      evidence_refs:
      business_value:
      search_opportunity:
      confidence:
      recommendation:
```

A content gap does not automatically imply publishing.

---

# 52. Cannibalization Output Contract

```yaml
cannibalization_result:
  cases:
    - case_id:
      page_refs:
      topic_refs:
      query_refs:
      overlap_signals:
      intent_similarity:
      serp_similarity:
      severity:
      confidence:
      recommendation:
      evidence_refs:
```

The output should support:

```text
NO_CANNIBALIZATION
POSSIBLE
LIKELY
CONFIRMED
```

where the system's validation framework supports those distinctions.

---

# 53. Competitor Intelligence Output Contract

```yaml
competitor_result:
  competitors:
    - competitor_id:
      domain:
      competitor_type:
      entities:
      topics:
      pages:
      search_presence:
      evidence_refs:
      confidence:
```

The contract must distinguish:

```text
Business Competitor
```

from:

```text
Search Competitor
```

---

# 54. Decision Support Output Contract

```yaml
decision_result:
  decision_candidate:
    id:
    type:
    subject:
    recommendation:

  decision_factors:
    - factor:
      value:
      evidence_refs:

  alternatives:
    - option:
      benefits:
      risks:
      confidence:

  confidence:
  epistemic_state:
  risks:
  conflicts:
  evidence_refs:
  human_review_required:
```

---

# 55. Human Decision Output Contract

Human decisions must be represented separately.

```yaml
human_decision:
  decision_id:
  artifact_id:
  reviewer_id:
  action:
  rationale:
  scope:
  previous_decision_id:
  evidence_refs:
  created_at:
```

Possible actions:

```text
APPROVE
REJECT
MODIFY
MERGE
SPLIT
DEFER
OVERRIDE
REQUEST_MORE_EVIDENCE
ESCALATE
CANCEL
```

---

# 56. Workflow Step Output Contract

Every workflow step should return a standard execution envelope.

```yaml
step_output:
  step_id:
  status:
  artifact_refs:
  output_contract:
    id:
    version:
  validation:
  evidence_refs:
  confidence:
  errors:
  warnings:
  next_state:
```

---

# 57. Workflow Completion Contract

A workflow completion result should include:

```yaml
workflow_result:
  workflow_run_id:
  workflow_id:
  workflow_version:
  status:
  completed_steps:
  failed_steps:
  pending_steps:
  artifact_refs:
  decision_refs:
  human_review_status:
  evidence_summary:
  warnings:
  errors:
  completion_reason:
```

---

# 58. Artifact Contract

An artifact should expose:

```yaml
artifact:
  id:
  type:
  version:
  status:
  source_workflow_run:
  source_step:
  created_at:
  updated_at:
  provenance:
  validation:
  epistemic_state:
```

---

# 59. Artifact Lifecycle

Artifacts may move through:

```text
DRAFT
AI_PROPOSED
VALIDATED
UNDER_REVIEW
HUMAN_APPROVED
REJECTED
SUPERSEDED
ARCHIVED
```

Not every artifact type requires every state.

---

# 60. Contract Validation Pipeline

The complete pipeline is:

```text
Raw Model Output
       ↓
Parse
       ↓
Schema Validation
       ↓
Reference Validation
       ↓
Semantic Validation
       ↓
Evidence Validation
       ↓
Domain Validation
       ↓
Policy Validation
       ↓
Confidence Evaluation
       ↓
Persist / Reject / Review
```

---

# 61. Schema Validation

Schema validation checks:

* required fields
* data types
* object structure
* arrays
* enums
* formats
* references where encoded in schema

Schema validation should happen before business logic consumes the output.

Modern agent runtimes can enforce typed output schemas and validate the final result against those schemas.

---

# 62. Semantic Validation

Semantic validation checks:

```text
Does the entity exist?
Does the topic belong to this project?
Is the relationship valid?
Is the page reference valid?
Is the intent compatible with evidence?
Does the recommendation violate known constraints?
```

---

# 63. Evidence Validation

Evidence validation checks:

* required evidence exists
* evidence references are valid
* evidence is relevant
* evidence is sufficiently fresh
* source provenance exists
* claims do not exceed evidence

---

# 64. Business Validation

Business validation checks:

* business relevance
* strategic constraints
* market scope
* commercial priorities
* approved terminology
* excluded topics
* strategic exceptions

---

# 65. Policy Validation

Policy validation checks:

* authorization
* permissions
* allowed actions
* tool restrictions
* workflow rules
* human approval requirements

---

# 66. Write Gate

Before an output becomes durable project state:

```text
Validated Output
      ↓
Write Policy
      ↓
Authorized?
   ├── yes → persist
   └── no  → reject / review
```

The system must not write arbitrary AI output directly into canonical knowledge.

---

# 67. Staging

AI-generated changes should often be staged before becoming canonical.

Example:

```text
AI Proposal
    ↓
Staging
    ↓
Validation
    ↓
Human Review
    ↓
Canonical State
```

This is particularly important for:

* entity merges
* page architecture
* strategic decisions
* large-scale changes

---

# 68. Canonical State

Only validated or approved data should become canonical according to the artifact's governance rules.

For example:

```text
AI topic candidate
≠
Approved topic
```

and:

```text
AI page recommendation
≠
Approved page architecture
```

---

# 69. Contract Compatibility

Consumers must declare which contract versions they support.

Example:

```yaml
consumer:
  supported_contracts:
    - topic.discovery.output@1.x
```

Compatibility checks should occur before workflow execution when practical.

---

# 70. Contract Negotiation

Future systems may support negotiation between:

```text
Producer
```

and:

```text
Consumer
```

For example:

```text
Producer supports:
1.0
1.1
2.0

Consumer supports:
1.0
1.1

Selected:
1.1
```

MVP may use centrally registered contracts instead of runtime negotiation.

---

# 71. Contract Migration

When a breaking contract changes:

```text
Contract v1
     ↓
Migration Adapter
     ↓
Contract v2
```

Adapters should be explicit.

Silent shape conversion is prohibited when semantics may change.

---

# 72. Contract Registry

The system should maintain a registry containing:

```text
Contract ID
Version
Owner
Schema
Semantic Rules
Producer
Consumers
Compatibility
Status
Created At
Deprecated At
```

---

# 73. Contract Status

Recommended:

```text
DRAFT
ACTIVE
DEPRECATED
RETIRED
```

Only `ACTIVE` contracts should be used for new production workflows.

---

# 74. Contract Deprecation

A deprecated contract should:

* remain readable where required
* have migration guidance
* identify replacement version
* record deprecation date
* prevent new dependencies when appropriate

Historical workflow runs must remain interpretable.

---

# 75. Contract Testing

Every contract should have automated tests.

Test:

* valid output
* missing required field
* invalid type
* invalid enum
* invalid reference
* invalid semantic relationship
* missing evidence
* invalid confidence
* invalid state
* incompatible version

---

# 76. Golden Outputs

The system should maintain representative valid outputs.

Example:

```text
golden_topic_discovery.json
golden_intent_result.json
golden_serp_result.json
golden_page_mapping.json
```

These become regression fixtures.

---

# 77. Negative Fixtures

The test suite must also contain intentionally invalid outputs.

Examples:

```text
missing evidence
wrong entity ID
invalid intent
unknown topic
malformed confidence
conflicting state
unauthorized recommendation
```

The system should reject them appropriately.

---

# 78. Contract Regression

Whenever:

* agent prompts change
* models change
* tools change
* workflows change
* schemas change

contract tests must run.

---

# 79. AI Output Repair

The system may attempt limited repair for formatting failures.

Example:

```text
Invalid JSON
    ↓
Controlled repair
    ↓
Validation
```

Repair must not silently change semantic content.

If semantic validity remains uncertain:

```text
REQUIRES_REVIEW
```

or:

```text
FAILED
```

should be returned.

---

# 80. Retry Policy for Invalid Outputs

A limited retry may be appropriate when:

```text
schema invalid
missing required field
format violation
```

Retries should be:

* bounded
* observable
* counted
* cost-controlled

If repeated attempts fail, the workflow should fail or request review.

Structured-output systems commonly treat failure to satisfy the schema after bounded retries as an error rather than returning unvalidated data.

---

# 81. No Silent Coercion

The system should avoid dangerous implicit conversions.

Example:

```text
"42"
```

must not automatically become:

```text
42
```

if the semantic meaning matters and the contract expects a number.

Any coercion must be explicit and tested.

---

# 82. No Silent Defaults

Defaults should be declared in the contract.

A missing:

```text
confidence
```

must not silently become:

```text
confidence = 1.0
```

Likewise, missing evidence must not silently become an empty evidence list while retaining a successful status.

---

# 83. Output Completeness

Contracts should define which fields are:

```text
REQUIRED
OPTIONAL
CONDITIONAL
DERIVED
SYSTEM_GENERATED
```

This prevents ambiguity around missing information.

---

# 84. Conditional Requirements

Some fields may be required only under specific conditions.

Example:

```text
If epistemic_state = INFERRED
→ evidence_refs required

If status = REQUIRES_REVIEW
→ review_reason required

If recommendation exists
→ decision_factors required
```

---

# 85. Cross-Field Validation

Some rules cannot be expressed through simple field types.

Examples:

```text
status = SUCCESS
requires validation.status = VALID
```

or:

```text
epistemic_state = HUMAN_APPROVED
requires human_decision_ref
```

These are semantic contract rules.

---

# 86. Output and Human Approval

An output should never claim:

```text
HUMAN_APPROVED
```

unless a valid human decision exists.

Likewise:

```text
authorized_action = true
```

requires an actual authorization record.

---

# 87. Output and Existing Decisions

When output conflicts with an existing approved decision, the output should contain:

```yaml
conflicts:
  - type: existing_decision_conflict
    decision_id:
    description:
```

The workflow may then route to human review.

---

# 88. Output and Historical Data

Outputs should be aware of temporal state.

For search-derived outputs:

```text
observed_at
```

is required.

For historical comparisons:

```text
comparison_period
```

should be explicit.

---

# 89. Output Freshness

Outputs derived from time-sensitive data should expose freshness.

Example:

```yaml
freshness:
  observed_at:
  valid_until:
  status:
```

Possible status:

```text
FRESH
AGING
STALE
UNKNOWN
```

---

# 90. Output and Search Reality

Search intelligence outputs should preserve:

```text
query
search_context
SERP snapshot
provider
capture time
```

This prevents a generic query result from being interpreted as universal search truth.

---

# 91. Output and Business Reality

Strategic recommendations should preserve business context.

Example:

```yaml
business_context:
  market:
  audience:
  product:
  priority:
  constraints:
```

This ensures a recommendation can be understood in its original strategic context.

---

# 92. Output and Knowledge Graph

Outputs should use stable references to:

* entities
* relationships
* attributes
* topics
* pages
* queries
* evidence

This allows downstream systems to enrich the shared knowledge graph without duplicating canonical objects.

---

# 93. Output and UI

The UI should consume structured outputs rather than parse agent prose.

For example:

```text
Decision Card
    ├── Recommendation
    ├── Confidence
    ├── Evidence
    ├── Risks
    ├── Alternatives
    └── Approval
```

This allows the interface to remain consistent even when model providers change.

---

# 94. Output and API

API responses should expose stable contracts.

The API should not directly expose raw model responses as the primary application interface.

Preferred:

```text
Model Output
    ↓
Internal Contract
    ↓
Validated Application Object
    ↓
API Response Contract
```

---

# 95. Internal vs External Contracts

Not every internal model should become a public API contract.

Distinguish:

```text
AI Internal Contract
Application Contract
Persistence Contract
Public API Contract
UI Contract
```

Adapters may translate between them.

---

# 96. Provider Independence

Output contracts must not depend unnecessarily on a particular model provider.

For example, the application should not require provider-specific response structures.

Preferred:

```text
Provider A
Provider B
Provider C
      ↓
Normalized AI Contract
      ↓
Application
```

---

# 97. Model Independence

Changing the LLM provider or model should not require rewriting the entire application.

The model-specific adapter should transform:

```text
Provider Output
```

into:

```text
Canonical Agent Output
```

---

# 98. Tool Output Contracts

Tools should also have contracts.

Example:

```yaml
tool_output:
  tool_id:
  tool_version:
  status:
  data:
  evidence_refs:
  errors:
  warnings:
```

Tool outputs become evidence/input for agents and workflows.

---

# 99. Agent-to-Agent Contract

Agents should communicate through structured artifacts/contracts.

Example:

```text
Topic Discovery Agent
        ↓
Topic Discovery Output Contract
        ↓
Topic Validation Agent
```

Not:

```text
Agent A
  ↕
Free-form conversation
  ↕
Agent B
```

---

# 100. Orchestrator Contract

The Orchestrator should consume:

```text
Capability Contract
+
Input Contract
+
Output Contract
+
Workflow Policy
```

and produce:

```text
Step Result
+
Artifact References
+
Workflow State
```

---

# 101. Contract and Context Management

Output contracts should identify context dependencies where relevant.

Example:

```yaml
context_requirements:
  required:
    - validated_topics
    - search_context

  optional:
    - competitor_data
```

This integrates with:

`25_CONTEXT_MANAGEMENT.md`

---

# 102. Contract and Skills

When an agent uses an installed skill/tool, the output provenance should identify it where material to the result.

Example:

```yaml
provenance:
  tools:
    - tool_id:
      version:
```

This integrates with:

`26_SKILLS_AND_TOOLING_POLICY.md`

---

# 103. Contract and Observability

Every significant output should be traceable to:

```text
workflow_run
step
agent
agent_version
model
prompt_version
tool_calls
artifact
validation
```

This enables debugging and auditability.

---

# 104. Contract and Cost Tracking

The execution envelope may include:

```yaml
usage:
  input_tokens:
  output_tokens:
  tool_calls:
  provider_calls:
  estimated_cost:
```

Cost metadata should not become part of the semantic result itself unless required.

---

# 105. Contract and Performance

The system should measure:

* schema validation latency
* semantic validation latency
* retry count
* output repair count
* rejection rate
* contract failure rate

High contract failure rates may indicate:

* poor prompting
* inadequate schema design
* model mismatch
* insufficient context
* unclear agent boundaries

---

# 106. Contract Failure Classification

A contract failure should identify its layer.

Example:

```text
SHAPE_FAILURE
MEANING_FAILURE
EVIDENCE_FAILURE
POLICY_FAILURE
WRITE_FAILURE
```

This makes debugging significantly easier.

---

# 107. Output Contract Anti-Patterns

The following are prohibited.

## 107.1 Free-Form-Only Agent Interfaces

Important downstream data must not depend on prose parsing.

## 107.2 Schema Without Semantics

A valid schema does not prove the data is correct.

## 107.3 Unversioned Contracts

Changing field meanings without versioning is prohibited.

## 107.4 Hidden Defaults

Missing data must not silently become arbitrary values.

## 107.5 Missing Provenance

Important inferred results must remain traceable.

## 107.6 Confidence Without Evidence

Confidence must not be presented as unsupported certainty.

## 107.7 Human Approval Fabrication

The system must never mark output human-approved without an actual approval.

## 107.8 Silent Semantic Migration

Changing the meaning of a field without changing its contract version is prohibited.

## 107.9 Direct AI-to-Database Writes

Unvalidated AI output must not become canonical data.

## 107.10 Provider-Leaking Contracts

Application contracts must not unnecessarily depend on a specific AI provider.

---

# 108. MVP Contract Architecture

The MVP should implement:

```text
Contract Registry
        ↓
Agent Output Schemas
        ↓
Schema Validation
        ↓
Semantic Validation
        ↓
Evidence Validation
        ↓
Artifact Persistence
        ↓
Workflow Consumption
```

Recommended implementation technologies may include:

* Python type models
* Pydantic
* JSON Schema
* PostgreSQL persistence
* versioned contract definitions

The exact implementation is governed by `07_TECHNICAL_ARCHITECTURE.md`.

---

# 109. MVP Required Contracts

At minimum:

```text
AgentExecutionResult
WorkflowStepResult
EvidenceReference
EntityResult
EAVResult
TopicDiscoveryResult
TopicValidationResult
QueryDiscoveryResult
IntentResult
SERPResult
ClusteringResult
PageCandidateResult
DecisionCandidateResult
HumanDecisionResult
ArtifactResult
WorkflowResult
ErrorResult
```

---

# 110. Future Contract Capabilities

Future versions may support:

* schema registries
* automatic compatibility testing
* contract migration tools
* generated API types
* generated UI types
* provider-specific adapters
* contract observability dashboards
* automated contract linting
* contract impact analysis
* contract dependency graphs

---

# 111. Contract Governance

Changes to important contracts must follow:

```text
Change Proposal
      ↓
Impact Analysis
      ↓
Compatibility Analysis
      ↓
Schema Update
      ↓
Semantic Rule Update
      ↓
Tests
      ↓
Migration if Required
      ↓
Approval
      ↓
Release
```

---

# 112. Contract Change Impact Analysis

Before changing a contract, identify:

```text
Producers
Consumers
Workflows
Database mappings
API endpoints
UI components
Tests
Historical artifacts
Migration requirements
```

No breaking change should be introduced without understanding its downstream impact.

---

# 113. Contract Documentation

Each active contract should document:

* purpose
* owner
* version
* fields
* semantics
* required fields
* enums
* validation rules
* evidence requirements
* examples
* failure cases
* compatibility
* consumers

---

# 114. Contract Examples

Examples should include both:

### Valid

```json
{
  "status": "SUCCESS",
  "confidence": 0.84,
  "epistemic_state": "INFERRED",
  "evidence_refs": ["evidence_123"]
}
```

### Invalid

```json
{
  "status": "SUCCESS",
  "confidence": "very sure"
}
```

The latter fails schema validation.

But even this:

```json
{
  "status": "SUCCESS",
  "confidence": 0.99,
  "evidence_refs": []
}
```

may be schema-valid while failing evidence validation.

---

# 115. Contract Decision Rule

The system should follow:

```text
Schema Valid
    ↓
Not necessarily Correct
    ↓
Semantic Validation
    ↓
Not necessarily Authorized
    ↓
Policy Validation
    ↓
Not necessarily Strategically Approved
    ↓
Human Decision when Required
```

---

# 116. Output Contract Operating Model

The complete model is:

```text
                  AI / TOOL
                     │
                     ▼
              Structured Output
                     │
                     ▼
              Schema Validation
                     │
                     ▼
             Semantic Validation
                     │
                     ▼
              Evidence Validation
                     │
                     ▼
               Domain Validation
                     │
                     ▼
              Policy Validation
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Valid                  Invalid
          │                     │
          ▼                     ▼
    Persist / Review       Reject / Retry
          │
          ▼
      Artifact
          │
          ▼
   Workflow Consumer
          │
          ▼
   Decision Engine
          │
          ▼
    Human Review
          │
          ▼
    Approved State
```

---

# 117. Non-Negotiable Output Contract Rules

The following rules are mandatory:

1. Important agent outputs must use structured contracts.
2. Contracts must be versioned.
3. Schemas must be machine-validatable.
4. Schema validity must not be treated as semantic truth.
5. Semantic validation is mandatory for important outputs.
6. Evidence requirements must be explicit.
7. Provenance must be preserved.
8. Confidence must be distinct from authority.
9. Epistemic state must remain explicit.
10. Human approval must never be fabricated.
11. Missing evidence must not be hidden.
12. Conflicts must remain visible.
13. Partial results must be explicit.
14. Failures must be machine-readable.
15. Retryability must be explicit.
16. Structured refusal must be supported.
17. Empty valid results must be distinguishable from failures.
18. IDs must be stable.
19. References must point to canonical objects.
20. Cross-field semantic rules must be enforced.
21. AI output must not directly become canonical state without validation.
22. Public application contracts should remain provider-independent.
23. Agent-to-agent communication must use structured contracts.
24. Contract changes require impact analysis.
25. Breaking changes require version changes.
26. Historical artifacts must remain interpretable.
27. Contract tests are mandatory.
28. Negative fixtures are mandatory for critical contracts.
29. Context requirements must be explicit where relevant.
30. Tool and model provenance must be preserved where material.
31. High-impact outputs must include decision factors and risks.
32. Recommendations must remain distinct from decisions.
33. Human decisions must remain distinct from AI outputs.
34. Contract validation must fail closed for critical integrity violations.
35. No output contract may be used to conceal uncertainty.

---

# 118. Definition of Done

The output contract architecture is considered implemented correctly when:

* active contracts are registered
* contracts are versioned
* agent outputs are structured
* schemas are validated
* semantic validation exists
* evidence validation exists
* policy validation exists
* confidence semantics are defined
* epistemic states are enforced
* provenance is persisted
* errors are structured
* partial results are supported
* refusals are supported
* empty valid results are supported
* stable IDs are used
* artifact references are validated
* cross-field rules are enforced
* contract compatibility is tested
* golden fixtures exist
* negative fixtures exist
* regression tests exist
* contract changes are governed
* provider-specific output is normalized
* human approval is represented explicitly
* AI recommendations cannot silently become approved decisions
* downstream workflows consume validated contracts
* auditability exists

---

# 119. Final Contract Model

The intended architecture is:

```text
                    EXTERNAL / AI WORLD
                           │
                           ▼
                 Provider / Tool Output
                           │
                           ▼
                  Canonical AI Adapter
                           │
                           ▼
                 Versioned Output Contract
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Schema Validation         Contract Compatibility
              │
              ▼
       Semantic Validation
              │
              ▼
        Evidence Validation
              │
              ▼
         Domain Validation
              │
              ▼
        Policy Validation
              │
       ┌──────┴──────┐
       ▼             ▼
    Valid          Invalid
       │             │
       ▼             ▼
   Artifact      Retry / Reject /
       │          Review / Escalate
       ▼
    Workflow
       │
       ▼
 Decision Engine
       │
       ▼
 Human Review
       │
       ▼
 Approved Decision
       │
       ▼
 Living SEO Knowledge
```

The output-contract system therefore serves as the **typed integrity boundary between probabilistic AI behavior and deterministic application behavior**.

Its job is not merely to force models to return JSON.

Its deeper purpose is to ensure that every important AI-produced object has:

**structure, semantics, provenance, evidence, confidence, versioning, validation, and an explicit authority state.**

---

# 120. Document Control

```yaml
document:
  id: "16"
  filename: "16_OUTPUT_CONTRACTS.md"
  status: "APPROVED_AS_BASELINE_OUTPUT_CONTRACTS"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

purpose:
  - structured_agent_outputs
  - workflow_contracts
  - validation
  - provenance
  - interoperability
  - versioning
  - auditability

core_layers:
  - schema_validation
  - semantic_validation
  - evidence_validation
  - domain_validation
  - policy_validation
  - persistence_validation

core_epistemic_states:
  - OBSERVED
  - INFERRED
  - ESTIMATED
  - RECOMMENDED
  - HUMAN_APPROVED
  - CONFLICTED
  - UNKNOWN

core_output_statuses:
  - SUCCESS
  - PARTIAL
  - INCOMPLETE
  - REQUIRES_REVIEW
  - FAILED
  - REJECTED
  - CONFLICTED

core_artifact_states:
  - DRAFT
  - AI_PROPOSED
  - VALIDATED
  - UNDER_REVIEW
  - HUMAN_APPROVED
  - REJECTED
  - SUPERSEDED
  - ARCHIVED

core_contracts:
  - AgentExecutionResult
  - WorkflowStepResult
  - EvidenceReference
  - EntityResult
  - EAVResult
  - TopicDiscoveryResult
  - TopicValidationResult
  - QueryDiscoveryResult
  - IntentResult
  - SERPResult
  - ClusteringResult
  - PageCandidateResult
  - DecisionCandidateResult
  - HumanDecisionResult
  - ArtifactResult
  - WorkflowResult
  - ErrorResult

validation_model:
  shape: "schema"
  meaning: "semantic + domain + evidence"
  action: "policy + authorization + write_gate"

architecture:
  contract_registry: true
  versioned_contracts: true
  provider_independent_application_contracts: true
  structured_agent_communication: true
  direct_unvalidated_ai_to_canonical_state: false

authority:
  recommendation: "ai_or_decision_engine"
  strategic_decision: "human"
  consequential_action: "authorized_human_or_policy"

primary_dependencies:
  - "13_AGENT_SPECIFICATIONS.md"
  - "14_AGENT_WORKFLOW.md"
  - "15_HUMAN_IN_THE_LOOP.md"

related:
  - "03_MASTER_RULES.md"
  - "04_SYSTEM_ARCHITECTURE.md"
  - "05_AI_AGENT_ARCHITECTURE.md"
  - "06_DATA_ARCHITECTURE.md"
  - "07_TECHNICAL_ARCHITECTURE.md"
  - "08_SEO_KNOWLEDGE_MODEL.md"
  - "09_ENTITY_EAV_MODEL.md"
  - "10_TOPIC_MODELING_AND_CLUSTERING.md"
  - "11_SEARCH_AND_SERP_INTELLIGENCE.md"
  - "12_SEO_DECISION_ENGINE.md"
  - "13_AGENT_SPECIFICATIONS.md"
  - "14_AGENT_WORKFLOW.md"
  - "15_HUMAN_IN_THE_LOOP.md"
  - "21_DEVELOPMENT_AND_DEBUG.md"
  - "22_TESTING_AND_VALIDATION.md"
  - "25_CONTEXT_MANAGEMENT.md"
  - "26_SKILLS_AND_TOOLING_POLICY.md"
```
