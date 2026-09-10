# 14 — Agent Workflow

**Document:** `14_AGENT_WORKFLOW.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Agent Workflow & Orchestration Specification
**Status:** `APPROVED_AS_BASELINE_AGENT_WORKFLOW`
**Authority:** Baseline specification for workflow composition, execution, orchestration, state management, dependencies, checkpoints, human review, failure handling, and workflow lifecycle.

---

## 1. Purpose

This document defines how the SEO Research & Strategy Copilot executes multi-step research, analysis, validation, and decision workflows.

The workflow layer connects:

* Human strategic intent
* Tasks
* Workflow planning
* The Central Orchestrator
* Specialized AI agents
* Deterministic services
* External tools and providers
* Shared knowledge
* Evidence
* The SEO Decision Engine
* Human review
* Authorized actions
* Evaluation and learning

The workflow system must transform a strategic objective into an explicit, observable, resumable sequence of controlled operations.

The workflow system is not itself the intelligence layer.

It is the execution and coordination layer that determines:

> **what needs to happen, in what order, under which conditions, using which capabilities, with which evidence, and with which approval requirements.**

---

# 2. Core Principle

The fundamental workflow model is:

```text
Human Strategic Objective
        ↓
Workflow Planning
        ↓
Task Definition
        ↓
Dependency Resolution
        ↓
Context Assembly
        ↓
Agent / Service Execution
        ↓
Evidence + Structured Output
        ↓
Validation
        ↓
Workflow State Update
        ↓
Decision Engine
        ↓
Human Review
        ↓
Authorized Action
        ↓
Outcome
        ↓
Evaluation
        ↓
Learning
```

The workflow engine must never treat successful execution of an AI call as equivalent to successful completion of the strategic objective.

---

# 3. Workflow vs Agent vs Orchestrator

These concepts must remain distinct.

## 3.1 Workflow

A workflow defines:

* objective
* steps
* dependencies
* conditions
* execution order
* checkpoints
* approval gates
* retry policies
* failure policies
* required outputs
* completion criteria

A workflow answers:

> **What sequence of work should happen?**

---

## 3.2 Agent

An agent provides a specialized intelligence capability.

Examples:

* Entity Agent
* Topic Discovery Agent
* Intent Agent
* SERP Intelligence Agent
* Topic Clustering Agent
* Page Architecture Agent

An agent answers:

> **How should this specific analytical task be performed?**

Agents must operate within workflow boundaries.

---

## 3.3 Orchestrator

The Central Orchestrator:

* receives workflow/task requests
* determines required capabilities
* resolves dependencies
* assembles context
* invokes agents/services
* manages execution state
* evaluates workflow conditions
* manages retries
* enforces permissions
* creates checkpoints
* routes human review
* records evidence
* returns structured results

The Orchestrator answers:

> **Which capability should execute now, with what context, and what should happen next?**

---

## 3.4 Decision Engine

The Decision Engine evaluates analytical outputs against:

* business objectives
* search reality
* semantic knowledge
* evidence
* confidence
* constraints
* existing website state
* strategic rules
* human decisions

It answers:

> **What does the available evidence support us doing?**

The Decision Engine does not replace human strategic authority.

---

# 4. Workflow Design Principles

All workflows must follow these principles.

## 4.1 Explicitness

Every meaningful workflow step must have:

* stable identifier
* purpose
* input contract
* output contract
* dependencies
* required context
* capability/agent
* permission requirements
* validation rules
* failure behavior

---

## 4.2 Deterministic Execution

Workflow execution should be deterministic wherever possible.

AI may determine:

* classifications
* hypotheses
* semantic relationships
* recommendations
* confidence
* candidate actions

But the workflow engine should deterministically control:

* state transitions
* dependency checks
* authorization
* retries
* persistence
* checkpointing
* timeout handling
* output validation
* approval gates

---

## 4.3 Evidence Preservation

Every important analytical output must preserve its supporting evidence.

Workflow execution must not discard provenance between steps.

Example:

```text
SERP Observation
    ↓
Intent Inference
    ↓
Topic Validation
    ↓
Cluster Decision
    ↓
Page Recommendation
```

The page recommendation must remain traceable to the evidence collected earlier in the workflow.

---

## 4.4 Resumability

A workflow must be resumable after:

* application restart
* worker failure
* provider timeout
* network failure
* AI failure
* human delay
* partial execution
* deployment
* temporary infrastructure failure

The system must not require restarting the entire workflow unless explicitly necessary.

---

## 4.5 Human Control

Human review must be a first-class workflow state.

A workflow may pause for:

* strategic approval
* ambiguous entity resolution
* topic validation
* page mapping approval
* architecture approval
* conflict resolution
* high-impact action authorization

---

## 4.6 No Hidden Workflow State

Important workflow state must be persisted.

The system must not rely on:

* LLM conversation history
* worker memory
* process memory
* temporary prompts
* undocumented state

as the only source of workflow continuity.

---

# 5. Workflow Object Model

A workflow consists of several core objects.

```text
Workflow
 ├── Workflow Version
 ├── Workflow Run
 │    ├── Step
 │    │    ├── Task
 │    │    ├── Context
 │    │    ├── Evidence
 │    │    ├── Output
 │    │    ├── Validation
 │    │    └── Checkpoint
 │    ├── Decisions
 │    ├── Approvals
 │    └── Errors
 └── Completion Result
```

---

# 6. Workflow Definition

A workflow definition is a versioned specification describing how a class of objectives should be executed.

Conceptual structure:

```yaml
workflow:
  id: seo_research_and_strategy
  version: 1.0

  objective:
    description: >
      Build an evidence-backed SEO strategy from business context
      through topical mapping and page architecture.

  inputs:
    - business_context
    - website_context
    - market_context

  steps:
    - id: business_research
    - id: entity_model
    - id: eav_enrichment
    - id: topic_discovery
    - id: topic_validation
    - id: query_discovery
    - id: intent_analysis
    - id: serp_analysis
    - id: topic_clustering
    - id: page_mapping
    - id: decision_support
    - id: human_review
    - id: architecture
```

This is conceptual and does not prescribe the final implementation schema.

---

# 7. Workflow Run

A Workflow Run represents one execution instance of a workflow definition.

A run must have:

* workflow ID
* workflow version
* project ID
* workspace/tenant ID
* run ID
* initiating user/task
* start timestamp
* current status
* current step
* execution metadata
* accumulated artifacts
* evidence references
* decision references
* approval state
* errors
* completion state

Example statuses:

```text
PLANNED
READY
RUNNING
WAITING_FOR_DEPENDENCY
WAITING_FOR_HUMAN
PAUSED
RETRYING
PARTIALLY_COMPLETED
FAILED
COMPLETED
CANCELLED
EXPIRED
```

---

# 8. Workflow Step

A step represents one meaningful unit of execution.

A step may invoke:

* AI agent
* deterministic service
* search provider
* crawler
* database operation
* validation service
* human review
* decision engine

A step must define:

```yaml
step:
  id:
  type:
  purpose:
  depends_on:
  inputs:
  context_requirements:
  capability:
  tools:
  permissions:
  output_contract:
  validation:
  retry_policy:
  failure_policy:
  approval_policy:
  checkpoint_policy:
```

---

# 9. Step Types

The workflow engine should support several step types.

## 9.1 AI Analysis

Invokes a specialized AI capability.

Examples:

```text
Entity Extraction
Intent Classification
Topic Discovery
Topic Validation
Cluster Analysis
Decision Support
```

---

## 9.2 Deterministic Processing

Examples:

```text
Normalization
Deduplication
Canonicalization
Filtering
Aggregation
Scoring
Schema validation
Database operations
```

---

## 9.3 External Data Acquisition

Examples:

```text
SERP collection
Keyword metrics
Website crawling
Competitor discovery
Search analytics retrieval
```

---

## 9.4 Validation

Validates:

* schema
* evidence
* confidence
* consistency
* business constraints
* data quality
* workflow requirements

---

## 9.5 Human Review

Pauses workflow execution until a human decision is provided.

---

## 9.6 Decision

Invokes the SEO Decision Engine.

---

## 9.7 Conditional Routing

Determines the next workflow branch based on explicit conditions.

---

# 10. Workflow Graph

Workflows should be represented conceptually as directed graphs.

```text
A → B → C → D
```

or:

```text
        → B →
A →              D
        → C →
```

or:

```text
A → B → [condition]
          ├── yes → C
          └── no  → D
```

The workflow engine must support dependency-aware execution.

A step may execute only when its required dependencies have reached valid completion states.

---

# 11. Sequential Execution

Sequential execution should be used where later analysis depends strongly on previous output.

Example:

```text
Business Research
      ↓
Entity Modeling
      ↓
EAV Enrichment
      ↓
Topic Discovery
```

This ensures that topic discovery operates on a richer semantic model.

---

# 12. Parallel Execution

Independent work should execute in parallel where safe.

Example:

```text
                → Keyword Metrics
               /
Topic Universe →
               \
                → SERP Discovery
```

Parallel execution may reduce:

* latency
* workflow duration
* unnecessary waiting

but must not violate:

* data dependencies
* provider limits
* concurrency limits
* cost budgets
* ordering requirements

---

# 13. Conditional Execution

Workflow branches must be explicit.

Example:

```text
Topic Validation
       ↓
Is confidence sufficient?
       ├── YES → SERP Analysis
       └── NO  → Human Review
```

Another example:

```text
Existing Page Analysis
       ↓
Strong existing coverage?
       ├── YES → Cannibalization Analysis
       └── NO  → Content Gap Analysis
```

Conditions must be machine-readable whenever possible.

---

# 14. Iterative Execution

Some workflows require iterative refinement.

Example:

```text
Topic Discovery
      ↓
Validation
      ↓
Insufficient coverage?
      ↓
Additional Discovery
      ↓
Validation
```

Iteration must have:

* maximum iteration count
* measurable stopping conditions
* budget constraints
* quality thresholds

The AI must not create an unbounded loop.

---

# 15. Review Workflow

A review workflow follows:

```text
Analysis
   ↓
Validation
   ↓
Human Review
   ↓
Approved / Rejected / Modify
   ↓
Next Step
```

Human feedback must become structured workflow state rather than disappearing into conversation text.

---

# 16. Retry Workflow

Transient failures may be retried.

Examples:

* network timeout
* temporary provider failure
* rate limit
* worker interruption

Retry policy should define:

```text
maximum attempts
backoff strategy
retryable errors
non-retryable errors
fallback behavior
```

AI reasoning failures should not automatically be retried indefinitely.

---

# 17. Fallback Workflow

A fallback may be used when the preferred capability fails.

Example:

```text
Primary SERP Provider
       ↓
Failure
       ↓
Fallback Provider
       ↓
Normalize
       ↓
Continue
```

Provider fallback must preserve provenance.

The system must record which provider actually produced the evidence.

---

# 18. Core SEO Research Workflow

The canonical strategic workflow is:

```text
Business Understanding
        ↓
Entity Model
        ↓
EAV Enrichment
        ↓
Topic Universe
        ↓
Topic Validation
        ↓
Query Discovery
        ↓
Intent Analysis
        ↓
SERP Intelligence
        ↓
Topic / Query Clustering
        ↓
Page Candidates
        ↓
SEO Decision Engine
        ↓
Human Validation
        ↓
Topical Map
        ↓
Page Architecture
        ↓
Internal Linking
```

This is a reference workflow, not a mandatory sequence for every project.

The Orchestrator must be able to omit, reorder, repeat, or branch steps when justified by:

* available data
* user objective
* project maturity
* website state
* workflow requirements
* dependencies

---

# 19. Business Research Workflow

Conceptual flow:

```text
Business Input
      ↓
Business Research
      ↓
Market Understanding
      ↓
Audience / Need Modeling
      ↓
Business Entity Identification
      ↓
Evidence Validation
      ↓
Business Knowledge Model
```

Outputs should include:

* business entities
* products/services
* audiences
* markets
* business priorities
* differentiators
* constraints
* terminology
* evidence
* uncertainty

---

# 20. Entity Workflow

```text
Business Knowledge
      ↓
Entity Discovery
      ↓
Entity Resolution
      ↓
Entity Classification
      ↓
Relationship Extraction
      ↓
Evidence Validation
      ↓
Entity Graph
```

Potential human checkpoint:

```text
Ambiguous entity
      ↓
Human Resolution
```

The workflow must not silently merge ambiguous entities.

---

# 21. EAV Workflow

```text
Entities
   ↓
Attribute Discovery
   ↓
Value Extraction
   ↓
Normalization
   ↓
Entity References
   ↓
Evidence
   ↓
EAV Validation
   ↓
Knowledge Enrichment
```

Conflicting facts should become explicit conflicts.

They must not be silently overwritten.

---

# 22. Topic Discovery Workflow

```text
Business + Entity + EAV
          ↓
Need / Problem Discovery
          ↓
Topic Candidates
          ↓
Semantic Expansion
          ↓
Query Evidence
          ↓
Topic Normalization
          ↓
Topic Universe
```

The workflow should avoid turning every keyword into a separate topic.

---

# 23. Topic Validation Workflow

Topic candidates should be evaluated using multiple signals.

Potential inputs:

* business relevance
* entity relevance
* audience need
* search evidence
* SERP evidence
* intent
* competition
* existing page coverage
* strategic value
* confidence

Example:

```text
Topic Candidate
      ↓
Business Relevance
      ↓
Semantic Validity
      ↓
Search Evidence
      ↓
SERP Evidence
      ↓
Existing Coverage
      ↓
Validation Score
      ↓
Accept / Reject / Review
```

---

# 24. Query Discovery Workflow

```text
Validated Topic
      ↓
Query Sources
      ↓
Query Collection
      ↓
Normalization
      ↓
Canonicalization
      ↓
Deduplication
      ↓
Search Context Assignment
      ↓
Query Set
```

Query sources may include:

* search APIs
* keyword providers
* SERP data
* related searches
* PAA-like sources
* website search data
* analytics
* user-provided data
* AI-generated hypotheses

AI-generated queries must be clearly marked as generated or inferred until externally validated.

---

# 25. Intent Workflow

```text
Query
 ↓
Search Context
 ↓
SERP Evidence
 ↓
Intent Signals
 ↓
Intent Classification
 ↓
Confidence
 ↓
Intent Distribution
 ↓
Intent Validation
```

Intent should not be inferred from query wording alone when stronger SERP evidence is available.

---

# 26. SERP Intelligence Workflow

```text
Query
  ↓
Search Context
  ↓
Provider Selection
  ↓
SERP Acquisition
  ↓
Raw Evidence Storage
  ↓
Normalization
  ↓
Feature Detection
  ↓
Result Classification
  ↓
Intent Signals
  ↓
Competitor Signals
  ↓
SERP Similarity
  ↓
Search Intelligence
```

Raw evidence must remain available for audit and reprocessing.

---

# 27. Topic Clustering Workflow

Potential signals:

```text
Semantic Similarity
Entity Overlap
Intent Similarity
SERP Similarity
Page-Type Similarity
Content-Format Similarity
Business Relationship
EAV Relationship
```

Conceptual flow:

```text
Topics / Queries
       ↓
Feature Extraction
       ↓
Similarity Analysis
       ↓
Candidate Clusters
       ↓
Cluster Quality Evaluation
       ↓
Cluster Validation
       ↓
Human Review if Necessary
       ↓
Final Clusters
```

The system must allow:

```text
UNCLUSTERED
```

when evidence does not justify grouping.

---

# 28. Page Candidate Workflow

```text
Validated Topics
      ↓
Clusters
      ↓
Intent
      ↓
SERP Evidence
      ↓
Existing Pages
      ↓
Page-Type Analysis
      ↓
Candidate Page Groups
      ↓
Page Mapping Recommendation
```

A topic cluster does not automatically equal a page.

The workflow must explicitly evaluate whether multiple topics should:

* share one page
* become separate pages
* become supporting content
* remain unassigned
* require human review

---

# 29. SEO Decision Workflow

The Decision Engine should receive:

```text
Business Context
+
Knowledge Model
+
Topic Model
+
Search Intelligence
+
Existing Website
+
Competitive Intelligence
+
Evidence
+
Confidence
+
Human Constraints
```

It should produce:

```text
Decision Candidate
+
Decision Factors
+
Evidence
+
Confidence
+
Risks
+
Alternatives
+
Recommended Action
```

The workflow must distinguish:

```text
Analysis
    ≠
Recommendation
    ≠
Decision
    ≠
Authorized Action
```

---

# 30. Human Validation Workflow

Human validation may occur at different points.

Examples:

```text
Entity Resolution
Topic Validation
Intent Conflict
Cluster Approval
Page Mapping
Topical Map
Page Architecture
Internal Linking
Strategic Prioritization
```

Possible review states:

```text
PENDING_REVIEW
APPROVED
REJECTED
MODIFICATION_REQUESTED
DEFERRED
ESCALATED
```

---

# 31. Human Review as Workflow State

Human review must be persisted.

Conceptual structure:

```yaml
review:
  id:
  workflow_run_id:
  step_id:
  reviewer:
  status:
  decision:
  comments:
  modifications:
  timestamp:
```

The workflow resumes from the review checkpoint after the decision is recorded.

---

# 32. Workflow Context Assembly

Each step must receive only the context required for its task.

Context may contain:

```text
Project Context
Business Context
Entity Context
EAV Context
Topic Context
Search Context
SERP Evidence
Website Context
Previous Step Outputs
Human Decisions
Relevant Historical Decisions
```

The workflow must not blindly pass the entire project state into every AI call.

This is both a quality and cost requirement.

---

# 33. Context Dependency Declaration

Each step should declare its context requirements.

Example:

```yaml
context_requirements:
  required:
    - validated_topics
    - search_context
    - existing_pages

  optional:
    - competitor_data
    - historical_serps
```

The Context Management system defined in `25_CONTEXT_MANAGEMENT.md` is responsible for retrieval and assembly.

---

# 34. Evidence Propagation

Evidence should propagate through workflow steps without requiring every agent to independently rediscover it.

Example:

```text
SERP Evidence
      ↓
Intent Agent
      ↓
Intent Evidence Reference
      ↓
Clustering Agent
      ↓
Cluster Evidence Reference
      ↓
Decision Engine
      ↓
Decision Evidence Chain
```

Derived claims must reference their upstream evidence.

---

# 35. Provenance Chain

A workflow should preserve a trace such as:

```text
Source
 ↓
Observation
 ↓
Normalized Data
 ↓
Inference
 ↓
Recommendation
 ↓
Human Decision
```

Example:

```text
SERP Snapshot
     ↓
Observed SERP Pattern
     ↓
Inferred Dominant Intent
     ↓
Recommended Page Type
     ↓
Human Approved Page Type
```

---

# 36. Workflow State Machine

A conceptual workflow state machine:

```text
PLANNED
   ↓
READY
   ↓
RUNNING
   ├──────────────→ WAITING_FOR_HUMAN
   │                       ↓
   │                    RESUMED
   │                       ↓
   ├──────────────→ RETRYING
   │                       ↓
   │                    RUNNING
   │
   ├──────────────→ PAUSED
   │
   ├──────────────→ PARTIALLY_COMPLETED
   │
   └──────────────→ FAILED
                           ↓
                        RECOVERY

RUNNING
   ↓
COMPLETED
```

Exact implementation states may evolve, but state transitions must remain explicit and auditable.

---

# 37. Checkpoints

Checkpoints allow workflow recovery.

A checkpoint should capture enough state to resume safely.

Potential checkpoint boundaries:

* after expensive provider calls
* after major agent outputs
* after human approval
* before irreversible actions
* after data persistence
* after workflow branch completion

Checkpointing should be proportional to:

* cost
* execution duration
* failure probability
* reversibility

---

# 38. Idempotency

Workflow steps that may be retried must be idempotent where possible.

Examples:

```text
Normalize dataset
Store SERP snapshot
Create topic candidates
Persist clustering result
Generate decision candidate
```

A repeated execution must not unintentionally create:

* duplicate entities
* duplicate topics
* duplicate evidence
* duplicate workflow events
* duplicate external actions

---

# 39. Idempotency Keys

Conceptually:

```text
workflow_run_id
+
step_id
+
input_version
+
capability_version
```

may contribute to an execution identity.

The final implementation may use another scheme, but duplicate execution must be detectable.

---

# 40. Dependency Resolution

Dependencies must be resolved before execution.

Example:

```text
Page Architecture
requires:
    validated_topics
    approved_page_candidates
    intent_analysis
    existing_page_model
```

If a required artifact is missing or invalid:

```text
Do not execute
       ↓
WAITING_FOR_DEPENDENCY
```

The workflow must not fabricate missing inputs.

---

# 41. Dynamic Workflow Planning

The system should support context-dependent workflow composition.

Example:

### New website

```text
Business
→ Entity
→ EAV
→ Topics
→ Search
→ SERP
→ Clustering
→ Pages
```

### Existing mature website

```text
Existing Pages
→ Search Performance
→ Cannibalization
→ Content Gaps
→ SERP Drift
→ Decision Engine
```

### Specific topic request

```text
Existing Knowledge
→ Topic Validation
→ Query Discovery
→ SERP
→ Intent
→ Page Decision
```

The Orchestrator should choose the minimum sufficient workflow for the objective.

---

# 42. AI-Assisted Workflow Planning

AI may assist in planning workflows.

It may determine:

* relevant capabilities
* likely dependencies
* required evidence
* missing information
* candidate workflow branches
* recommended sequence

However:

> AI-generated workflow plans must be validated before execution.

The system must not allow an LLM to silently redefine system-level permissions or bypass approval gates.

---

# 43. Workflow Planning vs Workflow Execution

These must remain separate.

```text
Planning
    ↓
Proposed Workflow
    ↓
Validation
    ↓
Authorization
    ↓
Execution
```

Planning may be probabilistic.

Execution should be controlled and stateful.

---

# 44. Step-Level Authorization

A workflow may be authorized globally, but high-impact steps may require additional authorization.

Example:

```text
Research
    → automatically allowed

Analysis
    → automatically allowed

Recommendation
    → allowed

Human strategic decision
    → human required

External publishing
    → explicit authorization required
```

Authorization must be checked at the step level.

---

# 45. Permissions

A workflow step must declare required permissions.

Examples:

```text
knowledge.read
knowledge.write
search.execute
serp.execute
website.read
analytics.read
decision.create
human_review.request
external_action.execute
```

The Orchestrator must enforce these permissions.

---

# 46. Workflow Security

The workflow system must enforce:

* tenant isolation
* workspace isolation
* project isolation
* user authorization
* tool permissions
* secret isolation
* external provider credentials
* audit logging
* prompt-injection defenses
* untrusted content boundaries

External website content must never be treated as trusted instructions.

---

# 47. Prompt Injection Boundary

Workflow steps that consume external content must distinguish:

```text
Data
≠
Instructions
```

For example, text retrieved from:

* websites
* SERPs
* documents
* competitor pages
* user-generated content

must be treated as untrusted data.

It must not be allowed to override:

* system policies
* workflow rules
* permissions
* tool restrictions
* human approvals

---

# 48. Failure Classification

Failures should be classified.

Recommended categories:

```text
INPUT_INVALID
DEPENDENCY_MISSING
AUTHORIZATION_DENIED
PROVIDER_ERROR
RATE_LIMITED
TIMEOUT
SCHEMA_INVALID
AI_OUTPUT_INVALID
VALIDATION_FAILED
DATA_CONFLICT
LOW_CONFIDENCE
HUMAN_REVIEW_REQUIRED
SYSTEM_ERROR
UNKNOWN
```

Failure classification determines recovery behavior.

---

# 49. Failure Handling

The workflow should follow:

```text
Failure
 ↓
Classify
 ↓
Determine Retryability
 ↓
Retry / Fallback / Pause / Escalate / Fail
```

The workflow must never hide failures behind an apparently successful output.

---

# 50. Low Confidence Handling

Low confidence is not necessarily a technical failure.

Example:

```text
Intent Analysis
      ↓
Confidence = low
      ↓
Additional SERP evidence?
      ├── yes → collect
      └── no  → human review
```

The system should distinguish:

```text
Execution Failure
```

from:

```text
Knowledge Uncertainty
```

---

# 51. Conflict Handling

Conflicting evidence should produce explicit conflict state.

Example:

```text
Provider A → informational intent
Provider B → commercial intent
SERP       → mixed intent
```

Possible result:

```text
CONFLICTED
```

The workflow may then:

* acquire additional evidence
* compare source reliability
* ask for human review
* defer the decision

It must not silently select one interpretation without justification.

---

# 52. Workflow Cancellation

A user or authorized system process may cancel a workflow.

Cancellation must define:

* whether currently running steps are interrupted
* whether queued steps are removed
* whether partial outputs are retained
* whether external actions are rolled back
* whether the workflow can be resumed

Cancellation must not imply deletion of historical evidence.

---

# 53. Workflow Pause and Resume

Workflows may be paused due to:

* human review
* user request
* provider outage
* budget limit
* missing data
* maintenance
* dependency failure

Resume should continue from the latest valid checkpoint.

---

# 54. Workflow Versioning

Every workflow definition must be versioned.

Example:

```text
seo_strategy_workflow@1.0
seo_strategy_workflow@1.1
```

A running workflow should remain associated with its original workflow version unless an explicit migration mechanism exists.

Changing the workflow definition must not silently alter historical workflow semantics.

---

# 55. Agent Versioning Inside Workflows

Agent versions should also be recorded.

Example:

```text
Workflow:
seo_strategy_workflow@1.2

Agent:
topic_validation_agent@2.1

Model:
provider/model@version

Prompt:
topic_validation_prompt@7
```

This enables reproducibility and regression analysis.

---

# 56. Workflow Observability

Every workflow should expose:

### Execution metrics

* duration
* step count
* success rate
* retry count
* failure rate
* provider latency
* AI latency
* human waiting time

### Quality metrics

* validation failures
* low-confidence outputs
* conflict rate
* human rejection rate
* revision rate
* evidence completeness

### Cost metrics

* token usage
* model cost
* provider cost
* SERP calls
* crawling cost
* workflow total cost

---

# 57. Workflow Event Log

Important lifecycle events should be recorded.

Examples:

```text
WORKFLOW_CREATED
WORKFLOW_STARTED
STEP_STARTED
STEP_COMPLETED
STEP_FAILED
STEP_RETRIED
CHECKPOINT_CREATED
HUMAN_REVIEW_REQUESTED
HUMAN_REVIEW_COMPLETED
BRANCH_SELECTED
WORKFLOW_PAUSED
WORKFLOW_RESUMED
WORKFLOW_CANCELLED
WORKFLOW_COMPLETED
```

Events should be immutable audit records where appropriate.

---

# 58. Workflow Artifacts

Workflow outputs should be treated as artifacts.

Examples:

```text
Business Model
Entity Graph
EAV Dataset
Topic Universe
Query Dataset
Intent Dataset
SERP Dataset
Cluster Model
Page Candidate Model
Topical Map
Page Architecture
Internal Linking Recommendations
Decision Record
```

Artifacts should have:

* stable identity
* version
* provenance
* source workflow
* source step
* creation timestamp
* validity state

---

# 59. Workflow Output Contracts

Every important step must produce a structured output conforming to its contract.

Example:

```yaml
output:
  status:
  artifact:
  evidence:
  confidence:
  epistemic_state:
  warnings:
  conflicts:
  recommendations:
```

The exact schema is governed by:

`16_OUTPUT_CONTRACTS.md`

---

# 60. Validation Between Steps

Outputs should be validated before becoming inputs to downstream steps.

```text
Agent Output
     ↓
Schema Validation
     ↓
Semantic / Domain Validation
     ↓
Evidence Validation
     ↓
Confidence Evaluation
     ↓
Persist
     ↓
Next Step
```

Invalid outputs must not silently propagate.

---

# 61. Workflow Data Consistency

The workflow engine must distinguish:

```text
Persisted
Validated
Derived
Proposed
Approved
Published
```

A proposed artifact must not be treated as an approved artifact.

---

# 62. Workflow and Shared Knowledge

Workflow execution should enrich the shared knowledge model when appropriate.

Example:

```text
SERP Workflow
      ↓
SERP Snapshot
      ↓
Search Intelligence
      ↓
Knowledge Model
```

The workflow should not duplicate canonical data unnecessarily.

The shared knowledge layer remains the source of truth for persistent domain knowledge.

---

# 63. Workflow and Decision History

Important decisions should reference their originating workflow.

Example:

```text
Decision:
Create dedicated page for Topic X

Source:
Workflow Run #123
Step: page_decision
Evidence:
SERP snapshots
Intent analysis
Existing page analysis
Business relevance
```

This creates an auditable decision history.

---

# 64. Workflow and Human Learning

Human corrections should become structured signals.

Example:

```text
AI:
Topic A + Topic B = same page

Human:
Reject

Reason:
Different user needs
```

The system should persist this as feedback.

Future workflow evaluation may use it to improve:

* clustering
* page mapping
* intent classification
* recommendations

Human feedback must not automatically modify production models without an explicit evaluation and deployment process.

---

# 65. Cost and Latency Management

The workflow engine should optimize expensive operations.

Principles:

1. Retrieve existing evidence before collecting new evidence.
2. Reuse valid artifacts.
3. Avoid redundant LLM calls.
4. Avoid redundant SERP calls.
5. Parallelize independent work.
6. Use deterministic processing where sufficient.
7. Use smaller models when appropriate.
8. Escalate to stronger models only when needed.
9. Enforce workflow budgets.
10. Stop when the decision has sufficient evidence.

---

# 66. Progressive Evidence Acquisition

The workflow should support progressive research.

Example:

```text
Basic Topic Evidence
       ↓
Sufficient?
   ├── yes → continue
   └── no
        ↓
Additional Search Evidence
        ↓
Sufficient?
   ├── yes → continue
   └── no
        ↓
Human Review
```

This avoids collecting maximum data by default.

---

# 67. Stop Conditions

Every iterative or expensive workflow must have stopping conditions.

Examples:

```text
confidence >= threshold
evidence_count >= minimum
cluster_stability >= threshold
no new high-value topics found
budget exhausted
maximum iterations reached
human decision required
```

The system must explicitly report why it stopped.

---

# 68. Workflow Completion

A workflow is complete only when:

1. All required steps are completed.
2. Required outputs pass validation.
3. Required evidence exists.
4. Required human approvals are complete.
5. No blocking conflicts remain.
6. Required artifacts are persisted.
7. Workflow state is marked complete.
8. Final result is auditable.

---

# 69. Partial Completion

A workflow may legitimately end as:

```text
PARTIALLY_COMPLETED
```

when:

* some branches succeeded
* other branches failed
* the user stopped execution
* providers were unavailable
* evidence was insufficient
* human review remains unresolved

Partial completion must not be represented as full completion.

---

# 70. Workflow Quality Gates

Recommended gates:

### Gate 1 — Input Quality

```text
Required business context exists?
```

### Gate 2 — Semantic Quality

```text
Entity model sufficiently reliable?
```

### Gate 3 — Topic Quality

```text
Topic candidates validated?
```

### Gate 4 — Search Quality

```text
Required search evidence available?
```

### Gate 5 — Mapping Quality

```text
Page relationships sufficiently supported?
```

### Gate 6 — Decision Quality

```text
Evidence + confidence + business relevance sufficient?
```

### Gate 7 — Human Approval

```text
Required strategic decisions approved?
```

---

# 71. Workflow Anti-Patterns

The following patterns are prohibited.

## 71.1 Giant Autonomous Agent

One LLM performs:

```text
Research → analysis → strategy → architecture → execution
```

without explicit workflow boundaries.

---

## 71.2 Agent-to-Agent Free Chat

Agents independently communicate through uncontrolled conversations.

Communication must occur through structured contracts and the Orchestrator.

---

## 71.3 Hidden Dependencies

A step silently relies on data that is not declared.

---

## 71.4 Unbounded Loops

AI repeatedly calls itself until it decides it is finished.

---

## 71.5 Silent Failure

A failed step returns an apparently valid empty result.

---

## 71.6 Fake Evidence

The workflow generates unsupported evidence to satisfy a downstream contract.

---

## 71.7 Context Dumping

The complete project database is passed to every AI call.

---

## 71.8 Workflow-as-Prompt

The entire workflow exists only inside a large prompt.

Workflow state must be represented structurally and persistently.

---

## 71.9 Uncontrolled Self-Modification

An AI agent changes workflow definitions, permissions, or system rules during execution without explicit governance.

---

## 71.10 Automatic Strategic Action

The system turns an AI recommendation directly into a strategic website change without required human authorization.

---

# 72. MVP Workflow Architecture

The MVP should support:

```text
Workflow Definition
      ↓
Central Orchestrator
      ↓
Step Execution
      ↓
Agent Invocation
      ↓
Deterministic Services
      ↓
Persistent Workflow State
      ↓
Checkpoints
      ↓
Validation
      ↓
Human Review
      ↓
Decision Engine
```

Recommended MVP implementation:

```text
Modular Monolith
```

with:

* workflow service
* orchestrator
* agent registry
* task executor
* persistence layer
* context retrieval
* evidence service
* validation layer
* human review interface
* provider adapters

---

# 73. MVP Workflow Set

Initial workflows should include:

### Workflow A — Business-to-Topic Research

```text
Business
→ Entity
→ EAV
→ Topic Discovery
→ Topic Validation
```

### Workflow B — Topic-to-Search Intelligence

```text
Topic
→ Query Discovery
→ Intent
→ SERP
```

### Workflow C — Topic-to-Page Mapping

```text
Validated Topics
→ Clustering
→ Existing Page Analysis
→ Page Candidates
→ Decision Support
```

### Workflow D — Existing Website Audit

```text
Website
→ Page Inventory
→ Search Performance
→ Cannibalization
→ Content Gaps
→ Opportunity Analysis
```

### Workflow E — Full Strategy Workflow

```text
Business
→ Knowledge
→ Topics
→ Search
→ Clustering
→ Pages
→ Decision Engine
→ Human Review
→ Topical Map
→ Architecture
```

---

# 74. Future Workflow Capabilities

Future versions may support:

* adaptive research depth
* event-driven workflows
* long-running research jobs
* workflow scheduling
* automatic freshness checks
* SERP drift workflows
* competitor monitoring
* new-topic detection
* cannibalization monitoring
* content performance feedback
* strategy re-evaluation
* workflow simulation
* workflow optimization
* policy-aware automation
* multi-project orchestration

These capabilities must not be implemented by weakening the core control model.

---

# 75. Workflow Extensibility

New capabilities should be added through registered modules.

A new capability should define:

```text
Capability ID
Version
Purpose
Input Contract
Output Contract
Required Context
Required Tools
Permissions
Failure Policy
Validation
Cost Characteristics
```

The Orchestrator should discover capabilities through the registry rather than hardcoding every agent.

---

# 76. Workflow and Tool Selection

The Orchestrator may select tools dynamically based on task requirements.

Example:

```text
Need:
SERP Evidence

Capability:
SERP Intelligence

Available Tools:
Provider A
Provider B
Provider C

Selection Factors:
coverage
cost
latency
freshness
reliability
availability
```

Tool selection must respect provider abstraction and permissions.

---

# 77. Workflow and Skills

When a required capability is unavailable:

```text
Capability Required
      ↓
Check Registered Capabilities
      ↓
Check Available Skills / Tools
      ↓
Capability Exists?
   ├── yes → execute
   └── no
        ↓
Can install?
   ├── yes → installation workflow
   └── no → report capability unavailable
```

Skill installation and tool acquisition must follow:

`26_SKILLS_AND_TOOLING_POLICY.md`

The workflow must never silently install untrusted capabilities.

---

# 78. Workflow Context Efficiency

The workflow system should minimize unnecessary context transmission.

Each step should receive:

```text
Minimum sufficient context
+
Relevant evidence
+
Required prior outputs
+
Applicable human decisions
```

Not:

```text
Entire conversation
+
Entire database
+
All previous agent outputs
```

This improves:

* cost
* latency
* reasoning quality
* privacy
* reproducibility

---

# 79. Workflow Reproducibility

A completed workflow should be reproducible to the extent technically possible.

The system should record:

* workflow version
* agent versions
* prompt versions
* model identifiers
* tool/provider versions where available
* input versions
* evidence references
* configuration
* relevant thresholds
* human decisions

Exact deterministic reproduction of external AI/provider outputs is not always possible, but execution provenance must remain available.

---

# 80. Workflow Testing

Workflow testing must cover multiple levels.

## 80.1 Unit Tests

Test:

* state transitions
* dependency resolution
* conditions
* retry rules
* authorization
* checkpoint creation

---

## 80.2 Integration Tests

Test:

* orchestrator + agents
* database
* provider adapters
* evidence persistence
* workflow state persistence

---

## 80.3 Workflow Tests

Test complete workflows with controlled fixtures.

---

## 80.4 Failure Tests

Simulate:

* provider outage
* timeout
* malformed AI output
* missing dependency
* authorization failure
* database failure
* duplicate execution
* human rejection

---

## 80.5 Regression Tests

Previously valid workflows must remain valid after:

* agent changes
* prompt changes
* model changes
* workflow changes
* provider changes

---

## 80.6 End-to-End Tests

Validate:

```text
User Objective
→ Workflow
→ Agents
→ Evidence
→ Decision
→ Human Review
→ Final Artifact
```

---

# 81. Workflow Evaluation

Workflow quality should be measured separately from agent quality.

Possible workflow-level metrics:

```text
Task Completion Rate
Workflow Success Rate
Mean Workflow Duration
Human Revision Rate
Failure Recovery Rate
Evidence Completeness
Decision Acceptance Rate
Cost per Completed Objective
Redundant Execution Rate
```

A workflow can be operationally successful while producing poor analytical results.

Both dimensions must be evaluated.

---

# 82. Workflow Debugging

The debugging process follows:

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
Fix
 ↓
Targeted Test
 ↓
Regression Test
 ↓
Verify
 ↓
Document
```

Debugging must identify whether the failure occurred in:

* workflow planning
* dependency resolution
* context assembly
* agent execution
* deterministic processing
* external provider
* validation
* persistence
* human review
* state transition

---

# 83. Workflow Auditability

For every completed strategic workflow, the system should be able to answer:

```text
What was requested?
Who requested it?
Which workflow version executed?
Which steps ran?
Which agents were used?
Which tools were used?
Which evidence was collected?
Which assumptions were made?
What uncertainty existed?
What decisions were recommended?
What did the human approve?
What artifacts were produced?
Why did the workflow complete?
```

This is a core product requirement.

---

# 84. Workflow Decision Boundary

The authority hierarchy is:

```text
Human Strategic Authority
        ↓
SEO Decision Engine
        ↓
Workflow / Orchestrator
        ↓
Agent Analysis
        ↓
Tools / External Evidence
```

This hierarchy must not be inverted.

An agent cannot override a human strategic decision.

A workflow cannot convert a recommendation into an authorized action unless the applicable policy explicitly allows it.

---

# 85. Workflow and External Actions

External actions should be treated differently from analytical actions.

### Analytical

```text
Research
Analyze
Classify
Cluster
Recommend
```

### External / consequential

```text
Publish
Modify website
Delete content
Change architecture
Create redirects
Modify links
Change metadata
```

Consequential actions require explicit authorization according to project policy.

---

# 86. Workflow Lifecycle

The complete lifecycle is:

```text
Objective
   ↓
Plan
   ↓
Validate Plan
   ↓
Authorize
   ↓
Initialize
   ↓
Execute
   ↓
Checkpoint
   ↓
Validate
   ↓
Review
   ↓
Decide
   ↓
Act if Authorized
   ↓
Evaluate
   ↓
Persist Outcome
   ↓
Learn
```

---

# 87. Canonical Operating Model

The complete SEO workflow operating model is:

```text
Human Strategy
      ↓
Objective
      ↓
Workflow Planning
      ↓
Central Orchestrator
      ↓
Dependency Resolution
      ↓
Context Assembly
      ↓
Relevant Agent / Deterministic Capability
      ↓
Evidence Retrieval
      ↓
Execution
      ↓
Structured Output
      ↓
Validation
      ↓
Confidence + Epistemic State
      ↓
Persisted Artifact
      ↓
Next Workflow Step
      ↓
SEO Decision Engine
      ↓
Human Review
      ↓
Authorized Action
      ↓
Outcome
      ↓
Evaluation
      ↓
Learning
```

---

# 88. Non-Negotiable Workflow Principles

The following rules are mandatory:

1. Workflows must be explicit.
2. Workflow state must be persistent.
3. Workflow steps must have defined contracts.
4. Dependencies must be explicit.
5. Agents must operate through workflow boundaries.
6. Agent-to-agent free-form coordination is prohibited.
7. Evidence must propagate through the workflow.
8. Provenance must be preserved.
9. AI-generated outputs must be validated.
10. Low confidence must remain visible.
11. Conflicts must remain visible.
12. Missing evidence must never be fabricated.
13. Human review must be a first-class state.
14. High-impact actions require authorization.
15. Retries must be bounded.
16. Iterations must have stopping conditions.
17. Workflow execution must be resumable.
18. Important operations must be idempotent.
19. Workflow versions must be recorded.
20. Agent/tool/model versions must be traceable.
21. External provider failures must not be hidden.
22. Context must be task-specific.
23. Workflow planning and workflow execution must remain separate.
24. The Orchestrator coordinates; it does not replace specialized intelligence.
25. The Decision Engine supports decisions; it does not replace human strategic authority.
26. Successful execution does not equal strategic correctness.
27. Partial completion must never be reported as full completion.
28. No workflow may silently expand project scope.
29. No AI system may silently modify workflow governance or permissions.
30. Every strategic output must be auditable.

---

# 89. Relationship to Other Documents

This document depends on and interacts with:

### `03_MASTER_RULES.md`

Defines non-negotiable project governance.

### `04_SYSTEM_ARCHITECTURE.md`

Defines the system-level architectural boundaries.

### `05_AI_AGENT_ARCHITECTURE.md`

Defines the agent architecture and operating model.

### `06_DATA_ARCHITECTURE.md`

Defines persistent data and evidence structures.

### `07_TECHNICAL_ARCHITECTURE.md`

Defines implementation and runtime architecture.

### `08_SEO_KNOWLEDGE_MODEL.md`

Defines the domain knowledge model used by workflows.

### `09_ENTITY_EAV_MODEL.md`

Defines entity and EAV structures.

### `10_TOPIC_MODELING_AND_CLUSTERING.md`

Defines topic and clustering intelligence.

### `11_SEARCH_AND_SERP_INTELLIGENCE.md`

Defines search and SERP acquisition and analysis.

### `12_SEO_DECISION_ENGINE.md`

Defines decision logic and decision support.

### `13_AGENT_SPECIFICATIONS.md`

Defines individual agent responsibilities and contracts.

### `15_HUMAN_IN_THE_LOOP.md`

Defines human review and authority boundaries.

### `16_OUTPUT_CONTRACTS.md`

Defines structured agent and workflow outputs.

### `21_DEVELOPMENT_AND_DEBUG.md`

Defines implementation and debugging discipline.

### `22_TESTING_AND_VALIDATION.md`

Defines testing and validation requirements.

### `23_PROJECT_CONTROL_CENTER.md`

Defines project state and execution control.

### `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md`

Defines project task organization and dependency management.

### `25_CONTEXT_MANAGEMENT.md`

Defines context retrieval and context lifecycle.

### `26_SKILLS_AND_TOOLING_POLICY.md`

Defines skill and tool acquisition and governance.

---

# 90. Definition of Done

The workflow architecture is considered implemented correctly only when:

* workflow definitions are versioned
* workflow runs are persisted
* workflow steps are explicit
* dependencies are enforced
* context requirements are declared
* agent invocation is contract-based
* outputs are validated
* evidence is preserved
* provenance is traceable
* checkpoints exist
* workflows can resume
* retries are bounded
* failures are classified
* human review is persisted
* authorization is enforced
* workflow versions are recorded
* agent/tool/model provenance is recorded
* observability exists
* audit logs exist
* workflow tests exist
* failure tests exist
* regression tests exist
* partial completion is supported
* no-fabrication rules are enforced
* strategic actions remain under appropriate human authority

---

# 91. Final Workflow Model

The intended architecture is:

```text
                         HUMAN
                           │
                           ▼
                    Strategic Objective
                           │
                           ▼
                  Workflow Planner
                           │
                           ▼
                 Workflow Definition
                           │
                           ▼
                 Central Orchestrator
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
       Context          Dependency        Policy
       Assembly         Resolution        Checks
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                    Workflow Step
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
           Agent       Deterministic    Tool /
         Capability      Service        Provider
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                     Structured Output
                           │
                           ▼
                       Validation
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Evidence     Confidence    Conflicts
              │            │            │
              └────────────┼────────────┘
                           ▼
                    Persisted Artifact
                           │
                           ▼
                    Next Workflow Step
                           │
                           ▼
                   SEO Decision Engine
                           │
                           ▼
                     HUMAN REVIEW
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
              Approved          Rejected /
                  │              Modified
                  ▼
          Authorized Action
                  │
                  ▼
               Outcome
                  │
                  ▼
              Evaluation
                  │
                  ▼
               Learning
```

The workflow system therefore acts as the **controlled execution backbone** of the SEO Decision Engine.

It does not replace SEO intelligence, specialized agents, the knowledge model, or human strategy.

Its purpose is to make the entire research-to-decision process:

**structured, dependency-aware, evidence-backed, resumable, testable, observable, auditable, and controllable.**

---

# 92. Document Control

```yaml
document:
  id: "14"
  filename: "14_AGENT_WORKFLOW.md"
  status: "APPROVED_AS_BASELINE_AGENT_WORKFLOW"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

architecture:
  workflow_model: "persistent_versioned_workflow_graph"
  orchestration: "central_orchestrator"
  runtime_default: "modular_monolith"
  execution_model:
    - sequential
    - parallel
    - conditional
    - iterative
    - review
    - retry
    - fallback

core_objects:
  - workflow_definition
  - workflow_version
  - workflow_run
  - workflow_step
  - task
  - context
  - evidence
  - artifact
  - checkpoint
  - approval
  - decision
  - workflow_event

core_principles:
  - explicit_workflows
  - persistent_state
  - explicit_dependencies
  - structured_agent_invocation
  - evidence_preservation
  - provenance
  - resumability
  - idempotency
  - bounded_retries
  - human_control
  - authorization
  - observability
  - auditability
  - no_fabrication

canonical_flow:
  - business_research
  - entity_model
  - eav_enrichment
  - topic_discovery
  - topic_validation
  - query_discovery
  - intent_analysis
  - serp_intelligence
  - topic_clustering
  - page_candidates
  - decision_engine
  - human_review
  - topical_map
  - page_architecture
  - internal_linking

authority:
  strategic: "human"
  decision_support: "seo_decision_engine"
  orchestration: "central_orchestrator"
  execution: "workflow_engine"
  intelligence: "specialized_agents"
  evidence: "tools_and_external_sources"

primary_dependencies:
  - "15_HUMAN_IN_THE_LOOP.md"
  - "16_OUTPUT_CONTRACTS.md"

related:
  - "05_AI_AGENT_ARCHITECTURE.md"
  - "06_DATA_ARCHITECTURE.md"
  - "11_SEARCH_AND_SERP_INTELLIGENCE.md"
  - "12_SEO_DECISION_ENGINE.md"
  - "13_AGENT_SPECIFICATIONS.md"
  - "21_DEVELOPMENT_AND_DEBUG.md"
  - "22_TESTING_AND_VALIDATION.md"
  - "25_CONTEXT_MANAGEMENT.md"
  - "26_SKILLS_AND_TOOLING_POLICY.md"
```
