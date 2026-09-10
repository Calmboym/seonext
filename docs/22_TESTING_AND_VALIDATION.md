# 22 — Testing and Validation

**Document:** `22_TESTING_AND_VALIDATION.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Testing, Validation, Quality Assurance, AI Evaluation & Verification Specification
**Status:** `APPROVED_AS_BASELINE_TESTING_AND_VALIDATION`
**Authority:** Baseline specification for software testing, AI evaluation, data validation, workflow verification, contract testing, security testing, regression testing, runtime validation, and release-quality assessment.

---

# 1. Purpose

This document defines how correctness, reliability, safety, quality, and production readiness are tested and validated across the SEO Research & Strategy Copilot / SEO Decision Engine.

The system cannot be considered reliable merely because:

* the application starts;
* the API responds;
* the frontend renders;
* unit tests pass;
* an LLM produces plausible text;
* a workflow completes;
* a provider returns data.

Testing must establish that the system produces **correct, valid, evidence-supported, authorized, reproducible-enough, and appropriately bounded behavior**.

The central principle is:

```text
Implementation
    ↓
Testing
    ↓
Validation
    ↓
Evidence
    ↓
Verification
    ↓
Confidence in System Behavior
```

---

# 2. Core Testing Philosophy

The system follows:

```text
Test the Code
+
Test the Data
+
Test the Contracts
+
Test the AI
+
Test the Workflow
+
Test the Integrations
+
Test the Security
+
Test the User Experience
+
Test the System as a Whole
```

No single testing layer is sufficient.

---

# 3. Testing Pyramid

The preferred testing distribution is:

```text
                    E2E
                  /     \
             Workflow / Integration
                /          \
          Contract / AI Evaluation
              /              \
        Domain / Application / Data
                 /       \
               Unit Tests
```

Lower-level tests should be:

* faster;
* more deterministic;
* more numerous.

Higher-level tests should verify system behavior across boundaries.

---

# 4. Validation Is Broader Than Testing

Testing asks:

> Does the implementation behave as expected under defined conditions?

Validation asks:

> Is the behavior actually correct and appropriate for the intended product and domain?

Therefore:

```text
Testing ⊂ Validation
```

A system can pass technical tests while failing domain validation.

Example:

```text
SERP parser:
100% unit tests pass
```

but:

```text
SERP intent classification:
businessly incorrect
```

The second problem requires domain/AI validation.

---

# 5. Quality Model

System quality should be evaluated across:

```text
Correctness
Reliability
Consistency
Evidence Support
Semantic Validity
Security
Performance
Cost
Freshness
Explainability
Recoverability
Usability
Accessibility
Maintainability
```

---

# 6. Test Categories

The project should support:

1. Unit Testing
2. Domain Testing
3. Application Testing
4. Data Testing
5. Contract Testing
6. Integration Testing
7. AI Module Testing
8. Agent Testing
9. Workflow Testing
10. Retrieval Testing
11. Search/SERP Testing
12. Frontend Testing
13. API Testing
14. Security Testing
15. Performance Testing
16. Cost Testing
17. Evaluation Testing
18. Regression Testing
19. End-to-End Testing
20. Failure and Recovery Testing
21. Accessibility Testing
22. Migration Testing
23. Deployment Verification

---

# 7. Unit Testing

Unit tests verify small deterministic units.

Examples:

* canonicalization;
* entity normalization;
* EAV validation;
* topic scoring;
* intent rule evaluation;
* SERP classification;
* page similarity;
* confidence calculations;
* decision policies.

Unit tests should be:

* fast;
* deterministic;
* isolated;
* easy to diagnose.

Avoid unnecessary external dependencies.

---

# 8. Domain Testing

Domain tests validate SEO and business semantics.

Examples:

```text
Topic ≠ Keyword
Topic ≠ Page
Intent ≠ Query
Entity ≠ Topic
```

Tests should verify that these distinctions remain intact.

Example:

```text
Two semantically related keywords
```

must not automatically produce:

```text
One page
```

unless the relevant page-mapping rules support that conclusion.

---

# 9. Domain Invariants

Important invariants should be explicitly tested.

Examples:

```text
An entity has a stable identity.
An EAV fact references valid entity/attribute/value objects.
A topic belongs to the appropriate project.
A decision references evidence or explicitly records insufficient evidence.
A human approval references an authorized actor.
A workflow cannot transition through an invalid state.
A canonical artifact cannot be silently overwritten.
```

---

# 10. Application Testing

Application tests verify use cases.

Examples:

```text
CreateProject
StartResearch
ValidateTopic
AnalyzeSERP
BuildTopicCluster
GeneratePageCandidates
ApproveRecommendation
```

These tests verify:

* orchestration of domain rules;
* authorization;
* persistence;
* contracts;
* error behavior.

---

# 11. Data Testing

Data testing validates:

* schema;
* constraints;
* relationships;
* uniqueness;
* foreign keys;
* nullability;
* temporal state;
* provenance;
* tenant isolation;
* data types;
* derived data.

Example:

```text
Entity → Topic → Page → Decision
```

must maintain valid references.

---

# 12. Database Integrity Testing

Database tests should verify:

* migrations;
* constraints;
* indexes where behavior depends on them;
* foreign keys;
* unique constraints;
* transactions;
* rollback behavior;
* concurrent updates;
* soft deletion;
* historical records.

Critical persistence operations should be tested under failure conditions.

---

# 13. Transaction Testing

Transactions should be tested for:

```text
Success
Rollback
Partial Failure
Concurrent Access
Constraint Violation
Retry
Idempotent Re-execution
```

A workflow should not leave invalid partial state when an atomic operation is expected.

---

# 14. Multi-Tenant / Project Isolation Testing

The system must verify that:

```text
Project A
≠
Project B
```

for:

* entities;
* topics;
* SERPs;
* evidence;
* pages;
* decisions;
* workflows;
* cached data;
* vector retrieval;
* AI context.

Cross-project data leakage must be treated as a critical defect.

---

# 15. Contract Testing

Contract tests verify that producers and consumers agree.

Examples:

```text
Agent → Output Contract
Backend → API
API → Frontend
Provider Adapter → Normalizer
Workflow Step → Workflow Engine
```

Contract testing must include:

* valid outputs;
* invalid outputs;
* missing fields;
* unexpected fields where relevant;
* enum violations;
* incompatible versions;
* malformed nested objects.

---

# 16. Schema Testing

Every important structured output should be tested against its schema.

Test:

```text
Valid
Invalid
Incomplete
Null
Wrong Type
Wrong Enum
Unexpected Structure
```

Schema validity is necessary but not sufficient.

---

# 17. Semantic Validation Testing

A schema-valid result may still be wrong.

Example:

```json
{
  "topic": "example",
  "confidence": 0.95
}
```

can be structurally valid but semantically unsupported.

Semantic tests should verify:

* entity references;
* relationships;
* topic meaning;
* intent consistency;
* evidence relationships;
* domain constraints.

---

# 18. Evidence Validation Testing

AI recommendations should be tested for evidence support.

Verify:

```text
Claim
→ Evidence
→ Source
→ Context
→ Timestamp
```

Tests should detect:

* missing evidence;
* unrelated evidence;
* stale evidence;
* invalid references;
* unsupported claims.

---

# 19. Epistemic-State Testing

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

Tests must ensure these states are not incorrectly assigned.

Examples:

```text
Provider-reported SERP
→ OBSERVED
```

```text
AI-inferred intent
→ INFERRED
```

```text
AI recommendation
→ RECOMMENDED
```

```text
Conflicting sources
→ CONFLICTED
```

The system must not turn:

```text
INFERRED
```

into:

```text
OBSERVED
```

without evidence.

---

# 20. Confidence Testing

Confidence must not be confused with truth.

Test that confidence reflects defined signals such as:

* evidence quality;
* agreement;
* data completeness;
* model reliability;
* ambiguity;
* retrieval quality.

A system should be able to produce:

```text
LOW CONFIDENCE
```

without treating it as an error.

---

# 21. AI Testing Philosophy

AI outputs require evaluation rather than only traditional assertions.

The test model is:

```text
Input
→ Context
→ Evidence
→ Model
→ Output
→ Validation
→ Evaluation
```

AI testing should assess:

* correctness;
* consistency;
* evidence support;
* structured output adherence;
* relevance;
* business alignment;
* confidence calibration;
* failure behavior.

---

# 22. AI Golden Datasets

Golden datasets should contain reviewed examples.

Examples:

```text
golden/entities/
golden/topics/
golden/intents/
golden/serp/
golden/clusters/
golden/page_mapping/
golden/decisions/
```

Each case should ideally define:

```yaml id="xk9qfs"
input:
expected:
acceptable_variations:
required_evidence:
constraints:
evaluation_notes:
```

Golden datasets must represent realistic diversity.

---

# 23. Golden Outputs Are Not Absolute Truth

AI evaluation should allow acceptable variation.

For example:

Two topic labels may differ linguistically while representing the same underlying concept.

Therefore evaluation should distinguish:

```text
Exact Match
Semantic Match
Acceptable Variation
Incorrect
Unsupported
```

---

# 24. Agent Testing

Every important agent should have:

### Input Tests

* valid input;
* missing input;
* ambiguous input;
* invalid input.

### Context Tests

* sufficient context;
* insufficient context;
* stale context;
* conflicting context.

### Tool Tests

* successful tool;
* tool timeout;
* malformed response;
* permission denial.

### Output Tests

* valid;
* incomplete;
* unsupported;
* conflicting;
* low-confidence.

---

# 25. Agent Boundary Testing

Agents should be tested to ensure they do not exceed responsibilities.

Example:

The Topic Discovery Agent should not silently:

```text
approve a page architecture
```

or:

```text
publish content
```

unless explicitly authorized by architecture and workflow rules.

---

# 26. Agent Failure Testing

Test failures such as:

```text
LLM timeout
LLM malformed output
Provider unavailable
Tool failure
Context unavailable
Database failure
Validation rejection
Permission denial
Budget exceeded
```

Expected behavior must be defined.

---

# 27. Agent Idempotency Testing

If the same task executes twice with the same idempotency key:

```text
Run A
Run A duplicate
```

the system should not create unintended duplicate artifacts.

Test:

* duplicate requests;
* retries;
* worker restarts;
* workflow resumes.

---

# 28. Workflow Testing

Workflows must be tested as stateful systems.

Test:

```text
Start
→ Execute
→ Complete
```

and:

```text
Start
→ Failure
→ Retry
→ Resume
→ Complete
```

and:

```text
Start
→ Human Review
→ Approval
→ Continue
```

---

# 29. Workflow State Testing

Test every valid state transition.

Also test invalid transitions.

Example:

```text
COMPLETED → RUNNING
```

should normally be rejected.

---

# 30. Workflow Recovery Testing

Test:

* worker crash;
* provider timeout;
* database failure;
* process restart;
* queue duplication;
* partial completion;
* human review pause;
* retry exhaustion.

The expected recovery path must be explicit.

---

# 31. Workflow Dependency Testing

If:

```text
Topic Validation
```

depends on:

```text
Topic Discovery
```

the workflow should not execute the dependent step before its required input exists.

Dependency failures must be detectable.

---

# 32. Parallel Execution Testing

When steps execute in parallel, test:

* concurrent success;
* one branch failure;
* all branches failure;
* partial completion;
* synchronization;
* duplicate execution;
* race conditions.

Parallelism must not corrupt shared state.

---

# 33. Search Intelligence Testing

Search testing should verify:

* query normalization;
* search-context identity;
* provider adapter;
* metric normalization;
* freshness;
* localization;
* language;
* device;
* SERP parsing;
* feature detection.

---

# 34. SERP Testing

SERP fixtures should include:

* organic results;
* paid results;
* featured snippets;
* PAA;
* local pack;
* knowledge panels;
* video;
* image;
* shopping;
* news;
* mixed SERPs.

The parser should gracefully handle unknown or new feature types.

---

# 35. SERP Intent Evaluation

Intent classification should be evaluated against reviewed SERP examples.

Test:

```text
Dominant Intent
Mixed Intent
Ambiguous Intent
Intent Drift
Insufficient Evidence
```

Do not force a single intent when the evidence supports multiple intents.

---

# 36. SERP Similarity Testing

Test similarity using multiple signals:

```text
URL overlap
Domain overlap
Page type overlap
Entity overlap
Content format
Intent
SERP features
```

Do not test similarity using only:

```text
Keyword text similarity
```

---

# 37. Topic Clustering Testing

Clustering tests should verify:

* semantic similarity;
* intent similarity;
* SERP similarity;
* entity overlap;
* business relevance;
* cluster coherence;
* separation quality.

Test both:

```text
Should Cluster Together
```

and:

```text
Should Remain Separate
```

cases.

---

# 38. False-Merge Testing

Important clustering regression cases should explicitly test false merges.

Example:

```text
Same entity
+
Different search intent
=
Potentially separate clusters
```

The system must not force everything related to one entity into one page.

---

# 39. False-Split Testing

Also test false splits.

Example:

```text
Different keyword wording
+
Same intent
+
Strong SERP similarity
=
Potentially same page
```

---

# 40. Page Mapping Testing

Page candidate decisions should be evaluated using:

* intent;
* SERP similarity;
* entity/topic relationship;
* business distinction;
* existing page coverage;
* content type;
* canonicalization;
* strategic requirements.

The output should distinguish:

```text
Existing Page
New Page Candidate
Merge Candidate
Uncertain
```

---

# 41. Cannibalization Testing

Test cases should include:

```text
True Cannibalization
False Positive
Different Intent
Different Audience
Different Business Purpose
Historical Rank Fluctuation
Strong SERP Overlap
Weak SERP Overlap
```

Cannibalization should not be inferred from keyword overlap alone.

---

# 42. Content Gap Testing

Test:

```text
True Gap
Existing Coverage
Partial Coverage
Competitor-Only Opportunity
Low-Value Candidate
Insufficient Evidence
```

A missing competitor page does not automatically mean the user needs a new page.

---

# 43. Internal Linking Testing

Test:

* valid source page;
* valid target page;
* relevance;
* duplicate links;
* orphan pages;
* excessive links;
* anchor suggestions;
* confidence;
* existing architecture.

The system should not create nonsensical links merely because two pages share keywords.

---

# 44. Decision Engine Testing

The decision engine should be tested independently of AI generation.

Test:

```text
Evidence
+
Signals
+
Business Constraints
+
Rules
+
Confidence
→
Recommendation
```

Decision tests should verify that changes in inputs produce expected changes in recommendation.

---

# 45. Decision Sensitivity Testing

Where appropriate, test:

```text
Small Evidence Change
→
Recommendation Change?
```

This helps identify unstable decision logic.

Unexpected recommendation flips should be investigated.

---

# 46. Human-in-the-Loop Testing

Test:

```text
Approve
Reject
Modify
Override
Request Evidence
Defer
Escalate
```

Verify:

* authorization;
* audit record;
* decision scope;
* timestamp;
* actor;
* resulting state;
* downstream workflow behavior.

---

# 47. Human Approval Integrity

Tests must ensure that:

```text
AI recommendation
```

cannot become:

```text
HUMAN_APPROVED
```

without an actual authorized human action.

No synthetic or automatic approval should be accepted as human approval.

---

# 48. Frontend Testing

Frontend testing should include:

### Unit

Components and utilities.

### Component

Interactive component behavior.

### Integration

Feature behavior with API mocks.

### E2E

Real user journeys.

---

# 49. Frontend Contract Testing

Verify that frontend assumptions match backend contracts.

Test:

* response schemas;
* error formats;
* optional fields;
* enum values;
* pagination;
* streaming;
* localization;
* empty states.

---

# 50. AI Streaming Testing

If AI responses are streamed:

Test:

```text
Connection
First Event
Incremental Events
Malformed Event
Connection Drop
Reconnect
Completion
Error Event
Cancellation
```

The UI should not enter an inconsistent state after interrupted streaming.

---

# 51. API Testing

API tests should verify:

* authentication;
* authorization;
* request validation;
* response contracts;
* errors;
* pagination;
* filtering;
* rate limits;
* streaming;
* idempotency.

---

# 52. Security Testing

Security testing is mandatory.

Test:

* authentication;
* authorization;
* tenant isolation;
* privilege escalation;
* session handling;
* CSRF where relevant;
* XSS;
* injection;
* SSRF;
* unsafe file handling;
* secret exposure;
* API abuse;
* rate limiting;
* prompt injection;
* tool authorization.

---

# 53. Prompt Injection Testing

AI components must be tested against malicious or misleading content originating from:

* web pages;
* competitor pages;
* search results;
* documents;
* user-provided content;
* tool responses.

The system should distinguish:

```text
Data
```

from:

```text
Instructions
```

embedded inside retrieved content.

---

# 54. Tool Authorization Testing

Test that an agent cannot invoke tools outside its permission set.

Example:

```text
Research Agent
→ permitted research tools
```

must not become:

```text
Research Agent
→ destructive administrative action
```

---

# 55. Performance Testing

Performance testing should cover:

* API latency;
* database queries;
* vector retrieval;
* workflow execution;
* SERP collection;
* LLM calls;
* frontend rendering;
* concurrent users;
* concurrent workflows.

---

# 56. Load Testing

Load tests should model realistic usage.

Examples:

```text
Many projects
Many topics
Large SERP datasets
Concurrent AI tasks
Concurrent users
Large evidence sets
```

Do not optimize only for tiny development datasets.

---

# 57. Stress Testing

Stress testing intentionally exceeds normal load to identify:

* bottlenecks;
* queue saturation;
* memory issues;
* database exhaustion;
* provider throttling;
* failure cascades.

The goal is controlled failure rather than pretending failure will never occur.

---

# 58. Cost Testing

AI workflows should be evaluated for:

* token usage;
* number of model calls;
* tool calls;
* retries;
* context size;
* model selection;
* cache effectiveness.

Define expected cost envelopes for representative workflows.

---

# 59. Context Efficiency Testing

Measure:

```text
Relevant Context
/
Total Context
```

where practical.

Test whether unnecessary context causes:

* higher cost;
* worse answers;
* slower responses;
* context overflow.

---

# 60. Retrieval Testing

Retrieval should be evaluated using reviewed queries.

Measure:

* recall;
* precision;
* ranking;
* freshness;
* project isolation;
* evidence relevance.

Test:

```text
Correctly Retrieved
Missed
Irrelevant
Stale
Wrong Project
```

---

# 61. Vector Search Testing

Verify:

* embedding generation;
* embedding version;
* metadata filters;
* project filters;
* similarity thresholds;
* deterministic identifiers;
* index availability.

Changing embedding models should trigger appropriate evaluation.

---

# 62. Migration Testing

Database migrations must be tested through:

```text
Previous Schema
→ Migration
→ New Schema
→ Application Tests
```

Test:

* fresh installation;
* upgrade from representative previous versions;
* rollback where supported;
* data preservation;
* constraints.

---

# 63. Provider Contract Testing

For every important external provider:

```text
Provider
→ Adapter
→ Normalizer
→ Internal Contract
```

Test against:

* real representative responses where permitted;
* fixtures;
* malformed responses;
* changed fields;
* rate limits;
* timeout behavior.

---

# 64. Mock Provider Testing

Mock providers should support:

```text
Success
Timeout
Rate Limit
Invalid Response
Authentication Failure
Partial Response
Empty Response
Malformed Response
```

This allows reliable failure testing without depending on external availability.

---

# 65. Regression Testing

Every significant defect should produce regression coverage when practical.

Regression tests should be tagged or organized so that important historical failures remain visible.

Examples:

```text
REG-ENTITY-001
REG-SERP-004
REG-CLUSTER-009
REG-AUTH-003
```

---

# 66. Negative Testing

The system must be tested with invalid or adversarial inputs.

Examples:

* empty input;
* malformed query;
* invalid project ID;
* conflicting entities;
* unsupported language;
* huge payload;
* malicious content;
* malformed provider response;
* invalid workflow transition.

A robust system is defined partly by how it fails.

---

# 67. Boundary Testing

Test limits such as:

* zero items;
* one item;
* maximum supported items;
* very long text;
* maximum context;
* maximum workflow depth;
* maximum query length;
* rate limit threshold.

Boundary failures often reveal hidden assumptions.

---

# 68. Property-Based Testing

Where suitable, use property-based testing for deterministic logic.

Examples:

```text
Canonicalization should be idempotent.
Sorting should preserve expected ordering properties.
Normalization should not create invalid identifiers.
Repeated normalization should produce the same canonical representation.
```

---

# 69. Determinism Testing

Deterministic components should produce identical outputs for identical inputs.

For AI components, exact determinism may not be guaranteed.

Instead test:

* structural validity;
* semantic invariants;
* acceptable output range;
* evaluation score;
* evidence requirements.

---

# 70. Reliability Testing

Reliability testing should include repeated execution.

Test whether repeated workflows:

```text
Same Input
Same Context
Same Configuration
```

produce acceptably consistent outcomes.

Large unexplained variance should trigger investigation.

---

# 71. Freshness Testing

Search and knowledge data should be tested for freshness.

Verify:

* timestamp;
* TTL;
* snapshot identity;
* invalidation;
* refresh behavior.

A stale result should be distinguishable from a current observation.

---

# 72. Conflict Testing

Provide conflicting evidence intentionally.

Verify that the system:

```text
detects conflict
→ preserves provenance
→ avoids false certainty
→ reports uncertainty
```

It should not silently discard contradictory evidence.

---

# 73. Explainability Testing

The system should be tested for observable explanation quality.

A recommendation should expose:

* relevant evidence;
* decision factors;
* confidence;
* assumptions;
* warnings;
* provenance.

It should not expose private chain-of-thought.

---

# 74. Output Completeness Testing

Conditional fields must appear when required.

Example:

If:

```text
epistemic_state = RECOMMENDED
```

then the output may require:

* rationale;
* evidence;
* confidence;
* recommendation metadata.

If:

```text
status = CONFLICTED
```

then conflict information should be present.

---

# 75. Error Contract Testing

Every major error should have predictable semantics.

Test:

```text
Error Code
Message
Category
Retryability
HTTP Mapping
Correlation ID
Context
```

Do not allow internal exceptions to randomly leak through API responses.

---

# 76. Accessibility Testing

The frontend must be tested for:

* keyboard navigation;
* focus management;
* screen readers;
* semantic structure;
* contrast;
* color-independent semantics;
* accessible forms;
* accessible dialogs;
* accessible charts;
* reduced motion;
* RTL/LTR behavior.

Target:

```text
WCAG 2.2 AA
```

where applicable.

---

# 77. Localization Testing

Test:

* English;
* Persian;
* German;
* RTL;
* LTR;
* long translations;
* numeric formatting;
* dates;
* currencies;
* pluralization;
* mixed-language content.

Layout must remain functional after translation expansion.

---

# 78. Visualization Testing

Test analytical visualizations for:

* correct data;
* correct labels;
* correct relationships;
* empty state;
* large dataset behavior;
* interaction;
* keyboard accessibility;
* alternative representations.

A beautiful graph containing incorrect relationships is a failed feature.

---

# 79. E2E Testing

E2E tests should represent actual user journeys.

Example:

```text
Create Project
→ Define Business
→ Research Entities
→ Discover Topics
→ Validate Topics
→ Analyze Search
→ Cluster Topics
→ Review Page Candidates
→ Review Recommendation
→ Approve
```

The exact journey should be determined by the implemented workflow.

---

# 80. Critical E2E Journeys

At minimum, the product should eventually cover:

### Project Creation

```text
Create → Configure → Open
```

### Research

```text
Research → Evidence → Topics
```

### Search Intelligence

```text
Query → SERP → Intent → Analysis
```

### Mapping

```text
Topics → Clusters → Pages
```

### Decision

```text
Recommendation → Human Review → Decision
```

### Recovery

```text
Failure → Resume → Completion
```

---

# 81. Test Data Governance

Test data must:

* be deterministic where possible;
* avoid unnecessary personal data;
* be versioned;
* be reproducible;
* have clear ownership.

Production data should not automatically become test data.

---

# 82. Test Isolation

Tests should not unintentionally depend on:

* another test;
* execution order;
* local machine state;
* developer credentials;
* external provider availability.

Tests should clean up their state where required.

---

# 83. Test Environment

The test environment should provide controlled versions of:

```text
PostgreSQL
Redis
Vector Store
Mock LLM
Mock Search
Mock SERP
Mock SEO Provider
```

External services should be used only where their behavior itself is being tested.

---

# 84. CI Validation

CI should execute relevant checks automatically.

Conceptually:

```text
Lint
↓
Type Check
↓
Unit
↓
Domain
↓
Contract
↓
Integration
↓
AI Evaluation
↓
Security
↓
Build
↓
E2E
```

The exact pipeline can optimize speed without weakening required quality gates.

---

# 85. Test Categorization

Tests should be tagged by:

```text
unit
domain
integration
contract
ai
agent
workflow
security
performance
e2e
regression
slow
external
```

This enables targeted execution.

---

# 86. Test Selection

For a small code change:

```text
Targeted Tests
→ Related Tests
```

For a cross-cutting change:

```text
Targeted
→ Module
→ Integration
→ Regression
```

For a release:

```text
Full Required Suite
```

---

# 87. AI Evaluation Thresholds

AI features should define task-specific acceptance criteria.

Examples:

```text
Intent Classification
→ minimum acceptable agreement

Entity Resolution
→ minimum precision / acceptable ambiguity

Topic Clustering
→ minimum coherence / separation

Evidence Selection
→ minimum evidence relevance

Decision Support
→ minimum reviewed-case agreement
```

Thresholds must be defined using representative datasets rather than arbitrary numbers.

---

# 88. AI Evaluation Dimensions

For each AI capability evaluate:

| Dimension   | Question                              |
| ----------- | ------------------------------------- |
| Correctness | Is the result right?                  |
| Relevance   | Does it answer the task?              |
| Evidence    | Is it supported?                      |
| Consistency | Is behavior stable enough?            |
| Confidence  | Is uncertainty appropriate?           |
| Safety      | Does it respect boundaries?           |
| Cost        | Is execution economically reasonable? |
| Latency     | Is it operationally acceptable?       |

---

# 89. Human Evaluation

Some AI outputs require human evaluation.

Human reviewers should score criteria explicitly.

Example:

```text
1–5 Relevance
1–5 Evidence Quality
1–5 Business Fit
1–5 Semantic Accuracy
```

Human evaluation datasets should be versioned.

---

# 90. Inter-Rater Consideration

For subjective evaluations, multiple reviewers may be required.

Differences should be analyzed.

If reviewers disagree substantially, the evaluation rubric may be underspecified.

Do not automatically treat reviewer disagreement as model failure.

---

# 91. Calibration Testing

If the system outputs confidence, evaluate whether confidence corresponds to actual correctness.

Example:

```text
High Confidence
→
Should usually have high correctness/support
```

A system that is wrong with high confidence is particularly risky.

---

# 92. Drift Testing

The system should eventually detect:

* SERP drift;
* intent drift;
* entity changes;
* competitor changes;
* topic changes;
* model behavior drift;
* provider changes.

Historical datasets should support drift evaluation.

---

# 93. Model Regression

When changing:

* model;
* prompt;
* retrieval;
* tool;
* context policy;

run the relevant AI regression suite.

Compare:

```text
Previous Version
vs
New Version
```

Do not rely on one successful example.

---

# 94. Prompt Regression

Prompt changes should trigger tests covering:

* output schema;
* semantics;
* evidence;
* tool use;
* refusal behavior;
* confidence;
* cost;
* latency.

Prompts are production artifacts.

---

# 95. Tool Regression

When a tool changes:

Test:

```text
Tool Input
Tool Output
Error Behavior
Permission
Normalization
Downstream Agent Behavior
```

A tool change may affect multiple agents.

---

# 96. Release Validation

A release candidate should pass:

```text
Code Quality
+
Tests
+
Contracts
+
AI Evaluation
+
Security
+
Performance
+
Runtime Verification
```

with no unresolved critical failures.

---

# 97. Release Blocking Conditions

A release should be blocked by issues such as:

* critical security vulnerability;
* cross-project data leakage;
* broken authentication/authorization;
* corrupted database migration;
* invalid core contracts;
* major workflow corruption;
* fabricated external data;
* unvalidated destructive behavior;
* severe regression in critical AI functionality.

---

# 98. Known Limitations

A release may proceed with known non-critical limitations only when:

* explicitly documented;
* understood;
* appropriately classified;
* accepted by the responsible authority;
* not violating critical quality/security requirements.

---

# 99. Test Failure Investigation

When a test fails:

```text
Failure
→ Reproduce
→ Determine Flaky vs Real
→ Inspect Evidence
→ Classify
→ Fix
→ Re-run
→ Regression
```

Do not simply rerun until it passes.

---

# 100. Flaky Test Policy

Flaky tests should be tracked.

A flaky test should not be silently disabled.

Possible actions:

* fix synchronization;
* isolate dependency;
* control randomness;
* improve fixture;
* quarantine temporarily with explicit ownership.

---

# 101. Test Debt

Missing tests should be tracked as technical debt.

Examples:

```text
No E2E for workflow recovery
No golden dataset for intent
No tenant isolation test
No provider failure fixture
```

Test debt should have priority based on risk.

---

# 102. Verification Status

Each important feature should be classified as:

```text
IMPLEMENTED
TESTED
VALIDATED
RUNTIME_VERIFIED
PARTIALLY_VERIFIED
UNVERIFIED
BLOCKED
```

These states must not be conflated.

---

# 103. Evidence of Verification

Verification evidence may include:

* test command;
* test results;
* evaluation report;
* runtime trace;
* API response;
* screenshot;
* database verification;
* provider response;
* benchmark.

Claims of completion should reference actual evidence.

---

# 104. Testing Documentation

Every important test suite should document:

* purpose;
* scope;
* prerequisites;
* command;
* fixtures;
* expected result;
* known limitations.

---

# 105. Test Naming

Test names should describe behavior.

Prefer:

```text
test_topic_cluster_separates_queries_with_different_serp_intent
```

over:

```text
test_cluster_1
```

A good test name communicates the invariant.

---

# 106. Failure Messages

Test failures should provide useful diagnostics.

Prefer:

```text
Expected page candidates to remain separate because SERP intent differs.
Observed merge score: 0.91.
Intent similarity: 0.34.
```

over:

```text
Assertion failed.
```

---

# 107. Test Coverage

Code coverage is useful but insufficient.

High coverage does not guarantee:

* domain correctness;
* AI quality;
* evidence validity;
* security;
* user experience.

Coverage should be treated as one metric among many.

---

# 108. Risk-Based Testing

Testing priority should reflect risk.

High-risk areas:

```text
Authentication
Authorization
Tenant Isolation
Data Integrity
Decision Engine
AI Evidence
Workflow State
External Billing if introduced
Destructive Actions
```

These require stronger validation.

---

# 109. Testing the Living Model

Because the product maintains a living SEO intelligence model, test:

* historical state;
* versioning;
* updates;
* derived artifacts;
* reprocessing;
* stale data;
* contradictions;
* human corrections;
* knowledge graph relationships.

An update should not unexpectedly destroy historical truth.

---

# 110. Reprocessing Tests

When new evidence arrives:

```text
Old State
+
New Evidence
→
Reprocessing
→
New Derived State
```

Test that:

* source data remains preserved;
* derived data is correctly updated;
* previous state remains auditable;
* decisions can be traced to the relevant version.

---

# 111. Cache and Freshness Tests

Test:

```text
Cache Hit
Cache Miss
Expiration
Invalidation
Refresh
Concurrent Refresh
Stale Data
```

Ensure cached data respects project and search context boundaries.

---

# 112. Security Regression

Every resolved security defect should have a permanent regression test where practical.

Security tests should not be removed merely because the original issue is fixed.

---

# 113. Performance Regression

Important performance baselines should be recorded.

Examples:

```text
API p95 latency
Workflow completion time
SERP processing throughput
Vector retrieval latency
AI token usage
Frontend initial render
```

Changes causing meaningful regressions should be investigated.

---

# 114. Cost Regression

Track representative workflow cost.

Example:

```text
Research Project
→ expected model calls
→ expected token range
→ expected provider calls
```

Significant unexplained increases should block or trigger review depending on severity.

---

# 115. Accessibility Regression

Accessibility checks should run continuously.

Do not wait until final release.

---

# 116. Testing and Context Management

Tests should provide compact evidence.

Instead of loading an entire repository after every failure, retrieve:

* failing test;
* affected implementation;
* relevant contract;
* recent change;
* relevant documentation.

This keeps debugging context efficient.

---

# 117. Testing and Skills/Tools

When specialized testing capability is needed:

1. identify the requirement;
2. inspect available tooling;
3. install/use a required skill when permitted;
4. validate its output;
5. record relevant usage;
6. avoid unnecessary dependencies.

Tool policy is governed by:

`26_SKILLS_AND_TOOLING_POLICY.md`.

---

# 118. Testing and Human Authority

Automated tests may verify whether a recommendation satisfies technical and domain criteria.

They do not replace human strategic authority.

For example:

```text
Test:
Recommendation has valid evidence.
```

does not mean:

```text
Human:
Must approve recommendation.
```

The final strategic decision remains governed by HITL rules.

---

# 119. Test Architecture

The testing architecture should mirror the system architecture:

```text
Unit
 ↓
Domain
 ↓
Application
 ↓
Intelligence
 ↓
Workflow
 ↓
API
 ↓
Frontend
 ↓
E2E
```

Cross-cutting:

```text
Security
Data
Contracts
AI Evaluation
Performance
Observability
```

---

# 120. Minimal MVP Testing Scope

The MVP should prioritize:

### Mandatory

* unit tests;
* domain tests;
* application tests;
* database integration tests;
* API tests;
* contract tests;
* core agent tests;
* workflow tests;
* AI golden tests for critical agents;
* security tests;
* regression tests;
* basic E2E;
* mock provider tests.

### Strongly Recommended

* retrieval evaluation;
* SERP fixture evaluation;
* accessibility testing;
* performance baseline;
* cost baseline.

---

# 121. Future Testing Scope

Future expansion may include:

* continuous AI evaluation;
* automated drift detection;
* advanced red teaming;
* large-scale load testing;
* model benchmarking;
* provider A/B evaluation;
* adaptive test generation;
* production shadow evaluation;
* anomaly detection;
* continuous semantic validation.

---

# 122. Testing Anti-Patterns

The following are prohibited or strongly discouraged:

### "The App Starts"

Startup success is not product validation.

### "The API Returns 200"

HTTP success does not prove semantic correctness.

### "The LLM Sounds Good"

Plausible language does not prove evidence-supported correctness.

### "Coverage Is 90%"

Coverage does not equal quality.

### "Retry Until Green"

Repeated retries do not fix root causes.

### "Mock Everything Forever"

Critical real integration behavior eventually requires controlled real verification.

### "Ignore Flaky Tests"

Flakiness is a reliability problem.

### "Disable Security for Tests"

Security controls must not be bypassed to make tests pass.

### "Golden Dataset of Five Examples"

Tiny datasets cannot validate complex AI behavior.

### "Human Approval by Default"

Automation must not fabricate human decisions.

---

# 123. Definition of Test Completeness

A feature is sufficiently tested when:

* its deterministic logic has appropriate unit/domain coverage;
* its contracts are tested;
* its persistence behavior is tested;
* its failure modes are tested;
* its AI behavior is evaluated where applicable;
* its workflow behavior is tested where applicable;
* its security boundary is tested;
* its UI behavior is tested where applicable;
* its critical user journey is covered;
* regressions are protected;
* runtime behavior is verified where required.

---

# 124. Definition of Done for Testing

Testing for a task is complete only when:

1. required test categories are identified;
2. targeted tests are implemented;
3. tests pass;
4. relevant regression tests pass;
5. AI evaluation is completed where applicable;
6. security validation is completed where applicable;
7. runtime verification is completed where required;
8. known failures are documented;
9. test evidence is recorded;
10. verification status is updated.

---

# 125. Final Testing Model

The system's complete validation pipeline is:

```text
Requirement
    ↓
Acceptance Criteria
    ↓
Unit / Domain Tests
    ↓
Contract Tests
    ↓
Data Tests
    ↓
AI / Agent Evaluation
    ↓
Workflow Tests
    ↓
Integration Tests
    ↓
Security Tests
    ↓
Frontend Tests
    ↓
E2E Tests
    ↓
Performance / Cost Validation
    ↓
Runtime Verification
    ↓
Regression Suite
    ↓
Release Decision
```

---

# 126. Non-Negotiable Rules

1. Testing is mandatory for meaningful implementation.
2. Validation is broader than technical testing.
3. Passing tests does not automatically prove domain correctness.
4. AI outputs require evaluation, not merely schema validation.
5. Evidence support must be tested for important AI decisions.
6. Confidence must not be treated as truth.
7. Human approval must never be fabricated.
8. Tenant/project isolation must be tested.
9. Security boundaries must be tested.
10. Workflow state transitions must be tested.
11. Failure and recovery paths must be tested.
12. External providers must have failure fixtures.
13. Critical defects must generate regression protection.
14. Prompt changes require appropriate regression evaluation.
15. Model changes require comparison against representative datasets.
16. Retrieval quality must be evaluated.
17. Freshness and contradiction behavior must be tested.
18. Frontend/backend contracts must be tested.
19. Runtime verification must be distinguished from static test success.
20. Flaky tests must be investigated, not silently ignored.
21. Test coverage is a metric, not a definition of correctness.
22. Tests must not bypass security controls.
23. Test data must be controlled and reproducible.
24. No fabricated test results.
25. No claim of "all tests pass" unless the relevant suite was actually executed.
26. The testing strategy must evolve with the architecture and living SEO intelligence model.

---

# 127. Relationship to Other Documents

This document depends on:

* `03_MASTER_RULES.md`
* `04_SYSTEM_ARCHITECTURE.md`
* `05_AI_AGENT_ARCHITECTURE.md`
* `06_DATA_ARCHITECTURE.md`
* `07_TECHNICAL_ARCHITECTURE.md`
* `08_SEO_KNOWLEDGE_MODEL.md`
* `09_ENTITY_EAV_MODEL.md`
* `10_TOPIC_MODELING_AND_CLUSTERING.md`
* `11_SEARCH_AND_SERP_INTELLIGENCE.md`
* `12_SEO_DECISION_ENGINE.md`
* `13_AGENT_SPECIFICATIONS.md`
* `14_AGENT_WORKFLOW.md`
* `15_HUMAN_IN_THE_LOOP.md`
* `16_OUTPUT_CONTRACTS.md`
* `17_UI_UX_SPECIFICATION.md`
* `18_FRONTEND_ARCHITECTURE.md`
* `19_DESIGN_SYSTEM.md`
* `20_PROJECT_STRUCTURE.md`
* `21_DEVELOPMENT_AND_DEBUG.md`

It directly informs:

* `23_PROJECT_CONTROL_CENTER.md`
* `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md`
* `25_CONTEXT_MANAGEMENT.md`
* `26_SKILLS_AND_TOOLING_POLICY.md`

---

# 128. Document Control

```yaml
document:
  id: "22"
  filename: "22_TESTING_AND_VALIDATION.md"
  status: "APPROVED_AS_BASELINE_TESTING_AND_VALIDATION"
  authority: "baseline_testing_validation_and_quality_assurance"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

core_principle:
  testing: "verify_expected_behavior"
  validation: "verify_actual_correctness_and_appropriateness"
  evidence_required: true
  no_fake_results: true

test_layers:
  - "unit"
  - "domain"
  - "application"
  - "data"
  - "contract"
  - "integration"
  - "ai"
  - "agent"
  - "workflow"
  - "retrieval"
  - "search_serp"
  - "frontend"
  - "api"
  - "security"
  - "performance"
  - "cost"
  - "evaluation"
  - "regression"
  - "e2e"
  - "failure_recovery"
  - "accessibility"
  - "migration"
  - "deployment_verification"

ai_evaluation:
  golden_datasets: true
  semantic_evaluation: true
  evidence_evaluation: true
  confidence_evaluation: true
  regression_evaluation: true
  human_evaluation_when_required: true
  prompt_regression: true
  model_regression: true
  chain_of_thought_storage: false

agent_testing:
  input_validation: true
  context_validation: true
  tool_validation: true
  output_validation: true
  boundary_testing: true
  failure_testing: true
  idempotency_testing: true

workflow_testing:
  state_transitions: true
  dependency_validation: true
  retry_testing: true
  recovery_testing: true
  human_review_testing: true
  concurrency_testing: true

security_testing:
  authentication: true
  authorization: true
  tenant_isolation: true
  prompt_injection: true
  tool_authorization: true
  regression_required: true

data_testing:
  schema: true
  constraints: true
  transactions: true
  migrations: true
  provenance: true
  freshness: true
  contradiction_handling: true
  historical_state: true

integration_testing:
  mock_providers: true
  failure_fixtures: true
  provider_contracts: true
  runtime_verification_when_required: true

frontend_testing:
  component: true
  integration: true
  accessibility: true
  localization: true
  visualization: true
  e2e: true

release:
  critical_security_failure_blocks: true
  data_integrity_failure_blocks: true
  core_contract_failure_blocks: true
  major_workflow_corruption_blocks: true
  fabricated_external_data_blocks: true
  unresolved_noncritical_limitations_require_explicit_documentation: true

verification_states:
  - "IMPLEMENTED"
  - "TESTED"
  - "VALIDATED"
  - "RUNTIME_VERIFIED"
  - "PARTIALLY_VERIFIED"
  - "UNVERIFIED"
  - "BLOCKED"

next_dependency:
  document: "23_PROJECT_CONTROL_CENTER.md"
  purpose: "project_state_task_control_authorization_and_execution_governance"
```

---

**End of `22_TESTING_AND_VALIDATION.md`**
