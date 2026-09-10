# 10 — Topic Modeling and Clustering

**Document:** `10_TOPIC_MODELING_AND_CLUSTERING.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Topic Intelligence / Semantic Clustering Specification
**Status:** `APPROVED_AS_BASELINE_TOPIC_MODELING_AND_CLUSTERING`
**Authority:** Baseline specification for topic discovery, validation, representation, clustering, and page-candidate formation
**Depends On:** `08_SEO_KNOWLEDGE_MODEL.md`, `09_ENTITY_EAV_MODEL.md`
**Related To:** `11_SEARCH_AND_SERP_INTELLIGENCE.md`, `12_SEO_DECISION_ENGINE.md`, `13_AGENT_SPECIFICATIONS.md`, `14_AGENT_WORKFLOW.md`, `16_OUTPUT_CONTRACTS.md`

---

# 1. Purpose

This document defines how the system discovers, represents, validates, expands, clusters, and prioritizes topics.

The purpose of topic modeling is not to group keywords mechanically.

The system must identify meaningful semantic territories that connect:

* entities;
* attributes;
* relationships;
* user needs;
* queries;
* intents;
* SERP patterns;
* business relevance;
* and potential pages.

The core principle is:

```text
Topic Modeling
≠
Keyword Clustering
```

Keyword clustering is one technique that may contribute evidence to topic modeling.

The final topic model must represent the underlying semantic structure of the domain.

---

# 2. Core Definition of a Topic

A `Topic` is a coherent semantic area representing a meaningful subject, need, problem, entity domain, or relationship that may be relevant to users and/or the business.

A topic can contain:

```text
Topic
├── Entities
├── Attributes
├── Relationships
├── User Needs
├── Queries
├── Keywords
├── Intents
├── Search Contexts
├── SERP Patterns
├── Related Topics
├── Business Relevance
└── Evidence
```

A topic is therefore a semantic object, not merely a list of similar strings.

---

# 3. Topic vs Keyword

The system must preserve this distinction:

```text
Keyword
=
A search expression or normalized search term.

Topic
=
A coherent semantic area connecting multiple expressions,
entities, needs, intents, and relationships.
```

Example:

```text
Keywords:
best running shoes
running shoes for beginners
best shoes for marathon
running shoes for flat feet
```

These may belong to:

```text
Topic:
Running Shoes
```

But they may also represent different:

* subtopics;
* audiences;
* needs;
* intents;
* page candidates.

The system must not assume that lexical similarity means page equivalence.

---

# 4. Topic vs Entity

An entity is an identifiable object or concept.

A topic is a semantic area.

Example:

```text
Entity:
Paris

Topic:
Travel to Paris
```

Another:

```text
Entity:
Nike

Topic:
Nike Running Shoes
```

An entity may participate in many topics.

A topic may contain many entities.

---

# 5. Topic vs Intent

Intent describes the user's goal.

Topic describes what the user is concerned with.

Example:

```text
Topic:
Running Shoes

Intent:
Commercial Investigation
```

The same topic may contain:

```text
Informational
Commercial Investigation
Transactional
Local
Navigational
```

depending on the user need and query.

Therefore:

```text
Topic ≠ Intent
```

---

# 6. Topic vs Page

A topic is a semantic concept.

A page is an information architecture decision.

Therefore:

```text
Topic
   ↓
Intent + SERP + Business Context
   ↓
Page Candidate
```

A topic should not automatically become a page.

One topic may produce:

```text
0 pages
1 page
multiple pages
```

depending on evidence.

---

# 7. Topic Modeling Objectives

The topic modeling subsystem must answer:

1. What topics exist in this domain?
2. Which topics are supported by evidence?
3. Which topics are relevant to the business?
4. Which topics are relevant to users?
5. Which topics are distinct?
6. Which topics overlap?
7. Which topics belong together?
8. Which topics are subtopics?
9. Which topics represent different intents?
10. Which topics deserve separate pages?
11. Which topics can be consolidated?
12. Which topics are missing?
13. Which topics are emerging?
14. Which topics are strategically important?
15. How confident is the system in each conclusion?

---

# 8. Topic Sources

Topics may originate from multiple sources.

## 8.1 Business Sources

```text
Products
Services
Categories
Business terminology
Sales terminology
Customer questions
Internal documentation
Business priorities
```

## 8.2 Semantic Sources

```text
Entities
Attributes
Relationships
Knowledge graph
EAV facts
Entity descriptions
```

## 8.3 Search Sources

```text
Queries
Keywords
Search suggestions
Related searches
SERPs
People Also Ask
Search trends
Search features
```

## 8.4 Website Sources

```text
Existing pages
Navigation
Categories
Headings
Content
Internal links
Structured data
```

## 8.5 Competitive Sources

```text
Competitor pages
Competitor topics
Competitor categories
Competitor SERPs
Competitive gaps
```

## 8.6 Human Sources

```text
Strategic priorities
Approved topics
Rejected topics
Business constraints
Domain expertise
Editorial decisions
```

No single source should automatically define the complete topic universe.

---

# 9. Topic Discovery

Topic discovery should combine multiple signals.

Conceptually:

```text
Business Knowledge
+
Entity/EAV Knowledge
+
Search Expressions
+
User Needs
+
SERP Evidence
+
Website Evidence
+
Competitive Evidence
+
Human Input
        ↓
Topic Candidates
```

The output of discovery is a **candidate universe**, not a final strategy.

---

# 10. Topic Candidate

A `Topic Candidate` is a possible topic that has not yet passed all validation criteria.

Example:

```yaml
topic_candidate:
  name: "Running Shoes for Beginners"
  source: "search + entity expansion"
  related_entities:
    - running_shoes
    - beginner_runner
  related_queries:
    - "best running shoes for beginners"
  confidence: 0.78
  state: INFERRED
```

Candidate topics must remain distinguishable from validated topics.

---

# 11. Topic Representation

A topic should have a structured representation.

Conceptually:

```yaml
topic:
  id:
  canonical_name:
  description:
  type:
  parent_topic:
  entities:
  attributes:
  relationships:
  needs:
  queries:
  keywords:
  intents:
  search_contexts:
  related_topics:
  business_relevance:
  search_relevance:
  coverage:
  opportunity:
  confidence:
  evidence:
  state:
  version:
  created_at:
  updated_at:
```

The exact implementation belongs to the data architecture and output contracts.

---

# 12. Topic Types

The system may classify topics using extensible types.

Examples:

```text
Entity-Centered
Category-Centered
Problem-Centered
Need-Centered
Use-Case-Centered
Attribute-Centered
Comparison-Centered
Process-Centered
Audience-Centered
Location-Centered
Journey-Centered
Product-Centered
Service-Centered
```

A topic may have multiple characteristics.

The system must avoid forcing every topic into one mutually exclusive type.

---

# 13. Topic Granularity

Topics exist at multiple levels.

Example:

```text
Running
  └── Running Shoes
       ├── Beginner Running Shoes
       ├── Trail Running Shoes
       ├── Marathon Running Shoes
       ├── Stability Running Shoes
       └── Running Shoe Brands
```

The model must support hierarchical relationships without assuming that every hierarchy is correct.

---

# 14. Topic Hierarchy

Possible relationships include:

```text
PARENT_OF
CHILD_OF
BROADER_THAN
NARROWER_THAN
RELATED_TO
OVERLAPS_WITH
ALTERNATIVE_TO
CONTRASTS_WITH
DEPENDS_ON
```

These relationships should not be reduced to a generic `related_to`.

---

# 15. Topic Boundaries

Every validated topic should have an explicit or inferable boundary.

A topic boundary answers:

```text
What belongs inside this topic?

What belongs outside?

Which neighboring topics should remain separate?

What user need does this topic serve?
```

This is essential for avoiding uncontrolled topic expansion.

---

# 16. Topic Core

A topic should have a semantic core.

The core may contain:

```text
Primary Entity
Primary Need
Primary Attribute Set
Primary Intent Set
Core Query Set
Core SERP Pattern
```

Example:

```text
Topic:
Best Running Shoes

Core Entity:
Running Shoes

Core Need:
Choose an appropriate running shoe

Primary Intent:
Commercial Investigation

Core Queries:
best running shoes
top running shoes
best shoes for running
```

---

# 17. Topic Periphery

A topic may also have peripheral concepts.

Examples:

```text
Related Entities
Secondary Attributes
Adjacent Needs
Supporting Queries
Alternative Intents
Related Topics
```

The system must distinguish:

```text
Core
```

from:

```text
Peripheral
```

to prevent overly broad clusters.

---

# 18. Topic Expansion

Topic expansion identifies additional concepts related to an existing topic.

Potential expansion sources:

```text
Entity attributes
Entity relationships
Query variants
Related searches
SERP features
Competitor content
User questions
Journey stages
Historical knowledge
```

Expansion must be evidence-driven.

AI-generated concepts without supporting evidence should be marked as inferred or hypothetical.

---

# 19. Semantic Expansion

Semantic expansion may identify:

```text
Synonyms
Related entities
Attributes
Subtopics
Use cases
Problems
Questions
Alternatives
Comparisons
```

Example:

```text
Topic:
Running Shoes

Expansion:
Cushioning
Stability
Heel drop
Pronunciation/pronation
Terrain
Distance
Foot type
```

The system must distinguish semantic relatedness from page-level equivalence.

---

# 20. Query Expansion

Query expansion may generate candidate expressions based on:

* entity names;
* attributes;
* relationships;
* user needs;
* modifiers;
* questions;
* locations;
* audience;
* journey stage.

Generated queries must be explicitly labeled as generated or inferred unless validated against search evidence.

---

# 21. Topic Discovery from EAV

EAV data is a major topic discovery source.

Example:

```text
Entity:
Running Shoes

Attributes:
Cushioning
Stability
Weight
Heel Drop
Terrain
Distance
Price
Brand
```

These attributes can produce candidate topics:

```text
Running Shoe Cushioning
Running Shoe Stability
Lightweight Running Shoes
Trail Running Shoes
Running Shoes for Marathon
Affordable Running Shoes
```

Not every attribute deserves a topic.

Business relevance, user need, search evidence, and SERP evidence must determine whether the attribute represents meaningful search territory.

---

# 22. Topic Discovery from Relationships

Relationships may reveal topics that keywords alone miss.

Example:

```text
Entity A → compatible_with → Entity B
Entity A → alternative_to → Entity C
Entity A → used_for → Use Case D
```

These relationships may generate:

```text
Compatibility Topics
Alternative Topics
Use-Case Topics
Comparison Topics
```

This is a major reason the product requires a semantic entity model.

---

# 23. Topic Discovery from User Needs

User needs can generate topic candidates independently of existing keyword data.

Example:

```text
Need:
Choose the right hotel for a family trip
```

Potential topics:

```text
Family Hotels
Hotels with Family Rooms
Best Areas for Families
Family Hotel Amenities
```

This prevents the system from being limited by the vocabulary already present in keyword databases.

---

# 24. Topic Discovery from SERPs

SERPs can reveal semantic structure through:

```text
Ranking page similarity
Title patterns
Content formats
SERP features
Entity co-occurrence
Repeated subtopics
Intent distribution
```

SERP-derived topics are observations/inferences and must retain provenance.

---

# 25. Topic Discovery from Competitors

Competitor websites can reveal:

```text
Topic Coverage
Category Structure
Entity Coverage
Subtopic Coverage
Content Formats
Commercial Pages
Information Architecture
```

Competitor presence is evidence of market activity, not proof that the business should copy the competitor.

---

# 26. Topic Validation

Topic discovery produces candidates.

Validation determines whether a candidate represents a meaningful strategic topic.

Validation should consider:

```text
Semantic Coherence
User Need
Search Evidence
SERP Coherence
Business Relevance
Entity Coherence
Intent Coherence
Competitive Evidence
Page Potential
Duplication Risk
Confidence
```

---

# 27. Topic Validation States

A topic may be:

```text
CANDIDATE
VALIDATED
STRATEGIC
LOW_PRIORITY
MERGE_REQUIRED
SPLIT_REQUIRED
REJECTED
CONFLICTED
UNKNOWN
```

These states must be explicit.

---

# 28. Semantic Coherence

A cluster is semantically coherent when its members share meaningful relationships beyond superficial lexical similarity.

Signals include:

```text
Shared Entity
Shared Need
Shared Attributes
Shared Relationships
Shared Intent
Semantic Similarity
SERP Similarity
```

---

# 29. SERP Coherence

SERP overlap is one of the strongest signals for determining whether search expressions may belong to the same page/topic.

If different queries repeatedly produce substantially similar SERPs, they may indicate:

```text
Shared Search Intent
```

and potentially:

```text
Shared Page Opportunity
```

However, SERP overlap must not be treated as the sole criterion.

---

# 30. Search Intent Coherence

Queries with different wording may belong together when they express the same underlying need and intent.

Example:

```text
best crm software
top crm platforms
best crm tools
```

may represent one commercial investigation topic.

But:

```text
what is crm
best crm software
```

may require different treatment despite lexical overlap.

---

# 31. Business Coherence

Two semantically related topics may still require separate strategic treatment.

Example:

```text
Topic A:
Free CRM

Topic B:
Enterprise CRM
```

The semantic relationship may be strong.

The business relevance, audience, conversion path, and page strategy may differ.

---

# 32. Topic Clustering

Clustering groups related items into meaningful semantic groups.

Potential inputs:

```text
Keywords
Queries
Entities
Topics
Pages
SERPs
Content
```

The system should support multiple clustering modes.

---

# 33. Clustering Dimensions

Possible dimensions include:

```text
Lexical Similarity
Semantic Similarity
Entity Similarity
Attribute Similarity
Intent Similarity
SERP Similarity
Need Similarity
Page Similarity
Business Similarity
```

No single similarity dimension should dominate by default.

---

# 34. Multi-Signal Clustering

The preferred clustering model is:

```text
Cluster Similarity
=
f(
  Semantic Similarity,
  Entity Relationships,
  Intent Similarity,
  SERP Similarity,
  Need Similarity,
  Business Context
)
```

The exact scoring formula belongs to implementation and decision-engine specifications.

---

# 35. Hard vs Soft Clustering

The system should support both:

### Hard Clustering

An item belongs to one primary cluster.

Useful for:

* initial page candidates;
* simple reporting;
* certain operational workflows.

### Soft Clustering

An item may have multiple memberships with different strengths.

Useful for:

* overlapping topics;
* entity-rich domains;
* multi-intent queries;
* complex semantic structures.

The knowledge model should prefer soft relationships where reality is ambiguous.

---

# 36. Cluster Membership

A membership relationship should contain:

```yaml
cluster_membership:
  item_id:
  topic_id:
  membership_score:
  membership_type:
  confidence:
  evidence:
  reason:
```

This allows the system to distinguish:

```text
Primary Member
Secondary Member
Related
Peripheral
Uncertain
```

---

# 37. Cluster Quality

Cluster quality should be evaluated using:

```text
Cohesion
Separation
Intent Consistency
SERP Consistency
Entity Coherence
Need Coherence
Business Relevance
Boundary Clarity
Page Potential
```

A mathematically strong embedding cluster can still be strategically poor.

---

# 38. Over-Clustering

Over-clustering occurs when unrelated concepts are grouped together.

Example:

```text
Running Shoes
Running Shoe Repair
Running Shoe Cleaning
Running Shoe Brands
```

These may be related semantically but may represent distinct:

* needs;
* intents;
* page types;
* user journeys.

The system must detect excessive breadth.

---

# 39. Under-Clustering

Under-clustering occurs when closely related concepts are unnecessarily separated.

Example:

```text
best crm software
best crm tools
top crm platforms
```

may be unnecessarily split into separate topics when evidence suggests a common page opportunity.

---

# 40. Cluster Splitting

A cluster should be considered for splitting when:

```text
Intent diverges
SERPs diverge
Needs diverge
Audience diverges
Business purpose diverges
Page type diverges
Topic boundary becomes unclear
```

The system should provide evidence for split recommendations.

---

# 41. Cluster Merging

Clusters may be candidates for merging when:

```text
Intent is highly aligned
SERPs strongly overlap
Needs are equivalent
Entities and attributes overlap
Business purpose is similar
Page scope can reasonably contain both
```

Merging must not be based only on semantic embedding distance.

---

# 42. Page Candidate Clustering

Topic clustering and page clustering are related but distinct.

A page candidate cluster asks:

> Which concepts should potentially be represented by the same page?

This requires stronger evidence than:

> Which concepts are semantically related?

Therefore:

```text
Semantic Cluster
≠
Page Cluster
```

---

# 43. Page Candidate Decision

A page candidate should consider:

```text
Topic Coherence
Intent Coherence
SERP Overlap
User Need
Business Value
Content Scope
Page Type
Cannibalization Risk
Existing Page Coverage
```

The final decision belongs to the strategy/page architecture layer.

---

# 44. Topic Hierarchy Construction

A hierarchy may be derived from:

```text
Entity Relationships
Topic Inclusion
Attribute Relationships
User Journey
Search Demand
Website Structure
Business Taxonomy
```

Example:

```text
Travel
├── Destinations
│   ├── France
│   │   └── Paris
│   └── Italy
│       └── Rome
├── Accommodation
│   ├── Hotels
│   └── Hostels
└── Transportation
    ├── Flights
    └── Trains
```

This hierarchy is a hypothesis until validated.

---

# 45. Hierarchy Is Not Always the Best Model

Some topic relationships are better represented as graphs.

Example:

```text
Paris
↔ Hotels
↔ Attractions
↔ Transportation
↔ Restaurants
```

A strict tree can hide meaningful cross-connections.

The system should therefore support:

```text
Hierarchy
+
Graph Relationships
```

---

# 46. Topic Graph

A topic graph may contain:

```text
Topic A
  ├── related_to → Topic B
  ├── broader_than → Topic C
  ├── narrower_than → Topic D
  ├── overlaps_with → Topic E
  ├── supports → Topic F
  └── depends_on → Topic G
```

This enables richer topical architecture than a flat taxonomy.

---

# 47. Topic Similarity

Topic similarity may be calculated from:

```text
Semantic Embeddings
Entity Overlap
Attribute Overlap
Need Overlap
Query Overlap
Intent Overlap
SERP Overlap
Relationship Overlap
```

Similarity does not imply consolidation.

---

# 48. Topic Distance

Topic distance should be multidimensional.

Two topics may be:

```text
Semantically Close
Intentually Far
Business Close
SERP Far
```

This is meaningful information.

The system should preserve these dimensions rather than compressing them into one score.

---

# 49. Topic Relevance

Topic relevance should be evaluated separately for:

```text
Semantic Relevance
Search Relevance
Business Relevance
Audience Relevance
Strategic Relevance
```

Example:

```text
Topic:
Celebrity News

Semantic Relevance: High
Search Demand: High
Business Relevance: Low
Strategic Relevance: Low
```

The topic should not automatically become a priority.

---

# 50. Topic Priority

Topic priority is a decision-oriented concept.

Conceptually:

```text
Priority
=
f(
  Business Relevance,
  Search Relevance,
  User Need,
  Intent,
  Opportunity,
  Competitive Context,
  Existing Authority,
  Confidence
)
```

Priority must not be confused with topic validity.

A valid topic can be low priority.

---

# 51. Topic Opportunity

Opportunity is derived from topic knowledge plus search and business evidence.

Potential factors:

```text
Search Demand
Business Value
Intent Fit
SERP Opportunity
Competitive Strength
Existing Coverage
Authority
Conversion Potential
Strategic Importance
```

The exact scoring logic belongs to `12_SEO_DECISION_ENGINE.md`.

---

# 52. Topic Coverage

Coverage should be represented at several levels:

```text
Entity Coverage
Attribute Coverage
Need Coverage
Intent Coverage
Query Coverage
Content Coverage
Page Coverage
Journey Coverage
```

Example:

```text
Topic Coverage:
82%

Entity Coverage:
90%

Intent Coverage:
55%

Page Coverage:
40%
```

This gives a more useful picture than keyword count alone.

---

# 53. Topic Gaps

A topic gap may occur when:

```text
Important Entity
+
Important Attribute/Need
+
Relevant Search/Business Evidence
+
Insufficient Website Coverage
```

Topic gaps should be distinguished from keyword gaps.

---

# 54. Topic Cannibalization

Potential topic cannibalization occurs when multiple existing pages target overlapping semantic territory in a way that creates strategic or search competition.

Signals include:

```text
Same Intent
Same Topic
Similar Queries
High SERP Competition
Overlapping Scope
Ranking Substitution
```

Topic similarity alone is insufficient.

---

# 55. Topic Freshness

Topics can change over time.

New topics may emerge from:

```text
New Products
New Technologies
New Search Behavior
New Regulations
New Events
New Competitors
New User Needs
```

Existing topics may decline.

The system should track:

```text
Emerging
Stable
Growing
Declining
Stale
```

where evidence supports such classification.

---

# 56. Emerging Topic Detection

Emerging topics may be detected through:

```text
New Queries
Rapid Query Growth
New SERP Patterns
New Entities
Competitor Adoption
Business Events
Search Trends
```

Emergence must be evidence-backed.

AI speculation should be labeled separately.

---

# 57. Topic Lifecycle

A topic lifecycle may be:

```text
DISCOVERED
   ↓
CANDIDATE
   ↓
VALIDATED
   ↓
STRATEGIC
   ↓
IMPLEMENTED
   ↓
MONITORED
   ↓
UPDATED
   ↓
STALE / REJECTED
```

A topic may move backward when new evidence invalidates previous assumptions.

---

# 58. Human Validation

Human validation is required for strategically important topic decisions.

Humans may:

```text
Approve
Reject
Rename
Merge
Split
Reclassify
Prioritize
Deprioritize
Add Constraint
Add Evidence
```

The system must preserve the original AI proposal and the human decision.

---

# 59. Topic Decision Record

A significant topic decision should preserve:

```yaml
decision:
  topic_id:
  action:
  previous_state:
  new_state:
  evidence:
  recommendation:
  human_actor:
  timestamp:
  rationale:
  version:
```

The system should expose the decision history without exposing private model chain-of-thought.

---

# 60. Explainability

For each important clustering or topic recommendation, the system should provide concise decision factors.

Example:

```text
Recommendation:
Merge Topic A and Topic B

Evidence:
- 82% SERP overlap
- shared primary intent
- same core entity
- overlapping user need
- no meaningful page-scope conflict

Confidence:
0.89
```

This is sufficient for decision support without exposing hidden reasoning traces.

---

# 61. Provenance

Topic conclusions must retain provenance.

Possible provenance:

```text
Business Input
Website
SERP
Search API
SEO API
Entity Knowledge
Human Decision
AI Inference
Historical Observation
```

Derived topic structures should reference the inputs from which they were generated.

---

# 62. Versioning

Topic structures must be versioned.

A topic version may change when:

```text
Name changes
Boundary changes
Members change
Parent changes
Intent changes
SERP evidence changes
Business relevance changes
```

Historical versions should remain accessible.

---

# 63. Reproducibility

Topic clustering should be reproducible where practical.

The system should preserve:

```text
Input Dataset
Embedding Model
Model Version
Clustering Method
Parameters
Prompt Version
Rules
Timestamp
Output Version
```

This is necessary for debugging and evaluation.

---

# 64. Model Independence

Topic modeling must not depend permanently on a single:

* LLM;
* embedding model;
* search provider;
* clustering library;
* SEO API.

Provider-specific implementations must remain behind abstraction boundaries.

---

# 65. Deterministic and AI Components

Topic modeling should combine deterministic and AI techniques.

### Deterministic

```text
Normalization
Deduplication Rules
Thresholds
Taxonomy Validation
Graph Constraints
Data Validation
```

### AI / Statistical

```text
Semantic Similarity
Topic Discovery
Intent Interpretation
Relationship Inference
Cluster Interpretation
Topic Naming
Boundary Suggestions
```

The combination is preferred over an entirely LLM-driven pipeline.

---

# 66. Topic Naming

AI may propose canonical topic names.

Naming should consider:

```text
Semantic Accuracy
User Language
Business Language
Search Language
Specificity
Consistency
```

The system should avoid keyword-stuffed artificial names.

---

# 67. Topic Descriptions

A validated topic should have a concise semantic description.

Example:

```text
Topic:
Family Hotels in Paris

Description:
Accommodation options in Paris relevant to families,
including family rooms, amenities, locations, and booking considerations.
```

The description defines the semantic boundary.

---

# 68. Topic Boundary Testing

The system should test boundaries using neighboring topics.

For each topic:

```text
Core Concepts
Adjacent Concepts
Excluded Concepts
Potential Overlaps
```

Example:

```text
Topic:
Paris Hotels

Adjacent:
Paris Hostels
Paris Apartments
Paris Neighborhoods

Potential Overlap:
Best Areas to Stay in Paris
```

This helps prevent topic sprawl.

---

# 69. Topic Clustering Evaluation

Evaluation should include:

### Intrinsic Metrics

```text
Silhouette
Cohesion
Separation
Embedding Distance
```

### Semantic Metrics

```text
Intent Consistency
Entity Coherence
Need Coherence
Boundary Quality
```

### Search Metrics

```text
SERP Overlap
Ranking URL Overlap
SERP Feature Similarity
```

### Strategic Metrics

```text
Business Relevance
Page Potential
Cannibalization Risk
Human Approval Rate
```

No single metric should determine success.

---

# 70. Failure Modes

The system must detect:

```text
Insufficient Data
Weak Cluster Separation
Conflicting Intent
Ambiguous Topic Boundary
Over-Clustering
Under-Clustering
Entity Resolution Failure
SERP Data Missing
Search Context Mismatch
Business Context Missing
Low Confidence
```

When confidence is insufficient, the system should return:

```text
UNKNOWN
```

or:

```text
REQUIRES_HUMAN_REVIEW
```

rather than fabricate certainty.

---

# 71. Context Sensitivity

Topic clustering may vary by:

```text
Country
Language
Audience
Device
Season
Search Engine
Date
Business
```

Therefore topic models must be associated with relevant context when required.

A topic that is valid in one market may not have the same structure in another.

---

# 72. Multilingual Topic Modeling

The system must support multilingual topics.

The model should distinguish:

```text
Canonical Concept
Localized Expression
Search Expression
```

Example:

```text
Canonical Concept:
Hotel Booking

English:
hotel booking

Persian:
رزرو هتل

German:
Hotel buchen
```

These may map to the same semantic concept while having different:

* search behavior;
* intent;
* SERPs;
* demand;
* page requirements.

Translation alone is not sufficient for multilingual SEO modeling.

---

# 73. International Topic Variance

The system must not assume that a topic structure is identical across languages.

For example:

```text
English SERP
≠
German SERP
≠
Persian SERP
```

Topic validation may therefore need locale-specific evidence.

---

# 74. Topic-to-Page Candidate Matrix

A useful intermediate artifact is:

| Topic   | Intent | SERP Coherence | Business Relevance | Existing Coverage | Page Candidate    |
| ------- | ------ | -------------- | ------------------ | ----------------- | ----------------- |
| Topic A | High   | High           | High               | Low               | Yes               |
| Topic B | Medium | Low            | High               | Low               | Review            |
| Topic C | High   | High           | Low                | None              | No                |
| Topic D | High   | High           | High               | High              | Optimize Existing |

This matrix is a decision-support artifact, not the final architecture.

---

# 75. Topic Universe

The system should maintain a `Topic Universe`.

The universe contains:

```text
Validated Topics
Candidate Topics
Rejected Topics
Historical Topics
Emerging Topics
Strategic Topics
```

This prevents the system from repeatedly rediscovering the same concepts.

---

# 76. Topic Deduplication

Before creating a new topic, the system should check:

```text
Exact Canonical Match
Semantic Match
Entity Match
Need Match
Intent Match
SERP Match
Existing Topic Relationships
```

Possible outcomes:

```text
CREATE_NEW
LINK_EXISTING
MERGE
REVIEW
REJECT_DUPLICATE
```

---

# 77. Topic Discovery Iteration

Topic discovery should be iterative.

Example:

```text
Initial Entity Model
       ↓
Initial Topics
       ↓
Search Research
       ↓
New Queries
       ↓
New Intents
       ↓
New SERP Evidence
       ↓
New Topics
       ↓
Refined Topic Boundaries
```

The system must support re-entry into previous stages.

---

# 78. Topic Model as Living Knowledge

The topic model is not a one-time report.

It should evolve when:

```text
Business changes
Search changes
SERPs change
Competitors change
New entities appear
New queries emerge
Human strategy changes
Pages are created
Performance changes
```

This is essential to the long-term Living SEO Intelligence System.

---

# 79. Relationship to Search Intelligence

`11_SEARCH_AND_SERP_INTELLIGENCE.md` supplies evidence about:

```text
Queries
SERPs
Intent Signals
Search Features
Ranking Patterns
Search Context
```

Topic modeling consumes this evidence.

Search evidence can also trigger topic-model updates.

---

# 80. Relationship to Decision Engine

`12_SEO_DECISION_ENGINE.md` consumes topic intelligence for:

```text
Priority
Opportunity
Page Creation
Optimization
Consolidation
Expansion
Internal Linking
Content Gap Resolution
```

Topic modeling should not independently make final strategic decisions.

---

# 81. Relationship to Agent Architecture

Relevant agents may include:

```text
Topic Discovery Agent
Topic Validation Agent
Topic Clustering Agent
SERP Agent
Entity Agent
Intent Agent
Topical Map Agent
Page Architecture Agent
```

The central orchestrator controls workflow and dependency management.

Agents must communicate through structured contracts and shared knowledge, not uncontrolled conversational chains.

---

# 82. Topic Modeling Workflow

A conceptual workflow:

```text
Collect Inputs
      ↓
Normalize
      ↓
Resolve Entities
      ↓
Extract Needs
      ↓
Extract Candidate Topics
      ↓
Expand Topics
      ↓
Generate Candidate Queries
      ↓
Acquire Search Evidence
      ↓
Classify Intent
      ↓
Analyze SERPs
      ↓
Cluster
      ↓
Validate
      ↓
Merge / Split
      ↓
Score Relevance
      ↓
Human Review
      ↓
Persist Topic Model
```

This is a conceptual workflow.

The orchestrator may parallelize independent operations.

---

# 83. Topic Modeling Output

A topic modeling result should be structured.

Conceptually:

```yaml
topic_model_result:
  project_id:
  model_version:
  topics:
    - topic_id:
      canonical_name:
      description:
      type:
      entities:
      needs:
      queries:
      intents:
      parent_topic:
      related_topics:
      members:
      relevance:
      confidence:
      evidence:
      state:
  clusters:
    - cluster_id:
      topic_ids:
      cohesion:
      confidence:
      evidence:
  recommendations:
    - action:
      topic_ids:
      confidence:
      evidence:
  warnings:
    - type:
      message:
      affected_topics:
```

The exact machine contract belongs to `16_OUTPUT_CONTRACTS.md`.

---

# 84. Minimum Required Topic Object

Every validated topic should minimally have:

```text
topic_id
canonical_name
description
state
confidence
evidence
entities
needs
intents
queries
relationships
business_relevance
search_relevance
```

Optional fields may be added without violating the core model.

---

# 85. Quality Gates

A topic model should not be considered production-ready unless:

```text
Entity Resolution Quality → Acceptable
Topic Boundaries → Defined
Intent Consistency → Acceptable
SERP Evidence → Available where required
Duplicate Topics → Controlled
Cluster Quality → Evaluated
Provenance → Preserved
Confidence → Represented
Human Review → Completed where required
Version → Recorded
```

---

# 86. Anti-Patterns

The system must not:

1. Cluster solely by keyword string similarity.
2. Treat search volume as topic validity.
3. Create one page per keyword automatically.
4. Merge topics solely because their embeddings are close.
5. Split topics solely because keywords differ lexically.
6. Ignore SERP evidence.
7. Ignore business relevance.
8. Ignore user needs.
9. Treat AI-generated topics as observed facts.
10. Hide uncertainty.
11. Destroy historical topic versions.
12. Let every agent invent its own topic taxonomy.
13. Treat a flat topic list as a topical map.
14. Treat topic clusters as final page architecture.
15. Copy competitor topic structures without strategic validation.
16. Assume one global topic model works identically across every locale.
17. Use one score to represent all topic dimensions.
18. silently merge ambiguous topics.

---

# 87. MVP Scope

The MVP should support:

```text
Topic Candidate Discovery
Entity/EAV-Based Expansion
Keyword/Query-Based Discovery
Basic Semantic Similarity
Intent Association
SERP-Based Validation
Multi-Signal Clustering
Topic Deduplication
Topic Hierarchy
Topic Relationships
Topic Confidence
Evidence / Provenance
Human Validation
Topic Versioning
Basic Opportunity Inputs
```

The MVP should avoid unnecessary complexity such as a fully autonomous continuously learning clustering system.

---

# 88. Future Scope

Future versions may support:

```text
Dynamic Topic Graphs
Real-Time Topic Emergence
Adaptive Clustering
Learning-to-Rank Topic Priority
Cross-Market Topic Comparison
Automated Topic Boundary Discovery
Probabilistic Topic Graphs
Temporal Topic Forecasting
Advanced SERP-Driven Topic Evolution
AI Search / Answer Engine Topic Modeling
Cross-Channel Topic Intelligence
```

These features require validation before implementation.

---

# 89. Definition of Done

Topic modeling is considered complete for a task when:

1. Relevant source data has been collected.
2. Entities have been normalized/resolved sufficiently.
3. Candidate topics have been generated.
4. Topics have been semantically represented.
5. Relevant queries and needs are connected.
6. Intent relationships are available.
7. SERP evidence has been incorporated where required.
8. Clusters have been evaluated.
9. Merge/split decisions have been considered.
10. Topic boundaries are understandable.
11. Business relevance is represented.
12. Confidence is represented.
13. Provenance is preserved.
14. Human review has occurred where required.
15. Output conforms to the defined contract.
16. The resulting model is persisted and versioned.
17. Warnings and unresolved ambiguities are explicitly reported.

---

# 90. Final Conceptual Model

The product should treat topic modeling as:

```text
Entities
+
Attributes
+
Relationships
+
Needs
+
Queries
+
Intent
+
SERPs
+
Business Context
+
Competitive Context
+
Human Knowledge
        ↓
Semantic Topic Universe
        ↓
Validated Topic Model
        ↓
Topic Relationships
        ↓
Page Candidates
        ↓
Topical Map
        ↓
SEO Decisions
```

The essential distinction is:

```text
Keyword Clustering
=
Grouping expressions.

Topic Modeling
=
Understanding semantic territories and their relationships.

Page Clustering
=
Determining which concepts may reasonably share a page.

Topical Mapping
=
Designing the strategic structure of those validated topics.

Page Architecture
=
Turning that strategy into website structure.
```

These layers must remain distinct.

---

# 91. Non-Negotiable Principles

1. **Topic ≠ Keyword.**
2. **Topic ≠ Page.**
3. **Topic ≠ Intent.**
4. **Semantic similarity does not automatically imply page equivalence.**
5. **SERP evidence is a major signal for page-level clustering.**
6. **Business relevance must remain separate from search demand.**
7. **User needs are first-class inputs to topic discovery.**
8. **Entities and EAV relationships are major sources of topic discovery.**
9. **Clusters must be multi-signal.**
10. **Hard clustering must not be forced when soft membership better represents reality.**
11. **Topic boundaries must be explicit or inferable.**
12. **Merge and split decisions require evidence.**
13. **AI-generated topics must not be represented as observed facts.**
14. **Uncertainty must remain visible.**
15. **Topic models must be versioned.**
16. **Historical topic states must remain recoverable.**
17. **Multilingual topic structures must be validated locally.**
18. **Competitor structures are evidence, not strategy.**
19. **Topic models are inputs to the Decision Engine, not substitutes for it.**
20. **Human strategy remains authoritative for final topic decisions.**

---

# 92. Final Status

```yaml
document: 10_TOPIC_MODELING_AND_CLUSTERING.md
status: APPROVED_AS_BASELINE_TOPIC_MODELING_AND_CLUSTERING

purpose:
  - topic discovery
  - semantic topic representation
  - topic validation
  - multi-signal clustering
  - topic boundary management
  - page-candidate support
  - topical-map foundation

core_distinctions:
  topic_vs_keyword: required
  topic_vs_entity: required
  topic_vs_intent: required
  topic_vs_page: required
  semantic_cluster_vs_page_cluster: required
  topic_model_vs_topical_map: required

primary_signals:
  - entities
  - attributes
  - relationships
  - user_needs
  - queries
  - intent
  - serp
  - business_relevance
  - competitive_context
  - human_validation

clustering:
  strategy: multi_signal
  supports_soft_membership: true
  supports_hard_membership: true
  serp_evidence: required_where_applicable

knowledge_requirements:
  provenance: required
  confidence: required
  versioning: required
  uncertainty: required
  historical_state: required

human_control:
  strategic_topic_decisions: human_authoritative

architecture_role:
  semantic_intelligence_module

next_dependencies:
  - 11_SEARCH_AND_SERP_INTELLIGENCE.md
  - 12_SEO_DECISION_ENGINE.md
  - 13_AGENT_SPECIFICATIONS.md
  - 14_AGENT_WORKFLOW.md
  - 16_OUTPUT_CONTRACTS.md
```

**Final Status: `APPROVED_AS_BASELINE_TOPIC_MODELING_AND_CLUSTERING`**
