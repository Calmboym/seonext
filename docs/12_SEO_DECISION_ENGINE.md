# 12 — SEO Decision Engine

**Document:** `12_SEO_DECISION_ENGINE.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Decision Intelligence Specification
**Status:** `APPROVED_AS_BASELINE_SEO_DECISION_ENGINE`
**Authority:** Baseline specification for transforming business, semantic, search, website, competitive, and historical evidence into explicit, explainable, prioritized SEO recommendations and decisions.

**Depends On:**

* `01_PRD.md`
* `02_PRODUCT_VISION.md`
* `03_MASTER_RULES.md`
* `04_SYSTEM_ARCHITECTURE.md`
* `05_AI_AGENT_ARCHITECTURE.md`
* `06_DATA_ARCHITECTURE.md`
* `08_SEO_KNOWLEDGE_MODEL.md`
* `09_ENTITY_EAV_MODEL.md`
* `10_TOPIC_MODELING_AND_CLUSTERING.md`
* `11_SEARCH_AND_SERP_INTELLIGENCE.md`

**Related To:**

* `13_AGENT_SPECIFICATIONS.md`
* `14_AGENT_WORKFLOW.md`
* `15_HUMAN_IN_THE_LOOP.md`
* `16_OUTPUT_CONTRACTS.md`
* `17_UI_UX_SPECIFICATION.md`
* `21_DEVELOPMENT_AND_DEBUG.md`
* `22_TESTING_AND_VALIDATION.md`
* `23_PROJECT_CONTROL_CENTER.md`
* `24_INDEX_ROADMAP_TASKS_DEPENDENCIES.md`
* `25_CONTEXT_MANAGEMENT.md`
* `26_SKILLS_AND_TOOLING_POLICY.md`

---

# 1. Purpose

The SEO Decision Engine is the decision-intelligence layer of the product.

Its responsibility is to transform accumulated evidence and analysis into:

* explicit strategic options
* prioritized opportunities
* recommended actions
* confidence assessments
* identified constraints
* identified risks
* evidence-backed decisions
* human-review requests
* decision history
* measurable outcomes

The Decision Engine exists because SEO research alone does not produce strategy.

The system may know:

* what entities exist
* what attributes they have
* what topics are relevant
* what users search for
* what search intent appears dominant
* what SERPs contain
* what competitors rank
* what pages already exist
* where content gaps exist
* where cannibalization may exist
* what internal links exist
* what business objectives matter

But knowing these things is different from deciding what should happen next.

The Decision Engine provides that missing layer.

---

# 2. Core Principle

The fundamental operating model is:

```text
Business Reality
        +
Semantic Knowledge
        +
Search Reality
        +
Website Reality
        +
Competitive Reality
        +
Historical Performance
        +
Human Constraints
        ↓
Evidence
        ↓
Analysis
        ↓
Candidate Options
        ↓
Scoring & Constraint Evaluation
        ↓
Recommendation
        ↓
Human Review
        ↓
Decision
        ↓
Action
        ↓
Outcome
        ↓
Learning
```

The central principle is:

> **Search intelligence provides evidence. The Decision Engine transforms evidence into explicit, explainable strategic options and recommendations. Human authority approves strategic decisions.**

The Decision Engine must never become an opaque system that silently converts uncertain signals into irreversible strategic actions.

---

# 3. What the Decision Engine Is

The Decision Engine is a structured reasoning and prioritization system that evaluates possible SEO actions against:

* business objectives
* semantic relevance
* search demand
* search intent
* SERP characteristics
* competition
* current website coverage
* topical authority considerations
* entity importance
* conversion potential
* implementation effort
* strategic fit
* risk
* evidence quality
* confidence
* temporal considerations
* explicit human constraints

It produces recommendations that can be inspected, challenged, modified, approved, rejected, or deferred.

---

# 4. What the Decision Engine Is Not

The Decision Engine is **not**:

* a keyword generator
* a keyword-volume sorting table
* a ranking predictor
* a black-box SEO oracle
* an autonomous publisher
* a replacement for business strategy
* a replacement for human judgment
* an automatic content factory
* a system that treats search volume as demand
* a system that assumes every topic requires a page
* a system that automatically creates pages from clusters
* a system that automatically merges pages based on one similarity signal
* a system that automatically redirects URLs
* a system that silently changes strategic policy
* a system that fabricates missing evidence

The engine makes reasoning explicit.

---

# 5. Decision Intelligence Model

The Decision Engine operates across five conceptual levels:

```text
Observation
    ↓
Analysis
    ↓
Recommendation
    ↓
Decision
    ↓
Outcome
```

These levels must never be conflated.

## 5.1 Observation

An observation is something directly supported by available evidence.

Example:

```text
Three analyzed queries show substantial SERP overlap.
```

This does not automatically mean the pages should be merged.

---

## 5.2 Analysis

Analysis interprets observations.

Example:

```text
The queries appear to represent closely related search intents and
currently produce highly overlapping result sets.
```

Analysis may contain inference and therefore requires appropriate confidence and provenance.

---

## 5.3 Recommendation

A recommendation proposes an action.

Example:

```text
Consider consolidating the two existing pages into a single stronger page.
```

A recommendation is not yet an approved strategic decision.

---

## 5.4 Decision

A decision is an explicitly accepted strategic choice.

Example:

```text
Approved:
Consolidate /guide-a and /guide-b into /guide.
```

Decisions require an authority context.

---

## 5.5 Outcome

An outcome records what happened after execution.

Example:

```text
After consolidation:
- organic clicks changed by X
- impressions changed by Y
- ranking distribution changed by Z
```

Outcomes become future evidence.

---

# 6. Decision Lifecycle

Every material decision should follow this lifecycle:

```text
1. Evidence Collection
2. Evidence Validation
3. Analysis
4. Candidate Generation
5. Candidate Comparison
6. Scoring
7. Constraint Evaluation
8. Risk Evaluation
9. Recommendation
10. Human Review
11. Approval / Rejection / Deferral
12. Action
13. Outcome Measurement
14. Post-Decision Evaluation
15. Learning
```

Not every decision requires every stage to have the same depth.

For example:

* adding an internal link may require lightweight evaluation
* merging major pages may require extensive evidence
* restructuring an entire topical map requires strategic review

The system must scale decision depth according to decision impact.

---

# 7. Decision Types

The Decision Engine should support a controlled vocabulary of decision types.

## 7.1 Topic Decisions

Examples:

* pursue topic
* deprioritize topic
* monitor topic
* investigate topic
* expand topic
* narrow topic
* merge topic concepts
* split topic concepts

---

## 7.2 Page Decisions

Examples:

* create page
* update page
* expand page
* narrow page
* merge pages
* split page
* consolidate pages
* redirect page
* preserve page
* deprecate page
* monitor page

---

## 7.3 Internal Linking Decisions

Examples:

* add internal link
* remove internal link
* strengthen contextual link
* change anchor strategy
* connect related entities
* create hub-to-detail relationship
* create supporting-to-primary relationship

---

## 7.4 Content Decisions

Examples:

* create content
* update content
* refresh content
* expand missing coverage
* remove obsolete content
* restructure content
* improve intent alignment
* change content format

---

## 7.5 Topical Map Decisions

Examples:

* add topic cluster
* remove topic cluster
* merge clusters
* split cluster
* change parent-child relationship
* change supporting-topic relationship
* revise topical priority

---

## 7.6 Competitive Decisions

Examples:

* investigate competitor
* monitor competitor
* analyze competitor page
* identify competitor gap
* evaluate competitor strategy
* revise opportunity priority based on competitive evidence

---

## 7.7 Strategic Decisions

Examples:

* prioritize commercial topic
* prioritize informational topic
* allocate research resources
* allocate content resources
* defer an opportunity
* change strategic emphasis
* investigate a business/search mismatch

Strategic decisions require stronger human involvement.

---

# 8. Decision Object

Every material decision should have a structured representation.

Conceptually:

```yaml
decision:
  id: DEC-001
  project_id: PROJECT-001
  type: CREATE_PAGE

  target:
    type: TOPIC
    id: TOPIC-123

  question:
    text: "Should this topic receive a dedicated page?"

  context:
    business_goal: "Increase qualified organic acquisition"
    market: "..."
    language: "..."
    country: "..."

  evidence:
    - evidence_id: EVIDENCE-001
    - evidence_id: EVIDENCE-002

  analysis:
    summary: "..."
    findings:
      - "..."
      - "..."

  options:
    - option_id: OPTION-A
      action: CREATE_PAGE
    - option_id: OPTION-B
      action: MERGE_WITH_EXISTING_PAGE
    - option_id: OPTION-C
      action: DEPRIORITIZE

  scores:
    opportunity: 0.82
    priority: 0.76
    confidence: 0.88

  constraints:
    - "..."

  risks:
    - "..."

  recommendation:
    action: CREATE_PAGE
    rationale: "..."

  approval:
    status: PENDING

  outcome:
    status: NOT_EXECUTED
```

This is a conceptual model. The implementation schema must be defined consistently with `06_DATA_ARCHITECTURE.md` and `16_OUTPUT_CONTRACTS.md`.

---

# 9. Evidence Requirements

No material recommendation should exist without traceable evidence.

Evidence may originate from:

* business research
* entity data
* EAV facts
* topic analysis
* query research
* search metrics
* SERP observations
* competitor analysis
* website crawling
* existing page data
* analytics
* historical performance
* internal-link analysis
* human-provided constraints
* previous decisions
* previous outcomes

Every evidence item should preserve:

* source
* timestamp
* provenance
* scope
* confidence
* epistemic state
* relevant entity/topic/page
* collection method
* provider where applicable
* version where applicable

---

# 10. Evidence Graph

Decision reasoning should be represented as a traceable relationship:

```text
Evidence
   ↓
Claim
   ↓
Analysis
   ↓
Candidate Option
   ↓
Score
   ↓
Recommendation
   ↓
Decision
   ↓
Action
   ↓
Outcome
```

This allows the system to answer:

* Why was this recommended?
* Which evidence supports it?
* Which assumptions were used?
* Which scores influenced the recommendation?
* What alternatives were considered?
* Who approved the decision?
* When was it approved?
* What happened afterward?
* Was the recommendation successful?

---

# 11. Epistemic States

The Decision Engine must preserve epistemic distinctions.

Supported states include:

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

### Observed

```text
The page currently ranks for 17 tracked queries.
```

### Inferred

```text
The query group appears to share a dominant informational intent.
```

### Estimated

```text
Estimated opportunity based on incomplete demand data.
```

### Recommended

```text
Create a dedicated page.
```

### Human Approved

```text
The recommendation was explicitly approved.
```

### Conflicted

```text
Search evidence favors consolidation while business requirements
favor maintaining separate pages.
```

### Unknown

```text
Insufficient evidence to determine whether a separate page is justified.
```

The engine must never silently convert `UNKNOWN` into `RECOMMENDED`.

---

# 12. Business Reality as a Decision Constraint

SEO decisions must be grounded in business reality.

Relevant business inputs may include:

* business model
* products
* services
* revenue model
* margins
* customer segments
* target markets
* strategic priorities
* commercial priorities
* conversion paths
* product availability
* geographic availability
* regulatory constraints
* operational capacity
* brand positioning

A topic can have strong search demand and still be strategically irrelevant.

Therefore:

```text
Search Opportunity ≠ Business Priority
```

The Decision Engine must preserve this distinction.

---

# 13. Search Reality as Evidence

Search intelligence contributes evidence such as:

* query demand
* trend
* SERP composition
* intent
* result overlap
* ranking competition
* page types
* content formats
* SERP features
* volatility
* localization
* device context
* temporal patterns

Search signals should inform decisions rather than dictate them.

For example:

```text
High volume
+
Low business relevance
=
Potentially low priority
```

Similarly:

```text
Low volume
+
Very high business value
+
Strong conversion intent
=
Potentially high priority
```

---

# 14. Website Reality

The engine must account for what already exists.

Relevant website signals include:

* existing URLs
* page topics
* page intent
* content quality
* rankings
* impressions
* clicks
* conversions
* backlinks
* internal links
* duplicate coverage
* outdated content
* thin coverage
* topical relationships
* historical performance

The system must never treat a proposed page as independent from the existing information architecture.

---

# 15. Competitive Reality

Competitive analysis should consider:

* competing domains
* competing pages
* SERP competitors
* topic coverage
* entity coverage
* content formats
* search intent alignment
* page quality signals
* topical depth
* historical changes

The system must distinguish:

```text
Business Competitor
```

from:

```text
Search Competitor
```

A site can compete in SERPs without being a direct business competitor.

---

# 16. Decision Dimensions

A recommendation may be evaluated across multiple dimensions.

Core dimensions:

1. Business Relevance
2. Strategic Fit
3. Search Demand
4. Intent Fit
5. SERP Opportunity
6. Competition
7. Existing Coverage
8. Topical Importance
9. Entity Importance
10. Conversion Potential
11. Expected Impact
12. Effort
13. Cost
14. Risk
15. Confidence
16. Data Quality
17. Time Sensitivity
18. Dependency Impact

Not every decision needs every dimension.

The applicable dimensions depend on the decision type.

---

# 17. Hard Constraints vs Soft Signals

The Decision Engine must distinguish between:

## Hard Constraints

Conditions that can invalidate an option.

Examples:

```text
Product is not available in target market.
```

```text
Business does not provide the service.
```

```text
Required page type violates an explicit business constraint.
```

```text
Human explicitly prohibits this action.
```

## Soft Signals

Signals that influence prioritization.

Examples:

* search volume
* competition estimate
* topical centrality
* SERP similarity
* estimated traffic
* content effort
* conversion potential

Hard constraints must not be treated as ordinary weighted signals.

An option violating a hard constraint should normally be:

```text
INELIGIBLE
```

rather than merely receiving a lower score.

---

# 18. Scoring Framework

The engine may use normalized scoring to compare candidates.

Conceptually:

```text
Opportunity Score
=
f(
  business relevance,
  search opportunity,
  intent fit,
  SERP opportunity,
  topical importance,
  conversion potential,
  competitive conditions
)
```

Priority may additionally incorporate:

```text
Priority Score
=
f(
  opportunity,
  expected impact,
  effort,
  risk,
  strategic timing,
  dependencies
)
```

Confidence is separate:

```text
Confidence
=
f(
  evidence quality,
  evidence quantity,
  evidence agreement,
  data freshness,
  model uncertainty,
  provider reliability
)
```

The system must not collapse all three concepts into one number.

Therefore:

```text
Opportunity ≠ Priority ≠ Confidence
```

---

# 19. Opportunity Score

Opportunity answers:

> "How attractive does this SEO opportunity appear based on available evidence?"

Possible dimensions:

* business relevance
* search opportunity
* intent alignment
* SERP opportunity
* conversion potential
* competitive environment
* topical importance

Opportunity does not determine execution priority by itself.

---

# 20. Priority Score

Priority answers:

> "Given the opportunities available, what should we consider doing first?"

Priority may account for:

* expected impact
* effort
* cost
* risk
* strategic importance
* dependencies
* timing
* available resources
* existing commitments

A lower-volume opportunity can therefore outrank a higher-volume opportunity.

---

# 21. Confidence Score

Confidence answers:

> "How strongly does the available evidence support this conclusion?"

Confidence should consider:

* evidence quality
* source reliability
* evidence consistency
* freshness
* data completeness
* ambiguity
* model uncertainty
* provider limitations

A high opportunity with low confidence should not automatically become a high-priority action.

Example:

```text
Opportunity: 0.91
Priority:    0.74
Confidence:  0.43
```

This should trigger additional research or human review rather than automatic execution.

---

# 22. Uncertainty

The Decision Engine must explicitly represent uncertainty.

Possible reasons:

* insufficient SERP data
* incomplete keyword data
* conflicting providers
* ambiguous intent
* unclear business value
* insufficient competitor coverage
* stale data
* rapidly changing SERP
* incomplete website crawl
* unresolved entity identity

The correct response to uncertainty may be:

```text
INVESTIGATE
```

rather than:

```text
CREATE PAGE
```

---

# 23. Candidate Options

The engine should not assume that the first generated action is the only action.

For a page-cannibalization problem, options might be:

```text
A. Merge pages
B. Differentiate intent
C. Split topic
D. Preserve both
E. Redirect one page
F. Monitor
```

Candidate generation should occur before recommendation selection when the decision is material.

---

# 24. Option Comparison

Each candidate should be evaluated consistently.

Conceptual structure:

| Dimension       | Option A | Option B | Option C |
| --------------- | -------: | -------: | -------: |
| Business Fit    |     High |     High |   Medium |
| Search Fit      |     High |   Medium |     High |
| Expected Impact |     High |   Medium |   Medium |
| Effort          |   Medium |      Low |     High |
| Risk            |   Medium |      Low |     High |
| Confidence      |     High |     High |   Medium |

The UI should make the comparison understandable without exposing private reasoning traces.

---

# 25. Counterfactual Reasoning

For significant decisions, the system should support controlled counterfactual analysis.

Example:

```text
If we create a new page:
- expected coverage increases
- possible cannibalization risk increases
- implementation effort increases

If we update the existing page:
- lower implementation effort
- preserves existing authority
- may limit intent separation

If we defer:
- no immediate implementation cost
- opportunity may remain unaddressed
```

Counterfactuals are decision aids, not predictions with guaranteed outcomes.

---

# 26. Decision Policies

The engine should support explicit policies.

Examples:

```text
Do not create a new page when a sufficiently aligned existing page
already serves the same dominant intent unless there is evidence
supporting differentiation.
```

```text
Do not recommend redirects solely because two pages have similar
keywords.
```

```text
Do not prioritize topics solely by search volume.
```

```text
Do not execute irreversible URL changes without human approval.
```

Policies must be:

* explicit
* versioned
* testable
* auditable
* reviewable

---

# 27. Deterministic Logic vs AI Reasoning

The Decision Engine should use deterministic computation wherever possible.

## Deterministic Responsibilities

Examples:

* score normalization
* arithmetic
* threshold checks
* eligibility rules
* hard constraints
* dependency checks
* ranking of candidates
* data validation
* freshness checks
* confidence aggregation rules

## AI-Assisted Responsibilities

Examples:

* semantic interpretation
* ambiguous intent analysis
* synthesis of evidence
* candidate generation
* explanation drafting
* conflict interpretation
* contextual comparison
* hypothesis generation

AI should not be responsible for calculations that can be implemented deterministically.

---

# 28. LLM Boundary

LLMs may assist with:

* interpretation
* classification
* semantic comparison
* evidence synthesis
* natural-language explanation
* candidate generation
* uncertainty detection

LLMs should not silently determine:

* hard constraint validity
* final numerical calculations
* authorization
* irreversible actions
* security permissions
* human approval state

The architecture should make the distinction explicit.

---

# 29. Human Authority

Human users retain authority over:

* business priorities
* strategic direction
* brand constraints
* commercial priorities
* market selection
* major information architecture changes
* high-risk URL changes
* redirects
* consolidation
* major content removal
* execution approval

The system may recommend.

The system may rank.

The system may explain.

The system may automate low-risk actions where explicitly authorized.

But strategic authority remains human-controlled.

---

# 30. Human Review Levels

Decision impact can determine review requirements.

Conceptually:

```text
LOW IMPACT
↓
Automatable / optional review

MEDIUM IMPACT
↓
Human review recommended

HIGH IMPACT
↓
Human approval required

IRREVERSIBLE / HIGH RISK
↓
Explicit human approval required
```

Examples of high-impact decisions:

* deleting content
* redirecting URLs
* merging important pages
* changing core architecture
* changing major topical strategy
* changing strategic market focus

---

# 31. Decision Status

Decision lifecycle states may include:

```text
DRAFT
ANALYZING
READY_FOR_REVIEW
PENDING_APPROVAL
APPROVED
REJECTED
DEFERRED
EXECUTING
EXECUTED
MEASURED
REVERSED
SUPERSEDED
CANCELLED
```

The exact implementation state machine must remain consistent with the workflow architecture.

---

# 32. Recommendation Status vs Decision Status

These must remain separate.

Example:

```text
Recommendation:
CREATE_PAGE

Recommendation Status:
READY_FOR_REVIEW

Decision:
PENDING

Human Action:
NOT_YET_REVIEWED
```

The presence of a recommendation must never imply approval.

---

# 33. Decision Explainability

Every material recommendation should answer:

### What?

What action is recommended?

### Why?

Which evidence supports it?

### Compared With What?

What alternatives were considered?

### Why Not the Alternatives?

What factors made them less attractive?

### How Certain?

How strong is the evidence?

### What Could Change the Decision?

Which conditions would invalidate or alter the recommendation?

### What Happens Next?

What action is proposed?

---

# 34. Explanation Structure

A user-facing explanation should conceptually look like:

```text
Recommendation
Create a dedicated page for Topic X.

Why
- Strong business relevance
- Distinct search intent
- Limited existing coverage
- SERP evidence supports a dedicated page type

Risks
- Moderate implementation effort
- Competitive SERP

Confidence
High

Alternatives
- Expand existing page
- Defer

Decision Required
Human approval
```

The system should expose evidence and decision factors, not private chain-of-thought.

---

# 35. Conflict Resolution

Conflicting evidence must be represented explicitly.

Examples:

```text
Search evidence:
Strong demand

Business evidence:
Low commercial relevance
```

or:

```text
SERP evidence:
Separate intent

Existing website:
Strongly overlapping pages
```

The engine should not silently choose one source.

Instead:

```text
Conflict Detected
↓
Identify conflicting evidence
↓
Assess source reliability
↓
Determine whether conflict is resolvable
↓
Recommend investigation or human review
```

---

# 36. Source Reliability

Evidence sources may have different reliability.

The system should consider:

* source type
* directness
* freshness
* measurement quality
* provider reliability
* scope
* known limitations

Source reliability should influence confidence, not automatically determine strategic importance.

---

# 37. Temporal Decisions

SEO decisions exist within time.

The engine should consider:

* current state
* historical state
* trends
* seasonality
* SERP changes
* competitor changes
* business changes
* content changes
* previous decision outcomes

A decision should therefore be associated with:

```text
Decision Time
Evidence Time
Execution Time
Measurement Time
```

---

# 38. Decision Versioning

Decisions should be immutable historical records wherever practical.

Instead of silently editing:

```text
Decision v1
```

into:

```text
Decision v2
```

the system should preserve the relationship:

```text
v1 → superseded by → v2
```

This preserves strategic history.

---

# 39. Decision History

The system should allow users to inspect:

* previous decisions
* rejected recommendations
* deferred opportunities
* approved actions
* execution status
* measured outcomes
* decision reversals
* superseded decisions
* human feedback

This transforms the product from a stateless assistant into a living decision system.

---

# 40. Outcome Measurement

After execution, the system should attempt to measure relevant outcomes.

Possible outcomes:

* ranking changes
* impressions
* clicks
* CTR
* conversions
* organic revenue
* visibility
* indexed pages
* traffic distribution
* internal-link changes
* cannibalization changes
* content performance
* business outcomes

The system must distinguish:

```text
Observed Outcome
```

from:

```text
Causal Attribution
```

A change after an SEO action does not automatically prove the action caused it.

---

# 41. Learning Loop

The Decision Engine should learn from outcomes and human feedback.

Conceptual loop:

```text
Recommendation
      ↓
Human Decision
      ↓
Execution
      ↓
Outcome
      ↓
Evaluation
      ↓
Feedback
      ↓
Future Recommendations
```

Human feedback may include:

* approved
* rejected
* modified
* deferred
* reason
* business constraint
* strategic preference

This feedback can improve future recommendations.

---

# 42. No Silent Policy Learning

Human decisions must not silently change the global strategy.

For example:

If a user rejects one recommendation to create a page, the system must not automatically infer:

```text
Never recommend new pages.
```

Instead it may learn:

```text
For this project/context, similar page-creation recommendations
may require stronger evidence.
```

Any persistent policy change should be:

* explicit
* reviewable
* versioned
* attributable

---

# 43. Topic Decisions

Topic decisions should combine:

```text
Business Relevance
+
Entity Importance
+
Search Reality
+
Intent
+
SERP Opportunity
+
Existing Coverage
+
Strategic Fit
```

A topic should not become a page merely because it exists in the topic universe.

Possible outcomes:

```text
PURSUE
DEFER
INVESTIGATE
MONITOR
MERGE
SPLIT
DEPRIORITIZE
```

---

# 44. Page Creation Decisions

A page-creation recommendation should evaluate:

* topic validity
* search demand
* search intent
* SERP page-type evidence
* existing page coverage
* entity coverage
* business relevance
* conversion potential
* cannibalization risk
* expected impact
* effort
* strategic priority

A strong recommendation should establish why a **new page** is preferable to:

```text
Updating an existing page
```

or:

```text
Expanding an existing page
```

or:

```text
Merging with an existing page
```

---

# 45. Page Consolidation Decisions

Consolidation decisions require stronger evidence.

Possible signals:

* strong SERP overlap
* similar dominant intent
* overlapping entities
* overlapping topic scope
* duplicate or near-duplicate purpose
* weak differentiation
* competing URLs for similar searches

But:

```text
Similarity ≠ Automatic Consolidation
```

The engine must also evaluate:

* business purpose
* conversion differences
* audience differences
* geographic differences
* product differences
* historical performance
* backlink value
* existing rankings
* content differentiation

---

# 46. Page Split Decisions

A page may be a candidate for splitting when evidence indicates:

* multiple distinct intents
* distinct audiences
* distinct entities
* distinct products
* distinct search contexts
* different page types
* strong SERP separation
* excessive scope

Again:

```text
Semantic breadth ≠ automatic split
```

The business and search context must support the decision.

---

# 47. Content Update Decisions

Update recommendations should consider:

* outdated information
* changed search intent
* SERP changes
* declining performance
* missing entities
* missing attributes
* content gaps
* competitor changes
* business changes
* factual inaccuracies

The engine should distinguish:

```text
Refresh
```

from:

```text
Major Rewrite
```

and:

```text
Strategic Repositioning
```

---

# 48. Internal Linking Decisions

Internal-link recommendations should consider:

* topical relationship
* entity relationship
* parent-child relationships
* user journey
* page importance
* crawlability
* contextual relevance
* anchor semantics
* existing link structure
* redundancy

The engine should not recommend links solely because two pages share keywords.

---

# 49. Cannibalization Decisions

Cannibalization analysis should combine:

* query overlap
* SERP overlap
* intent overlap
* page-type overlap
* topic overlap
* entity overlap
* ranking patterns
* temporal ranking behavior
* business purpose

Possible decisions:

```text
NO_ACTION
MONITOR
DIFFERENTIATE
UPDATE
MERGE
REDIRECT
SPLIT
```

Automatic consolidation must not be triggered by one metric.

---

# 50. Content Gap Decisions

A content gap should become a decision candidate only after considering:

* business relevance
* search demand
* intent
* SERP opportunity
* competitor coverage
* existing website coverage
* entity/EAV coverage
* strategic importance
* effort
* expected impact

Possible outcomes:

```text
CREATE
UPDATE
EXPAND
DEFER
IGNORE
INVESTIGATE
```

---

# 51. Competitor Decisions

Competitor intelligence should answer questions such as:

* Which competitor gaps matter?
* Which competitor pages represent relevant search opportunities?
* Which topics are strategically important?
* Is the competitor advantage structural, content-based, or search-context-specific?
* Is imitation strategically appropriate?

The system must not assume:

```text
Competitor ranks → we should copy competitor.
```

Competitor evidence informs strategy; it does not define strategy.

---

# 52. Decision Dependencies

Some decisions depend on other decisions.

Example:

```text
Entity Validation
      ↓
Topic Validation
      ↓
Intent Validation
      ↓
Page Candidate
      ↓
Page Architecture
      ↓
Internal Linking
```

A recommendation should not be finalized if required upstream information is unresolved.

The Decision Engine should surface:

```text
BLOCKED_BY
DEPENDS_ON
CONFLICTS_WITH
SUPERSEDES
SUPPORTED_BY
RESULTED_IN
```

---

# 53. Decision Readiness

A candidate should be considered decision-ready only when minimum required evidence exists.

Conceptually:

```yaml
decision_readiness:
  evidence_complete: true
  required_dimensions_available: true
  hard_constraints_checked: true
  conflicts_resolved: true
  confidence_threshold_met: true
  human_review_required: true
```

Readiness thresholds should vary by decision type.

---

# 54. Low-Confidence Recommendations

A low-confidence recommendation should not necessarily disappear.

It may become:

```text
INVESTIGATE
```

or:

```text
MONITOR
```

or:

```text
REQUEST_MORE_DATA
```

This is preferable to producing false certainty.

---

# 55. Insufficient Data

The engine must explicitly support:

```text
INSUFFICIENT_DATA
```

Example:

```text
The system cannot determine whether a dedicated page is justified
because SERP evidence is unavailable for the relevant market.
```

The correct next action may be:

```text
Collect SERP data.
```

This is a valid system outcome.

---

# 56. Decision Confidence vs Recommendation Strength

These concepts should remain separate.

Example:

```text
Recommendation Strength: HIGH
Confidence: LOW
```

This means:

```text
If the current assumptions are correct, the action appears highly
valuable, but evidence quality is insufficient.
```

The UI should communicate this clearly.

---

# 57. Decision Engine and Orchestrator

The Central Orchestrator controls workflow execution.

The Decision Engine provides decision intelligence.

The relationship is:

```text
Orchestrator
    ↓
Requests analysis
    ↓
Agents / Services
    ↓
Produce evidence and analysis
    ↓
Decision Engine
    ↓
Evaluates candidate actions
    ↓
Produces recommendations
    ↓
Human Review
    ↓
Orchestrator executes approved workflow
```

The Decision Engine should not become a second uncontrolled orchestrator.

---

# 58. Decision Engine and Agents

Agents should provide specialized analysis.

Examples:

```text
Entity Agent
→ Entity evidence

Topic Agent
→ Topic evidence

Intent Agent
→ Intent evidence

SERP Agent
→ Search evidence

Competitor Agent
→ Competitive evidence

Page Analysis Agent
→ Website evidence
```

The Decision Engine synthesizes these inputs.

Agents should not bypass the Decision Engine to make independent strategic decisions.

---

# 59. Decision Engine and Knowledge Layer

The Decision Engine reads from the shared knowledge layer.

It may query:

* entities
* EAV facts
* topics
* keywords
* intents
* search contexts
* SERPs
* pages
* competitors
* evidence
* previous decisions
* outcomes

It may produce:

* claims
* recommendations
* decisions
* decision relationships
* outcome records

The knowledge layer remains the durable source of truth.

---

# 60. Decision Engine and Topical Maps

The Decision Engine should determine whether topic candidates justify inclusion in a topical map.

It may evaluate:

```text
Topic Validity
+
Business Relevance
+
Search Opportunity
+
Entity Importance
+
Intent
+
Competitive Landscape
```

The resulting recommendation may be:

```text
ADD_TO_MAP
REMOVE_FROM_MAP
MERGE
SPLIT
DEFER
MONITOR
```

The Topical Map is therefore an output of strategic reasoning, not simply a visualization of discovered keywords.

---

# 61. Decision Engine and Page Architecture

Page architecture decisions should follow from validated topic and search relationships.

The engine should help determine:

```text
Topic
   ↓
Page Candidate
   ↓
Page Type
   ↓
URL Concept
   ↓
Hierarchy
   ↓
Relationship
```

The Decision Engine should not directly generate arbitrary URLs without the appropriate architectural context.

---

# 62. Decision Engine and Information Architecture

Information Architecture is broader than individual SEO recommendations.

Therefore the Decision Engine may recommend IA changes, but major structural changes require human approval.

Example:

```text
Recommendation:
Create a dedicated product category layer.

Decision:
Pending human approval.
```

---

# 63. Search-to-Business Alignment

One of the most important functions of the Decision Engine is identifying mismatches between:

```text
What users search for
```

and:

```text
What the business should pursue
```

Examples:

```text
High search demand
+
Low business value
→ Deprioritize
```

```text
Low search demand
+
High business value
→ Investigate / prioritize selectively
```

```text
Strong search demand
+
Strong business value
+
Strong intent alignment
→ High opportunity
```

---

# 64. Decision Matrix

A conceptual prioritization matrix may be:

| Business Value | Search Opportunity | Typical Interpretation                                          |
| -------------- | ------------------ | --------------------------------------------------------------- |
| High           | High               | Strong candidate                                                |
| High           | Low                | Strategic opportunity / investigate                             |
| Low            | High               | Potential traffic opportunity, usually lower strategic priority |
| Low            | Low                | Usually deprioritize                                            |

This matrix is only a reasoning aid.

It must not replace contextual evaluation.

---

# 65. Effort and Impact

Priority should consider implementation economics.

A simple conceptual model:

```text
Priority
≈
Expected Impact
÷
Effort
```

But this should not be treated as a universal formula.

Risk, dependencies, strategic timing, and confidence can materially alter priority.

---

# 66. Risk Model

Decision risk may include:

* traffic loss
* ranking loss
* conversion loss
* business misalignment
* implementation complexity
* irreversible changes
* technical dependency
* data uncertainty
* incorrect intent interpretation
* incorrect entity resolution
* incorrect consolidation
* stale search evidence

High-risk recommendations require stronger evidence and stronger human control.

---

# 67. Reversible vs Irreversible Decisions

The engine should classify actions by reversibility.

### Reversible

Examples:

* add internal link
* update title
* refresh content
* add supporting section

### Partially Reversible

Examples:

* restructure content
* change page targeting
* modify information architecture

### Irreversible / High Risk

Examples:

* delete page
* permanent redirect
* large-scale consolidation
* destructive content removal

Irreversible actions require stronger safeguards.

---

# 68. Decision Automation Levels

Possible automation levels:

```text
LEVEL 0
Analysis only

LEVEL 1
Recommendation generation

LEVEL 2
Recommendation + human approval

LEVEL 3
Low-risk execution under explicit policy

LEVEL 4
Conditional automation

LEVEL 5
Highly autonomous execution
```

The MVP should remain primarily within:

```text
LEVEL 0–2
```

with carefully bounded Level 3 capabilities only where justified.

---

# 69. No Autonomous Strategic Execution by Default

The system must not:

* delete content
* redirect URLs
* restructure major IA
* publish content
* alter strategic priorities
* modify business assumptions

without appropriate authorization.

---

# 70. Auditability

Every decision should be auditable.

Audit data should include:

* decision ID
* project ID
* decision type
* evidence IDs
* analysis version
* scoring version
* policy version
* model/version where relevant
* recommendation
* human reviewer
* approval status
* timestamps
* execution status
* outcome
* supersession history

---

# 71. Observability

The system should record:

* decision latency
* candidate count
* evidence retrieval latency
* model usage
* token/cost metrics
* scoring failures
* validation failures
* rejected recommendations
* human overrides
* confidence distributions
* decision outcomes

This enables evaluation of the Decision Engine itself.

---

# 72. Cost and Latency Control

Decision evaluation should avoid unnecessary LLM calls.

Preferred sequence:

```text
Cheap deterministic filters
        ↓
Evidence retrieval
        ↓
Deterministic scoring
        ↓
LLM reasoning only where required
        ↓
Validation
```

Examples:

* hard constraints should be deterministic
* numerical scoring should be deterministic
* database filtering should happen before semantic synthesis
* expensive reasoning should be reserved for ambiguous or material decisions

---

# 73. Caching

Reusable decision inputs may be cached when freshness requirements allow.

Examples:

* topic scores
* entity importance
* SERP similarity
* intent classifications
* competitor observations

Cache invalidation must account for:

* new evidence
* changed business settings
* changed search context
* changed model version
* changed scoring policy

---

# 74. Versioning

The Decision Engine should version:

* decision rules
* scoring formulas
* thresholds
* prompts
* model versions
* output schemas
* policies
* recommendation logic

A historical decision should remain interpretable using the versions under which it was produced.

---

# 75. Reproducibility

Where practical, the system should be able to reconstruct:

```text
What evidence was available?
What rules were active?
What model was used?
What scoring configuration was used?
What recommendation was produced?
What human decision followed?
```

Perfect deterministic reproduction of every LLM output is not required, but decision provenance must be sufficient for audit and analysis.

---

# 76. Security

The Decision Engine must enforce:

* project isolation
* workspace isolation
* authorization
* role-based access
* evidence access controls
* decision access controls
* audit logging
* secret isolation
* provider credential isolation

A user must never be able to retrieve or influence another project's decision context without authorization.

---

# 77. Prompt and Tool Safety

AI-assisted decision reasoning must not blindly trust:

* retrieved documents
* web content
* competitor content
* page content
* tool outputs
* external provider responses

External content may contain:

* malicious instructions
* irrelevant text
* prompt injection
* misleading claims

External content is evidence, not authority.

---

# 78. Failure Modes

The Decision Engine must explicitly handle:

### Missing Evidence

```text
REQUEST_MORE_DATA
```

### Conflicting Evidence

```text
CONFLICTED
```

### Low Confidence

```text
INVESTIGATE
```

### Provider Failure

```text
DEGRADED_ANALYSIS
```

### Invalid Input

```text
VALIDATION_ERROR
```

### Policy Conflict

```text
HUMAN_REVIEW_REQUIRED
```

### Constraint Violation

```text
INELIGIBLE
```

### Model Failure

```text
FALLBACK / RETRY / ESCALATE
```

The system must not fabricate a decision merely to complete a workflow.

---

# 79. Graceful Degradation

If some evidence sources are unavailable, the system may produce a limited recommendation only when the remaining evidence is sufficient.

Example:

```text
SERP provider unavailable.

Available:
- business evidence
- entity model
- website data
- historical analytics

Result:
Preliminary recommendation only.
SERP validation required before final approval.
```

---

# 80. Decision Quality Evaluation

The Decision Engine should be evaluated on more than recommendation acceptance.

Metrics may include:

* recommendation accuracy
* human acceptance rate
* human modification rate
* human rejection rate
* outcome quality
* calibration of confidence
* false-positive rate
* false-negative rate
* decision latency
* evidence completeness
* explanation usefulness
* policy compliance
* regression rate

Human acceptance alone is not sufficient to establish quality.

---

# 81. Human Override

Humans may override recommendations.

An override should optionally capture:

```text
Original Recommendation
Override Action
Reason
Business Context
Reviewer
Timestamp
```

This feedback can become future evidence.

---

# 82. Decision Learning

Learning may occur at several levels:

### Project Level

```text
Project-specific preferences and constraints
```

### Workspace Level

```text
Shared strategic patterns
```

### Product Level

```text
General decision-quality improvements
```

These levels must remain isolated.

A project-specific decision must not automatically become a global product rule.

---

# 83. Decision Memory

The system should retrieve relevant historical decisions when evaluating new decisions.

Example:

```text
New topic candidate
      ↓
Retrieve similar historical decisions
      ↓
Compare evidence and outcomes
      ↓
Use as contextual evidence
```

Historical decisions are evidence, not unquestionable rules.

---

# 84. Similar Decision Retrieval

Relevant historical decisions may be retrieved by:

* decision type
* topic
* entity
* intent
* page type
* business goal
* market
* search context
* evidence pattern
* previous outcome

Semantic retrieval may assist, but structured filters remain important.

---

# 85. Decision Contradictions

The engine should detect contradictions such as:

```text
Previous decision:
Preserve separate pages.

New recommendation:
Merge pages.

```

This is not necessarily an error.

The engine should determine whether:

* evidence changed
* business strategy changed
* search reality changed
* previous decision was superseded
* context differs

If context is materially different, both decisions may remain valid.

---

# 86. Decision Supersession

When a new decision replaces an old one:

```text
DEC-001
    ↓
SUPERSEDED_BY
    ↓
DEC-014
```

The historical record should remain intact.

---

# 87. Decision Scope

Every decision should have explicit scope.

Examples:

```text
Project
Market
Country
Language
Device
Topic
Entity
Page
Query Set
Website
```

A decision made for one market should not automatically propagate to another.

---

# 88. Multilingual Decisions

For multilingual projects, decisions must account for:

* language
* market
* localized intent
* localized SERP
* local entities
* cultural differences
* local business availability

A topic relationship in one language does not automatically imply identical search behavior in another.

---

# 89. Geographic Decisions

Location may materially change:

* demand
* intent
* SERP
* competitors
* business availability
* conversion potential

Therefore decision context must preserve geographic scope.

---

# 90. Decision Context

A decision should carry enough context to remain interpretable.

Minimum context may include:

```text
Project
Market
Language
Country
Decision Type
Target Object
Evaluation Time
Evidence Snapshot
Policy Version
```

---

# 91. Decision Evidence Freshness

Some decisions require fresh evidence.

Examples:

* SERP volatility
* competitor monitoring
* seasonal topics
* rapidly changing products

The engine should define freshness requirements by decision type.

Example:

```text
URL consolidation:
historical + current evidence

SERP opportunity:
recent SERP evidence

Seasonal campaign:
time-sensitive search evidence
```

---

# 92. Decision Thresholds

Thresholds should be configurable.

Examples:

```text
minimum confidence
minimum opportunity
maximum risk
maximum effort
required SERP coverage
required evidence count
```

Thresholds must be versioned and auditable.

---

# 93. Avoiding False Precision

Scores should not imply mathematical certainty.

For example:

```text
Opportunity = 0.8137
```

does not mean the opportunity is objectively measurable to four decimal places.

The UI should communicate meaningful precision.

Possible representation:

```text
High
Medium
Low
```

with numeric values available where useful.

---

# 94. Recommendation Rationale

Rationale should focus on decision-relevant factors.

Good:

```text
The existing page already satisfies the dominant intent and has
strong historical performance. A new page would create substantial
overlap with limited additional business value.
```

Bad:

```text
The model internally considered 27 factors and generated latent
reasoning...
```

The product should expose evidence and concise decision factors rather than private chain-of-thought.

---

# 95. Decision Summary

Every material recommendation should have a concise summary:

```text
Action:
Create dedicated page

Target:
Topic X

Priority:
High

Confidence:
Medium

Primary Reasons:
- Strong business relevance
- Distinct intent
- Existing coverage is weak

Primary Risk:
SERP competition

Human Approval:
Required
```

---

# 96. Decision Engine Output Contract

A decision result should conceptually contain:

```yaml
decision_result:
  decision_type: CREATE_PAGE
  target:
    type: TOPIC
    id: TOPIC-123

  recommendation:
    action: CREATE_PAGE
    priority: HIGH

  scores:
    opportunity: 0.84
    priority: 0.78
    confidence: 0.71

  evidence:
    supporting: []
    conflicting: []

  constraints:
    satisfied: []
    violated: []

  risks: []

  alternatives: []

  explanation:
    summary: "..."

  review:
    required: true

  status:
    recommendation: READY_FOR_REVIEW
    decision: PENDING
```

The authoritative implementation contract belongs in:

```text
16_OUTPUT_CONTRACTS.md
```

---

# 97. Batch Decision Evaluation

The engine must support evaluating multiple candidates.

Example:

```text
100 topic candidates
      ↓
Eligibility filtering
      ↓
Evidence enrichment
      ↓
Opportunity scoring
      ↓
Priority scoring
      ↓
Confidence evaluation
      ↓
Human-review shortlist
```

This prevents humans from manually inspecting every low-value candidate.

---

# 98. Candidate Filtering

Filtering should happen before expensive reasoning.

Example:

```text
1000 topics
↓
200 fail hard constraints
↓
500 have insufficient evidence
↓
300 eligible candidates
↓
100 high-opportunity candidates
↓
30 high-priority candidates
↓
10 requiring human review
```

This is both a quality and cost-control mechanism.

---

# 99. Decision Queue

The system should maintain a decision queue containing:

* pending decisions
* priority
* confidence
* risk
* required reviewer
* dependencies
* freshness
* evidence completeness

The queue becomes an operational interface for human strategy.

---

# 100. Decision Prioritization

Decision queues should prioritize not only by opportunity.

Possible priority ordering:

```text
High Impact
+
High Confidence
+
Low/Moderate Risk
+
Actionable
```

Uncertain but potentially high-value opportunities may be routed to:

```text
Research Queue
```

rather than:

```text
Execution Queue
```

---

# 101. Research vs Decision Queues

The system should distinguish:

```text
Need More Knowledge
```

from:

```text
Ready to Decide
```

Example:

```text
Topic X
→ High potential
→ Low confidence
→ Research Queue
```

versus:

```text
Topic Y
→ High potential
→ High confidence
→ Decision Queue
```

---

# 102. Strategic Recommendation Categories

Recommendations may be categorized as:

```text
PURSUE
OPTIMIZE
CONSOLIDATE
EXPAND
DIFFERENTIATE
DEPRIORITIZE
MONITOR
INVESTIGATE
PROTECT
REMOVE
```

These categories should map to explicit actions.

---

# 103. Protect Decisions

Some decisions are about preserving valuable assets.

Examples:

* protect high-performing page
* preserve ranking-critical page
* avoid unnecessary consolidation
* preserve important internal-link relationships
* protect strategic content

The engine must optimize for avoiding harmful changes, not merely generating new actions.

---

# 104. Do-Nothing as a Decision

The engine must support:

```text
NO_ACTION
```

This is important.

If evidence does not justify intervention, the recommendation may be:

```text
No action required at this time.
Monitor for change.
```

A system that always recommends an action creates artificial work.

---

# 105. Monitor Decisions

Monitoring is appropriate when:

* evidence is insufficient
* trend is uncertain
* volatility is high
* opportunity is emerging
* business context may change
* a previous action requires observation

Monitoring should define:

```text
What to monitor
When to reassess
What threshold triggers reevaluation
```

---

# 106. Trigger-Based Reassessment

Decisions may be reopened when triggers occur.

Examples:

```text
SERP intent changes significantly
```

```text
Ranking falls below threshold
```

```text
Competitor enters SERP
```

```text
Business product changes
```

```text
Search demand changes materially
```

```text
New entity or attribute discovered
```

This supports the Living SEO Intelligence System vision.

---

# 107. Decision Drift

The system should detect when the evidence underlying an existing decision changes materially.

Example:

```text
Original decision:
Create informational guide.

Current state:
SERP is now dominated by transactional pages.

Result:
Decision Drift Detected.
```

The system should recommend reevaluation rather than silently changing the decision.

---

# 108. Decision Health

A decision may have a health state based on:

* evidence freshness
* business alignment
* search alignment
* outcome performance
* unresolved conflicts

Example:

```text
HEALTHY
STALE
AT_RISK
CONFLICTED
SUPERSEDED
UNKNOWN
```

---

# 109. Living Decision Model

The long-term system should maintain:

```text
Current Knowledge
+
Historical Knowledge
+
Current Decisions
+
Historical Decisions
+
Outcomes
+
Feedback
```

This transforms the system into a continuously updated strategic model.

---

# 110. Decision Graph

Decisions should be connected to the broader knowledge graph.

Example:

```text
Business Goal
      ↓
Entity
      ↓
Topic
      ↓
Query
      ↓
Intent
      ↓
SERP
      ↓
Page
      ↓
Recommendation
      ↓
Decision
      ↓
Action
      ↓
Outcome
```

This graph enables future reasoning across the entire SEO system.

---

# 111. Decision Provenance

Every recommendation should preserve:

```text
Source Evidence
      ↓
Derived Claim
      ↓
Analysis
      ↓
Scoring
      ↓
Recommendation
```

Provenance should be machine-readable.

---

# 112. Recommendation Provenance Example

```yaml
recommendation:
  action: MERGE_PAGES

  supported_by:
    - evidence_id: SERP-123
    - evidence_id: INTENT-456
    - evidence_id: PAGE-789

  conflicting_evidence:
    - evidence_id: BUSINESS-222

  confidence:
    value: 0.68
    reasons:
      - "Strong SERP overlap"
      - "Intent overlap"
      - "Business distinction remains unresolved"
```

This makes uncertainty visible.

---

# 113. Decision Safety Rules

The engine must:

1. Never fabricate evidence.
2. Never hide conflicts.
3. Never treat recommendations as approvals.
4. Never treat search volume as sufficient strategy.
5. Never automatically perform irreversible actions without authorization.
6. Never silently change policies.
7. Never confuse confidence with opportunity.
8. Never confuse topic similarity with page equivalence.
9. Never use one signal as universal proof.
10. Never claim causality from correlation alone.

---

# 114. Testing Strategy

The Decision Engine requires multiple testing layers.

## Unit Tests

Test:

* scoring
* normalization
* thresholds
* constraint evaluation
* confidence calculations
* state transitions

## Integration Tests

Test:

* knowledge retrieval
* evidence retrieval
* database persistence
* decision creation
* workflow integration

## AI Evaluation

Test:

* candidate generation
* semantic interpretation
* intent synthesis
* explanation quality
* uncertainty recognition
* conflict recognition

## Scenario Tests

Test scenarios such as:

* high demand / low business value
* low demand / high business value
* high opportunity / low confidence
* strong SERP overlap / different business purposes
* conflicting evidence
* missing SERP data
* stale data
* competitor change
* existing high-performing page

---

# 115. Regression Testing

Previously validated decisions should become regression cases.

If a change to:

* scoring
* prompt
* model
* policy
* retrieval
* data schema

causes materially different recommendations, the system should identify the change.

Strategic behavior must not change silently.

---

# 116. Calibration

Confidence should be evaluated against outcomes.

If recommendations with:

```text
Confidence = High
```

frequently prove unreliable, the confidence system is poorly calibrated.

Calibration should therefore be measured over time.

---

# 117. Explainability Testing

Explanations should be tested for:

* evidence support
* factual accuracy
* completeness
* consistency
* absence of fabricated claims
* usefulness to human reviewers

An explanation must not cite evidence that does not actually support the stated conclusion.

---

# 118. Human Review Testing

Test whether reviewers can correctly determine:

* what is being recommended
* why
* based on what evidence
* how confident the system is
* what risks exist
* what decision is required

The interface should not obscure these distinctions.

---

# 119. Decision Failure Handling

If decision evaluation fails:

```text
Detect
↓
Classify
↓
Preserve available evidence
↓
Retry if safe
↓
Fallback if available
↓
Escalate if required
↓
Record failure
```

A failed decision should not be represented as a successful recommendation.

---

# 120. MVP Scope

The MVP Decision Engine should support:

### Core Inputs

* business context
* entities
* topics
* queries
* intents
* SERPs
* existing pages
* competitors
* evidence

### Core Decision Types

* pursue topic
* create page
* update page
* merge pages
* differentiate pages
* internal link
* content gap
* cannibalization
* deprioritize
* monitor

### Core Outputs

* recommendation
* opportunity score
* priority score
* confidence
* evidence
* risks
* alternatives
* human-review status

### Core Controls

* hard constraints
* deterministic scoring
* human approval
* decision history
* provenance
* auditability

---

# 121. MVP Non-Goals

The MVP should not attempt:

* fully autonomous SEO execution
* automatic large-scale redirects
* automatic destructive content operations
* fully autonomous strategic planning
* unrestricted agent autonomy
* black-box reinforcement learning
* universal SEO ranking prediction
* guaranteed outcome prediction

---

# 122. Future Capabilities

Future versions may support:

* adaptive decision policies
* advanced causal analysis
* decision simulation
* multi-objective optimization
* resource allocation optimization
* automated monitoring triggers
* advanced anomaly detection
* strategy scenario planning
* portfolio-level SEO optimization
* continuous competitive intelligence
* decision outcome prediction
* richer knowledge-graph reasoning
* controlled autonomous execution

These capabilities require evidence that the architecture can support them safely.

---

# 123. Anti-Patterns

The following are prohibited:

## Keyword-Volume Decision Making

```text
Highest volume → highest priority
```

## One-Signal Consolidation

```text
High SERP similarity → automatic merge
```

## LLM-Only Decisions

```text
Prompt → answer → execute
```

## Hidden Scoring

```text
AI says 92/100 without explanation
```

## False Precision

```text
Score 0.873421 → interpreted as objective truth
```

## Recommendation-as-Approval

```text
AI recommendation → automatic strategic execution
```

## Silent Learning

```text
One rejection → permanent global rule
```

## Historical Erasure

```text
Update decision → delete old decision
```

## Evidence-Free Recommendation

```text
No evidence → confident recommendation
```

## Strategy by Competitor Copying

```text
Competitor ranks → copy competitor
```

---

# 124. Decision Engine Quality Gates

A material recommendation should pass:

```text
[ ] Correct target identified
[ ] Decision type valid
[ ] Required evidence available
[ ] Evidence provenance preserved
[ ] Hard constraints evaluated
[ ] Relevant dimensions evaluated
[ ] Opportunity separated from priority
[ ] Confidence evaluated independently
[ ] Conflicts identified
[ ] Risks identified
[ ] Alternatives considered where appropriate
[ ] Recommendation explicit
[ ] Human approval requirement determined
[ ] Output contract validated
[ ] Audit metadata recorded
```

---

# 125. Definition of Done

The Decision Engine is considered implemented only when:

### Architecture

* [ ] Decision Engine boundary is explicit.
* [ ] Orchestrator relationship is implemented.
* [ ] Agent boundaries are respected.
* [ ] Knowledge-layer integration is defined.

### Data

* [ ] Decision objects have stable IDs.
* [ ] Evidence references are persisted.
* [ ] Decision history is preserved.
* [ ] Decision status is modeled.
* [ ] Outcome relationships are supported.

### Intelligence

* [ ] Candidate options can be generated.
* [ ] Hard constraints are enforced.
* [ ] Scoring is deterministic where appropriate.
* [ ] Confidence is separate from priority.
* [ ] Uncertainty is represented.
* [ ] Conflicts are represented.

### Human Control

* [ ] Recommendations are separate from decisions.
* [ ] Human approval states exist.
* [ ] High-risk decisions require appropriate approval.
* [ ] Overrides are recorded.

### Explainability

* [ ] Recommendations identify supporting evidence.
* [ ] Risks are visible.
* [ ] Alternatives are available where required.
* [ ] Explanations do not expose private chain-of-thought.

### Reliability

* [ ] Missing data is handled.
* [ ] Provider failures are handled.
* [ ] Model failures are handled.
* [ ] Invalid outputs are rejected.
* [ ] No-fabrication rules are enforced.

### Testing

* [ ] Unit tests exist.
* [ ] Integration tests exist.
* [ ] Decision scenarios are covered.
* [ ] AI evaluation exists.
* [ ] Regression cases exist.
* [ ] Confidence calibration can be evaluated.

### Auditability

* [ ] Evidence provenance is preserved.
* [ ] Policy version is recorded.
* [ ] Scoring version is recorded.
* [ ] Model/version metadata is recorded where relevant.
* [ ] Human decisions are attributable.
* [ ] Historical decisions remain inspectable.

---

# 126. Final Decision Model

The Decision Engine can be summarized as:

```text
                BUSINESS REALITY
                       │
                       ▼
                SEMANTIC KNOWLEDGE
                       │
                       ▼
                 SEARCH REALITY
                       │
                       ▼
                WEBSITE REALITY
                       │
                       ▼
              COMPETITIVE REALITY
                       │
                       ▼
                 HISTORICAL DATA
                       │
                       ▼
                    EVIDENCE
                       │
                       ▼
                   ANALYSIS
                       │
                       ▼
               CANDIDATE OPTIONS
                       │
                       ▼
              CONSTRAINT CHECK
                       │
                       ▼
                 SCORING
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     OPPORTUNITY    PRIORITY    CONFIDENCE
          └────────────┼────────────┘
                       ▼
                    RISKS
                       │
                       ▼
                 RECOMMENDATION
                       │
                       ▼
                 HUMAN REVIEW
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       APPROVE       REJECT       DEFER
          │
          ▼
        ACTION
          │
          ▼
       OUTCOME
          │
          ▼
       FEEDBACK
          │
          ▼
        LEARNING
```

---

# 127. Non-Negotiable Principles

1. **Evidence precedes recommendation.**
2. **Recommendation is not decision.**
3. **Decision is not execution.**
4. **Human authority controls strategic decisions.**
5. **Opportunity, priority, and confidence are separate concepts.**
6. **Search volume is a signal, not a strategy.**
7. **Hard constraints are not ordinary scoring factors.**
8. **Uncertainty must be represented explicitly.**
9. **Conflicting evidence must not be hidden.**
10. **Every material recommendation must be traceable to evidence.**
11. **Deterministic logic should be used where deterministic logic is sufficient.**
12. **LLMs assist reasoning but do not become uncontrolled strategic authorities.**
13. **Irreversible actions require stronger controls.**
14. **Historical decisions must remain auditable.**
15. **Human feedback may inform learning but must not silently alter global policy.**
16. **No-action is a valid decision.**
17. **Monitor is a valid decision.**
18. **Insufficient data is a valid system outcome.**
19. **Competitor behavior informs strategy but does not define strategy.**
20. **The Decision Engine must optimize for decision quality, not recommendation volume.**

---

# 128. Relationship to the Overall System

The Decision Engine occupies the strategic center of the SEO intelligence pipeline:

```text
Business Research
      ↓
Entity Model
      ↓
EAV
      ↓
Topic Universe
      ↓
Topic Validation
      ↓
Intent
      ↓
SERP Intelligence
      ↓
Topic Clustering
      ↓
Website / Competitor Analysis
      ↓
─────────────────────────────
      SEO DECISION ENGINE
─────────────────────────────
      ↓
Strategic Recommendations
      ↓
Human Validation
      ↓
Topical Map
      ↓
Page Architecture
      ↓
Internal Linking
      ↓
Content / Execution
      ↓
Performance
      ↓
Outcome
      ↓
Living Knowledge Model
```

The Decision Engine is therefore not an isolated feature.

It is the layer that converts the system's accumulated intelligence into explicit strategic choices.

---

# 129. Final Architectural Statement

The SEO Decision Engine exists to answer:

> **Given what we know about the business, entities, topics, search behavior, SERPs, competitors, website, historical performance, constraints, and uncertainty, what should we consider doing, why, with what confidence, at what priority, and what decision remains for the human to make?**

Its output is not simply:

```text
"Create this page."
```

Its output is:

```text
Recommended Action
+
Evidence
+
Decision Factors
+
Alternatives
+
Opportunity
+
Priority
+
Confidence
+
Risks
+
Constraints
+
Human Approval Requirement
+
Decision History
+
Outcome Tracking
```

That is the foundation required for the product to evolve from an SEO research assistant into a genuine **SEO Decision Engine** and ultimately a **Living SEO Intelligence System**.

---

# 130. Document Control

```yaml
document:
  id: "12"
  filename: "12_SEO_DECISION_ENGINE.md"
  title: "SEO Decision Engine"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

status: "APPROVED_AS_BASELINE_SEO_DECISION_ENGINE"

purpose:
  - "Transform evidence into explicit SEO recommendations and decisions"
  - "Prioritize SEO opportunities"
  - "Preserve uncertainty and conflicts"
  - "Provide explainable decision intelligence"
  - "Support human strategic authority"
  - "Track decisions and outcomes over time"

core_objects:
  - "Evidence"
  - "Claim"
  - "Analysis"
  - "Candidate Option"
  - "Recommendation"
  - "Decision"
  - "Action"
  - "Outcome"
  - "Feedback"

core_scores:
  - "Opportunity"
  - "Priority"
  - "Confidence"

core_states:
  - "DRAFT"
  - "ANALYZING"
  - "READY_FOR_REVIEW"
  - "PENDING_APPROVAL"
  - "APPROVED"
  - "REJECTED"
  - "DEFERRED"
  - "EXECUTING"
  - "EXECUTED"
  - "MEASURED"
  - "REVERSED"
  - "SUPERSEDED"
  - "CANCELLED"

human_authority:
  strategic_decisions: true
  irreversible_actions: "explicit_approval_required"

architecture_role:
  position: "decision_intelligence_layer"
  controller: "central_orchestrator"
  inputs: "shared_knowledge_and_evidence"
  outputs: "recommendations_decisions_outcomes"

next_dependencies:
  - "13_AGENT_SPECIFICATIONS.md"
  - "14_AGENT_WORKFLOW.md"
  - "15_HUMAN_IN_THE_LOOP.md"
  - "16_OUTPUT_CONTRACTS.md"
```
