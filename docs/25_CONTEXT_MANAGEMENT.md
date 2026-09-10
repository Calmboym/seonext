# 25 — Context Management

**Document:** `25_CONTEXT_MANAGEMENT.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Context Architecture, Retrieval, Session Continuity, Context Optimization & AI Working-Memory Specification
**Status:** `APPROVED_AS_BASELINE_CONTEXT_MANAGEMENT`
**Authority:** Baseline specification for task-specific context retrieval, context assembly, persistent project continuity, context prioritization, context compression, session handoff, context validation, and AI context efficiency.

---

# 1. Purpose

Context Management defines how the SEO Research & Strategy Copilot preserves, retrieves, assembles, prioritizes, validates, and releases information required for reliable AI-assisted work.

The system must prevent the project from depending on:

* growing conversation history,
* repeated manual explanations,
* indiscriminate document loading,
* hidden assumptions,
* stale context,
* contradictory context,
* unnecessary token consumption.

The objective is:

```text
Minimum Sufficient Context
+
Maximum Relevant Authority
+
Explicit Provenance
+
Current Project State
=
Reliable AI Execution
```

---

# 2. Core Principle

Context is not the same as memory.

Context is the information required to perform a specific task correctly.

```text
Memory
    = information that may be useful later

Context
    = information currently required for a task
```

The system must therefore retrieve context dynamically according to the active objective.

---

# 3. Context as a First-Class System Capability

Context management is a cross-cutting capability used by:

* Project Control Center
* Orchestrator
* Agents
* Decision Engine
* Workflows
* Output Contracts
* Human Review
* Development
* Testing
* Debugging
* Tooling
* Documentation

Conceptually:

```text
                    ┌───────────────┐
                    │ Project State │
                    └───────┬───────┘
                            ↓
┌──────────────┐     ┌───────────────┐     ┌──────────────┐
│ Documentation│ ──→ │ Context Engine│ ←── │ Task / Goal  │
└──────────────┘     └───────┬───────┘     └──────────────┘
                             ↓
                    ┌─────────────────┐
                    │ Context Package │
                    └────────┬────────┘
                             ↓
                    Agent / Workflow / AI
```

---

# 4. Context Objectives

The context system must provide:

1. Relevance
2. Authority
3. Freshness
4. Completeness
5. Minimality
6. Provenance
7. Consistency
8. Task alignment
9. Security
10. Reproducibility

---

# 5. Context Sources

Context may originate from:

```text
Project Documentation
Project State
Task Definitions
Architecture Decisions
Decision Records
Source Code
Database State
Structured Knowledge
Evidence
Research Artifacts
Search/SERP Data
Agent Outputs
Workflow State
Human Decisions
Human Feedback
Test Results
Runtime Logs
Tool Results
External Provider Data
Historical Snapshots
```

Each source has different authority and freshness.

---

# 6. Context Source Hierarchy

When sources conflict, the system must prefer authoritative sources according to the canonical authority hierarchy defined in `03_MASTER_RULES.md` § 2 ("Rule Hierarchy"). This document does not define a competing hierarchy — refer to that section as the single source of truth. (Prior to this bootstrap, this section contained its own divergent hierarchy; that duplication has been resolved — see `.ai/PROJECT_STATE.md`.)

Context assembly (§ 7 onward) must resolve conflicts using that canonical hierarchy, not an independent ordering.

---

# 7. Context Types

The system should distinguish:

### Instruction Context

Rules governing the current task.

### Domain Context

SEO knowledge required for reasoning.

### Project Context

Current project state and decisions.

### Task Context

Specific objective and scope.

### Code Context

Relevant implementation.

### Data Context

Relevant database and knowledge state.

### Evidence Context

Sources supporting claims.

### Workflow Context

Current workflow state.

### User Context

Relevant user decisions and preferences.

### Tool Context

Available tools, permissions, and capabilities.

### Historical Context

Previous states required to understand change.

---

# 8. Context Package

A task should receive a structured context package.

Conceptually:

```yaml id="f6v4x7"
context:
  task:
  objective:
  scope:
  constraints:
  project_state:
  relevant_documents:
  relevant_decisions:
  relevant_code:
  relevant_data:
  relevant_evidence:
  workflow_state:
  human_decisions:
  tools:
  skills:
  tests:
  risks:
  blockers:
  historical_context:
```

---

# 9. Required vs Optional Context

Every context item should be classified.

```text id="8x2z9v"
REQUIRED
RECOMMENDED
OPTIONAL
EXCLUDED
```

### REQUIRED

Execution should not proceed safely without it.

### RECOMMENDED

Strongly useful but not always mandatory.

### OPTIONAL

May improve reasoning but is not necessary.

### EXCLUDED

Known to be irrelevant or unsafe for the current task.

---

# 10. Context Assembly Pipeline

```text id="v6yn5m"
Task
  ↓
Identify Objective
  ↓
Identify Scope
  ↓
Identify Dependencies
  ↓
Retrieve Authoritative Documents
  ↓
Retrieve Project State
  ↓
Retrieve Relevant Decisions
  ↓
Retrieve Relevant Code/Data
  ↓
Retrieve Evidence
  ↓
Retrieve Required Tool Context
  ↓
Filter Irrelevant Information
  ↓
Resolve Conflicts
  ↓
Rank Context
  ↓
Validate Completeness
  ↓
Assemble Context Package
  ↓
Execute
```

---

# 11. Task-Centered Retrieval

Context retrieval should begin from the task.

Not:

```text
Load everything
    ↓
Ask AI what matters
```

Preferred:

```text
Task
    ↓
Dependency Graph
    ↓
Relevant Knowledge
    ↓
Relevant Documents
    ↓
Relevant Code
    ↓
Relevant Evidence
```

---

# 12. Context Retrieval Inputs

The retrieval engine may use:

```text
Task ID
Feature ID
Module ID
Workflow Step
Agent ID
Objective
Query
Required Output Contract
Affected Data Entities
Dependencies
Current Project State
Human Decisions
```

---

# 13. Context Retrieval Strategies

The system may use multiple retrieval strategies.

### Exact Retrieval

Known document, section, task, or ID.

### Semantic Retrieval

Conceptually relevant content.

### Dependency Retrieval

Documents and artifacts required by dependencies.

### Graph Retrieval

Related entities, topics, decisions, or artifacts.

### Temporal Retrieval

Current or historical state.

### Evidence Retrieval

Sources supporting a claim.

### Hybrid Retrieval

Combination of structured filters and semantic similarity.

---

# 14. Hybrid Context Retrieval

Semantic similarity alone is insufficient.

A context retrieval system should combine:

```text
Metadata
+
Dependency
+
Authority
+
Semantic Similarity
+
Freshness
+
Task Relevance
+
Project Scope
```

Conceptually:

```text
Context Score =
Relevance
× Authority
× Freshness
× Scope Match
× Dependency Importance
```

The exact scoring formula may evolve.

---

# 15. Authority Scoring

Context should not be ranked solely by semantic similarity.

For example:

```text
Old AI-generated note
```

may be semantically closer than:

```text
Approved architecture document
```

The approved architecture must win when architecture is relevant.

---

# 16. Freshness

Context must account for temporal validity.

Examples:

```text
Current project state
Recent decision
Current code
Historical architecture
Old SERP snapshot
```

These are not interchangeable.

The system should expose freshness metadata.

---

# 17. Context Provenance

Every significant context item should retain:

```yaml id="wdxj8w"
provenance:
  source_type:
  source_id:
  source_version:
  retrieved_at:
  effective_at:
  authority:
  freshness:
  confidence:
```

This enables the system to answer:

> Why was this information included?

---

# 18. Context Confidence

Context itself may have different reliability.

Suggested states:

```text id="tljq3q"
VERIFIED
VALIDATED
OBSERVED
INFERRED
ESTIMATED
STALE
CONFLICTED
UNKNOWN
```

Low-confidence context must not silently appear as fact.

---

# 19. Context Conflict Detection

If two relevant context sources disagree:

```text id="e5n8pn"
Source A → Entity type = Product
Source B → Entity type = Service
```

the system must detect the conflict.

It should:

1. identify the conflict,
2. compare authority,
3. compare freshness,
4. preserve both sources,
5. determine whether a resolution exists,
6. request human input when necessary.

---

# 20. Context Conflict Policy

Never silently resolve material conflicts.

Preferred result:

```yaml id="3j6w2x"
conflict:
  status: CONFLICTED
  sources:
    - source_a
    - source_b
  resolution:
    status: REQUIRES_REVIEW
```

---

# 21. Context Completeness

Before execution, the system should determine whether required context exists.

```text id="k5ud0p"
COMPLETE
PARTIAL
INSUFFICIENT
CONFLICTED
UNKNOWN
```

If required context is insufficient, the AI should:

* retrieve additional context,
* request clarification,
* or stop.

It must not fabricate missing context.

---

# 22. Context Sufficiency

Context should be sufficient for the task, not exhaustive.

The correct question is:

> Is there enough authoritative information to perform this task reliably?

Not:

> Have we loaded everything?

---

# 23. Context Budget

Each AI execution should have a context budget.

The budget may consider:

```text
Token Capacity
Task Complexity
Model Limits
Cost
Latency
Required Evidence
Required Output
```

The context system should prioritize high-value information when the budget is constrained.

---

# 24. Context Prioritization

Recommended priority:

```text
1. Current task instructions
2. Critical project rules
3. Direct dependencies
4. Relevant authoritative documents
5. Current project state
6. Human decisions
7. Required data
8. Evidence
9. Relevant implementation
10. Supporting context
11. Historical context
12. Optional background
```

This ordering may change based on task type.

---

# 25. Context Compression

When context exceeds the budget, the system may compress it.

Compression must preserve:

* decisions,
* constraints,
* requirements,
* evidence,
* important relationships,
* unresolved conflicts,
* task scope,
* verification state.

Compression must not erase critical provenance.

---

# 26. Safe Compression

A compressed context should retain:

```yaml id="q0nqz7"
summary:
  source:
  source_version:
  original_reference:
  preserved_claims:
  preserved_decisions:
  preserved_constraints:
  preserved_conflicts:
  compression_method:
```

The system must be able to trace important claims back to original sources.

---

# 27. Context Summaries

Summaries are derived artifacts.

They must not replace authoritative sources.

```text id="qz6m8b"
Original Document
      ↓
Context Summary
      ↓
AI Execution
```

The summary may improve efficiency, but the original remains authoritative.

---

# 28. Context Caching

Frequently used context may be cached.

Examples:

```text
Project Rules
Design Tokens
Agent Registry
Current Project State
Active Workflow
Stable Domain Definitions
```

Cached context must have invalidation rules.

---

# 29. Cache Invalidation

Context cache should be invalidated when:

* source document changes,
* project state changes,
* decision changes,
* task scope changes,
* architecture changes,
* relevant data changes,
* context version expires.

---

# 30. Context Versioning

Context packages should be reproducible.

Recommended:

```yaml id="q5wh0u"
context_package:
  id:
  task_id:
  version:
  created_at:
  sources:
  source_versions:
  retrieval_strategy:
  ranking_strategy:
  compression:
```

This allows debugging of AI decisions.

---

# 31. Reproducibility

For important AI outputs, the system should be able to reconstruct:

```text id="1f8e1n"
Task
+
Context
+
Model
+
Prompt
+
Tools
+
Output Contract
+
Evidence
```

This does not require reproducing stochastic output exactly.

It requires preserving the execution conditions sufficiently for evaluation and debugging.

---

# 32. Context and AI Agents

Every agent should declare context requirements.

Example:

```yaml id="fl1u2j"
agent:
  id: topic-validation

  required_context:
    - topic
    - business_model
    - entity_model
    - search_context
    - serp_data
    - decision_rules

  optional_context:
    - competitor_history
```

---

# 33. Context and Workflows

Each workflow step should define its context.

```yaml id="v3e0ec"
workflow_step:
  id:
  input_context:
  required_context:
  produced_context:
  retained_context:
  discarded_context:
```

A workflow should not carry the entire context of every previous step indefinitely.

---

# 34. Context Propagation

Workflow context should be selectively propagated.

```text id="ly6gzo"
Step A
  ↓
Relevant Output
  ↓
Context Filter
  ↓
Step B
```

Not:

```text id="7i6i4g"
Step A
  ↓
Everything
  ↓
Step B
```

---

# 35. Context Lifecycle

```text id="tx3mne"
DISCOVER
   ↓
RETRIEVE
   ↓
FILTER
   ↓
RANK
   ↓
VALIDATE
   ↓
ASSEMBLE
   ↓
USE
   ↓
COMPRESS / CACHE
   ↓
EXPIRE / INVALIDATE
```

---

# 36. Context Retention

Not all context should be retained permanently.

### Persistent

* decisions,
* project state,
* approved documents,
* evidence,
* important outputs,
* audit records.

### Temporary

* intermediate reasoning inputs,
* transient tool results,
* temporary retrieval candidates.

### Ephemeral

* scratch data,
* temporary execution state,
* low-value intermediate artifacts.

Retention should follow project and data-governance policies.

---

# 37. Conversation Context

Conversation history may be useful but is not authoritative project state.

Conversation should be treated as:

```text id="4b0c0b"
TEMPORARY CONTEXT
```

Important decisions discovered in conversation should be persisted into the appropriate project artifact.

---

# 38. Conversation-to-State Promotion

When a conversation produces a material decision:

```text id="d4spq8"
Conversation
    ↓
Identify Decision
    ↓
Validate
    ↓
Human Confirmation Where Required
    ↓
Persist Decision
    ↓
Update Project State
```

The system must not rely on the conversation remaining available.

---

# 39. Session Continuity

A new session must be able to resume work.

Minimum persistent continuity:

```text id="y4vvvs"
Project State
Active Task
Authorization
Recent Decisions
Open Blockers
Verification State
Changed Files
Tests
Required Context
Next Action
```

---

# 40. Session Recovery

Recovery procedure:

```text id="qf8h7e"
Load Project State
        ↓
Identify Active Task
        ↓
Check Authorization
        ↓
Check Handoff
        ↓
Inspect Recent Changes
        ↓
Inspect Tests
        ↓
Check Blockers
        ↓
Rebuild Required Context
        ↓
Resume or Re-plan
```

---

# 41. Handoff Context

The handoff should be concise but sufficient.

```yaml id="qxyj9u"
handoff:
  current_task:
  objective:
  completed:
  incomplete:
  files_changed:
  tests_run:
  verification:
  blockers:
  decisions:
  risks:
  required_context:
  next_action:
```

---

# 42. Context and Project Control Center

The Project Control Center identifies the current state.

Context Management converts that state into task-specific working context.

```text id="0d4tcz"
Project Control Center
        ↓
Active Task
        ↓
Context Manager
        ↓
Task Context Package
```

---

# 43. Context and Documentation

The system should support section-level retrieval.

Instead of:

```text
Load entire 30-page document
```

prefer:

```text
Retrieve relevant section
+
Parent heading
+
Referenced definitions
+
Required dependencies
```

Full documents remain available for global audits.

---

# 44. Context and Documentation Dependencies

If document A depends on document B, retrieval may automatically include relevant sections of B.

Example:

```text id="yapm7v"
Agent Specification
      ↓
Output Contract
      ↓
Relevant contract definition
```

Only relevant portions should be loaded when possible.

---

# 45. Context and Source Code

Code retrieval should be task-oriented.

For a backend task:

```text id="qkfjv0"
Relevant module
+
Interfaces
+
Dependencies
+
Tests
+
Configuration
```

not the entire repository.

---

# 46. Code Context Boundaries

Code context should respect:

* module boundaries,
* dependency direction,
* ownership,
* public interfaces,
* test boundaries.

This helps prevent accidental coupling.

---

# 47. Context and Data

Data context may include:

```text
Entity Records
Topic Records
Search Data
SERP Snapshots
Decisions
Evidence
Page Records
Competitor Data
Historical State
```

The system must apply project and tenant isolation.

---

# 48. Context and Evidence

Evidence retrieval should prioritize:

```text
Directly relevant
Authoritative
Recent
Project-specific
Verifiable
```

AI-generated claims should not outrank primary evidence simply because they are semantically similar.

---

# 49. Context and Search Intelligence

Search tasks require contextual dimensions such as:

```text
Query
Language
Country
Location
Device
Search Engine
Date
Market
Audience
Topic
Entity
SERP Snapshot
```

Without these dimensions, search results may be misleading.

---

# 50. Context and Decision Engine

Decision context should include:

```text
Business Reality
Search Reality
Entity Context
Topic Context
Intent
SERP Evidence
Competitive Landscape
Existing Pages
Historical Decisions
Constraints
```

A decision should not be generated from search volume alone.

---

# 51. Context and Human Review

Human review context should prioritize:

```text
Recommendation
Evidence
Confidence
Alternatives
Conflicts
Business Impact
Relevant Existing Decisions
```

Private AI chain-of-thought must not be exposed as a substitute for explainability.

---

# 52. Context and Output Contracts

The output contract determines required context.

Example:

```text id="r2f8a0"
Page Candidate Contract
        ↓
Requires:
    topic
    intent
    SERP
    business relevance
    existing page inventory
```

Missing required context should produce an explicit incomplete state.

---

# 53. Context and Testing

Testing context should include:

```text
Requirement
Acceptance Criteria
Relevant Implementation
Expected Contract
Fixtures
Golden Dataset
Previous Regression Cases
Known Failure Modes
```

This prevents tests from being disconnected from project intent.

---

# 54. Context and Debugging

Debug context should include:

```text
Error
Stack Trace
Relevant Code
Configuration
Recent Changes
Task
Runtime Environment
Logs
Related Tests
Historical Failures
Provider Responses
```

Debugging should not require loading unrelated project material.

---

# 55. Context and Tooling

Tool context should include:

```text
Available Tools
Required Capabilities
Permissions
Versions
Provider Configuration
Known Limitations
Security Constraints
```

Tool usage must comply with `26_SKILLS_AND_TOOLING_POLICY.md`.

---

# 56. Context and Skills

If a task requires a skill:

```text id="bbj9sy"
Identify Capability
    ↓
Check Skill Registry
    ↓
Check Availability
    ↓
Check Permission
    ↓
Install if permitted
    ↓
Validate
    ↓
Use
    ↓
Record
```

The context package should include only the skill information relevant to the task.

---

# 57. Context Security

Context retrieval must enforce:

* authentication,
* authorization,
* tenant isolation,
* project isolation,
* least privilege,
* sensitive-data filtering,
* secret exclusion,
* auditability.

The context engine must not expose information merely because it is semantically relevant.

---

# 58. Sensitive Context

Sensitive information should be classified.

Examples:

```text
Credentials
API Keys
Private Business Data
Private User Data
Internal Security Information
Confidential Research
```

Secrets should never be included in AI prompts unless explicitly required and safely handled.

---

# 59. Prompt Injection Defense

Retrieved content may contain adversarial instructions.

The system must distinguish:

```text
Data
    ≠
Instructions
```

External content must not automatically gain authority over system instructions.

Retrieved web content, documents, or tool outputs must be treated as untrusted data unless explicitly designated otherwise.

---

# 60. Context Trust Boundary

```text id="y5yn6p"
System Rules
    ↓
Project Rules
    ↓
Task Instructions
    ↓
Trusted Structured Context
    ↓
Retrieved Evidence
    ↓
External / Untrusted Content
```

Lower-trust context cannot override higher-trust instructions.

---

# 61. Context Quality Metrics

The system should measure:

```text
Retrieval Precision
Retrieval Recall
Context Relevance
Context Completeness
Context Freshness
Context Redundancy
Context Conflict Rate
Context Compression Ratio
Token Utilization
Context-Related Error Rate
```

These are diagnostic metrics, not standalone quality guarantees.

---

# 62. Context Efficiency

The goal is not minimum token count.

The goal is:

```text
Maximum Decision-Relevant Information
per Unit of Context Cost
```

A slightly larger context may be justified when it materially reduces uncertainty.

---

# 63. Context Waste

Examples of context waste:

* repeated definitions,
* duplicated documents,
* irrelevant code,
* obsolete decisions,
* stale search data,
* unrelated UI details,
* unnecessary conversation history,
* repeated tool outputs.

The system should identify and reduce these.

---

# 64. Context Budget Escalation

If the task cannot be solved within the initial budget:

```text id="fylh7d"
Initial Context
      ↓
Assess Sufficiency
      ↓
Insufficient
      ↓
Expand Retrieval
      ↓
Reassess
      ↓
Execute or Stop
```

Context expansion should be deliberate.

---

# 65. Context Failure Modes

### Missing Context

Required information unavailable.

### Stale Context

Information no longer current.

### Conflicting Context

Sources disagree.

### Excessive Context

Too much irrelevant information.

### Insufficient Context

Not enough evidence for reliable execution.

### Wrong Context

Relevant to another task but not the current task.

### Untrusted Context

Retrieved content attempts to influence execution.

---

# 66. Context Failure Handling

The system should classify failures.

```text id="d0jvsh"
MISSING
STALE
CONFLICTED
INSUFFICIENT
IRRELEVANT
UNTRUSTED
UNAUTHORIZED
```

The response may be:

```text
RETRIEVE_MORE
REFRESH
REQUEST_REVIEW
REDUCE_CONTEXT
REJECT_SOURCE
STOP
```

---

# 67. Context Validation

Before AI execution:

```text id="ewt7zr"
[ ] Task matches context
[ ] Required context exists
[ ] Sources are authorized
[ ] Critical dependencies are present
[ ] Conflicts are identified
[ ] Freshness is acceptable
[ ] Sensitive data is controlled
[ ] Context budget is valid
```

---

# 68. Context Observability

For important executions, logs should record:

```yaml id="k1i7a2"
context_observation:
  task_id:
  context_package_id:
  sources:
  retrieval_method:
  context_size:
  compressed:
  conflicts:
  missing_items:
  freshness:
  execution_result:
```

The actual sensitive content need not be logged.

---

# 69. Context Reproducibility and Privacy

Reproducibility must not require indiscriminate retention of sensitive content.

The system should prefer:

```text
Source IDs
+
Versions
+
Hashes
+
Metadata
```

where sufficient.

---

# 70. Context Retention Policy

Retention should consider:

```text
Business Value
Audit Requirement
Security
Privacy
Cost
Reproducibility
Legal / Regulatory Requirements
```

Not every transient context package needs permanent storage.

---

# 71. Context Garbage Collection

Temporary context may be removed after:

* workflow completion,
* task completion,
* cache expiration,
* retention period,
* explicit invalidation.

Persistent evidence and decisions must remain according to their retention policy.

---

# 72. Context and Multilingual Data

The product supports multilingual operation.

Context retrieval must account for:

```text
Language
Locale
Terminology
Translated Terms
Canonical Entity IDs
Localized Search Context
```

The system should prefer canonical semantic identity over language-specific duplication.

---

# 73. Context and Entity Resolution

Entity identity is especially important for multilingual context.

Example:

```text
Persian Name
English Name
German Name
Alias
External Identifier
        ↓
Same Canonical Entity
```

Context should retrieve the canonical entity and relevant localized representations.

---

# 74. Context and Topic Modeling

Topic context should preserve:

```text
Topic ID
Canonical Name
Aliases
Entity Relationships
Intent
Queries
SERP Evidence
Cluster
Business Relevance
Validation State
Historical Versions
```

This prevents keyword-level retrieval from losing semantic meaning.

---

# 75. Context and Historical Intelligence

Historical context should be included when the task concerns:

* change detection,
* regression,
* trend,
* intent drift,
* SERP drift,
* previous decisions,
* architecture evolution.

Historical context should not automatically override current state.

---

# 76. Context and Living Model

The living SEO intelligence model acts as a persistent context substrate.

```text
Business
   ↕
Entities
   ↕
EAV
   ↕
Topics
   ↕
Queries
   ↕
Intent
   ↕
SERPs
   ↕
Pages
   ↕
Decisions
   ↕
Evidence
```

The context system retrieves relevant subgraphs rather than repeatedly reconstructing the entire model.

---

# 77. Context Graph Retrieval

For relationship-heavy tasks, graph traversal may be preferable.

Example:

```text id="azjv8n"
Topic
 ↓
Entity
 ↓
Attribute
 ↓
Query
 ↓
SERP
 ↓
Page
 ↓
Competitor
```

The retrieval engine may combine graph traversal with semantic retrieval.

---

# 78. Context and Knowledge Versioning

When knowledge changes, context should identify:

```text
Entity Version
Topic Version
Decision Version
SERP Snapshot
Contract Version
Agent Version
Prompt Version
```

This supports reproducibility and historical analysis.

---

# 79. Context Assembly for Decision Support

A decision-support context should normally contain:

```text
Decision Question
Business Constraints
Relevant Entity Model
Relevant Topics
Search Context
SERP Evidence
Existing Page State
Competitor Evidence
Historical Decisions
Alternative Options
Risks
Human Constraints
```

---

# 80. Context Assembly for Research

A research context should normally contain:

```text
Research Question
Scope
Business Model
Known Entities
Known Gaps
Relevant Evidence
Existing Knowledge
Search Context
Required Output Contract
```

---

# 81. Context Assembly for Implementation

An implementation context should normally contain:

```text
Task
Authorization
Acceptance Criteria
Architecture
Relevant Interfaces
Relevant Code
Relevant Tests
Configuration
Dependencies
Known Constraints
```

---

# 82. Context Assembly for Debugging

A debugging context should normally contain:

```text
Failure
Reproduction
Stack Trace
Relevant Code
Recent Changes
Runtime Environment
Configuration
Logs
Tests
Expected Behavior
Actual Behavior
```

---

# 83. Context Assembly for AI Evaluation

Evaluation context should contain:

```text
Task
Input
Expected Contract
Evaluation Criteria
Golden Dataset
Relevant Evidence
Model Version
Prompt Version
Tool Versions
Previous Result
```

---

# 84. Context Governance

Context policies should be governed by:

```text
03_MASTER_RULES.md
23_PROJECT_CONTROL_CENTER.md
24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md
25_CONTEXT_MANAGEMENT.md
26_SKILLS_AND_TOOLING_POLICY.md
```

No context mechanism may override project authority.

---

# 85. Context Governance Rules

1. Context must be task-relevant.
2. Authority must be explicit.
3. Provenance must be preserved.
4. Conflicts must be visible.
5. Missing context must not be fabricated.
6. Stale context must be identifiable.
7. Sensitive context must be protected.
8. External content is untrusted by default.
9. Context must be version-aware.
10. Persistent state must not depend on conversation history.
11. Context compression must preserve critical information.
12. Context retrieval must respect project boundaries.
13. AI must stop when required context is insufficient for reliable execution.

---

# 86. Context Testing

The context system must be tested for:

### Retrieval

* relevant results,
* irrelevant-result rejection,
* dependency retrieval,
* metadata filtering.

### Authority

* authoritative source ranking,
* conflict resolution,
* source trust.

### Freshness

* stale-context detection,
* cache invalidation.

### Security

* tenant isolation,
* authorization,
* sensitive-data filtering,
* prompt injection resistance.

### Efficiency

* context size,
* redundancy,
* retrieval latency,
* token efficiency.

---

# 87. Context Regression Testing

A change to:

* retrieval logic,
* ranking,
* embeddings,
* metadata filters,
* graph traversal,
* compression,
* source hierarchy,

may change AI behavior.

Therefore context retrieval requires regression testing.

---

# 88. Golden Context Sets

The project should maintain representative context-retrieval datasets.

Example:

```yaml id="ddc5t1"
golden_context_case:
  task:
  expected_sources:
  required_sources:
  forbidden_sources:
  expected_priority:
  acceptable_variation:
```

Evaluation should focus on task usefulness rather than exact ordering alone.

---

# 89. Context Evaluation Metrics

Useful evaluation dimensions:

```text
Task Relevance
Source Authority
Completeness
Freshness
Conflict Detection
Noise
Security
Latency
Token Efficiency
Downstream Task Success
```

---

# 90. Context Drift

Context drift occurs when:

```text
Current System
        ≠
Context Assumptions
```

Examples:

* document updated but cached summary remains old,
* code changed but retrieved interface is stale,
* decision changed but old decision remains in context,
* task scope changed but context package remains unchanged.

The system should detect and invalidate stale context.

---

# 91. Context Invalidation Triggers

Invalidate or rebuild context when:

```text
Task Scope Changes
Architecture Changes
Relevant Document Changes
Decision Changes
Project State Changes
Data Changes
Contract Changes
Agent Changes
Workflow Changes
Tool Changes
```

---

# 92. Context Dependency Graph

Context itself can be represented as a dependency graph.

```text
Task
 ↓
Required Document
 ↓
Relevant Section
 ↓
Data Model
 ↓
Implementation
 ↓
Test
 ↓
Evidence
```

This makes context assembly explainable.

---

# 93. Context Cost Management

The system should track:

```text
Tokens
Latency
Retrieval Calls
Embedding Calls
LLM Calls
Tool Calls
Cache Hits
Cache Misses
Compression
```

Cost optimization must not remove evidence required for reliable decisions.

---

# 94. Context and Progressive Disclosure

The system should use progressive context expansion.

```text
Level 1
Task + Rules

        ↓ if insufficient

Level 2
Dependencies + Relevant Documents

        ↓ if insufficient

Level 3
Code + Data + Evidence

        ↓ if insufficient

Level 4
Historical / broader project context

        ↓ if still insufficient

STOP / REQUEST HUMAN INPUT
```

This prevents unnecessary context explosion.

---

# 95. Context Minimum Viable Architecture

MVP should provide:

```text
Task-Centered Retrieval
Document Retrieval
Project State Retrieval
Decision Retrieval
Structured Context Packages
Context Provenance
Context Freshness
Context Validation
Session Handoff
Context Caching
Basic Security Isolation
```

---

# 96. Future Context Capabilities

Future versions may add:

* adaptive context planning,
* learned retrieval policies,
* graph-aware context optimization,
* predictive context prefetching,
* context quality scoring,
* automatic context contradiction detection,
* intelligent compression,
* task-specific retrieval models,
* cross-session semantic continuity,
* context-aware model routing,
* context-cost optimization,
* context failure prediction.

---

# 97. Anti-Patterns

### 97.1 Entire Project in Every Prompt

Wasteful and unreliable.

### 97.2 Conversation as Persistent Memory

Fragile.

### 97.3 Semantic Similarity Only

Ignores authority and dependencies.

### 97.4 Context Without Provenance

Impossible to audit reliably.

### 97.5 Silent Conflict Resolution

Can create false certainty.

### 97.6 Stale Cache as Current Truth

Dangerous.

### 97.7 Untrusted Content as Instructions

Security risk.

### 97.8 Context Compression Without Traceability

Destroys auditability.

### 97.9 Unlimited Context Expansion

Creates cost and reasoning degradation.

### 97.10 Saving Everything Forever

Creates security, privacy, and operational problems.

---

# 98. Definition of Done

The Context Management system is complete when it can:

* identify task-specific context,
* retrieve authoritative documents,
* retrieve project state,
* retrieve relevant decisions,
* retrieve relevant code/data/evidence,
* classify required and optional context,
* rank context using more than semantic similarity,
* track provenance,
* track freshness,
* detect conflicts,
* detect missing context,
* enforce project isolation,
* protect sensitive context,
* defend against instruction injection,
* assemble structured context packages,
* compress safely,
* cache and invalidate context,
* support session recovery,
* support reproducibility,
* support multilingual context,
* support graph-aware retrieval,
* integrate with agents and workflows,
* integrate with testing and debugging,
* measure context quality and cost.

---

# 99. Final Context Operating Model

```text
USER / SYSTEM OBJECTIVE
        ↓
TASK
        ↓
PROJECT CONTROL STATE
        ↓
DEPENDENCY GRAPH
        ↓
CONTEXT REQUIREMENTS
        ↓
AUTHORITATIVE RETRIEVAL
        ↓
SEMANTIC + STRUCTURED + GRAPH RETRIEVAL
        ↓
AUTHORITY / FRESHNESS / SECURITY FILTER
        ↓
CONFLICT DETECTION
        ↓
CONTEXT RANKING
        ↓
CONTEXT BUDGET
        ↓
COMPRESSION IF NEEDED
        ↓
CONTEXT VALIDATION
        ↓
CONTEXT PACKAGE
        ↓
AGENT / WORKFLOW / AI
        ↓
OUTPUT
        ↓
EVIDENCE + STATE UPDATE
        ↓
CONTEXT INVALIDATION / RETENTION
```

---

# 100. Final Context Principle

The system should never optimize for:

```text
"How much information can we give the AI?"
```

It should optimize for:

```text
"How can we give the AI the smallest amount of
authoritative, relevant, current, secure, and
verifiable information required to make a reliable decision?"
```

This is the central principle of Context Management.

---

# 101. Document Control

```yaml id="9p6n4c"
document:
  id: "25"
  filename: "25_CONTEXT_MANAGEMENT.md"
  status: "APPROVED_AS_BASELINE_CONTEXT_MANAGEMENT"
  authority: "baseline_context_retrieval_assembly_continuity_and_efficiency"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

core_capabilities:
  - task_centered_retrieval
  - authoritative_document_retrieval
  - project_state_retrieval
  - decision_retrieval
  - code_context_retrieval
  - data_context_retrieval
  - evidence_retrieval
  - context_ranking
  - context_validation
  - context_provenance
  - context_freshness
  - context_conflict_detection
  - context_compression
  - context_caching
  - cache_invalidation
  - context_versioning
  - session_continuity
  - session_recovery
  - context_security
  - prompt_injection_defense
  - multilingual_context
  - graph_aware_retrieval
  - context_cost_management

context_states:
  - VERIFIED
  - VALIDATED
  - OBSERVED
  - INFERRED
  - ESTIMATED
  - STALE
  - CONFLICTED
  - UNKNOWN

context_completeness:
  - COMPLETE
  - PARTIAL
  - INSUFFICIENT
  - CONFLICTED
  - UNKNOWN

context_priority:
  - REQUIRED
  - RECOMMENDED
  - OPTIONAL
  - EXCLUDED

context_failure_types:
  - MISSING
  - STALE
  - CONFLICTED
  - INSUFFICIENT
  - IRRELEVANT
  - UNTRUSTED
  - UNAUTHORIZED

retrieval_model:
  primary: "task_centered"
  methods:
    - structured
    - semantic
    - dependency
    - graph
    - temporal
    - evidence
    - hybrid

core_requirements:
  task_specific_context: true
  authoritative_sources: true
  provenance: true
  freshness: true
  conflict_detection: true
  context_validation: true
  project_isolation: true
  sensitive_data_protection: true
  prompt_injection_defense: true
  reproducibility: true
  session_continuity: true
  dynamic_context_expansion: true
  context_budgeting: true
  safe_compression: true
  cache_invalidation: true

conversation:
  authoritative_project_state: false
  role: "temporary_context"

security:
  external_content_trusted_by_default: false
  least_privilege: true
  tenant_isolation: true
  project_isolation: true
  secret_exposure_prevention: true

mvp:
  task_centered_retrieval: true
  document_retrieval: true
  project_state_retrieval: true
  decision_retrieval: true
  structured_context_packages: true
  provenance: true
  freshness: true
  validation: true
  session_handoff: true
  caching: true

relationships:
  master_rules: "03_MASTER_RULES.md"
  data_architecture: "06_DATA_ARCHITECTURE.md"
  seo_knowledge_model: "08_SEO_KNOWLEDGE_MODEL.md"
  entity_eav_model: "09_ENTITY_EAV_MODEL.md"
  search_serp_intelligence: "11_SEARCH_AND_SERP_INTELLIGENCE.md"
  agent_specifications: "13_AGENT_SPECIFICATIONS.md"
  agent_workflow: "14_AGENT_WORKFLOW.md"
  human_in_the_loop: "15_HUMAN_IN_THE_LOOP.md"
  output_contracts: "16_OUTPUT_CONTRACTS.md"
  development_and_debug: "21_DEVELOPMENT_AND_DEBUG.md"
  testing_and_validation: "22_TESTING_AND_VALIDATION.md"
  project_control_center: "23_PROJECT_CONTROL_CENTER.md"
  roadmap_dependencies: "24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md"
  skills_tooling_policy: "26_SKILLS_AND_TOOLING_POLICY.md"

next_dependency:
  document: "26_SKILLS_AND_TOOLING_POLICY.md"
  purpose: "skills_tool_discovery_installation_permissions_security_validation_and_usage_governance"
```

---

# 102. Final Status

```yaml id="6y9h2m"
status:
  document: "25_CONTEXT_MANAGEMENT.md"
  state: "APPROVED_AS_BASELINE_CONTEXT_MANAGEMENT"
  core_model: "task_centered_authoritative_context_retrieval"
  context_strategy: "minimum_sufficient_context"
  retrieval_strategy: "hybrid_structured_semantic_dependency_graph_temporal_evidence"
  source_of_truth: "authoritative_persistent_project_state_and_documents"
  conversation_as_persistent_state: false
  provenance_required: true
  freshness_required: true
  conflict_detection_required: true
  context_validation_required: true
  security_boundary: true
  prompt_injection_defense: true
  session_continuity: true
  next_document: "26_SKILLS_AND_TOOLING_POLICY.md"
```
