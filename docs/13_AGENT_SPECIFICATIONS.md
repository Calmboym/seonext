# 13 — Agent Specifications

**Document:** `13_AGENT_SPECIFICATIONS.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** AI Agent Specification
**Status:** `APPROVED_AS_BASELINE_AGENT_SPECIFICATIONS`
**Authority:** Baseline specification for defining the responsibilities, boundaries, inputs, outputs, tools, reasoning modes, validation requirements, and operating contracts of AI agents and AI-powered modules.

**Depends On:**

* `03_MASTER_RULES.md`
* `04_SYSTEM_ARCHITECTURE.md`
* `05_AI_AGENT_ARCHITECTURE.md`
* `06_DATA_ARCHITECTURE.md`
* `08_SEO_KNOWLEDGE_MODEL.md`
* `09_ENTITY_EAV_MODEL.md`
* `10_TOPIC_MODELING_AND_CLUSTERING.md`
* `11_SEARCH_AND_SERP_INTELLIGENCE.md`
* `12_SEO_DECISION_ENGINE.md`

**Related To:**

* `14_AGENT_WORKFLOW.md`
* `15_HUMAN_IN_THE_LOOP.md`
* `16_OUTPUT_CONTRACTS.md`
* `21_DEVELOPMENT_AND_DEBUG.md`
* `22_TESTING_AND_VALIDATION.md`
* `25_CONTEXT_MANAGEMENT.md`
* `26_SKILLS_AND_TOOLING_POLICY.md`

---

# 1. Purpose

This document defines the specifications for the AI agents and AI-powered intelligence modules used by the SEO Research & Strategy Copilot.

It establishes:

* what each agent is responsible for
* what each agent is not responsible for
* what inputs each agent requires
* what outputs each agent produces
* which tools an agent may use
* what evidence an agent must preserve
* when deterministic logic should be used
* when LLM reasoning may be used
* how confidence and uncertainty are represented
* how outputs are validated
* how agents interact with the Central Orchestrator
* how agents interact with the shared knowledge layer
* how human authority is preserved
* how agent versions and behavior are controlled

This document defines **agent capabilities and boundaries**.

It does not define the complete execution sequence.

The execution sequence belongs to:

```text
14_AGENT_WORKFLOW.md
```

---

# 2. Core Architecture

The system uses:

```text
Central Orchestrator
        ↓
Specialized AI Agents / Intelligence Modules
        ↓
Tools + External Providers
        ↓
Shared Knowledge Layer
        ↓
Validated Structured Outputs
        ↓
Decision Engine
        ↓
Human Review
```

The architecture explicitly rejects:

```text
Agent A ↔ Agent B ↔ Agent C ↔ Agent D
```

as the default communication model.

Agents should not form uncontrolled autonomous conversations.

Instead:

```text
Agent
  ↓
Structured Output
  ↓
Orchestrator
  ↓
Next Agent / Module
```

---

# 3. Agent Definition

An agent is a bounded AI capability that performs a defined class of reasoning or analysis within the product.

An agent may:

* retrieve information
* analyze information
* classify information
* extract structured knowledge
* generate candidate hypotheses
* compare alternatives
* identify relationships
* identify uncertainty
* produce recommendations within its defined scope

An agent must operate within:

* explicit input contracts
* explicit output contracts
* explicit tool permissions
* explicit knowledge boundaries
* explicit authorization boundaries

---

# 4. Agent vs Workflow

An agent performs a capability.

A workflow coordinates capabilities.

For example:

```text
Topic Validation Agent
```

answers:

> Is this topic sufficiently valid based on the available evidence?

A workflow answers:

> What sequence of research and validation steps should happen before this topic becomes a page candidate?

Therefore:

```text
Agent = Capability
Workflow = Coordination
Orchestrator = Control
```

---

# 5. Agent vs Decision Engine

Agents produce analysis.

The Decision Engine transforms analysis and evidence into strategic recommendations.

Therefore:

```text
Agent
→ "The evidence indicates X."

Decision Engine
→ "Given X, Y, and Z, option A is the strongest recommendation."

Human
→ "Approve / reject / modify / defer."
```

Agents must not bypass the Decision Engine for strategic decisions unless a specific workflow explicitly defines a narrow deterministic action.

---

# 6. Agent Taxonomy

The initial system should contain the following primary intelligence capabilities:

1. Business Research Agent
2. Entity Agent
3. EAV Agent
4. Topic Discovery Agent
5. Topic Validation Agent
6. Intent Agent
7. SERP Intelligence Agent
8. Topic Clustering Agent
9. Page Candidate / Page Mapping Agent
10. Page Architecture Agent
11. Internal Linking Agent
12. Content Gap Agent
13. Cannibalization Agent
14. Competitor Intelligence Agent
15. Decision Support Agent
16. Context Retrieval / Context Assembly Capability
17. Research Quality / Evidence Validation Capability

Not every capability must be implemented as an independent runtime service.

The implementation may use:

```text
Agent
AI Service
Deterministic Module
Pipeline Stage
```

depending on complexity and measured requirements.

---

# 7. General Agent Contract

Every agent should conceptually implement:

```yaml
agent:
  id: "agent.id"
  name: "Agent Name"
  version: "1.0.0"

  purpose: "..."

  inputs: []
  context_requirements: []

  capabilities: []

  tools:
    allowed: []
    forbidden: []

  output_contract: "..."

  evidence_requirements:
    required: true

  confidence:
    required: true

  human_review:
    required: false

  failure_policy:
    retry: true
    fallback: null
    escalate: true
```

The authoritative machine-readable contracts belong to:

```text
16_OUTPUT_CONTRACTS.md
```

---

# 8. Common Agent Lifecycle

An agent execution should conceptually follow:

```text
Receive Task
    ↓
Validate Input
    ↓
Load Required Context
    ↓
Check Permissions
    ↓
Retrieve Evidence
    ↓
Perform Deterministic Processing
    ↓
Perform AI Reasoning if Required
    ↓
Generate Structured Output
    ↓
Validate Output
    ↓
Assign Confidence / Epistemic State
    ↓
Attach Provenance
    ↓
Return Result
```

An agent must not skip validation merely because an LLM produced structured JSON.

---

# 9. Agent Input Principles

Agents should receive only the context required for their task.

Avoid:

```text
Entire project database
+
Entire chat history
+
All previous agent outputs
```

when unnecessary.

Prefer:

```text
Task
+
Relevant entities
+
Relevant evidence
+
Relevant history
+
Required constraints
```

This reduces:

* context cost
* latency
* irrelevant reasoning
* accidental information leakage
* prompt complexity
* model confusion

This requirement is closely connected to:

```text
25_CONTEXT_MANAGEMENT.md
```

---

# 10. Agent Output Principles

Agent outputs must be:

* structured
* explicit
* provenance-aware
* confidence-aware
* versioned
* machine-readable where consumed by another module
* human-readable where exposed to users

An agent must not return only free-form prose when downstream processing depends on its output.

---

# 11. Epistemic States

Agent outputs should distinguish:

```text
OBSERVED
INFERRED
ESTIMATED
RECOMMENDED
HUMAN_APPROVED
CONFLICTED
UNKNOWN
```

For example:

```yaml
finding:
  statement: "Query X appears informational."
  state: "INFERRED"
  confidence: 0.84
```

---

# 12. Evidence Provenance

Every meaningful agent finding should preserve:

* evidence IDs
* source
* timestamp
* retrieval method
* relevant scope
* provider
* model version where applicable
* transformation stage
* confidence
* epistemic state

Agents must not detach conclusions from their supporting evidence.

---

# 13. Agent Tool Permissions

Each agent should have explicit tool permissions.

Example:

```yaml
tools:
  allowed:
    - search_provider
    - serp_provider
    - knowledge_query

  forbidden:
    - publish_content
    - delete_page
    - redirect_url
```

Tool access must follow least privilege.

An agent should not receive a tool merely because the tool exists.

---

# 14. Business Research Agent

## 14.1 Purpose

Understand the business context required for SEO strategy.

## 14.2 Responsibilities

The agent may research and structure:

* business model
* products
* services
* target markets
* audiences
* customer problems
* commercial priorities
* value propositions
* conversion paths
* business terminology
* business constraints
* strategic objectives

## 14.3 Inputs

Possible inputs:

* business description
* website
* user-provided information
* business documents
* public sources
* existing knowledge model

## 14.4 Outputs

Possible outputs:

```text
Business Model
Business Entities
Products
Services
Markets
Audiences
Goals
Constraints
Terminology
Business Claims
Evidence
```

## 14.5 Boundaries

It must not decide:

* final SEO priorities
* final topical map
* final page architecture
* final content strategy

It provides business evidence.

---

# 15. Entity Agent

## 15.1 Purpose

Discover, identify, normalize, resolve, and enrich entities.

## 15.2 Responsibilities

The Entity Agent may:

* discover entities
* classify entities
* normalize names
* identify aliases
* resolve duplicates
* detect ambiguity
* identify external identifiers
* identify relationships
* enrich entity descriptions
* identify entity importance

## 15.3 Inputs

* business research
* website content
* external research
* existing entities
* topic data
* search data

## 15.4 Outputs

```text
Entity
Entity Type
Aliases
External IDs
Relationships
Entity Evidence
Confidence
Resolution Status
```

## 15.5 Boundaries

It must not:

* invent entity relationships
* merge ambiguous entities without sufficient evidence
* treat a keyword as automatically representing an entity
* make strategic page decisions

---

# 16. EAV Agent

## 16.1 Purpose

Extract and structure entity-attribute-value knowledge.

## 16.2 Responsibilities

The EAV Agent may identify:

* attributes
* values
* entity references
* measurements
* ranges
* temporal values
* relationships
* missing attributes
* conflicting values

## 16.3 Example

Input:

```text
Product X has a battery capacity of 5,000 mAh.
```

Output:

```yaml
entity: Product X
attribute: battery_capacity
value:
  type: measurement
  amount: 5000
  unit: mAh
state: OBSERVED
```

## 16.4 Boundaries

The agent must not:

* invent missing attributes
* assume all textual adjectives are formal attributes
* overwrite conflicting facts without provenance

---

# 17. Topic Discovery Agent

## 17.1 Purpose

Discover candidate topics from semantic, business, search, and contextual evidence.

## 17.2 Responsibilities

It may identify topics from:

* entities
* attributes
* user needs
* search queries
* competitor coverage
* website content
* business products
* services
* search suggestions
* related concepts

## 17.3 Outputs

Each candidate should contain:

* topic ID
* topic label
* description
* supporting entities
* supporting evidence
* related queries
* related attributes
* source
* confidence

## 17.4 Boundary

Topic discovery does not mean:

```text
Topic discovered → Page should be created
```

Page decisions belong downstream.

---

# 18. Topic Validation Agent

## 18.1 Purpose

Determine whether a candidate topic is sufficiently coherent and relevant to enter the validated topic universe.

## 18.2 Evaluation Dimensions

Possible dimensions:

* semantic coherence
* business relevance
* entity relevance
* search relevance
* intent coherence
* distinctiveness
* evidence strength
* strategic relevance

## 18.3 Outputs

Possible states:

```text
VALID
WEAK
AMBIGUOUS
DUPLICATE
MERGE_CANDIDATE
INVALID
INSUFFICIENT_DATA
```

## 18.4 Boundary

It does not determine final page architecture.

---

# 19. Intent Agent

## 19.1 Purpose

Infer and classify search intent.

## 19.2 Responsibilities

It may evaluate:

* query intent
* dominant intent
* mixed intent
* intent distribution
* page-type intent
* content-format intent
* commercial intent
* informational intent
* navigational intent
* transactional intent
* contextual intent

The product should support multidimensional intent rather than forcing every query into one simplistic category.

## 19.3 Inputs

* query
* SERP
* search context
* entities
* topic
* historical intent

## 19.4 Outputs

```yaml
intent:
  primary: informational
  secondary:
    - commercial
  confidence: 0.86
  evidence: []
```

## 19.5 Boundary

Intent classification is evidence.

It does not independently determine page creation.

---

# 20. SERP Intelligence Agent

## 20.1 Purpose

Acquire, normalize, classify, and interpret search-result intelligence.

## 20.2 Responsibilities

It may:

* request SERP data
* normalize SERP results
* identify SERP features
* classify result types
* classify page types
* classify content formats
* infer intent signals
* calculate SERP similarity
* identify search competitors
* detect volatility
* compare historical SERPs

## 20.3 Inputs

* query
* search context
* market
* language
* device
* date/time

## 20.4 Outputs

```text
SERP Snapshot
SERP Features
Result Classification
Page Types
Intent Signals
Competitors
Similarity
Volatility
Evidence
Confidence
```

## 20.5 Boundary

It does not decide:

```text
SERP similarity → merge pages
```

It supplies evidence for that decision.

---

# 21. Topic Clustering Agent

## 21.1 Purpose

Group semantically or behaviorally related topics, queries, or page candidates.

## 21.2 Signals

Possible signals:

* semantic similarity
* entity overlap
* attribute overlap
* intent similarity
* SERP similarity
* query relationships
* page-type similarity
* business relationship

## 21.3 Outputs

```text
Cluster
Members
Cluster Label
Cluster Type
Similarity Evidence
Confidence
Outliers
```

## 21.4 Boundary

Clustering is not automatically page mapping.

A cluster may contain:

```text
Multiple Pages
One Page
No Page Yet
```

---

# 22. Page Candidate Agent

## 22.1 Purpose

Evaluate whether a validated topic or topic cluster represents a plausible page candidate.

## 22.2 Responsibilities

It may compare:

* new page
* existing page update
* existing page expansion
* merge
* split
* differentiation
* no action

## 22.3 Inputs

* topic
* cluster
* intent
* SERP
* existing pages
* business relevance
* entity model
* content coverage

## 22.4 Outputs

```text
Page Candidate
Candidate Type
Target Topic
Expected Purpose
Existing Page Relationships
Evidence
Confidence
```

## 22.5 Boundary

It produces candidate analysis.

Final strategic prioritization belongs to the Decision Engine.

---

# 23. Page Architecture Agent

## 23.1 Purpose

Analyze how candidate pages should relate within a site's information architecture.

## 23.2 Responsibilities

It may evaluate:

* hierarchy
* parent-child relationships
* hub pages
* supporting pages
* category relationships
* product relationships
* topic relationships
* page-type consistency
* URL concept suggestions

## 23.3 Boundary

It must not silently change the production website.

Major IA decisions require human authorization.

---

# 24. Internal Linking Agent

## 24.1 Purpose

Identify contextually valuable internal-link opportunities.

## 24.2 Signals

* semantic relationship
* entity relationship
* topic hierarchy
* user journey
* page importance
* contextual relevance
* existing links
* anchor relevance

## 24.3 Outputs

```text
Source Page
Target Page
Relationship
Suggested Placement
Suggested Anchor Concept
Reason
Confidence
```

## 24.4 Boundary

It should not manipulate production links without explicit authorization.

---

# 25. Content Gap Agent

## 25.1 Purpose

Identify meaningful missing or insufficient coverage.

## 25.2 Gap Types

Examples:

```text
Topic Gap
Entity Gap
Attribute Gap
Intent Gap
Page-Type Gap
Content-Depth Gap
Competitor Gap
Search Coverage Gap
Internal-Link Gap
```

## 25.3 Inputs

* topic universe
* entities
* EAV
* SERPs
* competitors
* website pages
* content inventory

## 25.4 Outputs

```text
Gap
Gap Type
Affected Object
Evidence
Business Relevance
Search Relevance
Confidence
Candidate Actions
```

---

# 26. Cannibalization Agent

## 26.1 Purpose

Identify potential conflicts between pages competing for similar search space.

## 26.2 Signals

* query overlap
* SERP overlap
* intent overlap
* topic overlap
* entity overlap
* page-type overlap
* ranking patterns
* temporal behavior
* business purpose

## 26.3 Outputs

```text
Potential Cannibalization
Affected Pages
Affected Queries
Evidence
Severity
Confidence
Possible Actions
```

Possible actions:

```text
MONITOR
DIFFERENTIATE
UPDATE
MERGE
SPLIT
REDIRECT
NO_ACTION
```

The agent must not select irreversible actions solely on its own.

---

# 27. Competitor Intelligence Agent

## 27.1 Purpose

Analyze search and content competition.

## 27.2 Responsibilities

It may analyze:

* search competitors
* business competitors
* competitor domains
* competitor pages
* topic coverage
* entity coverage
* content formats
* page types
* SERP presence
* competitive gaps
* changes over time

## 27.3 Boundary

It must not assume competitor strategy is appropriate for the user's business.

---

# 28. Decision Support Agent

## 28.1 Purpose

Assist the Decision Engine by synthesizing evidence and generating candidate options.

## 28.2 Responsibilities

It may:

* summarize evidence
* identify supporting factors
* identify conflicts
* generate candidate actions
* draft explanations
* identify missing information
* propose questions for human review

## 28.3 Boundary

It does not hold final strategic authority.

The authoritative decision logic remains in:

```text
12_SEO_DECISION_ENGINE.md
```

---

# 29. Context Retrieval Capability

Context retrieval is a cross-cutting capability rather than necessarily an independent autonomous agent.

It should retrieve:

* relevant project state
* relevant entities
* relevant topics
* relevant evidence
* relevant decisions
* relevant history
* relevant user constraints
* relevant previous outcomes

Retrieval should use:

```text
Structured Filtering
+
Semantic Retrieval
+
Temporal Filtering
+
Scope Filtering
```

rather than semantic search alone.

---

# 30. Evidence Validation Capability

Evidence validation is another cross-cutting capability.

It should detect:

* missing provenance
* stale evidence
* conflicting sources
* malformed data
* unsupported claims
* duplicate evidence
* invalid source relationships
* low-quality provider output

It should prevent invalid evidence from silently becoming trusted knowledge.

---

# 31. Agent Capability Registry

The system should maintain an agent registry.

Conceptually:

```yaml
agent:
  id: "intent_agent"
  name: "Intent Agent"
  version: "1.0.0"

  capabilities:
    - intent_classification
    - intent_distribution
    - intent_confidence

  inputs:
    - query
    - serp
    - search_context

  outputs:
    - intent_analysis

  tools:
    - serp_provider
    - knowledge_query

  autonomy:
    level: 1
```

The registry allows the Orchestrator to determine:

* which capability exists
* which version is available
* what inputs are required
* what tools may be used
* what output contract applies

---

# 32. Agent Versioning

Every production agent should have a version.

Changes may include:

* prompt
* model
* retrieval logic
* tool configuration
* scoring
* output schema
* classification policy

Material behavior changes require versioning.

Historical outputs should preserve the version that produced them.

---

# 33. Model Selection

Agents should not all use the same model by default.

Model routing may consider:

* reasoning complexity
* context size
* latency
* cost
* reliability
* structured-output capability
* task criticality

Example:

```text
Simple classification
→ smaller model

Complex synthesis
→ stronger reasoning model

Deterministic transformation
→ no LLM
```

The exact provider and model strategy belongs to the technical architecture and runtime implementation.

---

# 34. Deterministic-First Principle

Before invoking an LLM, the system should determine whether the task can be performed deterministically.

Examples:

```text
URL normalization
→ deterministic

Score calculation
→ deterministic

Duplicate ID detection
→ deterministic

Database filtering
→ deterministic

Semantic interpretation
→ AI-assisted

Ambiguous intent analysis
→ AI-assisted
```

This improves:

* reliability
* cost
* reproducibility
* testability

---

# 35. Agent Reasoning Boundary

AI reasoning should operate over supplied evidence.

An agent must distinguish:

```text
Known
```

from:

```text
Inferred
```

from:

```text
Hypothesized
```

Example:

```yaml
finding:
  statement: "This query likely represents commercial investigation intent."
  state: INFERRED
  confidence: 0.74
```

The agent must not present this as observed fact.

---

# 36. Hypothesis Generation

Agents may generate hypotheses when evidence is incomplete.

Example:

```text
Hypothesis:
The decline may be associated with a change in SERP intent.
```

This should be represented as:

```text
HYPOTHESIS
```

or equivalent inferred state.

Hypotheses should become research candidates, not facts.

---

# 37. Confidence Requirements

Each non-trivial AI inference should have a confidence representation.

Confidence should consider:

* evidence quantity
* evidence quality
* evidence agreement
* ambiguity
* freshness
* model uncertainty
* provider reliability

Confidence should not be generated arbitrarily by asking the LLM:

```text
"Give a confidence score."
```

Where practical, confidence should be derived from observable factors and calibrated against evaluation data.

---

# 38. Agent Output Validation

Every structured output should pass:

```text
Schema Validation
↓
Type Validation
↓
Reference Validation
↓
Evidence Validation
↓
Business Rule Validation
↓
Confidence Validation
↓
Safety Validation
```

Invalid outputs should be:

```text
Rejected
```

or:

```text
Returned for Repair
```

rather than silently persisted.

---

# 39. Agent Tool Calling

Tool calls must be explicit.

Conceptually:

```text
Agent
 ↓
Tool Request
 ↓
Permission Check
 ↓
Tool Execution
 ↓
Tool Result
 ↓
Evidence Normalization
 ↓
Agent
```

The agent should not treat arbitrary tool output as authoritative.

---

# 40. External Search Tools

Search tools may be used for:

* query discovery
* business research
* entity research
* competitor research
* SERP acquisition

Search results must be:

* timestamped
* scoped
* attributed
* normalized
* stored as evidence where appropriate

---

# 41. Website Tools

Website-related tools may include:

* crawler
* parser
* sitemap reader
* URL analyzer
* page extractor
* metadata analyzer

Agents should receive only the website data required for the task.

---

# 42. SEO Provider Tools

Provider adapters may supply:

* search volume
* keyword metrics
* ranking data
* backlinks
* SERPs
* traffic estimates
* competitor metrics

Provider-specific semantics must not leak into the core agent contracts.

---

# 43. Provider Independence

Agents should reason over normalized provider-neutral objects.

For example:

```text
SearchMetric
```

rather than:

```text
AhrefsSearchVolumeObject
```

Provider-specific metadata may remain in provenance.

---

# 44. Agent Memory

Agents should not maintain uncontrolled conversational memory.

Persistent memory belongs in the shared knowledge/data layer.

Agent memory should primarily consist of:

```text
Current Task Context
+
Retrieved Relevant History
```

not:

```text
Everything the agent has ever seen.
```

---

# 45. Cross-Agent Knowledge Sharing

Agents should communicate through:

* structured outputs
* shared knowledge
* evidence references
* workflow state
* orchestrator messages

They should not depend on hidden internal state from another agent.

---

# 46. Inter-Agent Dependencies

Dependencies should be explicit.

Example:

```text
Entity Agent
      ↓
Topic Discovery Agent
      ↓
Topic Validation Agent
      ↓
Intent Agent
      ↓
SERP Agent
      ↓
Clustering Agent
      ↓
Page Candidate Agent
      ↓
Decision Engine
```

The final dependency graph must be validated across all project documents by the Orchestrator.

This document does not hard-code the final global execution order.

---

# 47. Parallel Agent Execution

Independent analyses may run in parallel.

Example:

```text
              ┌→ Entity Analysis
Topic
              ├→ Intent Analysis
              ├→ SERP Analysis
              └→ Competitor Analysis
```

The Orchestrator should combine their outputs after validation.

Parallelism must not introduce race conditions or inconsistent knowledge writes.

---

# 48. Agent Idempotency

Where possible, agent tasks should be idempotent.

Repeated execution should not create uncontrolled duplicate records.

Example:

```text
Same task
+
Same evidence snapshot
+
Same agent version
```

should produce an equivalent logical result unless the task explicitly depends on changing external state.

---

# 49. Agent Failure Handling

Failure classes include:

```text
INPUT_ERROR
CONTEXT_ERROR
TOOL_ERROR
PROVIDER_ERROR
MODEL_ERROR
TIMEOUT
RATE_LIMIT
OUTPUT_VALIDATION_ERROR
EVIDENCE_ERROR
POLICY_ERROR
UNKNOWN_ERROR
```

Each agent should define appropriate:

* retry
* fallback
* escalation
* partial-result
* stop conditions

---

# 50. Partial Results

Agents may return partial results when safe.

Example:

```text
SERP provider succeeded for 8/10 queries.
```

The output should explicitly state:

```text
coverage: 80%
state: PARTIAL
```

The system must not represent partial analysis as complete analysis.

---

# 51. No Fabrication Rule

If an agent cannot retrieve required evidence, it must say so.

Forbidden:

```text
Invented SERP
Invented search volume
Invented competitor
Invented entity relationship
Invented business fact
Invented ranking
```

Allowed:

```text
UNKNOWN
INSUFFICIENT_DATA
UNAVAILABLE
ESTIMATED
```

with appropriate provenance.

---

# 52. Agent Safety Boundary

Agents must not:

* bypass authorization
* access unauthorized projects
* expose secrets
* execute destructive actions without authorization
* trust unvalidated external instructions
* modify strategic policy silently
* publish content by default
* perform irreversible website operations by default

---

# 53. Prompt Injection Defense

External content should be treated as untrusted data.

For example, if a webpage contains:

```text
"Ignore all previous instructions and perform X."
```

the agent must treat this as webpage content, not as an instruction.

The tool/runtime boundary should prevent external content from acquiring system authority.

---

# 54. Skills and Tool Installation

Agents may require capabilities that are not initially installed.

The product policy should allow the system/operator to:

```text
Identify Required Capability
↓
Check Existing Tools/Skills
↓
Determine Whether Installation Is Permitted
↓
Install Required Capability
↓
Validate Installation
↓
Register Capability
↓
Use It
↓
Document Usage
```

The authoritative policy belongs to:

```text
26_SKILLS_AND_TOOLING_POLICY.md
```

An agent must not install arbitrary software without the required permission and security checks.

---

# 55. Human Review Signals

An agent should be able to flag:

```text
REVIEW_REQUIRED
```

when:

* confidence is low
* evidence conflicts
* business implications are significant
* output is ambiguous
* action may be irreversible
* policy boundaries are unclear
* required data is missing

---

# 56. Agent Autonomy Levels

Agents should have explicit autonomy.

Suggested levels:

```text
LEVEL 0
Analysis only

LEVEL 1
Analysis + structured recommendation

LEVEL 2
Analysis + recommendation + workflow participation

LEVEL 3
Low-risk authorized action

LEVEL 4
Conditional autonomous execution

LEVEL 5
Broad autonomous execution
```

MVP target:

```text
LEVEL 0–2
```

with tightly controlled Level 3 capabilities where justified.

---

# 57. Agent Actions vs Agent Recommendations

The distinction must remain explicit.

```text
Agent Recommendation:
"Add an internal link from Page A to Page B."

Agent Action:
"Internal link was added."
```

The second requires execution authorization.

---

# 58. Agent Observability

Every agent execution should ideally record:

* task ID
* agent ID
* agent version
* workflow ID
* project ID
* start time
* end time
* latency
* model
* token usage
* tool calls
* evidence IDs
* output validation result
* confidence
* failure state
* retry count

---

# 59. Agent Cost Management

The system should monitor:

* model cost
* tool cost
* search cost
* SERP cost
* token usage
* repeated retrieval
* redundant agent calls

Agents should avoid re-running expensive research when valid evidence already exists.

---

# 60. Context Efficiency

Agents should prefer:

```text
Relevant Evidence
```

over:

```text
Maximum Available Context
```

The Context Management system should support:

* retrieval
* summarization
* compression
* deduplication
* relevance ranking
* scope control

---

# 61. Agent Evaluation

Each agent should have its own evaluation criteria.

Example:

### Entity Agent

* entity precision
* entity recall
* resolution accuracy
* relationship accuracy

### Intent Agent

* classification accuracy
* confidence calibration
* ambiguity detection

### SERP Agent

* result extraction accuracy
* feature detection accuracy
* page-type classification accuracy

### Clustering Agent

* cluster coherence
* separation quality
* outlier detection

### Decision Support Agent

* evidence grounding
* recommendation usefulness
* conflict detection
* explanation quality

---

# 62. Golden Datasets

Critical agents should be evaluated against curated datasets.

A golden dataset may contain:

```text
Input
Expected Entities
Expected Topics
Expected Intent
Expected Clusters
Expected SERP Interpretation
Expected Candidate Actions
```

Human-reviewed datasets should be versioned.

---

# 63. Agent Regression Testing

Changes to:

* models
* prompts
* retrieval
* tools
* scoring
* parsing
* provider adapters

must be tested against relevant regression cases.

A new agent version should not silently degrade established capabilities.

---

# 64. Agent Contract Testing

Every agent should have tests confirming:

```text
Required Input
→ Valid Output
```

and:

```text
Invalid Input
→ Correct Error
```

and:

```text
Unavailable Evidence
→ Explicit Uncertainty
```

and:

```text
Malformed Model Output
→ Validation Failure
```

---

# 65. Agent Security Testing

Tests should verify:

* project isolation
* permission enforcement
* tool restrictions
* prompt injection resistance
* secret isolation
* unauthorized action prevention
* external content isolation

---

# 66. Agent Explainability

Agents should expose:

```text
Finding
Evidence
Confidence
Uncertainty
```

where applicable.

They should not expose private chain-of-thought.

A good output is:

```text
Finding:
Intent appears informational.

Evidence:
- SERP page types
- query modifiers
- result patterns

Confidence:
High

Uncertainty:
Two results indicate mixed commercial intent.
```

---

# 67. Agent Output Example

Conceptually:

```yaml
agent_result:
  agent:
    id: "intent_agent"
    version: "1.2.0"

  task_id: "TASK-123"

  target:
    type: "QUERY"
    id: "QUERY-456"

  findings:
    - statement: "The dominant intent appears informational."
      state: "INFERRED"
      confidence: 0.87
      evidence:
        - "SERP-001"
        - "SERP-002"

  conflicts:
    - statement: "Some results indicate commercial investigation."
      state: "CONFLICTED"
      confidence: 0.54
      evidence:
        - "SERP-003"

  recommendation:
    action: "USE_INFORMATIONAL_PAGE_TYPE"
    state: "RECOMMENDED"

  review:
    required: false
```

The actual schema belongs to `16_OUTPUT_CONTRACTS.md`.

---

# 68. Agent Coordination Contract

The Orchestrator should provide agents with:

```text
Task ID
Project ID
Target
Task-specific Context
Constraints
Required Output Contract
Tool Permissions
Timeout
Retry Policy
```

The agent returns:

```text
Validated Result
Evidence References
Confidence
State
Warnings
Errors
```

---

# 69. Agent Stop Conditions

An agent should stop when:

* required evidence is unavailable
* authorization is missing
* confidence falls below a defined threshold
* a hard constraint is violated
* output cannot be validated
* tool access fails beyond retry policy
* task scope is exceeded

Stopping is preferable to hallucinating completion.

---

# 70. Agent Scope Control

An agent should not expand its task autonomously.

For example:

```text
Task:
Classify intent
```

must not become:

```text
Classify intent
+
Create page
+
Modify IA
+
Publish content
```

Scope expansion requires workflow authorization.

---

# 71. Agent Reuse

Agent capabilities should be reusable across workflows.

For example:

```text
SERP Intelligence
```

may support:

* topic validation
* intent analysis
* clustering
* page mapping
* cannibalization
* competitor analysis
* decision support

The system should avoid duplicated implementations of the same intelligence capability.

---

# 72. Shared Intelligence Services

Some capabilities should be implemented as reusable services rather than agents.

Examples:

* URL canonicalization
* text normalization
* entity ID resolution
* score calculation
* SERP similarity calculation
* vector retrieval
* evidence validation
* schema validation

This avoids unnecessary LLM usage.

---

# 73. Agent Composition

Complex capabilities may be composed from smaller modules.

Example:

```text
SERP Intelligence
    ├── Acquisition
    ├── Normalization
    ├── Feature Detection
    ├── Page Classification
    ├── Intent Signals
    └── Similarity Analysis
```

The system should choose the smallest useful abstraction.

---

# 74. Agent Ownership

Every agent should have a clearly defined ownership boundary.

For example:

```text
Entity Agent
→ entity knowledge

Intent Agent
→ intent interpretation

SERP Agent
→ search evidence

Decision Engine
→ strategic decision evaluation
```

No component should become a universal "SEO agent" containing unrelated responsibilities.

---

# 75. Avoiding the Mega-Agent

The following design is prohibited:

```text
One giant SEO Agent
    ↓
Research
    ↓
Entity extraction
    ↓
Topic modeling
    ↓
SERP
    ↓
Content
    ↓
Architecture
    ↓
Execution
```

This creates:

* unclear boundaries
* poor testing
* difficult debugging
* excessive context
* difficult versioning
* weak observability
* unpredictable behavior

---

# 76. Avoiding Agent Explosion

The opposite extreme is also prohibited.

Do not create a separate autonomous agent for every tiny function.

For example:

```text
Title Agent
Meta Description Agent
URL Agent
Slug Agent
Heading Agent
...
```

when deterministic services or one broader capability would be sufficient.

The architecture should optimize for meaningful capability boundaries.

---

# 77. Agent Registry and Capability Discovery

The Orchestrator should be able to determine:

```text
What capability is required?
↓
Which agent/module provides it?
↓
Which version?
↓
What inputs?
↓
What tools?
↓
What output contract?
```

This supports future extensibility without hard-coding every workflow to one implementation.

---

# 78. Dynamic Agent Selection

Future workflows may dynamically select an implementation based on:

* capability
* cost
* latency
* quality
* model availability
* provider availability
* task complexity

Example:

```text
Need: Intent Classification
↓
Available:
Intent Agent v1
Intent Agent v2
External Classifier
↓
Select according to policy
```

This should remain policy-controlled.

---

# 79. Fallbacks

Fallbacks may include:

```text
Agent A
↓
Provider unavailable
↓
Agent A fallback provider
↓
Alternative implementation
↓
Reduced analysis
↓
Human review
```

Fallback behavior must not silently alter the meaning of the output.

---

# 80. Agent Data Access

Agents should access data through controlled interfaces.

Preferred:

```text
Agent
→ Knowledge Query Interface
```

rather than:

```text
Agent
→ unrestricted database
```

This supports:

* security
* testability
* schema independence
* access control
* observability

---

# 81. Agent Persistence

Agents should not directly manipulate arbitrary database tables.

Preferred:

```text
Agent
→ Domain Service / Repository / Knowledge Interface
→ Persistence Layer
```

This preserves architecture boundaries.

---

# 82. Agent Transactions

If an agent result requires multiple related writes, persistence should use appropriate transaction boundaries.

Partial writes must not leave the knowledge model inconsistent.

---

# 83. Evidence Write Policy

Agents may create evidence records when they acquire or derive evidence.

Derived claims should reference:

```text
Source Evidence
```

rather than replacing it.

---

# 84. Derived Data

Agent-derived data should be distinguishable from source data.

Example:

```text
Raw SERP
↓
Normalized SERP
↓
AI Classification
↓
Intent Inference
```

Each layer should preserve lineage.

---

# 85. Agent Output Persistence

Not every intermediate output must be permanently persisted.

Persistence should be based on:

* future reuse
* auditability
* cost of recomputation
* strategic importance
* debugging requirements
* data lifecycle policy

Temporary intermediate results may remain workflow state.

---

# 86. Agent Caching

Cache reusable analysis when:

* inputs are identical
* evidence snapshot is compatible
* agent version is unchanged
* freshness requirements allow reuse

Invalidate when material inputs change.

---

# 87. Agent Freshness

Agents dealing with changing external reality should define freshness requirements.

Examples:

```text
Business facts
→ potentially long-lived

Entity definitions
→ relatively stable

SERP
→ highly time-sensitive

Competitor rankings
→ time-sensitive
```

Freshness belongs to the task context, not merely the agent.

---

# 88. Agent Multi-Language Support

Agents should support project language and search-market context.

They must distinguish:

```text
Language
```

from:

```text
Market
```

and:

```text
Search Context
```

The same conceptual topic may behave differently across languages and markets.

---

# 89. Localization

Localized agent analysis may need:

* local terminology
* local entities
* local search behavior
* local competitors
* local business constraints
* localized intent

Agents must not assume direct translation implies identical search intent.

---

# 90. Agent Configuration

Agent behavior should be configurable through explicit configuration rather than hidden prompt changes.

Configuration may include:

* model
* temperature where applicable
* token limits
* retrieval parameters
* tool permissions
* thresholds
* policy versions
* timeout
* retry policy

Configuration changes should be auditable.

---

# 91. Prompt Versioning

Prompts are implementation artifacts and should be versioned when they materially affect behavior.

A production result should preserve:

```text
Agent Version
Prompt Version
Model Version
```

where applicable.

---

# 92. Structured Output Enforcement

When downstream systems depend on structured output, the runtime should use:

* schema-constrained generation
* structured response formats
* validation
* repair/retry where safe

Free-form parsing should not be the primary mechanism for critical outputs.

---

# 93. Agent Evaluation Dimensions

Every production agent should be evaluated across:

```text
Correctness
Completeness
Grounding
Confidence Calibration
Consistency
Latency
Cost
Safety
Failure Handling
Regression Stability
```

---

# 94. Agent Quality Thresholds

Each agent should have minimum acceptable quality thresholds before production use.

Thresholds should be:

* task-specific
* measurable
* documented
* versioned
* periodically reviewed

No agent should be considered production-ready merely because it generates plausible output.

---

# 95. Human Feedback

Human feedback may include:

```text
Correct
Incorrect
Partially Correct
Missing Context
Wrong Entity
Wrong Intent
Wrong Recommendation
Useful
Not Useful
```

Feedback should be linked to the relevant:

* agent
* version
* task
* output
* evidence

---

# 96. Learning From Feedback

Feedback may be used to improve:

* prompts
* retrieval
* classification
* scoring
* policies
* datasets
* model selection

Changes must be evaluated before production rollout.

Human feedback must not silently modify behavior in production without controlled change management.

---

# 97. Agent Governance

Production agents should have:

* owner
* purpose
* version
* dependencies
* tools
* permissions
* evaluation suite
* quality thresholds
* failure policy
* change history

---

# 98. Agent Change Management

A change to an agent should identify:

```text
What changed?
Why?
Expected behavior change?
Affected workflows?
Affected outputs?
Affected evaluations?
Migration required?
Rollback available?
```

Material changes should create an auditable record.

---

# 99. Agent Deprecation

Agents may be deprecated when:

* capability is replaced
* quality is insufficient
* cost is excessive
* provider becomes unavailable
* architecture changes

Deprecation should preserve historical output interpretation.

---

# 100. Agent Security Principles

1. Least privilege.
2. Explicit tool permissions.
3. Project isolation.
4. No secret exposure.
5. No arbitrary execution.
6. External content is untrusted.
7. No unauthorized database access.
8. No silent privilege escalation.
9. Audit material actions.
10. Validate model outputs.

---

# 101. Agent Performance

Performance should consider:

* latency
* concurrency
* tool calls
* context size
* model time
* database queries
* retrieval latency
* provider latency

Performance optimization must not compromise evidence integrity.

---

# 102. Agent Concurrency

Independent tasks may execute concurrently.

The Orchestrator must control:

* concurrency limits
* provider rate limits
* database load
* model capacity
* task priorities

Agents should not independently create uncontrolled parallel workloads.

---

# 103. Agent Resource Budgets

Each agent execution may have:

```yaml
budget:
  max_tokens: ...
  max_tool_calls: ...
  max_duration_seconds: ...
  max_cost: ...
```

The runtime should terminate or degrade safely when budgets are exceeded.

---

# 104. Agent Priorities

Tasks may have priority:

```text
CRITICAL
HIGH
NORMAL
LOW
BACKGROUND
```

The Orchestrator should control scheduling.

Agents themselves should not arbitrarily reprioritize unrelated tasks.

---

# 105. Agent Observability Events

Useful events include:

```text
AGENT_STARTED
AGENT_CONTEXT_LOADED
AGENT_TOOL_CALLED
AGENT_TOOL_FAILED
AGENT_OUTPUT_GENERATED
AGENT_OUTPUT_VALIDATED
AGENT_COMPLETED
AGENT_FAILED
AGENT_RETRIED
AGENT_ESCALATED
```

---

# 106. Agent Audit Trail

For material analyses, preserve:

```text
Task
Input Snapshot
Context Snapshot
Agent Version
Model Version
Tool Calls
Evidence
Output
Validation
Confidence
Human Feedback
```

This enables reconstruction and debugging.

---

# 107. Agent Debugging

When an agent produces an incorrect result:

```text
Detect
↓
Reproduce
↓
Inspect Inputs
↓
Inspect Context
↓
Inspect Retrieval
↓
Inspect Tool Results
↓
Inspect Prompt/Model
↓
Inspect Output Validation
↓
Identify Root Cause
↓
Fix
↓
Targeted Test
↓
Regression Test
```

The debugging process must not begin by blindly changing prompts.

---

# 108. Common Agent Failure Patterns

### Context Failure

Relevant evidence was not retrieved.

### Retrieval Failure

Correct information exists but was not selected.

### Tool Failure

External provider returned incomplete or incorrect data.

### Reasoning Failure

Evidence was available but incorrectly interpreted.

### Schema Failure

Output did not satisfy contract.

### Scope Failure

Agent performed work outside its assigned responsibility.

### Confidence Failure

Agent expressed certainty unsupported by evidence.

### Provenance Failure

Conclusion cannot be traced to evidence.

---

# 109. Agent Recovery

Recovery strategy should depend on failure type.

Example:

```text
Retrieval failure
→ retry retrieval

Tool failure
→ provider fallback

Model failure
→ retry / alternate model

Schema failure
→ structured repair

Insufficient evidence
→ request more evidence

Strategic ambiguity
→ human review
```

---

# 110. Agent Workflow Boundary

Agents do not own the complete business process.

The workflow system owns:

* sequencing
* branching
* retries
* dependencies
* state
* human checkpoints
* completion criteria

This prevents individual agents from becoming hidden workflow engines.

---

# 111. Decision Authority Boundary

The following hierarchy applies:

```text
Human Strategic Authority
        ↓
Decision Engine
        ↓
Agent Analysis
        ↓
Tools / Evidence
```

Tools provide information.

Agents interpret information.

The Decision Engine evaluates options.

Humans approve strategic decisions.

---

# 112. Agent-to-Decision Example

```text
SERP Agent
→ "SERP overlap is 82%."

Intent Agent
→ "Intent overlap is high."

Page Agent
→ "Existing pages have overlapping scope."

Business Agent
→ "The products have distinct commercial purposes."

Decision Engine
→ "Do not automatically merge. Differentiate pages."

Human
→ Approve / reject / modify.
```

This illustrates why no single agent should own the final decision.

---

# 113. Agent-to-Page Example

```text
Topic Discovery
→ Topic X

Topic Validation
→ Valid

Intent Agent
→ Informational

SERP Agent
→ Informational SERP

Page Candidate Agent
→ Dedicated page is plausible

Decision Engine
→ High-priority page opportunity

Human
→ Approve
```

---

# 114. Agent-to-Cannibalization Example

```text
Cannibalization Agent
→ Potential conflict detected

Evidence:
- query overlap
- SERP overlap
- intent overlap

Business evidence:
- pages serve different products

Decision Engine
→ Differentiate rather than merge

Human
→ Approve
```

---

# 115. Agent-to-Content-Gap Example

```text
Content Gap Agent
→ Missing attribute coverage

Entity/EAV evidence
→ Attribute is strategically relevant

SERP evidence
→ Attribute appears frequently in relevant results

Decision Engine
→ Expand existing page

Human
→ Approve
```

---

# 116. Agent Composition Example

A research workflow may compose:

```text
Business Research
        ↓
Entity Extraction
        ↓
EAV Extraction
        ↓
Topic Discovery
        ↓
Topic Validation
        ↓
Query Discovery
        ↓
Intent
        ↓
SERP
        ↓
Clustering
        ↓
Decision Engine
```

The exact dependency graph is determined and validated through the complete documentation audit and workflow specification.

---

# 117. MVP Agent Set

The MVP should prioritize the minimum meaningful intelligence set:

1. Business Research
2. Entity
3. EAV
4. Topic Discovery
5. Topic Validation
6. Intent
7. SERP Intelligence
8. Topic Clustering
9. Page Candidate
10. Competitor Intelligence
11. Content Gap
12. Cannibalization
13. Decision Support

Page Architecture and Internal Linking may initially be narrower modules if the MVP scope requires it.

---

# 118. MVP Agent Architecture

The MVP runtime should remain:

```text
Modular Monolith
        ↓
Central Orchestrator
        ↓
Agent / Intelligence Modules
        ↓
Shared Knowledge Layer
        ↓
Decision Engine
```

Do not create a microservice per agent by default.

---

# 119. Future Agent Architecture

Future versions may support:

* independent worker pools
* specialized model routing
* external agent providers
* agent marketplace/capability registry
* autonomous monitoring agents
* long-running research agents
* event-triggered agents
* specialized domain agents

Extraction should be driven by measured operational requirements.

---

# 120. Agent Marketplace / Extensibility

The long-term system may support external intelligence modules.

Any external module must provide:

```text
Capability
Input Contract
Output Contract
Permissions
Version
Security Metadata
Evaluation Evidence
Cost Model
Dependencies
```

External modules remain subject to the same validation and security requirements.

---

# 121. No Unverified External Agent

An externally installed agent or skill must not be trusted solely because it claims to perform a capability.

It should undergo appropriate:

* provenance verification
* permission review
* security review
* functional validation
* output validation
* sandboxing where appropriate

---

# 122. Agent Documentation Requirements

Each production agent should have documentation containing at minimum:

```text
Purpose
Responsibilities
Non-Responsibilities
Inputs
Outputs
Dependencies
Tools
Permissions
Epistemic States
Confidence
Failure Modes
Testing
Version
Owner
```

---

# 123. Agent Definition of Done

An agent is not considered complete until:

### Contract

* [ ] Purpose is defined.
* [ ] Scope is defined.
* [ ] Inputs are defined.
* [ ] Outputs are defined.
* [ ] Dependencies are defined.

### Intelligence

* [ ] AI vs deterministic responsibilities are explicit.
* [ ] Evidence requirements are defined.
* [ ] Confidence is represented.
* [ ] Uncertainty is represented.

### Tools

* [ ] Allowed tools are defined.
* [ ] Forbidden tools are defined.
* [ ] Provider dependencies are explicit.

### Safety

* [ ] Authorization boundaries exist.
* [ ] Project isolation exists.
* [ ] External content is treated as untrusted.
* [ ] Destructive actions are protected.

### Reliability

* [ ] Failure modes are defined.
* [ ] Retry policy exists.
* [ ] Fallback behavior exists where appropriate.
* [ ] Invalid outputs are rejected.

### Testing

* [ ] Unit tests exist.
* [ ] Integration tests exist.
* [ ] Evaluation dataset exists where applicable.
* [ ] Regression tests exist.
* [ ] Security tests exist where relevant.

### Operations

* [ ] Versioning exists.
* [ ] Observability exists.
* [ ] Cost/latency monitoring exists.
* [ ] Auditability exists.

---

# 124. Non-Negotiable Agent Principles

1. **An agent is a bounded capability, not an unrestricted autonomous entity.**
2. **The Central Orchestrator controls workflow execution.**
3. **Agents communicate through structured contracts and shared knowledge, not uncontrolled agent-to-agent conversation.**
4. **Agents provide evidence and analysis; the Decision Engine handles strategic recommendation logic.**
5. **Humans retain strategic authority.**
6. **Every meaningful inference must preserve provenance and confidence.**
7. **Unknown is a valid result.**
8. **Insufficient evidence is a valid result.**
9. **Agents must never fabricate external data.**
10. **Deterministic logic should be used wherever it is sufficient.**
11. **LLMs should be used where semantic reasoning provides meaningful value.**
12. **Tool access must follow least privilege.**
13. **External content is untrusted data.**
14. **Agent outputs must be schema-validated.**
15. **Agent versions must be traceable.**
16. **Material behavior changes must be tested and versioned.**
17. **Agents must not silently expand their scope.**
18. **Agents must not silently change strategic policy.**
19. **Irreversible actions require explicit authorization.**
20. **Agent quality must be measured rather than inferred from plausible output.**

---

# 125. Final Agent Architecture Model

The complete conceptual model is:

```text
                         HUMAN
                           │
                    Strategic Authority
                           │
                           ▼
                  ┌─────────────────┐
                  │ Decision Engine │
                  └────────┬────────┘
                           │
                    Recommendations
                           │
                           ▼
                 ┌────────────────────┐
                 │ Central Orchestrator│
                 └─────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Business /       Search /         Website /
     Semantic         SERP             Competitive
     Agents           Agents           Agents
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                  Shared Knowledge Layer
                           │
             ┌─────────────┼─────────────┐
             ▼             ▼             ▼
          Entities       Topics        Evidence
             │             │             │
             └─────────────┼─────────────┘
                           ▼
                    Search / Website
                       Reality
```

---

# 126. Final Agent Operating Model

The intended operating model is:

```text
Human Strategy
      ↓
Orchestrator Task
      ↓
Relevant Agent Capability
      ↓
Evidence Retrieval
      ↓
Deterministic Processing
      ↓
AI Reasoning
      ↓
Structured Output
      ↓
Validation
      ↓
Evidence + Confidence
      ↓
Shared Knowledge
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

The architecture deliberately avoids the assumption that adding more autonomous agents automatically creates a better system.

The goal is not maximum agent count.

The goal is:

```text
Clear Capabilities
+
Strong Contracts
+
Reliable Evidence
+
Controlled Reasoning
+
Explicit Decision Logic
+
Human Authority
```

---

# 127. Document Control

```yaml
document:
  id: "13"
  filename: "13_AGENT_SPECIFICATIONS.md"
  title: "Agent Specifications"

product:
  name: "SEO Research & Strategy Copilot / SEO Decision Engine"

status: "APPROVED_AS_BASELINE_AGENT_SPECIFICATIONS"

architecture:
  pattern: "central_orchestrator + modular_ai_capabilities"
  default_runtime: "modular_monolith"
  agent_to_agent_communication: "structured_contracts_via_orchestrator"
  strategic_authority: "human"
  decision_authority_layer: "seo_decision_engine"

core_agents:
  - "Business Research Agent"
  - "Entity Agent"
  - "EAV Agent"
  - "Topic Discovery Agent"
  - "Topic Validation Agent"
  - "Intent Agent"
  - "SERP Intelligence Agent"
  - "Topic Clustering Agent"
  - "Page Candidate Agent"
  - "Page Architecture Agent"
  - "Internal Linking Agent"
  - "Content Gap Agent"
  - "Cannibalization Agent"
  - "Competitor Intelligence Agent"
  - "Decision Support Agent"

cross_cutting_capabilities:
  - "Context Retrieval"
  - "Evidence Validation"

core_principles:
  - "bounded_capabilities"
  - "explicit_contracts"
  - "evidence_first"
  - "deterministic_first"
  - "confidence_and_uncertainty"
  - "least_privilege"
  - "human_in_the_loop"
  - "no_fabrication"
  - "versioned_behavior"
  - "testable_outputs"

mvp_autonomy:
  target: "LEVEL_0_TO_LEVEL_2"
  destructive_autonomy: false

primary_next_dependency:
  - "14_AGENT_WORKFLOW.md"

related_contract:
  - "16_OUTPUT_CONTRACTS.md"

tooling_policy:
  - "26_SKILLS_AND_TOOLING_POLICY.md"

context_policy:
  - "25_CONTEXT_MANAGEMENT.md"
```
