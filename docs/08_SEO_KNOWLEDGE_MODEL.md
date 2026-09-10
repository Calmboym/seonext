# 08_SEO_KNOWLEDGE_MODEL.md

**Document:** `08_SEO_KNOWLEDGE_MODEL.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** SEO Knowledge Model Specification
**Status:** `APPROVED_AS_BASELINE_SEO_KNOWLEDGE_MODEL`
**Depends On:** `01_PRD.md`, `02_PRODUCT_VISION.md`, `03_MASTER_RULES.md`, `04_SYSTEM_ARCHITECTURE.md`, `05_AI_AGENT_ARCHITECTURE.md`, `06_DATA_ARCHITECTURE.md`, `07_TECHNICAL_ARCHITECTURE.md`

---

# 1. Purpose

This document defines the semantic knowledge model that the SEO Research & Strategy Copilot uses to understand a business, its market, its entities, its search environment, its topics, its website, and the relationships between them.

The SEO Knowledge Model is the semantic foundation of the Decision Engine.

It defines:

* what the system knows
* how knowledge is represented
* how concepts relate
* how search behavior is represented
* how business reality is connected to search reality
* how evidence is attached to knowledge
* how uncertainty is represented
* how knowledge changes over time
* how agents retrieve and reason over knowledge
* how recommendations are derived from knowledge

The knowledge model must be broader than keyword research.

The system is not intended to become:

> `Keywords → Keywords → Keywords`

It must become:

> `Business → Entities → Attributes → Topics → Search Needs → Queries → SERPs → Pages → Relationships → Decisions`

---

# 2. Core Principle

SEO knowledge is a structured representation of the domain and its search ecosystem.

It is not:

* a collection of prompts
* a keyword spreadsheet
* a list of URLs
* a collection of embeddings
* a collection of AI-generated topics
* a static content calendar

The system should represent meaningful relationships between concepts.

A simplified representation is:

```text
Business
   ↓
Entities
   ↓
Attributes / Values
   ↓
Topics
   ↓
Search Needs
   ↓
Queries / Keywords
   ↓
SERPs
   ↓
Pages
   ↓
Content
   ↓
SEO Decisions
```

These relationships form the semantic substrate on which agents operate.

---

# 3. Knowledge Model Objective

The model must allow the system to answer questions such as:

* What does this business actually offer?
* Who are its relevant audiences?
* Which entities define its domain?
* What attributes describe those entities?
* Which topics emerge from those entities?
* Which search needs exist around those topics?
* How are users expressing those needs?
* What intent appears behind those searches?
* What does the current SERP indicate?
* Which competitors satisfy those needs?
* Which pages currently satisfy those needs?
* Which pages should exist?
* Which topics belong together?
* Which topics should remain separate?
* Where are content gaps?
* Where may cannibalization exist?
* Which internal links are semantically justified?
* Which opportunities deserve prioritization?
* What evidence supports each recommendation?
* How confident should the system be?
* What changed since the previous analysis?

---

# 4. Knowledge as a Graph

The conceptual model is graph-oriented.

Nodes represent meaningful objects.

Edges represent relationships.

Example:

```text
Entity: Hotel
      │
      ├── has_attribute → Location
      │
      ├── has_attribute → Price
      │
      ├── has_attribute → Amenities
      │
      ├── related_to → Destination
      │
      └── satisfies → Search Need
                              │
                              └── expressed_as → Query
                                                   │
                                                   └── produces → SERP
```

The underlying persistence may use relational structures, vector retrieval, and graph-compatible relationships.

A graph representation is a semantic abstraction, not a requirement that the MVP use a dedicated graph database.

---

# 5. Knowledge Model Layers

The knowledge model should be understood in layers:

```text
Layer 1 — Business Reality
Layer 2 — Domain / Entity Reality
Layer 3 — Semantic Reality
Layer 4 — Search Reality
Layer 5 — Website Reality
Layer 6 — Competitive Reality
Layer 7 — Evidence Reality
Layer 8 — Decision Reality
```

These layers are related but must not be conflated.

---

# 6. Business Reality

Business reality represents what the organization actually is and does.

It may contain:

* business
* brand
* products
* services
* markets
* audiences
* locations
* business models
* commercial priorities
* differentiators
* constraints
* offerings

Example:

```text
Business
 ├── offers → Product
 ├── serves → Audience
 ├── operates_in → Market
 ├── located_in → Geography
 └── differentiated_by → Attribute
```

---

# 7. Search Reality

Search reality represents what users actually search for and what the search environment currently returns.

It may contain:

* queries
* keywords
* search contexts
* intents
* SERPs
* result types
* page types
* competitors
* search features
* trends
* volatility

Search reality must not be inferred solely from business assumptions.

---

# 8. Business Reality vs Search Reality

The system must explicitly distinguish:

```text
Business Reality
```

from:

```text
Search Reality
```

Example:

A company may sell:

```text
Premium Hotel Packages
```

while users may search:

```text
best hotels in Istanbul
```

The business concept and the search expression are related but not identical.

The system must model the relationship rather than forcing one to equal the other.

---

# 9. Audience Model

Audience represents relevant users or user segments.

Possible properties include:

* audience type
* characteristics
* needs
* constraints
* motivations
* stage
* geography
* experience level

Audience should be modeled as a contextual entity rather than a simplistic demographic label.

---

# 10. User Need / Journey

A search query is an expression of a user need.

The system should therefore represent the underlying:

```text
Need
```

separately from:

```text
Query
```

Example:

```text
Need:
Find an affordable hotel in Paris

Possible queries:
- cheap hotels in Paris
- affordable hotels Paris
- best budget hotels Paris
- Paris hotels under €100
```

Different queries may express substantially the same underlying need.

---

# 11. Entity

An entity is a distinct concept, object, person, organization, product, place, service, or other identifiable unit of meaning.

Examples:

```text
Hotel
Paris
Hilton
Air France
Business Class
Laptop
MacBook Pro
SEO
Search Intent
```

Entities are not synonymous with keywords.

A keyword is a search expression.

An entity is a semantic object represented by that expression.

---

# 12. Entity Types

The system should support extensible entity types.

Examples:

```text
Organization
Brand
Product
Service
Person
Place
Destination
Category
Concept
Technology
Event
Document
Website
Page
Audience
Market
Feature
Attribute
Metric
```

Entity types must be extensible without requiring architectural redesign.

---

# 13. Entity Identity

Each entity should have:

* stable internal ID
* canonical name
* entity type
* aliases
* descriptions
* identifiers where available
* source references
* confidence
* lifecycle state

Example:

```yaml
entity:
  id: ent_123
  canonical_name: Paris
  type: place
  aliases:
    - Paris, France
    - City of Paris
```

---

# 14. Entity Resolution

The system must distinguish:

```text
same entity
```

from:

```text
similar entity
```

and:

```text
ambiguous entity
```

Example:

```text
Apple
```

may refer to:

* Apple Inc.
* apple fruit

The system must not merge them without sufficient evidence.

---

# 15. Entity Resolution Evidence

Resolution may use:

* exact identifiers
* canonical names
* aliases
* context
* descriptions
* relationships
* source evidence
* semantic similarity

No single similarity score should automatically determine identity in ambiguous cases.

---

# 16. Entity Lifecycle

Entities may have states:

```text
candidate
identified
validated
merged
deprecated
archived
```

Historical identity changes must be preserved.

---

# 17. Entity Relationships

Entities may be related through typed relationships.

Examples:

```text
offers
belongs_to
located_in
part_of
contains
uses
compatible_with
competes_with
alternative_to
related_to
depends_on
serves
targets
```

Relationships should have explicit semantics.

---

# 18. Relationship Confidence

Relationships may be:

```text
observed
inferred
estimated
recommended
human_approved
```

Example:

```yaml
relationship:
  subject: Product_A
  predicate: compatible_with
  object: Product_B
  status: inferred
  confidence: 0.82
```

---

# 19. EAV Model

The Entity–Attribute–Value model is a core representation mechanism.

Conceptually:

```text
Entity → Attribute → Value
```

Example:

```text
Hotel Paris
    → star_rating
    → 5

Hotel Paris
    → located_in
    → Paris
```

The model allows the knowledge base to represent heterogeneous attributes without requiring a rigid schema for every domain.

---

# 20. Attribute

An attribute describes a property, characteristic, behavior, or relationship associated with an entity.

Examples:

```text
price
location
capacity
brand
material
rating
availability
language
category
```

Attributes may themselves be modeled as entities where useful.

---

# 21. Value

A value represents the concrete value associated with an attribute.

Values may be:

* text
* number
* boolean
* date
* duration
* measurement
* entity reference
* structured object

Example:

```text
Product
 → weight
 → 1.4 kg
```

---

# 22. Typed Values

Values should preserve type information.

Bad:

```text
price = "100"
```

Preferred:

```yaml
attribute: price
value:
  type: monetary
  amount: 100
  currency: EUR
```

Typed values improve validation and reasoning.

---

# 23. Temporal Values

Some attributes change over time.

Example:

```text
price
availability
rating
ranking
search volume
competitor status
```

These must support temporal validity.

Example:

```yaml
value:
  valid_from: 2026-08-01
  valid_until: 2026-08-31
```

---

# 24. Topic

A topic is a meaningful thematic area that organizes related concepts, needs, entities, questions, and search expressions.

A topic is not merely a keyword.

Example:

```text
Topic:
Business Class Flights
```

may include:

```text
business class tickets
business class benefits
business class baggage
business class lounge
business class vs economy
```

---

# 25. Topic vs Entity

An entity is a semantic object.

A topic is a thematic area around which information and search needs can be organized.

Example:

```text
Entity:
Business Class

Topic:
Business Class Flights
```

An entity may participate in multiple topics.

---

# 26. Topic vs Keyword

A keyword is an observed or candidate search expression.

A topic represents a broader semantic unit.

Example:

```text
Topic:
Budget Hotels in Paris

Keywords:
cheap hotels paris
budget hotels paris
affordable hotels paris
cheap accommodation paris
```

One topic may contain many expressions.

---

# 27. Topic vs Page

A topic is a knowledge/search concept.

A page is a website information asset.

A topic may map to:

* one page
* multiple pages
* an existing page
* a proposed page
* no page yet

The mapping must be decided rather than assumed.

---

# 28. Topic Identity

Each topic should have:

* stable ID
* canonical label
* description
* parent relationships
* related entities
* associated search needs
* associated queries
* associated intents
* evidence
* status
* confidence

---

# 29. Topic Relationships

Supported conceptual relationships include:

```text
parent_of
child_of
supports
related_to
complements
alternative_to
prerequisite_for
broader_than
narrower_than
overlaps_with
distinct_from
```

These relationships enable topical-map construction.

---

# 30. Topic Granularity

Topics exist at different granularities.

Example:

```text
Travel
  ↓
Hotels
  ↓
Hotels in Paris
  ↓
Budget Hotels in Paris
  ↓
Hotels in Paris under €100
```

The system must not assume that the deepest topic should always become a separate page.

---

# 31. Topic Validity

A topic candidate should be evaluated against:

* semantic coherence
* business relevance
* search evidence
* user need
* distinctness
* potential page usefulness
* evidence quality

A topic with no meaningful purpose should not automatically enter the final topical map.

---

# 32. Search Query

A query represents an actual or observed search expression.

Examples:

```text
cheap hotels paris
best seo agency
how to choose a laptop
```

Queries are search expressions, not semantic objects.

---

# 33. Keyword

The system may retain the conventional SEO concept of keyword for compatibility with existing SEO data sources.

However:

> Keyword is a data representation of search language, not the primary semantic unit of the system.

Keywords should therefore be attached to:

* topics
* search needs
* intents
* entities
* SERPs

rather than existing as isolated records.

---

# 34. Query Canonicalization

Queries may differ lexically while expressing similar meaning.

The system should support:

```text
raw query
normalized query
canonical search expression
```

Example:

```text
"best hotels in paris"
"best paris hotels"
"top hotels paris"
```

These may be related but must not automatically be collapsed into one record without evidence.

---

# 35. Search Context

Intent and query meaning depend on context.

Search context may include:

* geography
* language
* device
* time
* season
* user stage
* query modifiers
* SERP environment
* business context

The same query can represent different needs in different contexts.

---

# 36. Intent

Intent represents the underlying purpose or information need behind a search.

Common categories may include:

```text
informational
navigational
commercial investigation
transactional
local
comparison
support
```

The system should support multi-dimensional intent rather than forcing every query into one simplistic label.

---

# 37. Intent Dimensions

Intent may include:

```text
goal
journey_stage
commerciality
specificity
urgency
locality
content_need
action_required
```

Example:

```yaml
intent:
  goal: comparison
  commerciality: high
  journey_stage: evaluation
  locality: local
```

---

# 38. Intent Evidence

Intent should be inferred from multiple signals:

* query semantics
* modifiers
* SERP composition
* page types
* result features
* user journey
* historical behavior
* business context

Entity-oriented search research similarly models search intents as structured knowledge associated with entities and query expressions rather than treating intent as a free-floating label.

---

# 39. SERP

A SERP is an observed search-result environment for a specific query and context at a specific time.

It may contain:

* organic results
* ads
* featured snippets
* maps
* shopping
* video
* news
* AI-generated search features
* other search features

A SERP is an observation, not a permanent truth.

---

# 40. SERP Observation

Every SERP observation should preserve:

```text
query
context
timestamp
provider
location
language
device
results
features
```

This enables historical comparison.

---

# 41. SERP Features as Signals

SERP features can provide signals about:

* intent
* query type
* content format
* commerciality
* locality
* user need

They should be treated as evidence, not absolute rules.

---

# 42. Search Intent vs SERP

Intent is a semantic interpretation.

SERP is an observed search environment.

Therefore:

```text
SERP → evidence for intent
```

not:

```text
SERP = intent
```

---

# 43. Page

A page is a website information asset identified by a URL or proposed URL.

A page may be:

```text
existing
proposed
archived
redirected
duplicate
canonical
```

Pages belong to the website reality layer.

---

# 44. Page Role

A page may have a role such as:

```text
homepage
category
product
service
landing
article
guide
comparison
directory
location
support
transactional
```

Page role is not the same as intent.

---

# 45. Content

Content is the information expressed on a page.

The system may model:

* sections
* claims
* entities
* topics
* attributes
* questions
* answers
* media
* structured data

Content should be connected to the knowledge model.

---

# 46. Page–Topic Relationship

A page may:

```text
targets
supports
covers
mentions
partially_covers
conflicts_with
```

a topic.

Example:

```text
Page A
   └── targets → Topic X
   └── supports → Topic Y
   └── mentions → Entity Z
```

---

# 47. Page–Intent Relationship

A page may satisfy one or more intent dimensions.

The relationship should include confidence.

Example:

```yaml
page_intent:
  page: page_123
  intent: commercial_investigation
  confidence: 0.91
```

---

# 48. Competitor

A competitor is an entity relevant to competitive search or business analysis.

Competitors may be:

```text
direct business competitors
search competitors
content competitors
SERP competitors
```

These categories must not be conflated.

---

# 49. Search Competitor vs Business Competitor

A website ranking for the same query is not necessarily a direct business competitor.

Example:

```text
Wikipedia
```

may compete for visibility without competing commercially.

The system should therefore represent:

```text
business_competitor
```

separately from:

```text
serp_competitor
```

---

# 50. Evidence

Evidence is a source or observation supporting a claim.

Examples:

* website page
* SERP observation
* search API result
* structured database
* business input
* analytics
* Search Console
* competitor page
* human decision

Evidence must preserve provenance.

---

# 51. Evidence Source

Every evidence item should contain, where available:

```text
source
source_type
retrieved_at
observed_at
location/context
provider
content/reference
reliability
```

---

# 52. Claim

A claim is a proposition about the domain.

Example:

```text
"Topic A and Topic B appear to satisfy the same search need."
```

Claims may be:

```text
observed
inferred
estimated
recommended
human_approved
```

---

# 53. Claim–Evidence Relationship

Claims should reference their supporting evidence.

```text
Claim
 ├── supported_by → Evidence A
 ├── supported_by → Evidence B
 └── contradicted_by → Evidence C
```

This enables conflict detection.

---

# 54. Recommendation

A recommendation is an AI-generated or rule-generated proposed action.

Examples:

```text
create_page
merge_pages
split_topic
improve_page
create_internal_link
investigate
defer
reject
```

A recommendation is not automatically a decision.

---

# 55. Decision

A decision is an authorized strategic conclusion.

Possible states:

```text
proposed
under_review
approved
rejected
superseded
cancelled
```

Human-approved decisions should be preserved as first-class knowledge.

---

# 56. Decision Provenance

A decision should reference:

```text
recommendation
evidence
decision factors
actor
timestamp
affected objects
previous decision
```

This creates a decision history.

---

# 57. Opportunity

An opportunity represents a potentially valuable SEO action or strategic possibility.

Examples:

```text
missing page
underdeveloped topic
high-value query cluster
competitor advantage
internal-link opportunity
SERP format opportunity
```

Opportunity should combine evidence rather than rely on a single metric.

---

# 58. Opportunity Scoring

Opportunity scoring may consider:

```text
business relevance
search demand
intent fit
competitive difficulty
current coverage
SERP opportunity
conversion potential
strategic priority
confidence
freshness
```

The exact scoring algorithm belongs to the Decision Engine specification.

The knowledge model stores the factors and evidence.

---

# 59. Content Gap

A content gap represents meaningful missing or insufficient coverage.

A gap may exist when:

```text
Business-relevant need
+
Search evidence
+
Insufficient website coverage
```

Competitor presence alone is insufficient to establish a meaningful gap.

---

# 60. Gap Types

The system should distinguish:

```text
topic_gap
entity_gap
attribute_gap
intent_gap
journey_gap
page_gap
content_depth_gap
SERP_format_gap
internal_link_gap
```

---

# 61. Cannibalization

Cannibalization represents a potential conflict where multiple pages compete for substantially overlapping search needs.

Possible signals:

* overlapping intents
* overlapping topics
* SERP overlap
* similar page roles
* ranking volatility
* query overlap
* semantic similarity

No single signal should automatically prove cannibalization.

---

# 62. Cannibalization States

```text
possible
probable
confirmed
resolved
false_positive
```

Confirmation may require human validation depending on impact.

---

# 63. Internal Link

An internal link represents a relationship between two pages.

It should be modeled semantically.

Example:

```text
Page A
   └── links_to → Page B
```

The relationship may include:

```text
supports
explains
expands
alternative_to
next_step
prerequisite
related
```

---

# 64. Link Recommendation

A recommended link should include:

```yaml
recommendation:
  source_page: page_a
  target_page: page_b
  relationship: expands
  rationale: ...
  confidence: 0.87
```

This allows the Internal Linking Agent to reason from semantic relationships.

---

# 65. Journey Model

A user journey represents a sequence of needs.

Example:

```text
Learn
 ↓
Explore
 ↓
Compare
 ↓
Evaluate
 ↓
Choose
 ↓
Purchase
 ↓
Use
 ↓
Support
```

Topics and pages may satisfy different stages.

---

# 66. Journey vs Intent

Intent represents the purpose of a specific search.

Journey represents the broader sequence of user needs.

Example:

```text
Journey:
Choose a laptop

Intent:
Compare MacBook vs Dell

Query:
macbook vs dell laptop
```

These concepts should remain separate.

---

# 67. Semantic Coverage

Coverage represents how well a website addresses relevant knowledge and search needs.

Coverage may include:

```text
entity coverage
attribute coverage
topic coverage
intent coverage
journey coverage
query coverage
page coverage
```

Coverage must not be reduced to keyword count.

---

# 68. Knowledge Relationships

A simplified relationship graph may look like:

```text
Business
   │
   ├── serves → Audience
   ├── operates_in → Market
   ├── offers → Product / Service
   │
   ▼
Entities
   │
   ├── has_attribute → Attribute / Value
   ├── related_to → Entity
   │
   ▼
Topics
   │
   ├── expressed_as → Query
   ├── satisfies → Search Need
   ├── has_intent → Intent
   │
   ▼
SERP
   │
   ├── contains → Search Result
   ├── signals → Intent
   └── includes → Competitor
   │
   ▼
Pages
   │
   ├── covers → Topic
   ├── satisfies → Intent
   ├── mentions → Entity
   └── links_to → Page
   │
   ▼
Decisions
   │
   ├── create
   ├── merge
   ├── improve
   ├── link
   └── defer
```

---

# 69. Knowledge States

All important knowledge should distinguish its epistemic state.

The baseline states are:

```text
OBSERVED
INFERRED
ESTIMATED
RECOMMENDED
HUMAN_APPROVED
```

These states must not be treated as interchangeable.

---

# 70. Observed

Observed means directly obtained from a source or system.

Example:

```text
SERP result #1 = example.com
```

---

# 71. Inferred

Inferred means derived through analysis.

Example:

```text
Query likely has commercial investigation intent.
```

---

# 72. Estimated

Estimated means calculated or approximated using incomplete or probabilistic data.

Example:

```text
Estimated opportunity value.
```

---

# 73. Recommended

Recommended means the system proposes an action.

Example:

```text
Recommend creating a dedicated comparison page.
```

---

# 74. Human Approved

Human approved means a qualified human has explicitly accepted the conclusion or action.

This is the highest authority for strategic project decisions unless later superseded.

---

# 75. Confidence

Knowledge items may carry confidence.

Confidence should be accompanied by factors.

Example:

```yaml
confidence:
  score: 0.84
  factors:
    - multiple_sources
    - strong_semantic_match
    - stable_serp_pattern
```

Confidence is not equivalent to truth.

---

# 76. Reliability

Confidence describes the system's belief in a specific conclusion.

Source reliability describes the trustworthiness or quality of the source.

They must remain separate.

```text
Source Reliability
        +
Evidence Quality
        +
Inference Strength
        ↓
Confidence
```

---

# 77. Contradictions

The knowledge model must support contradictory evidence.

Example:

```text
Source A:
Product price = €99

Source B:
Product price = €119
```

The system must not silently choose one.

It should represent:

```text
conflict_detected
```

and preserve both observations with timestamps and provenance.

---

# 78. Conflict Resolution

Resolution may use:

* source reliability
* recency
* contextual specificity
* directness
* corroboration
* human review

The resolution process must be explicit.

---

# 79. Knowledge Freshness

Knowledge has different freshness requirements.

Examples:

### Slow-changing

* entity identity
* business description

### Medium-changing

* product attributes
* competitor relationships

### Fast-changing

* prices
* SERPs
* rankings
* availability
* search features

Freshness policy must therefore be entity- and attribute-specific.

---

# 80. Temporal Knowledge

The model should support:

```text
valid_from
valid_until
observed_at
retrieved_at
superseded_at
```

This allows the system to reason about change.

---

# 81. Knowledge Versioning

Major knowledge structures should be versioned.

Examples:

```text
entity version
topic version
intent version
SERP observation version
page mapping version
decision version
```

Historical versions should remain auditable.

---

# 82. Semantic Drift

The system should detect when meaning changes over time.

Possible examples:

* search intent shifts
* SERP composition changes
* terminology changes
* product positioning changes
* competitor landscape changes
* topic relationships change

Semantic drift should trigger re-evaluation rather than silently modifying historical knowledge.

---

# 83. Search Reality Drift

Search reality may change independently from business reality.

Example:

```text
Business unchanged
        ↓
SERP changes
        ↓
Intent interpretation changes
        ↓
Opportunity changes
```

The knowledge model must support this distinction.

---

# 84. Business Reality Drift

The business may change:

```text
new product
new market
new service
new location
new audience
new positioning
```

These changes should propagate to affected knowledge and derived recommendations.

---

# 85. Dependency Graph

Knowledge objects may depend on others.

Example:

```text
Entity
 ↓
EAV
 ↓
Topic
 ↓
Intent
 ↓
SERP Analysis
 ↓
Cluster
 ↓
Page Recommendation
 ↓
Decision
```

When upstream knowledge changes, downstream results may become stale.

---

# 86. Knowledge Invalidation

The system should identify affected derived objects.

Example:

```text
Entity changed
      ↓
EAV stale
      ↓
Topic model potentially stale
      ↓
Topical map potentially stale
      ↓
Page recommendations potentially stale
```

Recomputation should be targeted rather than global whenever possible.

---

# 87. Knowledge Acquisition Pipeline

Knowledge acquisition should follow:

```text
Source
 ↓
Extraction
 ↓
Normalization
 ↓
Entity Resolution
 ↓
Relationship Extraction
 ↓
Validation
 ↓
Evidence Attachment
 ↓
Knowledge Persistence
 ↓
Derived Intelligence
```

---

# 88. Source Types

Sources may include:

```text
business input
website
search engine
SERP API
SEO API
analytics
Search Console
competitor websites
documents
structured databases
human decisions
```

---

# 89. Extraction

AI may be used to extract:

* entities
* attributes
* values
* topics
* claims
* relationships
* questions
* intents

Extraction results must remain distinguishable from source data.

---

# 90. Normalization

Normalization may include:

* name normalization
* URL normalization
* unit normalization
* language normalization
* query normalization
* entity type normalization
* category normalization

Normalization should preserve the raw source value.

---

# 91. Raw vs Canonical Knowledge

The system should preserve:

```text
Raw Observation
```

and:

```text
Canonical Representation
```

Example:

```text
Raw:
"€1,299"

Canonical:
amount = 1299
currency = EUR
```

This enables reprocessing.

---

# 92. Deduplication

Deduplication should distinguish:

```text
exact duplicate
semantic duplicate
related but distinct
ambiguous
```

Semantic similarity alone must not automatically merge records.

---

# 93. Topic Deduplication

Two topic candidates may be:

```text
same topic
closely related
different search needs
different intents
different page candidates
```

Topic merging should therefore consider:

* intent
* SERP overlap
* user need
* semantic similarity
* business role
* page usefulness

---

# 94. Knowledge Validation

Validation should occur at multiple levels.

```text
Schema Validation
 ↓
Data Validation
 ↓
Semantic Validation
 ↓
Relationship Validation
 ↓
Evidence Validation
 ↓
Domain Validation
```

---

# 95. Semantic Validation

Semantic validation asks:

* Does the relationship make sense?
* Does the entity type fit?
* Does the attribute apply to the entity?
* Is the topic coherent?
* Does the intent match the evidence?

---

# 96. Domain Validation

Domain validation checks business-specific constraints.

Example:

A company that does not sell hotels should not receive:

```text
hotel booking product
```

as an assumed business offering simply because users search for hotels.

---

# 97. Knowledge Quality Dimensions

The system should monitor:

```text
accuracy
completeness
consistency
freshness
provenance
confidence
uniqueness
relationship integrity
coverage
```

---

# 98. Knowledge Completeness

Completeness does not mean:

> store everything.

It means:

> store enough validated knowledge to support the intended decision.

The system should avoid unnecessary data accumulation.

---

# 99. Semantic Retrieval

Knowledge retrieval should support semantic similarity.

Embeddings may help retrieve:

* related entities
* similar topics
* related search needs
* similar content
* supporting evidence

But vector similarity must not replace structured relationships.

---

# 100. Hybrid Retrieval

The preferred retrieval model is:

```text
Structured Retrieval
        +
Semantic Retrieval
        +
Evidence Retrieval
```

Example:

```text
SQL filters
+
Vector similarity
+
Relationship traversal
+
Evidence ranking
```

---

# 101. Vector Embeddings

Embeddings are representations used for semantic retrieval.

They are not authoritative knowledge.

A vector should always remain associated with its source object and embedding version.

---

# 102. Embedding Versioning

When embedding models change:

```text
embedding_model_v1
embedding_model_v2
```

must remain distinguishable.

The system should support controlled re-embedding.

---

# 103. Graph-Compatible Retrieval

The system should support relationship traversal such as:

```text
Entity
 → attributes
 → related entities
 → topics
 → queries
 → SERPs
 → pages
```

This can be implemented through relational joins, recursive queries, or a future graph layer.

---

# 104. Agent Context Assembly

Agents should retrieve knowledge according to the task.

Example:

### Topic Validation

Retrieve:

```text
topic
related entities
search needs
queries
intent
SERP observations
existing pages
```

Do not automatically retrieve the entire project knowledge base.

---

# 105. Context Pack

The system may create task-specific context packages.

Example:

```yaml
context:
  objective: validate_topic
  entities: [...]
  topics: [...]
  queries: [...]
  intents: [...]
  serp: [...]
  pages: [...]
  evidence: [...]
```

---

# 106. Knowledge Reasoning Primitives

The system should support reusable reasoning primitives.

Examples:

```text
entity_similarity
entity_resolution
topic_similarity
topic_overlap
intent_alignment
serp_overlap
page_topic_fit
page_intent_fit
coverage_analysis
gap_detection
cannibalization_detection
relationship_strength
evidence_strength
opportunity_scoring
```

These primitives should combine deterministic logic with AI where appropriate.

---

# 107. Semantic Similarity

Similarity is a signal.

It is not a decision.

Example:

```text
similarity = 0.91
```

does not automatically mean:

```text
merge = true
```

The system should consider contextual and search evidence.

---

# 108. Search Need Equivalence

Two queries may be considered equivalent when they express substantially the same need.

This requires evaluating:

```text
semantic meaning
intent
SERP similarity
expected answer
user goal
```

---

# 109. Search Need Separation

Queries should remain separate when:

* intent differs
* desired answer differs
* SERPs materially differ
* user journey differs
* business action differs

This is critical for preventing bad clustering.

---

# 110. Topic Clustering Foundation

Topic clustering should operate over:

```text
topics
+
entities
+
search needs
+
queries
+
intent
+
SERPs
```

not only keywords.

The result is a semantic clustering structure rather than a lexical keyword grouping.

---

# 111. Topical Map Foundation

A topical map is a strategic representation derived from the knowledge graph.

It should reflect:

```text
entities
+
attributes
+
topics
+
relationships
+
search needs
+
intent
```

It is therefore an output of the knowledge model, not the knowledge model itself.

---

# 112. Page Architecture Foundation

Page architecture consumes knowledge about:

```text
topics
intent
search needs
existing pages
business priorities
content coverage
```

The knowledge model must not assume:

```text
one topic = one page
```

---

# 113. Internal Linking Foundation

Internal linking should use semantic relationships.

Example:

```text
Topic A
   ↓ supports
Topic B
   ↓ represented by
Page A
   ↓ links_to
Page B
```

This makes links interpretable rather than purely navigational.

---

# 114. Content Gap Foundation

Gap detection should compare:

```text
Required / valuable knowledge
        vs
Existing website coverage
```

The "required knowledge" side may be derived from:

* entities
* attributes
* user needs
* search evidence
* SERPs
* competitors
* business strategy

---

# 115. Cannibalization Foundation

Cannibalization analysis should compare pages through:

```text
Topic overlap
Intent overlap
Search-need overlap
SERP overlap
Query overlap
Page-role overlap
Historical ranking behavior
```

The knowledge model stores the relationships needed for that analysis.

---

# 116. Decision Engine Foundation

The Decision Engine should reason over:

```text
Business Reality
+
Search Reality
+
Website Reality
+
Competitive Reality
+
Evidence
+
Historical Decisions
```

This is the core transition from:

> SEO research

to:

> SEO decision intelligence.

---

# 117. Evidence Graph

A conceptual evidence graph may look like:

```text
Source
  ↓
Observation
  ↓
Claim
  ↓
Inference
  ↓
Recommendation
  ↓
Human Decision
```

Every major recommendation should be traceable through this chain.

---

# 118. Decision History

The knowledge model should preserve:

```text
what was recommended
why
what evidence existed
what human decided
when
what changed afterward
```

This allows the system to learn from historical decisions without rewriting history.

---

# 119. Human Feedback

Human actions may include:

```text
approve
reject
edit
merge
split
override
defer
mark_false_positive
```

These actions become structured knowledge.

---

# 120. Learning from Feedback

Feedback may improve:

* ranking
* thresholds
* prompts
* retrieval
* classification
* clustering
* recommendation quality

However, feedback should not automatically modify production behavior without validation.

---

# 121. Knowledge Governance

The system should define ownership for:

```text
business knowledge
entity knowledge
search observations
AI inferences
human decisions
```

Authority must be explicit.

---

# 122. Authority Hierarchy

A simplified hierarchy is:

```text
Human-approved project decision
        ↓
Validated project knowledge
        ↓
Observed source evidence
        ↓
Validated AI inference
        ↓
AI recommendation
        ↓
Unvalidated model output
```

This hierarchy should influence reasoning and conflict resolution.

---

# 123. Project Isolation

Knowledge must be isolated by:

```text
organization
workspace
project
```

A project must not accidentally retrieve another project's:

* entities
* topics
* competitors
* decisions
* evidence
* private business information

---

# 124. Knowledge Security

Sensitive knowledge must be protected through:

* authorization
* tenant isolation
* scoped retrieval
* access control
* audit logging
* secret separation

Knowledge retrieval is a security boundary.

---

# 125. Knowledge Observability

The system should be able to answer:

* Where did this entity come from?
* Why was this topic created?
* Which evidence supports this intent?
* Why was this page considered a gap?
* Which agent produced this inference?
* Which human approved this decision?
* When did this knowledge become stale?

---

# 126. Knowledge Auditability

Every material derived object should have provenance.

Example:

```yaml
derived_object:
  type: topic
  id: topic_123

provenance:
  source_entities:
    - entity_1
    - entity_2

  source_queries:
    - query_1

  source_serps:
    - serp_1

  generated_by:
    agent: topic_discovery
    version: 1.2
```

---

# 127. Knowledge Anti-Patterns

The following are prohibited:

### Keyword-Only Model

Treating keywords as the complete SEO universe.

### Topic = Keyword

Assuming every keyword is a topic.

### Topic = Page

Automatically creating a page for every topic.

### SERP = Intent

Treating one SERP observation as absolute intent truth.

### Embedding = Truth

Treating vector similarity as semantic certainty.

### AI Output = Fact

Persisting model output as authoritative without validation.

### Competitor = Business Competitor

Treating every ranking website as a commercial competitor.

### Gap = Missing Keyword

Defining gaps only through keyword absence.

### Cannibalization = Similarity

Declaring cannibalization based solely on semantic similarity.

### Static Knowledge

Assuming SEO knowledge never changes.

### No Provenance

Storing conclusions without evidence.

---

# 128. MVP Knowledge Model

The MVP should prioritize:

```text
Business
Entity
Entity Relationship
EAV
Topic
Query / Keyword
Intent
Search Context
SERP Observation
Page
Competitor
Evidence
Claim
Recommendation
Decision
Content Gap
Cannibalization
Internal Link
```

These are sufficient to establish the core SEO decision graph.

---

# 129. Future Knowledge Model

Future versions may add:

```text
knowledge graph inference
advanced journey modeling
entity evolution
semantic drift detection
automated opportunity discovery
multi-market knowledge
multi-language semantic alignment
external knowledge graph integration
advanced causal relationships
outcome modeling
SEO performance feedback
predictive opportunity modeling
```

These should extend the existing model rather than replace it.

---

# 130. Knowledge Model and International SEO

The semantic model must distinguish:

```text
entity identity
```

from:

```text
language expression
```

For example:

```text
Entity:
Hotel

English:
hotel

German:
Hotel

Persian:
هتل
```

Different linguistic expressions may refer to the same entity or concept.

---

# 131. Multilingual Knowledge

The system should support:

* canonical semantic identity
* localized labels
* localized queries
* localized intent
* localized SERPs
* language-specific evidence

Translation must not automatically imply identical search intent.

---

# 132. Market Context

The same entity can behave differently across markets.

Example:

```text
Entity:
"mobile phone"

Market A:
"smartphone"

Market B:
"handy"

Market C:
"گوشی"
```

Search behavior must remain market- and language-aware.

---

# 133. Knowledge Compression

The system should avoid storing redundant representations.

For example:

```text
1000 keywords
```

may represent:

```text
30 search needs
```

and:

```text
8 topics
```

The knowledge model should preserve both the raw expressions and the semantic abstraction.

---

# 134. Knowledge Expansion

The system may expand knowledge from:

```text
Entity
 ↓
Attributes
 ↓
Related Entities
 ↓
Topics
 ↓
Search Needs
 ↓
Queries
```

Expansion should remain bounded by relevance and evidence.

---

# 135. Knowledge Pruning

The system should also remove or deprioritize:

* irrelevant entities
* duplicate topics
* obsolete evidence
* stale recommendations
* invalid relationships
* rejected hypotheses

Historical records should generally remain preserved even when no longer active.

---

# 136. Knowledge Confidence Propagation

Confidence may propagate through derived relationships, but it should not be copied blindly.

Example:

```text
Evidence confidence
        ↓
Claim confidence
        ↓
Recommendation confidence
```

Each layer should account for additional uncertainty introduced during inference.

---

# 137. Uncertainty Propagation

If:

```text
Entity resolution = uncertain
```

then downstream:

```text
EAV
Topic
Intent
Recommendation
```

may also inherit uncertainty.

The system should make this visible.

---

# 138. Insufficient Evidence

The knowledge model must support:

```text
insufficient_evidence
```

as a valid state.

This is preferable to creating false precision.

---

# 139. Knowledge Decision Boundary

The system should distinguish:

```text
Known
Unknown
Uncertain
Conflicting
Not Applicable
Not Yet Researched
```

These states help agents decide what to do next.

---

# 140. Next-Research Recommendation

When knowledge is insufficient, the system may generate:

```text
research_needed
```

Example:

```yaml
research_needed:
  question: "Does this query have transactional intent?"
  required_evidence:
    - fresh_serp
    - page_type_distribution
```

This converts uncertainty into an actionable research task.

---

# 141. Knowledge-Driven Research

The system should not always research everything.

Instead:

```text
Current Knowledge
      ↓
Knowledge Gaps
      ↓
Research Priority
      ↓
Targeted Research
      ↓
Knowledge Update
```

This is a key mechanism for efficiency.

---

# 142. Knowledge-Driven Agent Execution

Agents should ask:

> What knowledge is required to make this decision?

rather than:

> What information can I collect?

This prevents unnecessary data accumulation.

---

# 143. SEO Knowledge as a Living System

The knowledge model should evolve continuously:

```text
Research
 ↓
Knowledge
 ↓
Decision
 ↓
Execution
 ↓
Observation
 ↓
Feedback
 ↓
Knowledge Update
```

This creates the foundation for the product's long-term "Living SEO Intelligence System" vision.

---

# 144. Core Knowledge Flow

The complete conceptual flow is:

```text
BUSINESS
   ↓
AUDIENCE / MARKET
   ↓
ENTITIES
   ↓
EAV
   ↓
TOPICS
   ↓
SEARCH NEEDS
   ↓
QUERIES
   ↓
INTENT
   ↓
SERP
   ↓
COMPETITORS
   ↓
PAGES
   ↓
COVERAGE
   ↓
GAPS / CANNIBALIZATION / OPPORTUNITIES
   ↓
RECOMMENDATIONS
   ↓
HUMAN DECISIONS
   ↓
NEW KNOWLEDGE
```

---

# 145. Final Conceptual Model

The SEO Knowledge Model can be summarized as:

```text
                       BUSINESS REALITY
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
          AUDIENCE          MARKET        OFFERINGS
                              │
                              ▼
                           ENTITIES
                              │
                     ┌────────┴────────┐
                     ▼                 ▼
                    EAV          RELATIONSHIPS
                     │                 │
                     └────────┬────────┘
                              ▼
                           TOPICS
                              │
                     ┌────────┴─────────┐
                     ▼                  ▼
                SEARCH NEEDS         JOURNEYS
                     │
                     ▼
                  QUERIES
                     │
                     ▼
                   INTENT
                     │
                     ▼
                    SERP
                     │
            ┌────────┴────────┐
            ▼                 ▼
       COMPETITORS        SERP SIGNALS
            │                 │
            └────────┬────────┘
                     ▼
                   PAGES
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       COVERAGE     LINKS     CONTENT
          │
     ┌────┴─────┐
     ▼          ▼
   GAPS   CANNIBALIZATION
     │          │
     └────┬─────┘
          ▼
     OPPORTUNITIES
          │
          ▼
    RECOMMENDATIONS
          │
          ▼
      HUMAN DECISION
          │
          ▼
   PERSISTENT KNOWLEDGE
```

---

# 146. Final Design Principles

The SEO Knowledge Model must remain:

### Semantic

It represents meaning rather than only strings.

### Structured

Important concepts have explicit types and relationships.

### Evidence-Based

Material knowledge can be traced to evidence.

### Temporal

Knowledge can change and historical states remain accessible.

### Uncertainty-Aware

Unknown and conflicting information are valid states.

### Search-Aware

Business knowledge is connected to real search behavior.

### Business-Aware

Search opportunities are evaluated against business reality.

### Page-Aware

Topics are not automatically treated as pages.

### Decision-Aware

Recommendations and decisions are distinct objects.

### Human-Governed

Human-approved decisions remain authoritative.

### Retrievable

Knowledge can be accessed through structured, semantic, and relationship-based retrieval.

### Extensible

New domains and entity types can be added without redesigning the system.

### Auditable

Important conclusions preserve provenance.

---

# 147. Relationship to Other Documents

This document is the semantic foundation for:

```text
06_DATA_ARCHITECTURE.md
    ↓
Defines persistence representation

09_ENTITY_EAV_MODEL.md
    ↓
Defines entity and EAV implementation in greater detail

10_TOPIC_MODELING_AND_CLUSTERING.md
    ↓
Defines topic construction and clustering

11_SEARCH_AND_SERP_INTELLIGENCE.md
    ↓
Defines search and SERP intelligence

12_SEO_DECISION_ENGINE.md
    ↓
Defines decision logic over this knowledge

13_AGENT_SPECIFICATIONS.md
    ↓
Defines agents operating over this model

14_AGENT_WORKFLOW.md
    ↓
Defines workflows using these knowledge objects

15_HUMAN_IN_THE_LOOP.md
    ↓
Defines human decisions and approvals

16_OUTPUT_CONTRACTS.md
    ↓
Defines machine-readable representations

25_CONTEXT_MANAGEMENT.md
    ↓
Defines how relevant knowledge is retrieved for AI context

26_SKILLS_AND_TOOLING_POLICY.md
    ↓
Defines capability acquisition used to acquire or process knowledge
```

---

# 148. Final Status

```yaml
document: 08_SEO_KNOWLEDGE_MODEL.md
status: APPROVED_AS_BASELINE_SEO_KNOWLEDGE_MODEL

purpose:
  semantic_foundation: true
  keyword_only_model: false
  decision_engine_foundation: true
  living_knowledge_system: true

core_model:
  business: true
  audience: true
  market: true
  entity: true
  relationship: true
  eav: true
  topic: true
  search_need: true
  query: true
  keyword: true
  intent: true
  search_context: true
  serp: true
  page: true
  content: true
  competitor: true
  evidence: true
  claim: true
  recommendation: true
  decision: true
  opportunity: true
  gap: true
  cannibalization: true
  internal_link: true
  journey: true

knowledge_states:
  observed: true
  inferred: true
  estimated: true
  recommended: true
  human_approved: true

quality:
  provenance: required
  confidence: required_where_meaningful
  uncertainty: supported
  contradiction_handling: required
  temporal_model: required
  versioning: required
  validation: required

retrieval:
  structured: required
  semantic: required
  relationship_based: required
  hybrid: preferred

security:
  project_isolation: required
  scoped_retrieval: required
  authorization: required
  auditability: required

architecture:
  relational_system_of_record: required
  vector_layer: supported
  graph_compatible_relationships: required
  dedicated_graph_database: not_required_for_mvp
```

---

# 149. Final Principle

> **The SEO Knowledge Model is the semantic memory of the system: it connects business reality, entities, search needs, queries, intent, SERPs, pages, evidence, and decisions into one evolving representation of what the system knows—and what it does not yet know.**
