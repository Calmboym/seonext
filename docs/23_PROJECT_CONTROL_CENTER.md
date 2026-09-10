# 23 — Project Control Center

**Document:** `23_PROJECT_CONTROL_CENTER.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Project State, Task Control, Authorization, Governance & Execution Control Specification
**Status:** `APPROVED_AS_BASELINE_PROJECT_CONTROL_CENTER`
**Authority:** Baseline specification for project state management, task authorization, execution control, dependency tracking, progress tracking, verification state, change control, handoff, and project-level operational governance.

---

## 1. Purpose

The Project Control Center is the operational control layer of the SEO Research & Strategy Copilot / SEO Decision Engine project.

It exists to answer, at any point in development:

* What is the current project state?
* What has been completed?
* What is currently being worked on?
* What is authorized to be implemented?
* What is blocked?
* What depends on what?
* Which documentation is authoritative?
* Which tests have actually been executed?
* Which outputs are verified versus merely implemented?
* What decisions have been made?
* What changed?
* What must happen next?
* What information must be carried into the next development session?

The Project Control Center is not merely a project-management dashboard.

It is the **execution governance system** that connects:

```text
Documentation
    ↓
Architecture
    ↓
Dependencies
    ↓
Work Breakdown Structure
    ↓
Task Authorization
    ↓
Implementation
    ↓
Testing
    ↓
Verification
    ↓
Project State
    ↓
Next Authorized Action
```

Its purpose is to prevent development from becoming an uncontrolled sequence of prompts, code changes, assumptions, and undocumented decisions.

---

# 2. Core Principle

The project must always have an explicit and inspectable state.

The system must never depend on conversational memory alone to determine:

* what has been done,
* what should be done next,
* what is allowed,
* what is blocked,
* what remains unverified,
* or what decisions were previously made.

The persistent project documentation and control artifacts are the source of truth.

```text
Conversation = temporary working context

Project Control Center = persistent execution state
```

---

# 3. Project Control Center Responsibilities

The Project Control Center governs:

1. Project identity
2. Project status
3. Milestone status
4. Module status
5. Feature status
6. Task status
7. Task authorization
8. Dependencies
9. Documentation status
10. Architecture decisions
11. Implementation state
12. Testing state
13. Runtime verification state
14. Blocking issues
15. Risks
16. Decisions
17. Changes
18. Human approvals
19. AI-generated recommendations
20. Handoff state
21. Context requirements
22. Skills/tooling requirements
23. Release readiness
24. Project history

---

# 4. Source of Truth Hierarchy

The project's authority hierarchy is defined canonically in `03_MASTER_RULES.md` § 2 ("Rule Hierarchy"). This document does not restate or redefine it — refer to that section as the single source of truth for conflict resolution. (Prior to this bootstrap, this section contained its own competing hierarchy; that duplication has been resolved — see `.ai/PROJECT_STATE.md`.)

A lower-level artifact must not silently override a higher-level authority.

For example:

```text
Code ≠ architecture authority

Task ≠ authorization authority

AI suggestion ≠ human decision

Test pass ≠ product approval

Conversation memory ≠ persistent project state
```

---

# 5. Relationship to Other Documents

The Project Control Center coordinates the fixed documentation system.

It does not replace any of the 26 documents.

Its role is operational coordination.

```text
01_PRD
    ↓
02_PRODUCT_VISION
    ↓
03_MASTER_RULES
    ↓
04_SYSTEM_ARCHITECTURE
    ↓
05_AI_AGENT_ARCHITECTURE
    ↓
06_DATA_ARCHITECTURE
    ↓
07_TECHNICAL_ARCHITECTURE
    ↓
08_SEO_KNOWLEDGE_MODEL
    ↓
09_ENTITY_EAV_MODEL
    ↓
10_TOPIC_MODELING_AND_CLUSTERING
    ↓
11_SEARCH_AND_SERP_INTELLIGENCE
    ↓
12_SEO_DECISION_ENGINE
    ↓
13_AGENT_SPECIFICATIONS
    ↓
14_AGENT_WORKFLOW
    ↓
15_HUMAN_IN_THE_LOOP
    ↓
16_OUTPUT_CONTRACTS
    ↓
17_UI_UX_SPECIFICATION
    ↓
18_FRONTEND_ARCHITECTURE
    ↓
19_DESIGN_SYSTEM
    ↓
20_PROJECT_STRUCTURE
    ↓
21_DEVELOPMENT_AND_DEBUG
    ↓
22_TESTING_AND_VALIDATION
    ↓
23_PROJECT_CONTROL_CENTER
    ↓
24_INDEX_ROADMAP_TASKS_DEPENDENCIES
    ↓
25_CONTEXT_MANAGEMENT
    ↓
26_SKILLS_AND_TOOLING_POLICY
```

This sequence is not necessarily the final runtime reading order.

The final dependency graph and reading order must be derived by auditing the complete documentation set.

---

# 6. Project State Model

The project state must be represented explicitly.

At minimum:

```yaml
project:
  id:
  name:
  version:
  status:
  phase:
  milestone:
  active_task:
  authorized_task:
  blocked:
  release_status:
```

Recommended project statuses:

```text
INITIALIZING
DOCUMENTING
PLANNING
READY
IN_PROGRESS
BLOCKED
PAUSED
VALIDATING
RELEASE_CANDIDATE
RELEASED
DEPRECATED
ARCHIVED
```

Only one primary project status should be active at a time.

Secondary conditions may be represented separately.

Example:

```yaml
status: IN_PROGRESS
conditions:
  - HAS_UNVERIFIED_RUNTIME_COMPONENTS
  - ONE_ACTIVE_TASK
```

---

# 7. Project State Must Be Evidence-Based

Every important state claim must have a basis.

Examples:

```text
"Implemented"
    → code exists

"Tested"
    → relevant test was executed

"Validated"
    → acceptance criteria were checked

"Runtime Verified"
    → behavior was verified in the relevant runtime environment

"Production Ready"
    → release criteria were satisfied
```

The system must never collapse these states into one generic `DONE`.

---

# 8. Verification State

Verification State is one of **two orthogonal status fields** tracked for every task or artifact — the other is Lifecycle Status (§ 33). They must never be conflated: a task's position in its workflow (Lifecycle Status) says nothing on its own about what has actually been confirmed about the work (Verification State).

Verification State uses the canonical vocabulary defined in `26_SKILLS_AND_TOOLING_POLICY.md` § 106:

```text
IMPLEMENTED
TESTED
VALIDATED
RUNTIME_VERIFIED
PARTIALLY_VERIFIED
UNVERIFIED
BLOCKED
```

(This replaces the earlier 12-value list, which duplicated several Lifecycle Status values — e.g. `AUTHORIZED`, `IN_PROGRESS`, `REJECTED` — inside what was meant to be a pure evidence axis. See `.ai/PROJECT_STATE.md` for the resolution.)

These states are progressive but not necessarily strictly linear.

For example:

```text
IMPLEMENTED
    ↓
TESTED
    ↓
VALIDATED
    ↓
RUNTIME_VERIFIED
```

A component may legitimately remain:

```text
IMPLEMENTED
UNVERIFIED
```

if its runtime environment is unavailable.

---

# 9. Task Model

Every development task must have an explicit identity.

Minimum task fields:

```yaml
task:
  id:
  title:
  description:
  parent:
  type:
  priority:
  status:
  authorization:
  dependencies:
  affected_documents:
  affected_modules:
  acceptance_criteria:
  verification_requirements:
  risks:
  owner:
  created_at:
  updated_at:
```

Task types may include:

```text
DOCUMENTATION
ARCHITECTURE
RESEARCH
IMPLEMENTATION
REFACTOR
BUG_FIX
MIGRATION
TEST
SECURITY
PERFORMANCE
UI
DATA
AI
INTEGRATION
OPERATIONS
VALIDATION
```

---

# 10. Task Hierarchy

The project follows:

```text
Project
    ↓
Phase
    ↓
Milestone
    ↓
Module
    ↓
Feature
    ↓
Epic
    ↓
Task
    ↓
Subtask
```

A task must not exist without a meaningful parent context.

The hierarchy allows project progress to be measured at multiple levels without losing traceability.

---

# 11. Task Authorization

Authorization is distinct from task existence.

A task may be:

```text
DEFINED
```

without being:

```text
AUTHORIZED
```

The system must explicitly distinguish:

```text
Planned
Authorized
Executed
Verified
```

Only authorized tasks may be implemented.

---

# 12. Authorization Rules

Before implementation, the control center must establish:

1. Task identity
2. Task scope
3. Parent feature/module
4. Dependencies
5. Required documentation
6. Acceptance criteria
7. Required tests
8. Required tools
9. Required skills
10. Risk level
11. Authorization state

Example:

```yaml
authorization:
  status: AUTHORIZED
  scope:
    - backend
    - entity_resolution
  excluded:
    - frontend
    - production_deployment
  authorized_by: human
```

AI must not infer authorization from proximity or conversational implication when the project policy requires explicit authorization.

---

# 13. Single Active Task Principle

Unless explicitly authorized otherwise, development should operate on one primary active task.

```text
ONE ACTIVE TASK
        ↓
FOCUSED CONTEXT
        ↓
CONTROLLED CHANGE
        ↓
TARGETED TESTING
        ↓
CLEAR VERIFICATION
```

Parallel work may exist when explicitly planned and technically isolated.

The control center must still identify the primary active task.

---

# 14. Task Scope Control

Every task should define:

### In Scope

What may change.

### Out of Scope

What must not change.

### Dependencies

What must already exist.

### Outputs

What the task must produce.

### Verification

How completion will be established.

Example:

```yaml
scope:
  in:
    - entity-resolution-service
    - unit-tests
    - contract-tests

  out:
    - UI
    - production-deployment
    - unrelated refactoring
```

This prevents scope expansion disguised as helpful implementation.

---

# 15. Dependency Management

Dependencies must be explicit.

A dependency may exist between:

* documents,
* tasks,
* modules,
* features,
* data models,
* APIs,
* agents,
* workflows,
* tests,
* infrastructure,
* external providers.

Example:

```text
ENTITY-RESOLUTION-IMPLEMENTATION
        ↓
ENTITY-AGENT
        ↓
TOPIC-DISCOVERY
        ↓
TOPIC-VALIDATION
```

A task cannot be considered ready merely because its parent task exists.

Its actual prerequisites must be satisfied.

---

# 16. Dependency Types

The system should distinguish:

```text
HARD_DEPENDENCY
SOFT_DEPENDENCY
DATA_DEPENDENCY
ARCHITECTURAL_DEPENDENCY
RUNTIME_DEPENDENCY
TEST_DEPENDENCY
DOCUMENTATION_DEPENDENCY
AUTHORIZATION_DEPENDENCY
EXTERNAL_PROVIDER_DEPENDENCY
HUMAN_DECISION_DEPENDENCY
```

Example:

```yaml
dependency:
  type: HUMAN_DECISION_DEPENDENCY
  required_for: PAGE_ARCHITECTURE_IMPLEMENTATION
  status: BLOCKED
```

---

# 17. Dependency Graph

The control center should maintain a directed dependency graph.

Conceptually:

```text
D1 ──→ D2 ──→ D3
             │
             ↓
            T1
             │
       ┌─────┴─────┐
       ↓           ↓
      T2           T3
       │           │
       └─────┬─────┘
             ↓
            T4
```

The graph must support:

* prerequisite detection,
* blocked-task detection,
* execution planning,
* parallelization,
* critical-path analysis,
* dependency impact analysis,
* change impact analysis.

---

# 18. Documentation State

Each document must have a state.

Recommended values:

```text
PLANNED
DRAFT
IN_REVIEW
APPROVED
SUPERSEDED
ARCHIVED
```

The project must also record:

```yaml
document:
  id:
  filename:
  version:
  status:
  last_reviewed:
  dependencies:
  dependents:
  change_history:
```

---

# 19. Documentation Completeness

Before implementation of architecture-sensitive functionality, the control center should verify that relevant documents are:

```text
AVAILABLE
RELEVANT
CONSISTENT
APPROVED
```

If required documentation is missing or contradictory, implementation may be blocked.

The system must not silently invent missing architectural decisions.

---

# 20. Documentation Audit

After the complete documentation set exists, the project control process must perform an audit.

The audit must determine:

* missing concepts,
* duplicated concepts,
* contradictions,
* obsolete decisions,
* undefined dependencies,
* circular dependencies,
* missing task definitions,
* unclear authority,
* implementation gaps,
* missing validation requirements.

The AI must derive the final dependency graph from the actual documents rather than assuming that document numbering represents dependency order.

---

# 21. Reading Order

The final reading order must be generated from the dependency graph.

The control process should classify documents as:

```text
FOUNDATIONAL
ARCHITECTURAL
DOMAIN
EXECUTION
INTERFACE
GOVERNANCE
OPERATIONAL
```

Then derive the minimum required context for the active task.

The entire documentation set does not need to be reloaded for every task.

---

# 22. Context Efficiency

The Project Control Center works together with `25_CONTEXT_MANAGEMENT.md`.

For every task, the system should identify:

```text
Required Context
Relevant Context
Optional Context
Irrelevant Context
```

Example:

```yaml
task_context:
  required:
    - 03_MASTER_RULES.md
    - 06_DATA_ARCHITECTURE.md
    - 09_ENTITY_EAV_MODEL.md
    - 13_AGENT_SPECIFICATIONS.md
    - 16_OUTPUT_CONTRACTS.md

  optional:
    - 08_SEO_KNOWLEDGE_MODEL.md

  excluded:
    - unrelated_frontend_documents
```

The goal is not maximum context.

The goal is **sufficient authoritative context with minimum unnecessary context**.

---

# 23. Milestone Control

A milestone represents a meaningful project outcome.

A milestone must define:

```yaml
milestone:
  id:
  name:
  objective:
  entry_criteria:
  tasks:
  dependencies:
  exit_criteria:
  verification:
  status:
```

A milestone is not complete because all tasks are marked implemented.

Its exit criteria must be satisfied.

---

# 24. Milestone Exit Criteria

Example:

```text
All required implementation tasks complete
        +
Required tests executed
        +
Required validations passed
        +
Critical defects resolved
        +
Runtime verification completed where possible
        +
Documentation updated
        +
Project state updated
        =
Milestone Complete
```

---

# 25. Release Control

Release readiness must be evaluated separately from implementation progress.

Possible release states:

```text
NOT_READY
BLOCKED
VALIDATING
RELEASE_CANDIDATE
APPROVED
RELEASED
```

Release blockers may include:

* P0/P1 security issue,
* failing critical tests,
* missing migration,
* data corruption risk,
* unverified critical integration,
* broken authentication,
* contract incompatibility,
* unresolved architecture conflict,
* missing required human approval.

---

# 26. Blocking Issues

Every blocker must be explicit.

```yaml
blocker:
  id:
  severity:
  description:
  affected_tasks:
  cause:
  required_action:
  owner:
  status:
  discovered_at:
```

Blockers should not be hidden inside task notes.

---

# 27. Blocker Severity

Recommended levels:

```text
P0 — Critical / immediate stop
P1 — High / blocks affected milestone or release
P2 — Medium / significant degradation
P3 — Low / manageable follow-up
```

P0 issues should normally stop affected execution immediately.

---

# 28. Risk Management

The control center should maintain a project risk register.

```yaml
risk:
  id:
  description:
  probability:
  impact:
  severity:
  affected_area:
  mitigation:
  contingency:
  owner:
  status:
```

Typical risks:

* architecture drift,
* provider dependency,
* AI hallucination,
* data-quality degradation,
* search-data volatility,
* prompt injection,
* model regression,
* cost explosion,
* context overflow,
* performance degradation,
* migration failure,
* security vulnerabilities,
* insufficient runtime verification.

---

# 29. Decision Registry

Important decisions must be recorded separately from implementation.

A decision should contain:

```yaml
decision:
  id:
  title:
  context:
  options:
  selected_option:
  rationale:
  consequences:
  affected_documents:
  affected_tasks:
  status:
  decided_by:
  date:
```

The registry prevents the same architectural or product question from being repeatedly reconsidered without new evidence.

---

# 30. Human Decision vs AI Recommendation

The control center must distinguish:

```text
AI Recommendation
        ≠
Human Decision
```

Example:

```yaml
recommendation:
  source: AI
  proposal: merge_topic_A_and_topic_B
  confidence: 0.87
  evidence:
    - serp_similarity
    - intent_similarity
    - entity_overlap

decision:
  status: HUMAN_APPROVED
  selected_action: merge
```

Only the second represents an authorized strategic decision.

---

# 31. Change Management

Every material change must have a traceable origin.

Change types:

```text
PRODUCT_CHANGE
ARCHITECTURE_CHANGE
DATA_MODEL_CHANGE
AI_BEHAVIOR_CHANGE
API_CHANGE
UI_CHANGE
SECURITY_CHANGE
DEPENDENCY_CHANGE
TOOLING_CHANGE
DOCUMENTATION_CHANGE
```

The system should identify:

```text
What changed?
Why?
Who/what requested it?
Which documents are affected?
Which tasks are affected?
Which tests must change?
Does authorization need to be renewed?
```

---

# 32. Architecture Change Control

Architecture must not change accidentally through implementation.

If implementation reveals a genuine architectural problem:

```text
Detect problem
    ↓
Document evidence
    ↓
Assess impact
    ↓
Propose change
    ↓
Human/authorized decision
    ↓
Update authoritative documents
    ↓
Update affected tasks
    ↓
Implement
    ↓
Test
```

Code should not become the accidental source of architecture.

---

# 33. Task Board

The project should maintain a task board containing at least:

```text
BACKLOG
READY
AUTHORIZED
IN_PROGRESS
BLOCKED
IN_REVIEW
TESTING
VALIDATING
DONE
REJECTED
CANCELLED
```

The board must be synchronized with the persistent project state.

This list constitutes the **Lifecycle Status** axis, orthogonal to the **Verification State** axis defined in § 8. Every task carries both fields independently — e.g. a task can be Lifecycle Status `IN_PROGRESS` and Verification State `UNVERIFIED` at the same time; that combination is expected, not an error.

---

# 34. Definition of Done

A task is `DONE` only when all applicable conditions are satisfied.

### Documentation

* Requirements are understood.
* Relevant documentation is consistent.
* Required changes are documented.

### Implementation

* Authorized scope is implemented.
* No unauthorized scope was added.
* Architecture boundaries are preserved.

### Validation

* Required tests are executed.
* Output contracts pass.
* Relevant semantic validation passes.
* Security requirements pass.

### Verification

* Runtime behavior is verified where applicable.
* Unverified components are explicitly marked.

### State

* Task status is updated.
* Evidence is recorded.
* Dependencies are updated.
* Risks/blockers are updated.

### Handoff

* Next action is clear.
* Remaining work is documented.
* Context requirements are identified.

---

# 35. No Fake Completion

The control center must prohibit statements such as:

```text
"Done"
"Fully working"
"Production ready"
"All tests pass"
"Integration verified"
```

unless the corresponding evidence exists.

Correct:

```text
Implementation complete.
Unit tests passed.
External integration unverified because provider credentials were unavailable.
```

Incorrect:

```text
Everything is working.
```

---

# 36. Evidence Registry

Important project claims should reference evidence.

Evidence may include:

```text
source document
code location
test result
test artifact
runtime log
API response
database state
screenshot
benchmark
human approval
external provider response
```

Conceptually:

```yaml
evidence:
  id:
  type:
  source:
  artifact:
  timestamp:
  related_task:
  related_claim:
  reliability:
```

---

# 37. Claim Tracking

Important claims should be classified as:

```text
OBSERVED
INFERRED
ESTIMATED
RECOMMENDED
HUMAN_APPROVED
CONFLICTED
UNKNOWN
```

The Project Control Center should preserve these epistemic states rather than flattening them into facts.

---

# 38. Implementation Ledger

The project should maintain a record of significant implementation changes.

```yaml
implementation:
  task_id:
  files_changed:
  modules_changed:
  database_changes:
  API_changes:
  agent_changes:
  workflow_changes:
  tests_added:
  tests_modified:
  status:
```

This creates traceability between authorization and actual code changes.

---

# 39. Test Ledger

Each task should identify its required verification.

Example:

```yaml
verification:
  required:
    - unit
    - integration
    - contract

  executed:
    - unit
    - contract

  status:
    unit: PASSED
    contract: PASSED
    integration: UNVERIFIED
```

This is more accurate than a single Boolean:

```yaml
tests_passed: true
```

---

# 40. Runtime Verification Ledger

Runtime verification should be independently tracked.

```yaml
runtime:
  environment:
  version:
  verification_status:
  verified_components:
  unverified_components:
  limitations:
  evidence:
```

This is particularly important when:

* external APIs are unavailable,
* credentials are missing,
* network access is restricted,
* infrastructure is unavailable,
* third-party services cannot be exercised.

---

# 41. External Dependency State

External dependencies should have explicit states.

```text
AVAILABLE
AVAILABLE_DEGRADED
UNAVAILABLE
UNAUTHORIZED
RATE_LIMITED
UNKNOWN
MOCKED
SIMULATED
```

A mocked provider must never be reported as equivalent to a verified real provider.

---

# 42. AI Execution State

AI tasks should expose:

```yaml
ai_execution:
  model:
  model_version:
  prompt_version:
  tools_used:
  skills_used:
  retrieval_sources:
  output_contract:
  validation_status:
  confidence:
```

This supports reproducibility and regression analysis.

---

# 43. Skills and Tooling State

The control center should track tool requirements.

```yaml
tooling:
  required:
  available:
  missing:
  installation_required:
  permission_status:
  validation_status:
```

If a required capability is unavailable:

```text
Identify capability
    ↓
Check available tools/skills
    ↓
Check permission
    ↓
Install if allowed
    ↓
Validate installation
    ↓
Use capability
    ↓
Record dependency
```

Tooling governance is defined in:

`26_SKILLS_AND_TOOLING_POLICY.md`

---

# 44. Human Approval Registry

Human approvals must be explicit.

```yaml
approval:
  id:
  subject:
  decision:
  scope:
  approver:
  timestamp:
  evidence:
  expires_at:
  status:
```

Possible decisions:

```text
APPROVED
REJECTED
APPROVED_WITH_CONDITIONS
DEFERRED
REQUEST_MORE_EVIDENCE
```

AI must never fabricate or infer a human approval.

---

# 45. Handoff Protocol

Every development session that changes project state should end with a structured handoff.

Minimum handoff:

```yaml
handoff:
  current_state:
  completed:
  active_task:
  blocked:
  verified:
  unverified:
  decisions:
  changed_documents:
  changed_files:
  tests:
  risks:
  next_authorized_action:
  required_context:
```

---

# 46. Next Action

The project must always attempt to identify the next legitimate action.

Possible next-action states:

```text
CONTINUE_ACTIVE_TASK
RUN_TESTS
FIX_FAILURE
REQUEST_HUMAN_DECISION
UPDATE_DOCUMENTATION
UNBLOCK_DEPENDENCY
AUTHORIZE_TASK
REVIEW_OUTPUT
PERFORM_RUNTIME_VERIFICATION
PLAN_NEXT_TASK
STOP
```

The next action must be derived from project state and dependencies.

It must not simply be:

```text
"continue coding"
```

---

# 47. Stop Conditions

The AI must stop execution when:

* authorization is missing,
* required dependency is unresolved,
* architecture conflict is detected,
* critical security issue appears,
* required human decision is missing,
* output contract cannot be satisfied,
* evidence is insufficient,
* data is contradictory and materially affects the decision,
* external dependency is required but unavailable,
* implementation would exceed authorized scope,
* test evidence is insufficient for a consequential action.

Stopping is a valid and often correct project action.

---

# 48. Automatic vs Human-Controlled Actions

The control center should classify actions.

### Low-risk reversible

May be automated when authorized.

Examples:

* formatting,
* local test execution,
* static analysis,
* regenerating derived artifacts.

### Medium-risk

Require stronger validation.

Examples:

* schema changes,
* data transformations,
* dependency upgrades,
* API changes.

### High-risk / consequential

Require explicit authorization and often human approval.

Examples:

* production migration,
* destructive data changes,
* publishing content,
* modifying critical security controls,
* changing business strategy,
* irreversible external actions.

---

# 49. Project State Machine

Conceptually:

```text
INITIALIZING
      ↓
DOCUMENTING
      ↓
PLANNING
      ↓
READY
      ↓
AUTHORIZED
      ↓
IN_PROGRESS
      ↓
TESTING
      ↓
VALIDATING
      ↓
VERIFIED
      ↓
RELEASE_CANDIDATE
      ↓
RELEASED
```

Failure paths:

```text
IN_PROGRESS → BLOCKED
TESTING → FAILED
VALIDATING → REQUIRES_REWORK
RELEASE_CANDIDATE → BLOCKED
```

Recovery:

```text
BLOCKED
   ↓
DEPENDENCY_RESOLVED
   ↓
READY
```

---

# 50. Project State Integrity

The control center must detect inconsistencies such as:

```text
Task = DONE
but required tests = NOT_RUN

Milestone = COMPLETE
but required task = BLOCKED

Feature = VERIFIED
but implementation = missing

Human approval = APPROVED
but no approval record exists

Production ready = TRUE
but P0 blocker = OPEN
```

These are state-integrity violations.

---

# 51. State Reconciliation

At meaningful checkpoints, the control process should reconcile:

```text
Documentation
↔
Task Board
↔
Code
↔
Tests
↔
Verification
↔
Decisions
↔
Project State
```

Any mismatch should be surfaced.

---

# 52. Project Audit

A project audit should inspect:

### Documentation

* completeness,
* contradictions,
* authority,
* dependencies.

### Architecture

* implementation alignment,
* boundary violations,
* undocumented changes.

### Tasks

* stale tasks,
* blocked tasks,
* unauthorized work,
* missing acceptance criteria.

### Testing

* missing coverage,
* unexecuted tests,
* flaky tests,
* unverified runtime behavior.

### AI

* model/prompt drift,
* contract violations,
* evidence quality,
* hallucination,
* regression.

### Security

* authentication,
* authorization,
* secrets,
* tool permissions,
* tenant isolation.

### Operations

* deployment,
* observability,
* backups,
* external dependencies.

---

# 53. Audit Severity

Audit findings should use:

```text
CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL
```

Critical findings must block affected release or execution.

---

# 54. Progress Metrics

Progress should not be represented only by percentage of tasks completed.

Useful dimensions include:

```text
Documentation Completeness
Architecture Completeness
Implementation Completeness
Test Completeness
Validation Completeness
Runtime Verification
Security Readiness
Integration Readiness
Human Approval Coverage
Known Risk
Open Blockers
```

A project can therefore be:

```text
90% implemented
40% runtime verified
```

which is materially different from:

```text
90% production ready
```

---

# 55. Quality Gates

Major transitions should use gates.

### Gate A — Documentation Ready

```text
Required docs available
No unresolved critical contradiction
Dependencies understood
```

### Gate B — Implementation Ready

```text
Task authorized
Dependencies satisfied
Acceptance criteria defined
Required context available
```

### Gate C — Validation Ready

```text
Implementation complete
Required tests available
Output contracts defined
Evidence requirements known
```

### Gate D — Release Ready

```text
Critical tests passed
Security validated
Runtime verification sufficient
Blockers resolved
Required approvals obtained
```

---

# 56. Critical Path

The control center should identify the critical path when useful.

Conceptually:

```text
Task A
  ↓
Task B
  ↓
Task D
  ↓
Task F
```

Tasks outside the critical path may be parallelized if:

* dependencies permit,
* context is isolated,
* authorization exists,
* testing remains controlled.

---

# 57. Parallel Work

Parallel execution is allowed only when dependency analysis supports it.

Example:

```text
             ┌── Entity Tests
Entity Model ┤
             ├── Entity Agent
             │
             └── Entity UI
```

Parallel work must not create conflicting writes or uncontrolled architectural divergence.

---

# 58. Change Impact Analysis

When a document, model, API, or architecture decision changes, the control center should determine:

```text
Affected documents
Affected modules
Affected agents
Affected workflows
Affected contracts
Affected tests
Affected UI
Affected migrations
Affected decisions
Affected tasks
```

This prevents local changes from producing invisible global inconsistency.

---

# 59. Versioning

Project control artifacts should be versioned.

At minimum:

```text
project state version
task board version
decision registry version
architecture version
contract version
agent version
workflow version
```

Historical states should remain inspectable.

---

# 60. Historical State

The system should preserve important project snapshots.

Example:

```yaml
snapshot:
  timestamp:
  project_version:
  active_task:
  completed_milestones:
  open_blockers:
  architecture_version:
  test_status:
  release_status:
```

This allows the team to understand how and why the project evolved.

---

# 61. Rollback Awareness

For reversible changes:

```text
Change
  ↓
Validate
  ↓
If failure
  ↓
Rollback
```

For irreversible changes:

```text
Proposal
  ↓
Impact analysis
  ↓
Human authorization
  ↓
Backup / recovery preparation
  ↓
Execution
  ↓
Verification
```

The control center should record rollback capability.

---

# 62. Project Health

Project health should be multidimensional.

Suggested health dimensions:

```yaml
health:
  architecture:
  documentation:
  implementation:
  testing:
  security:
  data:
  ai:
  integrations:
  performance:
  release:
```

Each may be:

```text
HEALTHY
AT_RISK
BLOCKED
UNKNOWN
```

`UNKNOWN` is preferable to an unsupported positive claim.

---

# 63. AI Project Manager Role

The AI may act as a project-control assistant.

It may:

* inspect project state,
* identify dependencies,
* detect inconsistencies,
* suggest next tasks,
* generate task plans,
* identify missing tests,
* summarize blockers,
* prepare handoffs,
* detect documentation drift,
* recommend context.

It must not silently:

* authorize itself,
* redefine product strategy,
* override human decisions,
* mark unverified work as verified,
* change architecture without governance,
* expand task scope.

---

# 64. Orchestrator Relationship

The central Orchestrator executes workflows.

The Project Control Center governs the project state surrounding those workflows.

Conceptually:

```text
Project Control Center
        ↓
Authorization + State
        ↓
Orchestrator
        ↓
Workflow
        ↓
Agents / Tools
        ↓
Evidence / Outputs
        ↓
Validation
        ↓
Project Control Center
```

The control center is therefore a governance layer, not an agent itself.

---

# 65. Decision Engine Relationship

The SEO Decision Engine makes domain-level recommendations and decisions according to its specification.

The Project Control Center determines:

```text
Can this task execute?
What is its current state?
Was it authorized?
Has it been verified?
What happens next?
```

The two must remain conceptually separate.

```text
Decision Engine = SEO decision intelligence

Project Control Center = project execution governance
```

---

# 66. Context Management Relationship

The control center should provide context requirements to the context-management system.

Example:

```yaml
context_request:
  task_id:
  objective:
  required_documents:
  required_decisions:
  required_code:
  required_evidence:
  excluded_context:
```

`25_CONTEXT_MANAGEMENT.md` defines the detailed retrieval and context lifecycle.

---

# 67. Skills and Tooling Relationship

The control center records capability requirements but does not replace the tooling policy.

For example:

```text
Task requires SERP provider integration
        ↓
Tool capability required
        ↓
Check tooling registry
        ↓
Install/enable if authorized
        ↓
Validate
        ↓
Record dependency
```

The detailed policy belongs to:

`26_SKILLS_AND_TOOLING_POLICY.md`

---

# 68. Security Requirements

The Project Control Center must protect:

* project state,
* credentials,
* API keys,
* internal evidence,
* audit logs,
* human identity,
* approval records,
* tenant boundaries,
* sensitive business information.

Authorization must be enforced at the application layer.

Client-side state must never be treated as authoritative authorization.

---

# 69. Auditability

Important actions should produce an audit event.

Examples:

```text
TASK_AUTHORIZED
TASK_STARTED
TASK_SCOPE_CHANGED
DOCUMENT_UPDATED
DECISION_CREATED
DECISION_OVERRIDDEN
APPROVAL_GRANTED
APPROVAL_REJECTED
TEST_EXECUTED
TEST_FAILED
BLOCKER_CREATED
BLOCKER_RESOLVED
RELEASE_BLOCKED
RELEASE_APPROVED
```

Each event should have:

```yaml
event:
  type:
  actor:
  timestamp:
  project_id:
  entity_id:
  previous_state:
  new_state:
  reason:
  evidence:
```

---

# 70. Observability

Project-control operations should be observable.

Useful metrics:

```text
active_tasks
blocked_tasks
task_cycle_time
failed_tasks
reopened_tasks
test_failure_rate
verification_rate
runtime_verification_rate
open_blockers
architecture_changes
scope_changes
approval_latency
AI_retry_rate
AI_contract_failure_rate
```

The goal is operational visibility, not vanity metrics.

---

# 71. Failure Handling

If project-control state becomes inconsistent:

```text
Detect
  ↓
Freeze affected transition
  ↓
Identify conflicting records
  ↓
Determine authoritative source
  ↓
Reconcile
  ↓
Validate
  ↓
Resume
```

The system must not silently overwrite contradictory state.

---

# 72. Recovery From Interrupted Sessions

If a development session ends unexpectedly, the next session must recover from persistent state.

Recovery procedure:

```text
Read Project Control Center
        ↓
Identify active task
        ↓
Inspect latest handoff
        ↓
Check changed files
        ↓
Check tests
        ↓
Check blockers
        ↓
Check authorization
        ↓
Load minimum required context
        ↓
Resume or re-plan
```

The next session must not assume that an interrupted task completed.

---

# 73. Session Start Protocol

At the beginning of a development session, Claude should:

1. Read the project control state.
2. Identify the active task.
3. Check authorization.
4. Check blockers.
5. Check relevant dependencies.
6. Identify required context.
7. Inspect recent changes.
8. Check verification state.
9. Determine the legitimate next action.

Only then should implementation begin.

---

# 74. Session End Protocol

Before ending a session, Claude should:

1. Record completed work.
2. Record incomplete work.
3. Record files changed.
4. Record tests executed.
5. Record verification state.
6. Record blockers.
7. Record decisions.
8. Update affected documentation.
9. Update task state.
10. Define next authorized action.
11. Prepare handoff context.

---

# 75. Project Control Center Canonical Workflow

```text
START SESSION
      ↓
LOAD PROJECT STATE
      ↓
AUDIT ACTIVE TASK
      ↓
CHECK AUTHORIZATION
      ↓
CHECK DEPENDENCIES
      ↓
LOAD REQUIRED CONTEXT
      ↓
IMPLEMENT / ANALYZE
      ↓
TEST
      ↓
VALIDATE
      ↓
VERIFY
      ↓
UPDATE STATE
      ↓
RECORD EVIDENCE
      ↓
CHECK BLOCKERS
      ↓
UPDATE DOCUMENTATION
      ↓
IDENTIFY NEXT ACTION
      ↓
HANDOFF
```

---

# 76. Project Control Center and WBS

The WBS defines the hierarchical work model.

The Project Control Center operationalizes it.

```text
WBS
  = What exists as work

Project Control Center
  = What is happening with that work
```

The two must remain synchronized.

---

# 77. Project Control Center and Task Board

The task board is an operational view.

The control center is the authoritative state model.

A UI board may display:

```text
READY
IN_PROGRESS
BLOCKED
TESTING
DONE
```

but the persistent state must retain the underlying:

* authorization,
* dependencies,
* evidence,
* verification,
* decisions,
* risks,
* timestamps.

---

# 78. Project Control Center and Roadmap

The roadmap describes strategic sequencing.

The control center tracks actual execution.

The roadmap may say:

```text
Build Entity Intelligence
```

The control center must say:

```text
ENTITY-042
Status: IMPLEMENTED
Unit Tests: PASSED
Integration: UNVERIFIED
Blocker: Provider X unavailable
Next Action: Run mock integration suite
```

---

# 79. MVP Project Control Center

The MVP must support:

### State

* project state,
* milestone state,
* task state.

### Authorization

* explicit task authorization,
* scope.

### Dependencies

* task dependencies,
* documentation dependencies.

### Verification

* implementation,
* test,
* validation,
* runtime verification.

### Governance

* decisions,
* blockers,
* risks,
* human approvals.

### Handoff

* active task,
* completed work,
* next action,
* context.

### Audit

* significant state changes.

---

# 80. Future Project Control Capabilities

Future versions may add:

* dependency graph visualization,
* automatic critical-path analysis,
* intelligent task decomposition,
* predictive blocker detection,
* project health scoring,
* architecture drift detection,
* automatic documentation consistency checking,
* AI-generated change-impact analysis,
* historical project analytics,
* resource/cost planning,
* automated release gates,
* policy-driven execution,
* adaptive workflow planning.

These must remain subordinate to project governance.

---

# 81. Anti-Patterns

The following are prohibited.

### 81.1 Conversation as source of truth

```text
"We discussed this earlier."
```

is not sufficient project state.

---

### 81.2 Implicit authorization

```text
The user mentioned the feature,
therefore implementation is authorized.
```

Incorrect.

---

### 81.3 Done = Code Exists

Implementation is not equivalent to verification.

---

### 81.4 Fake verification

Do not claim tests, runtime verification, or integrations that were not actually performed.

---

### 81.5 Hidden scope expansion

Do not modify unrelated systems without authorization.

---

### 81.6 Code-driven architecture

Do not let accidental implementation become the architectural specification.

---

### 81.7 State without evidence

Do not mark critical states without supporting evidence.

---

### 81.8 Stale task board

A task board that disagrees with persistent state is a project-control failure.

---

### 81.9 Silent conflict resolution

Contradictory state must be surfaced and reconciled explicitly.

---

### 81.10 Giant context loading

Do not load every project document for every task when task-specific context is sufficient.

---

### 81.11 Autonomous project redefinition

AI may optimize execution but may not silently redefine:

* product strategy,
* architecture,
* business priorities,
* human decisions.

---

# 82. Definition of Done — Project Control Center

This document is complete when the project has a defined mechanism for:

* persistent project state,
* task hierarchy,
* task authorization,
* dependency management,
* milestone management,
* blocker management,
* risk management,
* decision management,
* approval tracking,
* verification tracking,
* evidence tracking,
* documentation state,
* implementation state,
* test state,
* runtime verification,
* context requirements,
* tooling requirements,
* change management,
* session recovery,
* session handoff,
* project audit,
* release gating.

---

# 83. Final Operating Model

The complete project-control loop is:

```text
PROJECT STATE
      ↓
DOCUMENT AUDIT
      ↓
DEPENDENCY GRAPH
      ↓
TASK SELECTION
      ↓
AUTHORIZATION
      ↓
CONTEXT ASSEMBLY
      ↓
IMPLEMENTATION
      ↓
TESTING
      ↓
VALIDATION
      ↓
RUNTIME VERIFICATION
      ↓
EVIDENCE
      ↓
STATE UPDATE
      ↓
DOCUMENT UPDATE
      ↓
DECISION / APPROVAL
      ↓
NEXT AUTHORIZED ACTION
      ↓
HANDOFF
      ↓
NEXT SESSION
```

---

# 84. Non-Negotiable Project-Control Rules

1. Persistent project state is mandatory.
2. Conversation history is not the project state.
3. Every meaningful task must have an identity.
4. Authorization must be explicit.
5. Scope must be explicit.
6. Dependencies must be explicit.
7. Implementation and verification are separate states.
8. Tests must be actually executed before being reported as executed.
9. Runtime verification must be distinguished from implementation.
10. Unknown is a valid state.
11. AI recommendations are not human decisions.
12. Human approvals must be recorded explicitly.
13. Architecture changes require governance.
14. Scope expansion is prohibited without authorization.
15. Blockers must be explicit.
16. Important claims must have evidence.
17. Project state must be periodically reconciled.
18. Handoff must be persistent.
19. Context must be task-specific.
20. Required tools and skills must be tracked.
21. Release readiness must be evidence-based.
22. The AI must stop when required authority or evidence is missing.
23. No state may be upgraded merely to make the project appear more complete.
24. The control center must preserve historical decisions and important state transitions.
25. The project must always identify the next legitimate action.

---

# 85. Final Project Control Model

The SEO Research & Strategy Copilot / SEO Decision Engine uses:

```text
Human Authority
      ↓
Project Control Center
      ↓
Documentation + Dependency Graph
      ↓
Authorized Task
      ↓
Context Management
      ↓
Orchestrator
      ↓
Workflow
      ↓
Agents / Tools / Skills
      ↓
Structured Outputs
      ↓
Testing + Validation
      ↓
Evidence
      ↓
Human Review Where Required
      ↓
Project State Update
      ↓
Next Authorized Task
```

The fundamental distinction is:

```text
Project Control Center
    controls execution state

Decision Engine
    controls SEO reasoning and recommendations

Orchestrator
    controls workflow execution

Agents
    perform specialized intelligence

Tools
    acquire or manipulate external capabilities

Human
    retains strategic and consequential authority
```

---

# 86. Document Control

```yaml
document:
  id: "23"
  filename: "23_PROJECT_CONTROL_CENTER.md"
  status: "APPROVED_AS_BASELINE_PROJECT_CONTROL_CENTER"
  authority: "baseline_project_state_task_control_authorization_and_execution_governance"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

core_responsibilities:
  - project_state
  - milestone_state
  - task_state
  - task_authorization
  - dependency_management
  - documentation_state
  - implementation_tracking
  - testing_tracking
  - validation_tracking
  - runtime_verification
  - evidence_tracking
  - decision_tracking
  - approval_tracking
  - blocker_tracking
  - risk_tracking
  - change_management
  - session_recovery
  - session_handoff
  - release_gating

task_states:
  - BACKLOG
  - READY
  - AUTHORIZED
  - IN_PROGRESS
  - BLOCKED
  - IN_REVIEW
  - TESTING
  - VALIDATING
  - DONE
  - REJECTED
  - CANCELLED

verification_states:  # orthogonal to task_states above; see § 8
  - IMPLEMENTED
  - TESTED
  - VALIDATED
  - RUNTIME_VERIFIED
  - PARTIALLY_VERIFIED
  - UNVERIFIED
  - BLOCKED

epistemic_states:
  - OBSERVED
  - INFERRED
  - ESTIMATED
  - RECOMMENDED
  - HUMAN_APPROVED
  - CONFLICTED
  - UNKNOWN

project_statuses:
  - INITIALIZING
  - DOCUMENTING
  - PLANNING
  - READY
  - IN_PROGRESS
  - BLOCKED
  - PAUSED
  - VALIDATING
  - RELEASE_CANDIDATE
  - RELEASED
  - DEPRECATED
  - ARCHIVED

core_governance:
  explicit_authorization: true
  task_scope_control: true
  dependency_tracking: true
  evidence_based_state: true
  human_decision_authority: true
  runtime_verification_separation: true
  persistent_handoff: true
  historical_state_tracking: true
  architecture_change_control: true
  release_gates: true
  stop_conditions: true

anti_patterns:
  - conversation_as_source_of_truth
  - implicit_authorization
  - fake_completion
  - fake_verification
  - hidden_scope_expansion
  - code_driven_architecture
  - state_without_evidence
  - stale_task_state
  - silent_conflict_resolution
  - giant_context_loading
  - autonomous_project_redefinition

relationships:
  master_rules: "03_MASTER_RULES.md"
  system_architecture: "04_SYSTEM_ARCHITECTURE.md"
  agent_architecture: "05_AI_AGENT_ARCHITECTURE.md"
  data_architecture: "06_DATA_ARCHITECTURE.md"
  technical_architecture: "07_TECHNICAL_ARCHITECTURE.md"
  agent_specifications: "13_AGENT_SPECIFICATIONS.md"
  agent_workflow: "14_AGENT_WORKFLOW.md"
  human_in_the_loop: "15_HUMAN_IN_THE_LOOP.md"
  output_contracts: "16_OUTPUT_CONTRACTS.md"
  project_structure: "20_PROJECT_STRUCTURE.md"
  development_and_debug: "21_DEVELOPMENT_AND_DEBUG.md"
  testing_and_validation: "22_TESTING_AND_VALIDATION.md"
  roadmap_dependencies: "24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md"
  context_management: "25_CONTEXT_MANAGEMENT.md"
  skills_tooling_policy: "26_SKILLS_AND_TOOLING_POLICY.md"

next_dependency:
  document: "24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md"
  purpose: "documentation_index_roadmap_wbs_dependencies_task_board_and_execution_map"
```

---

# 87. Final Status

```yaml
status:
  document: "23_PROJECT_CONTROL_CENTER.md"
  state: "APPROVED_AS_BASELINE_PROJECT_CONTROL_CENTER"
  project_control_model: "persistent_state + explicit_authorization + dependency_graph + evidence_based_verification"
  execution_model: "authorized_task -> controlled_execution -> testing -> validation -> verification -> state_update"
  human_authority: "strategic_and_consequential"
  ai_authority: "analysis_recommendation_and_controlled_execution"
  source_of_truth: "persistent_project_documentation_and_control_state"
  conversation_as_source_of_truth: false
  fake_completion: false
  next_document: "24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md"
```
