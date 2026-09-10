# 21 — Development and Debug

**Document:** `21_DEVELOPMENT_AND_DEBUG.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Development Process, Debugging, Engineering Quality & Runtime Investigation Specification
**Status:** `APPROVED_AS_BASELINE_DEVELOPMENT_AND_DEBUG`
**Authority:** Baseline specification for development workflow, implementation discipline, debugging, failure investigation, incident analysis, regression prevention, runtime verification, and engineering handoff.

---

# 1. Purpose

This document defines how the SEO Research & Strategy Copilot / SEO Decision Engine is developed, investigated, debugged, verified, and handed off.

The objective is not merely to make code work.

The objective is to establish a repeatable engineering process in which:

```text
Requirement
    ↓
Authorized Task
    ↓
Implementation
    ↓
Validation
    ↓
Evidence
    ↓
Verification
    ↓
Documented State
```

is preferred over:

```text
Code
    ↓
"It seems to work"
```

The system is AI-heavy, data-heavy, workflow-driven, and integration-dependent.

Therefore debugging must cover more than conventional application bugs.

It must also cover:

* incorrect AI reasoning;
* incorrect evidence;
* stale search data;
* contract violations;
* workflow state corruption;
* context failures;
* provider failures;
* retrieval failures;
* data-model inconsistencies;
* authorization failures;
* frontend/backend mismatches;
* race conditions;
* cost/latency regressions;
* hallucinated outputs;
* incorrect business decisions.

---

# 2. Core Engineering Principle

The project's primary debugging loop is:

```text
Detect
  ↓
Reproduce
  ↓
Collect Evidence
  ↓
Classify
  ↓
Identify Root Cause
  ↓
Implement Fix
  ↓
Run Targeted Test
  ↓
Run Regression Tests
  ↓
Verify Runtime Behavior
  ↓
Document Resolution
```

Every meaningful defect should move through this loop.

A fix without verification is not a completed fix.

---

# 3. Development Philosophy

Development follows:

```text
Documentation
    ↓
Dependency Analysis
    ↓
Task Authorization
    ↓
Implementation
    ↓
Testing
    ↓
Verification
    ↓
State Update
```

The developer or coding agent MUST NOT treat the repository as the only source of truth.

The project documentation, current state, authorized task, contracts, tests, and implementation must remain consistent.

---

# 4. No Unauthorized Implementation

No implementation should begin merely because a developer identifies something that could be improved.

Before implementation, determine:

1. What task is being executed?
2. Is it authorized?
3. Which document defines the requirement?
4. Which modules are affected?
5. What dependencies exist?
6. What contracts are affected?
7. What tests are required?
8. What constitutes completion?

If authorization is unclear:

```text
STOP
→ inspect project state
→ inspect task board
→ inspect dependencies
→ request/derive authorization according to project control rules
```

Do not silently expand scope.

---

# 5. Development Task Lifecycle

Every implementation task should conceptually follow:

```text
Task Selected
    ↓
Read Relevant Documentation
    ↓
Inspect Existing Implementation
    ↓
Inspect Tests
    ↓
Identify Dependencies
    ↓
Define Acceptance Criteria
    ↓
Implement
    ↓
Targeted Validation
    ↓
Regression Validation
    ↓
Runtime Verification
    ↓
Update Documentation/State
    ↓
Handoff
```

---

# 6. Read Before Modify

Before changing code, inspect:

* relevant baseline documentation;
* project state;
* task definition;
* current implementation;
* related tests;
* related contracts;
* dependencies;
* recent changes;
* known defects.

Do not rewrite code based solely on the user's description of the problem when the repository contains evidence that can verify it.

---

# 7. Minimal Context Principle

Development context should be:

```text
Relevant
Current
Sufficient
Traceable
```

not:

```text
Everything in the repository
```

The developer should load only the documentation and source necessary for the current task.

Context management is governed by:

`25_CONTEXT_MANAGEMENT.md`.

---

# 8. Inspect Before Debugging

When a bug is reported, first inspect:

```text
Symptom
→ affected surface
→ execution path
→ relevant implementation
→ relevant state
→ relevant logs
→ relevant tests
```

Do not immediately modify the first file that appears suspicious.

---

# 9. Debugging Workflow

The canonical debugging process is:

## Step 1 — Detect

Identify the symptom.

Examples:

* API returns 500;
* topic cluster is incorrect;
* SERP analysis times out;
* frontend shows stale data;
* workflow remains stuck;
* AI output fails validation;
* duplicate pages are recommended;
* authorization is bypassed.

---

## Step 2 — Reproduce

A defect should be reproduced whenever practical.

Record:

* environment;
* input;
* user/project context;
* relevant IDs;
* provider;
* model;
* workflow state;
* timestamp;
* expected behavior;
* actual behavior.

If reproduction is impossible, document why.

---

# 10. Evidence Collection

Evidence may include:

* logs;
* stack traces;
* HTTP requests/responses;
* database state;
* workflow state;
* AI output;
* validation results;
* provider response;
* raw SERP;
* retrieved context;
* prompt version;
* model identifier;
* browser console;
* network traces;
* screenshots;
* metrics;
* traces.

Evidence must be preserved before making assumptions about root cause.

---

# 11. Root Cause Analysis

A debugging investigation must distinguish:

```text
Symptom
≠
Root Cause
```

Example:

```text
Symptom:
Topic validation returns no topics.

Possible root causes:
- invalid input contract
- topic retrieval failure
- embedding failure
- filtering bug
- confidence threshold too high
- provider failure
- incorrect project isolation
- stale knowledge
- model failure
```

The first visible error is not automatically the root cause.

---

# 12. Failure Classification

Defects should be classified before fixing.

Recommended categories:

```text
CODE
DATA
CONTRACT
DOMAIN
AI
PROMPT
MODEL
RETRIEVAL
SEARCH
SERP
INTEGRATION
WORKFLOW
STATE
CONCURRENCY
SECURITY
PERMISSION
PERFORMANCE
CONFIGURATION
INFRASTRUCTURE
FRONTEND
UX
OBSERVABILITY
DOCUMENTATION
ENVIRONMENT
```

Multiple classifications may apply.

---

# 13. Code Failures

Examples:

* incorrect branching;
* null handling;
* type errors;
* serialization errors;
* incorrect algorithm;
* incorrect transaction behavior.

Debug using:

* stack traces;
* unit tests;
* type checking;
* static analysis;
* targeted reproduction.

---

# 14. Data Failures

Examples:

* corrupted records;
* duplicate entities;
* invalid EAV facts;
* stale SERP snapshots;
* incorrect relationships;
* missing provenance.

Data bugs must be investigated at the source.

Do not merely patch the UI representation of incorrect data.

---

# 15. Contract Failures

Examples:

```text
Producer output
    ≠
Expected schema
```

or:

```text
Schema valid
but semantic requirements violated
```

Contract debugging must inspect:

* producer;
* contract version;
* schema;
* validator;
* consumer;
* compatibility rules.

---

# 16. Domain Failures

A domain failure occurs when technically valid code produces an invalid business/SEO result.

Example:

```text
Two keywords are semantically similar
```

does not automatically imply:

```text
They require one page.
```

Domain debugging must reference the relevant domain model and rules.

---

# 17. AI Failures

AI failures include:

* hallucination;
* unsupported inference;
* incorrect classification;
* inconsistent reasoning;
* incomplete extraction;
* wrong prioritization;
* incorrect recommendation;
* failure to respect constraints;
* failure to use evidence;
* inappropriate confidence.

AI failures MUST NOT automatically be treated as coding bugs.

Investigate:

```text
Input
→ Context
→ Evidence
→ Prompt
→ Model
→ Tool usage
→ Structured output
→ Validation
→ Decision logic
```

---

# 18. Prompt Failures

Prompt problems should be distinguished from model problems.

Investigate:

* prompt version;
* system instructions;
* task instructions;
* examples;
* context;
* output schema;
* tool instructions;
* ambiguity;
* missing constraints.

Do not change the model when the actual problem is an underspecified prompt.

---

# 19. Model Failures

Model-related failures should be investigated using:

* model identifier;
* model version;
* temperature or equivalent configuration;
* structured-output behavior;
* tool-calling behavior;
* token limits;
* context size;
* latency;
* provider status.

Model changes must be evaluated against regression datasets.

---

# 20. Retrieval Failures

A wrong AI answer may actually be a retrieval failure.

Inspect:

```text
Query
→ Retrieval
→ Ranking
→ Filtering
→ Context Assembly
→ Model
```

Measure:

* relevant evidence retrieved;
* irrelevant evidence retrieved;
* missing evidence;
* ranking quality;
* freshness;
* provenance.

---

# 21. Search/SERP Failures

Search intelligence bugs require inspection of:

* search context;
* query normalization;
* provider;
* raw response;
* normalization;
* SERP parser;
* result classification;
* feature detection;
* timestamp;
* geographic/language parameters.

Never assume a provider response is correct merely because it was returned successfully.

---

# 22. Integration Failures

External providers can fail through:

* timeout;
* rate limiting;
* authentication;
* invalid request;
* quota exhaustion;
* malformed response;
* service degradation;
* changed API behavior;
* schema changes.

Integration failures should be isolated behind adapters.

The system must not fabricate external results when a provider fails.

---

# 23. Workflow Failures

Workflow debugging must inspect:

```text
Workflow ID
Task ID
Step ID
Workflow Version
Current State
Previous State
Inputs
Outputs
Dependencies
Retries
Checkpoints
Human Review State
Errors
```

A workflow stuck in `RUNNING` may be caused by:

* worker failure;
* lost queue message;
* missing checkpoint;
* invalid state transition;
* unhandled exception;
* dependency never completed;
* human approval waiting state.

---

# 24. State Machine Validation

Workflow states must have explicit legal transitions.

Example:

```text
PENDING
  ↓
RUNNING
  ↓
WAITING_FOR_REVIEW
  ↓
APPROVED
  ↓
COMPLETED
```

Invalid transitions must be rejected.

Never repair state by directly modifying production rows unless an explicit recovery procedure exists.

---

# 25. Concurrency Debugging

Potential concurrency issues include:

* duplicate workflow execution;
* duplicate evidence insertion;
* conflicting human decisions;
* stale writes;
* double charging;
* duplicate external requests;
* race conditions in caching;
* concurrent project updates.

Use:

* idempotency keys;
* transactions;
* row locking where appropriate;
* optimistic concurrency where appropriate;
* unique constraints;
* distributed locks only where justified.

---

# 26. Database Debugging

When investigating database behavior inspect:

* SQL query;
* transaction boundary;
* isolation level;
* locks;
* indexes;
* constraints;
* migrations;
* connection pool;
* query timing;
* returned rows.

Do not solve database problems solely by increasing timeouts.

---

# 27. Cache Debugging

Cache failures may appear as:

* stale results;
* inconsistent state;
* missing data;
* wrong tenant data;
* unexpected latency;
* cache stampede.

Inspect:

```text
Cache Key
TTL
Namespace
Project/User Scope
Stored Value
Invalidation
Write Path
Read Path
```

Cache keys must include all dimensions necessary to prevent cross-context contamination.

---

# 28. Context Debugging

For an AI task, inspect:

```text
Task
↓
Required Context
↓
Retrieved Context
↓
Filtered Context
↓
Ranked Context
↓
Compressed Context
↓
Final Model Input
```

Questions:

* Was relevant context retrieved?
* Was irrelevant context included?
* Was context truncated?
* Was evidence provenance preserved?
* Was the correct project loaded?
* Was stale context used?

Context bugs can masquerade as model failures.

---

# 29. Frontend Debugging

Frontend investigation should inspect:

```text
User Action
→ Component
→ State
→ Request
→ API
→ Response
→ Cache
→ State Update
→ Render
```

Common categories:

* rendering;
* state;
* network;
* contract;
* hydration;
* routing;
* authorization;
* accessibility;
* responsive layout;
* performance.

Browser console errors alone are not sufficient evidence.

---

# 30. API Debugging

Inspect:

* request;
* authentication;
* authorization;
* validation;
* application use case;
* downstream dependencies;
* response contract;
* status code;
* logs;
* trace.

The API should expose stable error semantics rather than leaking internal exceptions.

---

# 31. Authentication and Authorization Debugging

Security bugs require elevated priority.

Investigate:

```text
Identity
→ Session
→ Authentication
→ Authorization
→ Resource Scope
→ Action Permission
```

Never rely on frontend restrictions.

A request that is unauthorized must be rejected server-side.

Security failures should receive regression tests immediately after remediation.

---

# 32. Observability During Debugging

Every meaningful operation should be traceable through identifiers such as:

```text
request_id
correlation_id
project_id
workflow_id
task_id
step_id
agent_run_id
decision_id
```

Do not log sensitive data unnecessarily.

Observability must support investigation without creating a privacy/security liability.

---

# 33. Logging Rules

Logs should be:

* structured;
* searchable;
* contextual;
* appropriately leveled;
* privacy-aware.

Useful levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Avoid logging:

* passwords;
* tokens;
* API keys;
* private secrets;
* unnecessary personal information;
* complete sensitive prompts when unsafe.

---

# 34. AI Observability

AI execution should record, where appropriate:

```text
agent
agent_version
model
provider
prompt_version
input_contract_version
output_contract_version
workflow_id
task_id
tool_calls
latency
token_usage
estimated_cost
validation_status
confidence
epistemic_state
failure_category
```

Do not store private chain-of-thought.

Store concise decision metadata and evidence references instead.

---

# 35. Error Handling

Errors should be explicit.

An error should answer:

* what failed;
* where;
* why if known;
* whether retryable;
* what context is affected;
* whether state was changed;
* whether human intervention is required.

Avoid generic:

```text
Something went wrong.
```

as the only internal diagnostic information.

---

# 36. Retry Policy

Retries should be applied only to retryable failures.

Examples often suitable for retry:

* transient network timeout;
* rate limiting with backoff;
* temporary provider unavailability.

Examples generally unsuitable for blind retry:

* invalid input;
* authorization failure;
* schema violation caused by deterministic code;
* domain validation rejection;
* unsupported operation.

Retries must be bounded.

---

# 37. Exponential Backoff

External transient failures should use bounded backoff where appropriate.

Conceptually:

```text
attempt 1
  ↓
short delay
  ↓
attempt 2
  ↓
longer delay
  ↓
attempt 3
  ↓
failure / fallback
```

Avoid infinite retries.

---

# 38. Failure Isolation

One failed capability should not automatically corrupt the entire project.

For example:

```text
SERP Provider Failure
```

should not imply:

```text
All Topic Data Deleted
```

The architecture should support partial completion and explicit degraded states.

---

# 39. Graceful Degradation

When possible:

```text
Full Intelligence
      ↓
Partial Intelligence
      ↓
Evidence-Insufficient State
      ↓
Human Review
```

The system should prefer:

```text
Insufficient Data
```

over:

```text
Fabricated Completeness
```

---

# 40. No-Fabrication Rule

If external or internal evidence is unavailable, the system must not invent:

* search volume;
* SERP results;
* competitor information;
* entity facts;
* page content;
* rankings;
* business attributes;
* citations;
* tool results.

The correct output may be:

```text
UNKNOWN
```

or:

```text
INSUFFICIENT_EVIDENCE
```

or:

```text
REQUIRES_RESEARCH
```

---

# 41. Debugging AI Recommendations

When an AI recommendation is wrong, investigate:

```text
Recommendation
↓
Decision factors
↓
Evidence
↓
Retrieved knowledge
↓
Business constraints
↓
Domain rules
↓
Model output
```

The objective is not to inspect or expose private chain-of-thought.

Instead, inspect the **observable decision inputs and outputs**.

---

# 42. Evidence-Based Debugging

Every important AI decision should be explainable through:

* evidence references;
* relevant entities;
* relevant topics;
* search context;
* measurable signals;
* confidence;
* assumptions;
* warnings;
* decision factors.

If these are absent, debugging becomes unnecessarily difficult.

---

# 43. Decision Debugging

A recommendation should be decomposable into factors.

For example:

```text
Page Separation Recommendation
├── SERP similarity
├── Intent similarity
├── Entity overlap
├── Content format
├── Business distinction
├── Existing page coverage
└── Confidence
```

If the recommendation is wrong, the system should help identify which factor caused the error.

---

# 44. Regression Prevention

Every resolved defect should be evaluated for regression risk.

Ask:

```text
Can this bug happen again?
```

If yes, add an appropriate test.

Possible regression mechanisms:

* unit test;
* integration test;
* contract fixture;
* golden dataset;
* AI evaluation;
* E2E test;
* security test;
* workflow test.

---

# 45. Test Selection During Debugging

Do not always run the entire suite first.

Use:

```text
Targeted Test
    ↓
Related Test Group
    ↓
Regression Suite
```

For example:

```text
Topic clustering bug
→ clustering unit tests
→ topic intelligence tests
→ workflow tests
→ full regression suite
```

The final verification scope depends on impact.

---

# 46. Runtime Verification

Passing tests does not automatically prove runtime correctness.

Runtime verification may require:

* starting the API;
* starting workers;
* connecting to PostgreSQL;
* connecting to Redis;
* calling an endpoint;
* executing a workflow;
* testing a real UI path;
* verifying logs;
* verifying persistence.

The final report must distinguish:

```text
Tested
Verified
Not Verified
Blocked
```

---

# 47. External Integration Verification

If an integration was not actually exercised, state:

```text
Implemented but runtime integration unverified.
```

Do not claim:

```text
Integration complete and working.
```

based solely on static code inspection.

---

# 48. Environment-Specific Bugs

When a bug occurs only in one environment, compare:

```text
Code Version
Environment Variables
Dependency Versions
Database Schema
External Services
OS
Runtime
Build Configuration
Feature Flags
```

Avoid environment-specific hacks unless explicitly justified.

---

# 49. Dependency Debugging

When a dependency causes unexpected behavior, record:

* package name;
* installed version;
* expected version;
* runtime version;
* compatibility constraints;
* recent upgrade;
* lockfile state.

Do not casually upgrade dependencies while debugging another issue.

That can introduce confounding variables.

---

# 50. Change Isolation

During debugging, prefer small changes.

Bad:

```text
Fix bug
+ refactor architecture
+ upgrade dependencies
+ rename modules
+ change database
```

Good:

```text
Reproduce
→ isolate cause
→ make minimal fix
→ test
→ verify
```

Refactoring can follow separately.

---

# 51. Debugging with Git

Use version control evidence.

Useful investigation:

```text
git status
git diff
git log
git blame
```

Identify:

* when behavior changed;
* which commit introduced it;
* whether a migration is missing;
* whether a generated file changed;
* whether local modifications affect reproduction.

Never discard user changes merely to simplify debugging.

---

# 52. Safe Reproduction

When possible, create a minimal reproduction.

Example:

```text
Full workflow
      ↓
Failing step
      ↓
Minimal input
      ↓
Minimal test
```

A minimal reproduction improves:

* root-cause identification;
* test quality;
* future regression prevention.

---

# 53. AI Determinism

AI outputs can be nondeterministic.

Therefore debugging should record enough metadata to reproduce the environment:

* model;
* provider;
* model configuration;
* prompt version;
* tool configuration;
* context;
* input;
* output schema;
* relevant temperature/sampling configuration.

Exact reproduction may not always be possible.

When it is not, use evaluation across repeated runs.

---

# 54. AI Evaluation During Debugging

For AI failures, compare:

```text
Baseline
vs
Current
```

using representative datasets.

Measure:

* schema validity;
* factual support;
* classification accuracy;
* evidence coverage;
* consistency;
* confidence calibration;
* business relevance.

A fix that improves one example but harms the broader evaluation set is not necessarily a valid fix.

---

# 55. Prompt Regression

Prompt changes must be treated as code changes.

A prompt change can affect:

* output format;
* reasoning behavior;
* tool usage;
* confidence;
* evidence selection;
* cost;
* latency.

Therefore prompt changes require appropriate regression evaluation.

---

# 56. Model Migration Debugging

When changing models:

```text
Old Model
    ↓
Evaluation Dataset
    ↓
New Model
    ↓
Comparison
    ↓
Decision
```

Do not assume a newer or larger model is automatically better.

Evaluate:

* quality;
* cost;
* latency;
* reliability;
* structured-output adherence;
* tool usage;
* multilingual performance.

---

# 57. Data Migration Debugging

After migrations verify:

* schema;
* row counts;
* constraints;
* indexes;
* foreign keys;
* representative records;
* derived data;
* search indexes;
* vector indexes;
* application compatibility.

Migration success means more than:

```text
Migration command exited 0.
```

---

# 58. Workflow Recovery

A failed workflow should be recoverable when architecture permits.

Recovery options:

```text
Retry Step
Resume Checkpoint
Restart Failed Branch
Invalidate Derived Artifact
Request Human Review
Abort Workflow
```

Recovery must preserve auditability.

Do not silently erase failure history.

---

# 59. Human Review During Debugging

If a system produces a questionable recommendation but evidence is inconclusive:

```text
AI uncertainty
    ↓
Human Review
    ↓
Decision
    ↓
Feedback
```

Human intervention should not be used to hide system defects.

The system should record the uncertainty and decision.

---

# 60. Debugging Security Issues

Security bugs are treated as high priority.

Process:

```text
Detect
→ Contain
→ Reproduce Safely
→ Assess Scope
→ Identify Root Cause
→ Patch
→ Add Regression Test
→ Re-audit
→ Document
```

Do not expose sensitive exploit details in ordinary logs.

Do not treat security fixes as optional cleanup.

---

# 61. Performance Debugging

Performance problems should be measured.

Investigate:

```text
Frontend
→ API
→ Application
→ Database
→ Retrieval
→ LLM
→ External Provider
```

Measure:

* latency;
* throughput;
* database query time;
* cache hit rate;
* token usage;
* provider latency;
* queue delay;
* rendering time.

Do not optimize based solely on intuition.

---

# 62. Cost Debugging

AI cost problems should inspect:

* model selection;
* prompt size;
* context size;
* redundant retrieval;
* repeated calls;
* unnecessary retries;
* workflow duplication;
* tool calls;
* caching.

Cost should be treated as an engineering signal.

---

# 63. Token and Context Debugging

If an AI task becomes expensive or fails due to context limits, inspect:

```text
Retrieved Documents
Entity Count
Topic Count
Evidence Count
Prompt Size
Output Budget
Redundant Information
Compression
```

Prefer context selection and compression over indiscriminate truncation.

---

# 64. Stale Data Debugging

When an answer appears outdated, inspect:

* source timestamp;
* freshness policy;
* cache TTL;
* snapshot date;
* provider timestamp;
* indexing timestamp;
* derived-data version.

Freshness must be visible.

---

# 65. Contradiction Debugging

If two sources disagree:

```text
Source A
≠
Source B
```

do not silently choose one unless a defined reliability policy supports it.

Represent:

```text
CONFLICTED
```

and evaluate:

* source reliability;
* timestamp;
* context;
* specificity;
* provenance.

---

# 66. Documentation Bugs

Documentation inconsistencies are defects when they can mislead implementation.

Examples:

* two docs define different agent responsibilities;
* output contract contradicts data architecture;
* project structure contradicts technical architecture;
* task board references nonexistent modules.

Documentation must be debugged like architecture.

---

# 67. Documentation Audit

When discovering a structural inconsistency:

```text
Detect contradiction
→ Identify authoritative document
→ Determine affected documents
→ Update consistently
→ Re-audit references
→ Record change if significant
```

Do not solve contradictions by adding another document that says something different.

---

# 68. Definition of Root Cause

A root cause should identify the mechanism that produced the failure.

Weak:

```text
AI produced wrong result.
```

Better:

```text
The intent classifier received SERP evidence from a different search context because the retrieval key omitted country.
```

The second explanation leads to an actionable fix.

---

# 69. Fix Quality

A good fix should:

* address the root cause;
* preserve architectural boundaries;
* avoid unnecessary scope expansion;
* have a targeted test;
* not introduce regressions;
* preserve compatibility where required;
* update documentation if behavior changed.

---

# 70. Avoid Symptom Patching

Do not fix:

```text
Wrong recommendation
```

by merely changing:

```text
UI text
```

if the underlying problem is:

```text
Incorrect decision logic
```

Likewise:

```text
500 error
```

should not be "fixed" by:

```text
catch Exception
return 200
```

unless the behavior is explicitly intended.

---

# 71. Stop Conditions

Debugging should stop when:

1. root cause is sufficiently established;
2. fix is implemented;
3. targeted tests pass;
4. relevant regression tests pass;
5. runtime behavior is verified where required;
6. no known regression remains;
7. state/documentation is updated.

If the issue cannot be resolved, stop with:

* evidence;
* current hypothesis;
* confirmed facts;
* blockers;
* attempted fixes;
* recommended next action.

Do not claim completion.

---

# 72. Failed Fix Tracking

If a fix attempt fails, record:

```text
Attempt
Hypothesis
Change
Observed Result
Why It Failed
Next Hypothesis
```

This prevents repeated experimentation and wasted context.

---

# 73. Development Handoff

A completed task should produce a concise handoff containing:

```text
Task
Status
Implemented Changes
Files Changed
Tests Run
Tests Passed
Runtime Verification
Known Limitations
Unverified Areas
Follow-up Tasks
Documentation Updated
```

The handoff must distinguish facts from assumptions.

---

# 74. No Fake Completion

The following statements are prohibited unless verified:

```text
"Everything works."
"Production ready."
"Integration is complete."
"All tests pass."
"Database migration is verified."
"AI quality is validated."
```

Instead use precise states:

```text
Implemented
Tested
Runtime Verified
Partially Verified
Unverified
Blocked
```

---

# 75. Development State Model

A task may use states such as:

```text
PLANNED
AUTHORIZED
IN_PROGRESS
BLOCKED
IMPLEMENTED
TESTING
VERIFIED
PARTIALLY_VERIFIED
FAILED
REQUIRES_REVIEW
COMPLETED
```

`IMPLEMENTED` does not imply `VERIFIED`.

`VERIFIED` does not automatically imply `COMPLETED` if documentation/state updates remain.

---

# 76. Debugging Evidence Model

Every significant debugging case should preserve:

```yaml id="xg6s2p"
issue:
  symptom: ""
  reproduction: ""
  environment: ""
  classification: ""
  evidence: []

analysis:
  confirmed_facts: []
  hypotheses: []
  root_cause: ""
  confidence: ""

fix:
  changes: []
  files: []

validation:
  targeted_tests: []
  regression_tests: []
  runtime_verification: []
  remaining_risks: []

state:
  status: ""
  follow_up: []
```

This is a conceptual model, not a mandatory literal schema.

---

# 77. Development Quality Gates

Before merging meaningful implementation:

```text
Architecture Check
    ↓
Type/Static Check
    ↓
Unit Tests
    ↓
Integration Tests
    ↓
Contract Tests
    ↓
AI Evaluation if applicable
    ↓
Security Checks
    ↓
Build
    ↓
Runtime Verification
```

The required gates depend on the task.

---

# 78. Pull Request / Change Review

A meaningful change should communicate:

* problem;
* scope;
* architectural impact;
* implementation;
* tests;
* migration;
* security impact;
* performance impact;
* AI impact;
* documentation impact.

Large unrelated changes should be avoided.

---

# 79. Refactoring Rules

Refactoring is allowed when authorized and justified.

A refactor should preserve behavior unless explicitly intended otherwise.

Before refactoring:

```text
Understand Existing Behavior
→ Identify Tests
→ Define Invariants
→ Refactor
→ Run Regression
```

Do not use refactoring as a way to conceal unresolved functional defects.

---

# 80. Technical Debt

Technical debt should be explicit.

Record:

* location;
* reason;
* risk;
* impact;
* proposed resolution;
* priority.

Technical debt must not silently become permanent architecture.

---

# 81. Dependency Upgrades

Dependency upgrades should be treated as controlled changes.

Before upgrade:

* identify affected modules;
* inspect changelog/release notes where appropriate;
* check compatibility;
* run tests.

After upgrade:

* run regression;
* verify runtime;
* inspect performance/security implications.

Avoid unrelated upgrades during focused bug fixes.

---

# 82. Debugging Tool Policy

Developers and coding agents may use appropriate tools for:

* repository inspection;
* static analysis;
* testing;
* profiling;
* database inspection;
* network debugging;
* browser debugging;
* AI evaluation.

Tool usage must follow:

`26_SKILLS_AND_TOOLING_POLICY.md`.

Tools should produce evidence, not replace engineering judgment.

---

# 83. AI Coding Agent Rules

When an AI coding agent is used, it MUST:

1. inspect relevant project documentation;
2. inspect current project state;
3. identify the authorized task;
4. inspect existing implementation;
5. avoid unnecessary scope expansion;
6. make bounded changes;
7. run appropriate tests;
8. report unverified areas;
9. update state/documentation;
10. avoid claiming work it did not perform.

---

# 84. Agent Debugging Boundary

AI agents should not be given unrestricted debugging authority.

A debugging agent may:

* inspect logs;
* inspect code;
* run tests;
* propose fixes;
* implement authorized fixes.

It should not automatically:

* modify production data;
* disable security controls;
* rotate credentials;
* delete evidence;
* bypass authorization;
* deploy irreversible changes.

Consequential actions require appropriate authorization.

---

# 85. Production Debugging

Production debugging must prioritize:

```text
Safety
Evidence Preservation
Minimal Intervention
Rollback
Observability
Auditability
```

Do not experiment directly against production when a safe reproduction environment exists.

---

# 86. Incident Severity

Suggested severity:

### P0 — Critical

Examples:

* unauthorized access;
* destructive data corruption;
* major security breach;
* system-wide failure.

### P1 — High

Examples:

* major workflow failure;
* widespread incorrect SEO decisions;
* significant data integrity issue.

### P2 — Medium

Examples:

* isolated feature failure;
* degraded non-critical workflow.

### P3 — Low

Examples:

* minor UI defect;
* low-impact usability issue.

Severity may be adjusted based on actual impact.

---

# 87. Incident Response

For significant production incidents:

```text
Detect
→ Contain
→ Assess
→ Recover
→ Verify
→ Root Cause
→ Regression Prevention
→ Document
```

Recovery should not erase evidence needed for root-cause analysis.

---

# 88. Rollback

Changes should have a rollback strategy where practical.

Possible rollback mechanisms:

* code rollback;
* feature flag;
* migration rollback;
* data restoration;
* provider fallback;
* workflow cancellation;
* artifact supersession.

Irreversible actions require stronger approval.

---

# 89. Feature Flags

Feature flags may be used for:

* experimental AI capabilities;
* new models;
* new workflows;
* risky migrations;
* staged rollout.

Flags must not become permanent hidden architecture.

Each significant flag should have:

* owner;
* purpose;
* status;
* rollout strategy;
* removal plan.

---

# 90. Reproducibility

Development should strive for reproducible builds and tests.

Record:

* runtime versions;
* dependency lockfiles;
* environment configuration;
* database schema version;
* relevant model/provider versions.

If exact reproduction is impossible, document the limitation.

---

# 91. Quality Over Speed

Fast implementation is not the primary objective.

The desired optimization is:

```text
Correct
+
Understandable
+
Testable
+
Recoverable
+
Maintainable
```

A fast but unverifiable implementation creates downstream cost.

---

# 92. Engineering Decision Rule

When multiple fixes are possible, prefer the solution that:

1. addresses the root cause;
2. preserves architecture;
3. minimizes hidden coupling;
4. improves observability;
5. is testable;
6. is reversible where practical;
7. preserves provider independence;
8. preserves human authority;
9. does not introduce unnecessary complexity.

---

# 93. Debugging Anti-Patterns

Avoid:

* changing code before reproducing;
* guessing root cause;
* fixing symptoms only;
* adding random retries;
* swallowing exceptions;
* disabling validation;
* disabling security to make tests pass;
* hardcoding provider responses;
* inventing missing data;
* modifying production data manually without procedure;
* upgrading dependencies unnecessarily;
* rewriting large modules for small bugs;
* changing multiple unrelated systems simultaneously;
* declaring success without evidence;
* relying exclusively on AI self-evaluation;
* exposing private chain-of-thought for debugging.

---

# 94. Final Development Model

The project's engineering operating model is:

```text
Documentation
    ↓
Project State
    ↓
Authorized Task
    ↓
Relevant Context
    ↓
Existing Implementation
    ↓
Evidence
    ↓
Implementation
    ↓
Targeted Validation
    ↓
Regression Validation
    ↓
Runtime Verification
    ↓
State Update
    ↓
Handoff
```

The debugging operating model is:

```text
Detect
    ↓
Reproduce
    ↓
Evidence
    ↓
Classify
    ↓
Root Cause
    ↓
Fix
    ↓
Targeted Test
    ↓
Regression
    ↓
Runtime Verification
    ↓
Document
```

---

# 95. Non-Negotiable Rules

1. No unauthorized implementation.
2. Read relevant documentation before modifying architecture or behavior.
3. Reproduce meaningful bugs whenever practical.
4. Preserve evidence before changing the system.
5. Distinguish symptom from root cause.
6. Classify failures before fixing them.
7. Treat AI failures as potentially involving input, context, retrieval, prompt, model, validation, or domain logic.
8. Never fabricate unavailable external data.
9. Never bypass output contracts.
10. Never bypass authorization to simplify debugging.
11. Never hide failures with broad exception handling.
12. Retries must be bounded and justified.
13. Failed workflows must remain auditable.
14. Important fixes require regression protection.
15. Prompt and model changes require appropriate AI evaluation.
16. Runtime verification must be distinguished from static implementation.
17. External integrations must not be claimed as verified unless actually exercised.
18. Security failures receive elevated priority.
19. Documentation contradictions are engineering defects.
20. Production changes must prioritize safety and auditability.
21. Debugging must produce evidence, not guesses.
22. Completion claims must match actual verification.
23. Context must remain task-specific and efficient.
24. AI coding agents must follow the same engineering discipline as human developers.
25. The project state must remain synchronized with implementation reality.

---

# 96. Definition of Done

A development or debugging task is complete only when:

* the authorized scope is implemented;
* the root cause is understood where applicable;
* architectural boundaries remain intact;
* contracts remain valid;
* targeted tests pass;
* required regression tests pass;
* security implications are addressed;
* runtime behavior is verified where required;
* external integrations are accurately classified as verified/unverified;
* relevant documentation is updated;
* project state is updated;
* known limitations are recorded;
* no false completion claim is made.

---

# 97. Relationship to Other Documents

This document depends on:

* `03_MASTER_RULES.md`
* `04_SYSTEM_ARCHITECTURE.md`
* `05_AI_AGENT_ARCHITECTURE.md`
* `07_TECHNICAL_ARCHITECTURE.md`
* `16_OUTPUT_CONTRACTS.md`
* `20_PROJECT_STRUCTURE.md`

It is directly related to:

* `21_DEVELOPMENT_AND_DEBUG.md`
* `22_TESTING_AND_VALIDATION.md`
* `23_PROJECT_CONTROL_CENTER.md`
* `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md`
* `25_CONTEXT_MANAGEMENT.md`
* `26_SKILLS_AND_TOOLING_POLICY.md`

It operationalizes the project's broader rules into a concrete engineering and debugging process.

---

# 98. Document Control

```yaml
document:
  id: "21"
  filename: "21_DEVELOPMENT_AND_DEBUG.md"
  status: "APPROVED_AS_BASELINE_DEVELOPMENT_AND_DEBUG"
  authority: "baseline_development_debugging_and_runtime_verification"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

development:
  documentation_first: true
  task_authorization_required: true
  bounded_changes: true
  evidence_driven: true
  runtime_verification_required_when_applicable: true
  no_fake_completion: true

debugging:
  canonical_loop:
    - "detect"
    - "reproduce"
    - "evidence"
    - "classify"
    - "root_cause"
    - "fix"
    - "targeted_test"
    - "regression"
    - "runtime_verification"
    - "document"

failure_categories:
  - "code"
  - "data"
  - "contract"
  - "domain"
  - "ai"
  - "prompt"
  - "model"
  - "retrieval"
  - "search"
  - "serp"
  - "integration"
  - "workflow"
  - "state"
  - "concurrency"
  - "security"
  - "permission"
  - "performance"
  - "configuration"
  - "infrastructure"
  - "frontend"
  - "ux"
  - "observability"
  - "documentation"
  - "environment"

validation:
  targeted_tests: true
  regression_tests: true
  runtime_verification: true
  ai_evaluation_when_applicable: true
  security_validation: true

ai_debugging:
  evidence_first: true
  prompt_version_tracking: true
  model_tracking: true
  context_tracking: true
  tool_tracking: true
  private_chain_of_thought_storage: false
  hallucinated_data_allowed: false

external_integrations:
  provider_independence: true
  no_fabrication: true
  runtime_verification_required_for_verified_status: true
  bounded_retries: true

security:
  authorization_bypass_for_debugging: false
  secrets_in_logs: false
  production_experimentation: restricted
  security_regression_tests: required

state:
  implementation_is_not_verification: true
  verification_is_not_necessarily_completion: true
  unverified_work_must_be_explicit: true

engineering:
  root_cause_over_symptom_patch: true
  minimal_change_preferred: true
  reproducibility_preferred: true
  observability_required: true
  auditability_required: true

next_dependency:
  document: "22_TESTING_AND_VALIDATION.md"
  purpose: "systematic_testing_validation_and_ai_evaluation"
```

---

**End of `21_DEVELOPMENT_AND_DEBUG.md`**
