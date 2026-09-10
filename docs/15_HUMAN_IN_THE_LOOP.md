# 15 — Human in the Loop

**Document:** `15_HUMAN_IN_THE_LOOP.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Human-in-the-Loop, Review, Approval & Strategic Authority Specification
**Status:** `APPROVED_AS_BASELINE_HUMAN_IN_THE_LOOP`
**Authority:** Baseline specification for human authority, review, validation, approval, rejection, escalation, intervention, feedback, and human-machine decision boundaries.

---

# 1. Purpose

This document defines how humans interact with the SEO Research & Strategy Copilot and how human judgment participates in the research, analysis, decision, and execution lifecycle.

The system is designed around:

```text
Human Strategy
+
AI Research
+
AI Analysis
+
Human Validation
```

The objective is not to eliminate human judgment.

The objective is to make human judgment:

* better informed
* faster
* evidence-backed
* explainable
* reproducible
* auditable
* strategically focused

The system must therefore optimize for:

> **Human decision quality, not maximum AI autonomy.**

---

# 2. Core Principle

The foundational authority model is:

```text
Human Strategic Authority
        ↓
SEO Decision Engine
        ↓
Workflow / Orchestrator
        ↓
AI Agents
        ↓
Tools / External Evidence
```

The direction of information flow may be bidirectional, but authority is not.

AI can:

* research
* analyze
* classify
* infer
* cluster
* compare
* detect
* recommend
* explain

AI cannot silently assume strategic authority.

---

# 3. Human-in-the-Loop Definition

Human-in-the-loop means that a human can:

* define objectives
* provide business context
* validate assumptions
* resolve ambiguity
* approve or reject recommendations
* modify outputs
* set constraints
* prioritize opportunities
* authorize consequential actions
* provide feedback
* override AI recommendations
* stop workflows

Human involvement may occur:

* before execution
* during execution
* after individual steps
* at decision gates
* before consequential actions
* after execution

Human review is therefore a workflow capability, not merely a UI feature.

---

# 4. Human Roles

The exact role model may evolve, but the system should conceptually distinguish responsibilities.

## 4.1 Strategic Owner

Responsible for:

* business priorities
* SEO objectives
* strategic positioning
* commercial priorities
* acceptable trade-offs
* final strategic decisions

---

## 4.2 SEO Strategist

Responsible for:

* SEO interpretation
* search strategy
* topic validation
* intent interpretation
* page mapping
* topical architecture
* internal linking strategy

---

## 4.3 Reviewer

Responsible for:

* validating AI outputs
* identifying errors
* confirming evidence
* rejecting unsupported recommendations
* requesting modifications

---

## 4.4 Operator

Responsible for authorized execution.

Examples:

* implementing approved page architecture
* publishing content
* modifying internal links
* applying metadata changes

---

## 4.5 Administrator

Responsible for:

* system configuration
* permissions
* workflow policies
* integrations
* access control

Roles may be combined in MVP, but permissions must remain conceptually separable.

---

# 5. Human Authority Model

Human authority is divided into several categories.

```text
Strategic Authority
    ↓
Decision Authority
    ↓
Approval Authority
    ↓
Execution Authority
    ↓
Administrative Authority
```

Possessing one authority does not automatically imply possessing all others.

---

# 6. AI Authority Boundary

AI capabilities may produce:

```text
Observation
Inference
Estimate
Recommendation
Decision Candidate
```

They must not silently produce:

```text
Human Strategic Decision
Human Approval
Authorized External Action
```

unless the project explicitly defines a lower-risk automated policy for that specific action.

---

# 7. Epistemic States

Human review must preserve epistemic state.

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

Intent appears commercial
→ INFERRED

Search demand estimated at X
→ ESTIMATED

Create dedicated product page
→ RECOMMENDED

Human approves dedicated page
→ HUMAN_APPROVED
```

These states must never be collapsed into a single generic "AI result" state.

---

# 8. Human Decision vs AI Recommendation

The system must distinguish:

```text
AI Recommendation
```

from:

```text
Human Decision
```

Example:

```text
AI:
Topic A and Topic B should share one page.

Human:
Reject.

Reason:
Different user needs and different commercial objectives.
```

The resulting state should explicitly record:

```text
AI Recommendation = rejected
Human Decision = separate pages
```

The AI recommendation must remain part of history.

It must not be overwritten as if it never existed.

---

# 9. Human Review States

A review may use states such as:

```text
NOT_REQUIRED
PENDING
IN_REVIEW
APPROVED
REJECTED
MODIFICATION_REQUESTED
DEFERRED
ESCALATED
CANCELLED
```

State transitions must be explicit.

---

# 10. Review Object

A conceptual review object:

```yaml
review:
  id:
  workflow_run_id:
  step_id:
  artifact_id:
  reviewer_id:
  review_type:
  status:
  decision:
  reason:
  comments:
  modifications:
  evidence_references:
  created_at:
  completed_at:
```

The final implementation may differ, but the semantic information must be preserved.

---

# 11. Review Types

The system should support multiple review types.

### Validation Review

Is the AI output correct?

### Strategic Review

Does the recommendation align with business strategy?

### Evidence Review

Is the recommendation adequately supported?

### Conflict Review

Which interpretation should be accepted when evidence conflicts?

### Architecture Review

Does the proposed page/site structure make sense?

### Risk Review

Could the proposed action create significant negative consequences?

### Execution Approval

Is the system authorized to perform the action?

---

# 12. When Human Review Is Required

Human review should be triggered when:

* strategic ambiguity exists
* evidence conflicts
* confidence is low
* business context is missing
* multiple valid strategies exist
* recommendation has significant consequences
* AI output contradicts an existing approved decision
* entity resolution is ambiguous
* page mapping is uncertain
* cannibalization interpretation is uncertain
* architecture changes are proposed
* external actions are requested
* policy requires approval

---

# 13. When Human Review May Not Be Required

Low-risk operations may be automated.

Examples:

```text
Normalization
Deduplication
Schema validation
Caching
Data formatting
Deterministic aggregation
Non-destructive evidence collection
```

Automation must still be observable and reversible where practical.

---

# 14. Risk-Based Human Review

Human review should be proportional to risk.

A conceptual model:

```text
Low Risk
    ↓
Automated

Medium Risk
    ↓
AI + Validation

High Risk
    ↓
AI + Validation + Human Approval

Critical / Irreversible
    ↓
Explicit Human Authorization
```

Risk should consider:

* reversibility
* business impact
* SEO impact
* data impact
* external visibility
* financial impact
* uncertainty
* confidence
* scope

---

# 15. Human Review Trigger Engine

The workflow may automatically request review when conditions are met.

Example:

```yaml
review_trigger:
  condition:
    confidence < 0.70
  action:
    request_human_review: true
```

Other triggers:

```text
conflict_detected
business_rule_violation
high_impact_action
architecture_change
insufficient_evidence
low_cluster_stability
ambiguous_entity
strategic_priority_conflict
```

Thresholds must be configurable and versioned.

---

# 16. Confidence Is Not Authority

High confidence does not grant AI authority.

For example:

```text
AI confidence: 0.98
```

does not mean:

```text
Human approval: automatic
```

Confidence measures uncertainty in the analysis.

Authority determines who can make the decision.

These are separate concepts.

---

# 17. Human Review UX

The review interface should present decision-relevant information.

A reviewer should see:

```text
Objective
↓
Recommendation
↓
Key Decision Factors
↓
Evidence
↓
Confidence
↓
Conflicts
↓
Risks
↓
Alternatives
↓
Existing Decisions
↓
Required Decision
```

The interface should minimize unnecessary information while preserving sufficient context.

---

# 18. Evidence-First Review

Human reviewers should be able to inspect evidence supporting an AI recommendation.

For example:

```text
Recommendation:
Create a dedicated page for Topic X.

Supporting evidence:
- SERP similarity
- dominant intent
- existing page coverage
- entity relationship
- business relevance
- competitor page patterns
```

The system should make the evidence chain inspectable.

---

# 19. No Private Chain-of-Thought Requirement

Human review does not require exposing hidden model reasoning or private chain-of-thought.

The system should instead expose:

* conclusions
* evidence
* decision factors
* assumptions
* confidence
* uncertainty
* conflicts
* alternatives
* provenance

The objective is explainability through evidence and structured rationale, not disclosure of private internal reasoning.

---

# 20. Decision Factors

AI recommendations should expose structured decision factors.

Example:

```yaml
decision_factors:
  business_relevance: high
  search_evidence: strong
  intent_alignment: high
  existing_page_coverage: low
  competition: medium
  confidence: 0.86
```

These factors allow humans to understand why a recommendation exists.

---

# 21. Alternative Recommendations

For meaningful strategic decisions, the system should provide alternatives when appropriate.

Example:

```text
Option A:
Create one comprehensive page.

Option B:
Create two specialized pages.

Option C:
Create one primary page + supporting content.
```

Each option should include:

* rationale
* evidence
* benefits
* risks
* confidence

The system must not manufacture alternatives when evidence does not support them.

---

# 22. Human Override

A human may override an AI recommendation.

Example:

```text
AI:
Merge Topic A and Topic B.

Human:
Keep separate.

Reason:
Commercially distinct offerings.
```

The override should be stored as:

```text
Human Decision
+
Reason
+
Timestamp
+
Reviewer
+
Affected Artifact
```

---

# 23. Override Hierarchy

When a human decision conflicts with an AI recommendation:

```text
Human Decision
    >
AI Recommendation
```

When a later AI analysis conflicts with an existing human-approved strategic decision, the system should:

1. surface the conflict
2. preserve the existing decision
3. present new evidence
4. request human review if change is appropriate

It must not silently overwrite the approved decision.

---

# 24. Strategic Decision Persistence

Important human decisions must become durable project knowledge.

Examples:

```text
Approved Target Market
Approved Entity Definition
Approved Topic
Rejected Topic
Approved Page Mapping
Approved Page Type
Approved Architecture
Rejected Recommendation
Business Priority
Strategic Constraint
```

These decisions should be retrievable by future workflows.

---

# 25. Human Decisions as Context

Future agents may need relevant human decisions.

Example:

```text
Human previously approved:
"Product X and Product Y are strategically separate."
```

A future clustering workflow must receive this decision when evaluating those entities.

Human decisions therefore become part of the shared context model.

---

# 26. Human Feedback

Feedback should be structured whenever possible.

Instead of:

```text
"This seems wrong."
```

prefer:

```yaml
feedback:
  category: business_context
  decision: reject
  reason: commercial_priority_mismatch
```

Possible categories:

```text
BUSINESS_CONTEXT
ENTITY_RESOLUTION
TOPIC_RELEVANCE
INTENT
SERP_INTERPRETATION
CLUSTERING
PAGE_MAPPING
ARCHITECTURE
INTERNAL_LINKING
EVIDENCE_QUALITY
MODEL_ERROR
MISSING_CONTEXT
OTHER
```

---

# 27. Human Feedback and Learning

Human feedback can be used to improve:

* agent prompts
* classification rules
* workflow routing
* retrieval
* ranking
* evaluation datasets
* clustering
* intent models
* recommendation quality

However:

> Human feedback must not automatically modify production behavior without evaluation and controlled deployment.

---

# 28. Feedback Lifecycle

```text
Human Feedback
      ↓
Normalize
      ↓
Classify
      ↓
Store
      ↓
Evaluate
      ↓
Aggregate
      ↓
Candidate Improvement
      ↓
Test
      ↓
Validate
      ↓
Deploy
```

---

# 29. Human Review and Workflow

Human review is a workflow step.

Example:

```text
Topic Clustering
      ↓
Validation
      ↓
Human Review
      ↓
Approved
      ↓
Page Mapping
```

When review is pending:

```text
Workflow Status = WAITING_FOR_HUMAN
```

The workflow must remain resumable.

---

# 30. Human Review and Checkpoints

A human review should normally create a checkpoint.

```text
Before Review
      ↓
Checkpoint
      ↓
WAITING_FOR_HUMAN
      ↓
Human Decision
      ↓
Resume
```

This prevents loss of workflow state.

---

# 31. Human Review and Time

Human review may take:

* seconds
* hours
* days
* weeks

The workflow system must not assume immediate response.

Long-running review states must therefore be persistent.

---

# 32. Review Expiration

Some approvals may expire when underlying evidence becomes stale.

Example:

```text
SERP-based recommendation approved
        ↓
SERP data becomes significantly outdated
        ↓
Review may require revalidation
```

Expiration policies should be defined according to artifact type.

---

# 33. Evidence Freshness and Approval

Human approval does not necessarily make an artifact permanently correct.

A decision may remain:

```text
HUMAN_APPROVED
```

while its underlying evidence becomes:

```text
STALE
```

The system should distinguish:

* approval state
* evidence freshness
* current validity

---

# 34. Human Review of Stale Decisions

When stale decisions materially affect a new workflow:

```text
Existing Approved Decision
          ↓
Freshness Check
          ↓
Still Valid?
      ├── yes → reuse
      └── no  → revalidation
```

The system should not blindly reuse outdated strategic assumptions.

---

# 35. Human Review and Conflicts

When conflicting information exists:

```text
Evidence A
Evidence B
Human Decision C
```

the system should preserve all three.

Example:

```text
Observed:
SERP is mixed.

AI:
Commercial intent likely.

Human:
Treat as informational because of business positioning.
```

This is not an error.

It is a valid strategic decision informed by multiple evidence layers.

---

# 36. Human Strategic Constraints

Humans may define constraints such as:

```text
Do not target Topic X.
Prioritize Product Y.
Avoid creating pages for low-margin services.
Use Persian-first terminology.
Keep Product A and Product B separate.
Do not create pages below a certain business value.
```

Constraints must be represented structurally.

They should be available to relevant workflows and agents.

---

# 37. Constraints vs Recommendations

The system must distinguish:

```text
Constraint
```

from:

```text
Recommendation
```

A recommendation may change.

A strategic constraint remains binding until explicitly changed by an authorized human.

---

# 38. Human-Defined Objectives

The quality of AI analysis depends heavily on objective definition.

The system should allow humans to specify:

* business goal
* target market
* audience
* priority
* timeframe
* risk tolerance
* constraints
* success criteria

The workflow should validate that required strategic context exists before executing major analysis.

---

# 39. Missing Human Context

When important strategic context is missing:

```text
Missing Context
      ↓
Cannot Safely Decide
      ↓
Request Human Input
```

The system should not invent:

* business priorities
* target audience
* positioning
* commercial importance
* strategic constraints

---

# 40. Human Review Questions

The system should generate focused questions rather than vague requests.

Bad:

```text
"Please review."
```

Better:

```text
"Should Topic A and Topic B target one page or two separate pages?"
```

With:

```text
Evidence
Confidence
Alternatives
Risks
```

---

# 41. Human Review Granularity

Review should occur at the appropriate granularity.

Possible levels:

```text
Project
Workflow
Step
Artifact
Entity
Topic
Cluster
Page
Decision
Action
```

Reviewing an entire workflow when only one topic is ambiguous creates unnecessary friction.

---

# 42. Batch Review

The system should support batch review for repetitive decisions.

Example:

```text
Review 100 topic candidates

Approve:
78

Reject:
15

Needs review:
7
```

Batch review must still preserve individual decisions.

---

# 43. Confidence-Based Review Queues

Review queues may prioritize:

1. High-impact decisions
2. Low-confidence decisions
3. Conflicted decisions
4. Novel patterns
5. High-value opportunities
6. Potentially irreversible actions

This helps humans spend time where it matters most.

---

# 44. Human Review Prioritization

A conceptual review priority score may consider:

```text
Impact
×
Uncertainty
×
Irreversibility
×
Strategic Importance
```

This is a prioritization mechanism, not a replacement for authorization rules.

---

# 45. Human Review and Page Architecture

Page architecture decisions often require human judgment because they combine:

* search reality
* semantic structure
* business strategy
* user experience
* technical constraints
* organizational constraints

AI should therefore produce:

```text
Recommended Architecture
+
Alternatives
+
Evidence
+
Risks
+
Confidence
```

Human approval should determine the final strategic architecture.

---

# 46. Human Review and Topical Maps

A topical map is a strategic artifact.

AI may propose:

```text
Pillar Topics
Supporting Topics
Relationships
Page Candidates
Coverage Gaps
```

Human review determines whether the map reflects:

* actual business priorities
* market positioning
* strategic differentiation
* desired audience journey

---

# 47. Human Review and Internal Linking

AI may recommend:

```text
Page A → Page B
Anchor concept → Page C
Supporting page → Pillar page
```

Human review may be required when:

* links alter important navigation
* anchors have strategic implications
* architecture changes
* large-scale modifications are proposed

---

# 48. Human Review and Cannibalization

Cannibalization detection should be evidence-based.

AI may detect:

```text
High SERP overlap
+
Similar intent
+
Similar topic
+
Multiple existing pages
```

It may recommend consolidation.

Human review may determine that pages should remain separate because:

* products differ
* audiences differ
* commercial objectives differ
* organizational ownership differs
* user journeys differ

---

# 49. Human Review and Content Gaps

A detected content gap is not automatically a publishing instruction.

The system should distinguish:

```text
Content Gap Detected
        ↓
Business Value Evaluation
        ↓
Opportunity Recommendation
        ↓
Human Decision
        ↓
Execution if Approved
```

---

# 50. Human Review and Search Reality

Search data should inform human strategy but not dictate it.

Example:

```text
High search demand
```

does not automatically mean:

```text
High strategic priority
```

Likewise:

```text
Low search volume
```

does not automatically mean:

```text
Low business value
```

Human strategy can intentionally prioritize:

* emerging topics
* strategic products
* high-value niches
* brand differentiation
* low-volume commercial queries
* underserved audiences

---

# 51. Human Review and Business Reality

The system must continuously distinguish:

```text
Search Reality
```

from:

```text
Business Reality
```

A good SEO decision reconciles both.

```text
SEO Decision
=
Business Reality
+
Search Reality
+
Semantic Understanding
+
Evidence
+
Human Strategy
```

---

# 52. Human-in-the-Loop and Automation Levels

The system may use autonomy levels:

```text
Level 0 — Human Only
Level 1 — AI Assisted
Level 2 — AI Proposed
Level 3 — AI Executes Low-Risk Tasks
Level 4 — AI Executes Policy-Bounded Tasks
Level 5 — High Autonomy
```

The MVP should primarily operate at:

```text
Level 0–2
```

Higher autonomy requires explicit governance and evidence.

---

# 53. Automation Promotion

A task should become more automated only when:

* quality is measured
* failure modes are understood
* confidence is reliable
* rollback is available
* authorization is clear
* human review history supports automation
* regression tests exist

Automation should be earned through evidence.

---

# 54. Human-in-the-Loop Safety Rule

No increase in AI autonomy may weaken:

* strategic authority
* authorization boundaries
* evidence requirements
* auditability
* rollback capability
* security
* project isolation

---

# 55. Human Review Audit Trail

Every meaningful human decision should record:

```text
Who
What
When
Why
Based on Which Evidence
Against Which Recommendation
Affecting Which Artifact
Under Which Workflow
```

This creates an auditable strategic history.

---

# 56. Human Decision Versioning

When a human changes a previous decision:

```text
Decision v1
    ↓
Human Revision
    ↓
Decision v2
```

The original decision should remain historically accessible.

---

# 57. Decision Reversal

A human may reverse a previous decision.

Example:

```text
Previously:
Separate pages.

Later:
Merge pages.
```

The system should preserve:

```text
Previous Decision
+
New Decision
+
Reason
+
Evidence
+
Timestamp
```

---

# 58. Decision Conflict Detection

The system should detect when a new decision conflicts with an existing approved decision.

Example:

```text
Existing:
Product A and B must remain separate.

New recommendation:
Merge A and B.
```

The workflow should surface:

```text
STRATEGIC_CONFLICT
```

and request appropriate human resolution.

---

# 59. Human Review Notifications

The system may notify humans when:

* review is required
* a workflow is blocked
* a high-impact conflict appears
* evidence becomes stale
* an approval expires
* a consequential action is ready

Notifications should be actionable and contextual.

---

# 60. Human Review and Context Management

The review interface must provide enough context for a meaningful decision.

However, context should remain focused.

The system should retrieve:

```text
Relevant Evidence
Relevant Prior Decisions
Relevant Business Constraints
Relevant Agent Output
Relevant Alternatives
```

rather than the entire project history.

---

# 61. Human Review and Skills/Tools

Humans should be informed when an AI recommendation depends materially on:

* a specific external provider
* an installed skill
* a tool
* a particular dataset
* a limited evidence source

This improves transparency and makes provider-dependent conclusions easier to evaluate.

---

# 62. Human Review and External Providers

If provider data is:

* incomplete
* stale
* unavailable
* estimated
* conflicting

the reviewer must be able to see this.

The system must not present provider-derived estimates as ground truth.

---

# 63. Human Review and AI Errors

When a reviewer identifies an AI error, the system should allow classification.

Examples:

```text
Wrong Entity
Wrong Intent
Wrong Cluster
Insufficient Evidence
Ignored Business Context
Incorrect Page Mapping
Hallucinated Claim
Incorrect Tool Interpretation
Missing Context
```

This allows systematic improvement.

---

# 64. Human Review and Hallucination Handling

If an AI output contains unsupported information:

1. mark the output invalid
2. preserve the original output for audit
3. record the error
4. prevent propagation
5. request correction or rerun
6. evaluate whether related outputs are affected

A hallucination must not silently become project knowledge.

---

# 65. Human Review and Data Quality

Humans may validate:

* entity identity
* EAV facts
* topic relevance
* intent
* page mapping
* business relevance

Validated data may become higher-confidence project knowledge.

The system must still preserve provenance indicating that the value was human-approved.

---

# 66. Human Review and Knowledge Graph

Human-approved relationships should be represented distinctly.

Example:

```text
Entity A
    └── relationship
          ├── AI inferred
          └── human approved
```

Human validation increases decision confidence but does not erase original provenance.

---

# 67. Human Review and Semantic Model

Human corrections can improve:

* entity resolution
* relationship semantics
* topic boundaries
* attribute interpretation
* query-to-topic mapping

These corrections become valuable future context.

---

# 68. Human Review and Search Intent

Intent may be ambiguous.

The system should allow humans to override:

```text
Informational
Commercial
Transactional
Navigational
Local
Comparative
Mixed
```

or other supported intent dimensions.

The original AI inference must remain available for evaluation.

---

# 69. Human Review and Clustering

Human reviewers may:

* merge clusters
* split clusters
* rename clusters
* reject clusters
* mark topics as independent
* mark a cluster as uncertain

The system should preserve the relationship between:

```text
AI Cluster
```

and:

```text
Human-Approved Cluster
```

---

# 70. Human Review and Page Mapping

Humans should be able to:

* assign topic to existing page
* create new page candidate
* merge page candidates
* split page candidates
* reject page candidate
* mark mapping as deferred

This is particularly important because:

```text
Topic ≠ Page
```

and:

```text
Cluster ≠ Page
```

---

# 71. Human Review and Topical Map Approval

A topical map should have explicit lifecycle states:

```text
DRAFT
AI_PROPOSED
UNDER_REVIEW
HUMAN_APPROVED
REJECTED
SUPERSEDED
ARCHIVED
```

Only an approved map should be considered authoritative for downstream execution.

---

# 72. Human Review and Page Architecture Approval

Page architecture should follow:

```text
AI Proposal
      ↓
Evidence Validation
      ↓
Human Review
      ↓
Approved Architecture
```

The approved architecture becomes a strategic project artifact.

---

# 73. Human Review and Internal Linking Approval

Internal-linking recommendations may be:

```text
AUTO_APPLY
REVIEW_REQUIRED
MANUAL_ONLY
```

depending on:

* scope
* risk
* architecture impact
* policy

---

# 74. Human Review and Publishing

Publishing should generally be separated from research.

Recommended lifecycle:

```text
Research
 ↓
Analysis
 ↓
Recommendation
 ↓
Human Approval
 ↓
Execution Plan
 ↓
Authorized Publishing
```

The research system must not silently publish based solely on AI analysis.

---

# 75. Human Review and Irreversible Actions

Irreversible or difficult-to-reverse actions should require explicit authorization.

Examples:

* deleting pages
* bulk redirects
* large-scale URL restructuring
* destructive data changes
* mass content replacement

The system should provide:

```text
Action
+
Impact
+
Risk
+
Rollback Plan
+
Evidence
```

before authorization.

---

# 76. Human Review and Rollback

For consequential actions, the system should record:

* original state
* proposed state
* approved state
* execution timestamp
* operator
* rollback capability

Human approval does not eliminate the need for operational safeguards.

---

# 77. Review Quality

Human review itself should be measurable.

Metrics may include:

```text
Review Acceptance Rate
AI Recommendation Rejection Rate
Revision Rate
Review Time
False Approval Rate
False Rejection Rate
Conflict Rate
Escalation Rate
```

These metrics help determine where AI requires improvement.

---

# 78. Human Review as Evaluation Dataset

Approved/rejected decisions may become evaluation examples.

Example:

```text
Input:
Topic cluster

AI Output:
Merge

Human:
Reject

Reason:
Different search intents
```

This can become a golden evaluation case for clustering.

---

# 79. Human Review Governance

Human feedback should not be treated as automatically correct in every technical sense.

For example, a human may intentionally override an SEO recommendation for business reasons.

The system should preserve:

```text
AI Analytical Assessment
```

and:

```text
Human Strategic Decision
```

as separate layers.

This distinction is critical for future analysis.

---

# 80. Human Review and Strategic Exceptions

A human may intentionally choose an option that is not predicted to maximize a specific SEO metric.

Examples:

* prioritizing strategic products
* protecting brand positioning
* supporting a new market
* entering an emerging category
* simplifying site architecture
* avoiding operational complexity

The system should support explicit strategic exceptions.

---

# 81. Strategic Exception Object

Conceptual structure:

```yaml
strategic_exception:
  id:
  rule_or_recommendation:
  override:
  reason:
  authorized_by:
  evidence:
  created_at:
  expires_at:
```

Strategic exceptions should be reviewable and versioned.

---

# 82. Human Review and Business Priority

Business priority should influence recommendations before final decision.

Example:

```text
Topic A:
Search Demand = High
Business Value = Low

Topic B:
Search Demand = Medium
Business Value = Very High
```

The system should allow Topic B to receive higher strategic priority.

Search volume must not become an automatic decision function.

---

# 83. Human Review and Uncertainty

A human should be able to explicitly choose:

```text
Proceed despite uncertainty
```

or:

```text
Collect more evidence
```

or:

```text
Defer decision
```

This allows uncertainty to be managed rather than hidden.

---

# 84. Human Review Decision Options

Recommended decision types:

```text
APPROVE
REJECT
MODIFY
MERGE
SPLIT
DEFER
REQUEST_MORE_EVIDENCE
ESCALATE
OVERRIDE
CANCEL
```

Only relevant options should be shown for each review type.

---

# 85. Human Review Workflow Example

```text
Topic Discovery
      ↓
Topic Validation
      ↓
Topic Cluster
      ↓
AI Recommendation
      ↓
Confidence = 0.61
      ↓
Human Review
      ↓
Reviewer sees:
  - topic definitions
  - entities
  - intent
  - SERP evidence
  - business relevance
  - alternatives
      ↓
Human:
APPROVE
      ↓
Persist Decision
      ↓
Continue Workflow
```

---

# 86. Human Review Conflict Example

```text
Existing Decision:
Topic A and Topic B are separate.

New AI Analysis:
SERP overlap increased significantly.

System:
STRATEGIC_CONFLICT

Human:
Review new evidence.

Decision:
Remain separate because products serve different audiences.

System:
Update decision rationale.
Preserve both historical states.
```

---

# 87. Human Review Failure Modes

The system must protect against:

### Rubber-Stamping

Humans approve everything without reviewing evidence.

### Review Fatigue

Too many low-value review requests.

### Context Overload

Too much information makes review ineffective.

### Hidden Bias

AI recommendations are accepted without questioning assumptions.

### Decision Loss

Human decisions are not persisted.

### Conflicting Decisions

New workflows ignore existing strategic decisions.

### Approval Ambiguity

It is unclear what exactly was approved.

---

# 88. Preventing Rubber-Stamping

The system should highlight:

* uncertainty
* conflicts
* unusual recommendations
* important evidence
* strategic trade-offs

Review interfaces should not make approval easier than understanding.

---

# 89. Preventing Review Fatigue

The system should:

* batch repetitive decisions
* prioritize high-impact items
* suppress unnecessary reviews
* reuse trusted validated patterns
* use deterministic automation for low-risk tasks
* learn from repeated approvals

---

# 90. Approval Scope

Every approval must have explicit scope.

Example:

```text
Approved:
Page mapping for Topic A.

Not necessarily approved:
Entire topical map.
```

Approvals must not be interpreted more broadly than their declared scope.

---

# 91. Approval Expiration

Some approvals may require expiration based on:

* evidence freshness
* market changes
* SERP drift
* business changes
* architecture changes

Expiration should trigger revalidation where appropriate.

---

# 92. Human Review Notifications and Blocking

A workflow should clearly indicate:

```text
BLOCKED_BY_HUMAN_REVIEW
```

when progress cannot safely continue.

It should identify:

* blocked step
* required decision
* reason
* impact
* available evidence

---

# 93. Human Review and Workflow Resume

After review:

```text
Review Completed
      ↓
Decision Persisted
      ↓
Validation
      ↓
Workflow Resume
```

The workflow should not restart from the beginning.

---

# 94. Human Review and Versioned Artifacts

When a reviewer modifies an AI-generated artifact:

```text
AI Artifact v1
      ↓
Human Modification
      ↓
Approved Artifact v2
```

Both versions should remain traceable.

---

# 95. Human Review and Audit

An auditor should be able to reconstruct:

```text
What AI recommended
What evidence AI used
What human changed
Why human changed it
What final decision became authoritative
What workflow continued afterward
```

This is mandatory for important strategic decisions.

---

# 96. Human Review and Security

Human review must respect:

* user permissions
* workspace isolation
* project access
* sensitive data boundaries
* approval authority
* action permissions

A user who can view an artifact does not automatically have permission to approve it.

---

# 97. Human Review and Multi-User Projects

Future versions may support:

```text
Reviewer A → SEO validation
Reviewer B → Business approval
Reviewer C → Execution authorization
```

The workflow must support role-specific approval policies.

---

# 98. Multi-Approval Workflows

High-impact actions may require multiple approvals.

Example:

```text
AI Recommendation
      ↓
SEO Approval
      ↓
Business Approval
      ↓
Execution Authorization
```

Approval requirements must be explicit and configurable.

---

# 99. Separation of Duties

For sensitive actions, the person who proposes an action may be different from the person who approves it.

This reduces risks associated with:

* accidental changes
* unauthorized actions
* conflicts of interest
* uncontrolled automation

---

# 100. Human Review and Decision Engine

The Decision Engine should produce decision candidates.

Human review determines whether:

```text
Candidate
```

becomes:

```text
Approved Decision
```

unless an explicitly authorized automated policy applies.

---

# 101. Human Review and Living SEO Model

Human decisions become part of the living SEO intelligence system.

The persistent model should therefore contain:

```text
Business Knowledge
Entity Knowledge
Search Knowledge
Website Knowledge
AI Inferences
Recommendations
Human Decisions
Historical Decisions
Outcomes
Feedback
```

This allows the system to learn from actual strategic choices rather than only external search data.

---

# 102. Human Review and Outcome Feedback

After execution, the system should compare:

```text
Expected Outcome
vs
Actual Outcome
```

Examples:

* ranking changes
* traffic changes
* conversion changes
* page performance
* crawl behavior
* engagement
* business outcomes

This feedback should be connected to the original decision.

---

# 103. Decision-to-Outcome Chain

The complete chain should be:

```text
Evidence
 ↓
AI Analysis
 ↓
Recommendation
 ↓
Human Decision
 ↓
Authorized Action
 ↓
Observed Outcome
 ↓
Evaluation
 ↓
Future Learning
```

This is one of the most important foundations of the living system.

---

# 104. Human-in-the-Loop MVP

The MVP should support:

* human-defined objectives
* human review requests
* approve/reject/modify
* review comments
* evidence inspection
* confidence visibility
* human decision persistence
* workflow pause/resume
* approval gates
* strategic constraints
* decision history
* basic feedback capture

---

# 105. Future Human-in-the-Loop Capabilities

Future versions may add:

* multi-user approval chains
* advanced review queues
* delegated authority
* review prioritization
* adaptive automation
* policy-based approvals
* strategic exception management
* outcome-based feedback
* automated review recommendations
* organization-wide decision memory
* decision simulations

---

# 106. Non-Negotiable Human-in-the-Loop Rules

The following rules are mandatory:

1. Human strategic authority must remain explicit.
2. AI recommendation must remain distinct from human decision.
3. Human decisions must be persistent.
4. Human overrides must be auditable.
5. Human approvals must have explicit scope.
6. Approval authority must be permission-controlled.
7. Low confidence must remain visible.
8. Conflicting evidence must remain visible.
9. Missing strategic context must trigger human input when required.
10. High-impact actions must require appropriate authorization.
11. Irreversible actions must require explicit approval.
12. AI confidence must never be treated as human authority.
13. Human review must be a workflow state.
14. Human review must be resumable.
15. Review requests must be focused and actionable.
16. Review fatigue must be actively controlled.
17. AI outputs must not be silently overwritten by human edits.
18. Historical decisions must remain traceable.
19. Strategic exceptions must be explicit.
20. Human feedback must be structured where possible.
21. Human feedback must not automatically alter production behavior.
22. Human-approved knowledge must preserve provenance.
23. Existing approved decisions must not be silently overridden.
24. New evidence must surface conflicts with existing decisions.
25. Search metrics must not automatically determine strategic priority.
26. Business context must remain a first-class decision input.
27. Human authority must not be weakened as automation increases.
28. Every important decision must be auditable.
29. The system must optimize human decision quality rather than maximum autonomy.
30. No consequential action may be presented as approved unless the required approval actually exists.

---

# 107. Definition of Done

The Human-in-the-Loop architecture is considered implemented correctly when:

* human roles are defined
* strategic authority is explicit
* review states exist
* review objects are persisted
* review triggers exist
* confidence is visible
* evidence is inspectable
* AI recommendations are distinct from human decisions
* human overrides are persisted
* strategic constraints are persisted
* workflow pause/resume works
* approval scope is explicit
* authorization is enforced
* high-impact actions require approval
* decision history is versioned
* feedback is captured
* conflicts are surfaced
* stale decisions can be identified
* human decisions can be retrieved as context
* review metrics are available
* audit trails exist
* human feedback can enter evaluation pipelines
* no AI action can silently override human authority

---

# 108. Final Human-in-the-Loop Model

The intended operating model is:

```text
                    HUMAN
                      │
          ┌───────────┴───────────┐
          │                       │
     Strategy                  Constraints
          │                       │
          └───────────┬───────────┘
                      ▼
                 AI Research
                      ↓
                 AI Analysis
                      ↓
                Recommendation
                      ↓
          Evidence + Confidence
                      ↓
               Decision Engine
                      ↓
                Human Review
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
     Approve        Modify        Reject
        │             │             │
        └─────────────┼─────────────┘
                      ▼
              Persist Decision
                      ↓
             Authorized Action
                      ↓
                   Outcome
                      ↓
                 Evaluation
                      ↓
              Feedback / Learning
                      ↓
              Living SEO Model
```

The system is therefore designed as:

> **AI-augmented strategic decision making, not AI replacement of strategic judgment.**

---

# 109. Document Control

```yaml
document:
  id: "15"
  filename: "15_HUMAN_IN_THE_LOOP.md"
  status: "APPROVED_AS_BASELINE_HUMAN_IN_THE_LOOP"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

authority:
  strategic: "human"
  analytical: "ai_agents"
  orchestration: "central_orchestrator"
  decision_support: "seo_decision_engine"
  consequential_action: "authorized_human_or_policy"

core_states:
  - NOT_REQUIRED
  - PENDING
  - IN_REVIEW
  - APPROVED
  - REJECTED
  - MODIFICATION_REQUESTED
  - DEFERRED
  - ESCALATED
  - CANCELLED

epistemic_states:
  - OBSERVED
  - INFERRED
  - ESTIMATED
  - RECOMMENDED
  - HUMAN_APPROVED
  - CONFLICTED
  - UNKNOWN

core_review_actions:
  - APPROVE
  - REJECT
  - MODIFY
  - MERGE
  - SPLIT
  - DEFER
  - REQUEST_MORE_EVIDENCE
  - ESCALATE
  - OVERRIDE
  - CANCEL

mvp_autonomy:
  target: "level_0_to_level_2"

core_principles:
  - human_strategic_authority
  - evidence_first_review
  - explicit_approval
  - persistent_decisions
  - auditable_overrides
  - confidence_without_authority
  - risk_based_review
  - focused_context
  - structured_feedback
  - reversible_automation
  - no_silent_override

primary_dependencies:
  - "14_AGENT_WORKFLOW.md"
  - "16_OUTPUT_CONTRACTS.md"

related:
  - "03_MASTER_RULES.md"
  - "05_AI_AGENT_ARCHITECTURE.md"
  - "06_DATA_ARCHITECTURE.md"
  - "08_SEO_KNOWLEDGE_MODEL.md"
  - "09_ENTITY_EAV_MODEL.md"
  - "11_SEARCH_AND_SERP_INTELLIGENCE.md"
  - "12_SEO_DECISION_ENGINE.md"
  - "13_AGENT_SPECIFICATIONS.md"
  - "16_OUTPUT_CONTRACTS.md"
  - "22_TESTING_AND_VALIDATION.md"
  - "23_PROJECT_CONTROL_CENTER.md"
  - "25_CONTEXT_MANAGEMENT.md"
  - "26_SKILLS_AND_TOOLING_POLICY.md"
```
