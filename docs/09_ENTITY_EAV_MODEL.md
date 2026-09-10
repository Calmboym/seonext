# 09_ENTITY_EAV_MODEL.md

**Document:** `09_ENTITY_EAV_MODEL.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Entity & EAV Model Specification
**Status:** `APPROVED_AS_BASELINE_ENTITY_EAV_MODEL`
**Depends On:** `06_DATA_ARCHITECTURE.md`, `08_SEO_KNOWLEDGE_MODEL.md`

---

# 1. Purpose

This document defines the detailed Entity and Entity–Attribute–Value (EAV) model used by the SEO Research & Strategy Copilot.

It translates the conceptual knowledge model defined in:

`08_SEO_KNOWLEDGE_MODEL.md`

into a more precise semantic structure for:

* entity discovery
* entity identification
* entity resolution
* entity normalization
* entity relationships
* attributes
* values
* EAV facts
* semantic triples
* provenance
* confidence
* temporal validity
* multilingual representation
* contradiction handling
* entity-to-topic relationships
* entity-to-page relationships
* entity-driven SEO reasoning

The purpose is not to create an abstract ontology for its own sake.

The purpose is to give the system a reliable semantic representation of the domain on which SEO research and decisions can operate.

---

# 2. Core Principle

The system must move from:

```text
String
```

to:

```text
Meaning
```

and from:

```text
Keyword List
```

to:

```text
Entity + Attributes + Values + Relationships + Search Context
```

An entity model provides the semantic layer needed to understand what users and businesses are actually talking about.

EAV is one representation mechanism for that knowledge. It must not be treated as synonymous with the entire knowledge model.

---

# 3. What EAV Means in This System

The canonical structure is:

```text
Entity → Attribute → Value
```

Example:

```text
Entity:
Hotel

Attribute:
star_rating

Value:
5
```

Another example:

```text
Entity:
Hotel Paris

Attribute:
located_in

Value:
Paris
```

The value may itself be another entity.

Therefore EAV supports both:

```text
Entity → Attribute → Literal Value
```

and:

```text
Entity → Relationship Attribute → Entity
```

---

# 4. EAV Is Not the Entire Semantic Model

The system must distinguish:

```text
Entity
Attribute
Value
Relationship
Fact
Claim
Evidence
```

EAV is a structured representation of facts.

It does not by itself define:

* search intent
* user journeys
* SERPs
* page architecture
* business strategy
* recommendations

Those concepts build on top of the entity model.

---

# 5. Entity as the Primary Semantic Object

An entity represents a distinguishable concept or object.

Examples:

```text
Organization
Brand
Product
Service
Person
Place
Destination
Technology
Concept
Category
Feature
Event
Audience
Market
```

An entity must have an identity independent of any single keyword or textual expression.

---

# 6. Entity vs Keyword

A keyword is a search expression.

An entity is what the expression refers to.

Example:

```text
Keyword:
"iphone 17"

Entity:
Apple iPhone 17
```

The relationship may be:

```text
Query
   ↓ refers_to
Entity
```

The query should not become the entity merely because they share the same text.

---

# 7. Entity vs Topic

An entity is a semantic object.

A topic is a thematic organization of knowledge and search needs.

Example:

```text
Entity:
MacBook Pro

Topic:
MacBook Pro for Students
```

The entity may participate in many topics.

---

# 8. Entity vs Page

A page is a website asset.

An entity is a semantic object.

A page can represent or discuss an entity.

```text
Entity
   ↓ represented_by
Page
```

But:

```text
Entity ≠ Page
```

---

# 9. Entity Identity

Every canonical entity should have:

```text
entity_id
canonical_name
entity_type
status
description
aliases
language_variants
identifiers
provenance
confidence
created_at
updated_at
```

Example:

```yaml
entity:
  id: ent_123
  canonical_name: Apple Inc.
  type: organization
  status: validated
```

---

# 10. Stable Entity IDs

Entity IDs must be stable.

The system must not use:

* keyword strings
* URLs
* display names

as the primary internal identity.

A name can change.

A URL can change.

An entity ID should remain stable.

---

# 11. Entity Types

The system should support extensible entity types.

Baseline types:

```text
organization
brand
product
service
person
place
destination
technology
concept
category
feature
event
audience
market
website
page
document
```

Additional domain-specific types may be introduced.

---

# 12. Entity Type Governance

New entity types should not be created casually.

A new type should be introduced when:

1. the semantic distinction is meaningful
2. existing types are insufficient
3. downstream reasoning benefits from the distinction
4. validation rules can be defined

Otherwise, the system should prefer existing types.

---

# 13. Entity Status

Entities may have lifecycle states:

```text
candidate
identified
validated
merged
deprecated
archived
```

These states describe the entity lifecycle, not its truth value.

---

# 14. Candidate Entity

A candidate entity is an entity discovered from:

* business research
* website content
* search data
* competitor research
* documents
* AI extraction

but not yet sufficiently validated.

Example:

```yaml
entity:
  name: "Example CRM"
  status: candidate
```

---

# 15. Validated Entity

A validated entity has sufficient evidence for the system to treat its identity as established within the project context.

Validation does not mean every attribute of the entity is known.

---

# 16. Entity Description

Descriptions should explain the semantic identity of the entity.

A description should not simply repeat the name.

Example:

```text
Apple Inc. is a technology company that develops consumer
electronics, software, and digital services.
```

Descriptions should have provenance where externally sourced or AI-derived.

---

# 17. Aliases

Entities may have multiple names.

Example:

```yaml
entity:
  canonical_name: "International Business Machines"
  aliases:
    - IBM
    - IBM Corp.
```

Aliases are expressions referring to the same entity.

---

# 18. Alias vs Related Entity

The system must distinguish:

```text
alias
```

from:

```text
related entity
```

Example:

```text
IBM
```

is an alias for:

```text
International Business Machines
```

whereas:

```text
IBM Watson
```

may be a separate entity related to IBM.

---

# 19. Multilingual Entity Names

An entity can have language-specific labels.

Example:

```yaml
entity:
  canonical_id: ent_123

  labels:
    en: Hotel
    de: Hotel
    fa: هتل
```

The semantic identity remains the same where evidence supports equivalence.

---

# 20. Translation vs Entity Equivalence

Translation does not automatically prove that two expressions represent the same search concept.

For example, two terms may be linguistic translations but have different:

* market meaning
* commercial usage
* search intent
* product scope

The system must preserve language-specific search evidence.

---

# 21. External Identifiers

Where reliable identifiers exist, they may be attached.

Examples include identifiers from:

* Wikidata
* official product catalogs
* internal business systems
* authoritative databases

External IDs should be treated as evidence for identity, not blindly as truth.

---

# 22. External Identifier Model

Example:

```yaml
identifiers:
  - namespace: wikidata
    value: Q12345

  - namespace: internal_catalog
    value: PROD-987
```

Identifiers must retain their namespace.

---

# 23. Entity Resolution

Entity resolution determines whether two observations refer to:

```text
the same entity
```

or:

```text
different entities
```

or:

```text
an unresolved entity
```

---

# 24. Entity Resolution States

The system should support:

```text
same
different
possible_same
ambiguous
unresolved
```

---

# 25. Entity Resolution Signals

Resolution may use:

```text
name similarity
alias matching
external identifiers
context
description
relationships
attributes
domain
URL
organization information
location
language
source authority
```

No single signal should dominate automatically in ambiguous cases.

---

# 26. Entity Resolution Workflow

```text
Observation
   ↓
Candidate Retrieval
   ↓
Similarity Analysis
   ↓
Context Comparison
   ↓
Identifier Check
   ↓
Relationship Comparison
   ↓
Confidence Assessment
   ↓
Resolution
```

---

# 27. Entity Resolution Example

Suppose the system encounters:

```text
"Apple"
```

Possible entities:

```text
Apple Inc.
Apple fruit
Apple Records
```

The system should use surrounding context to resolve the reference.

Example:

```text
"Apple released a new iPhone"
```

strongly supports:

```text
Apple Inc.
```

---

# 28. Ambiguous Entity Handling

If evidence is insufficient:

```yaml
resolution:
  status: ambiguous
  candidates:
    - ent_1
    - ent_2
  confidence: low
```

The system must not silently select one.

---

# 29. Entity Merge

Two entities may be merged only when sufficient evidence establishes that they represent the same canonical object.

A merge must preserve:

* original IDs
* source observations
* aliases
* provenance
* historical relationships

---

# 30. Entity Merge Record

Example:

```yaml
merge:
  surviving_entity: ent_123
  merged_entities:
    - ent_456
  reason: "Confirmed same organization"
  evidence:
    - evidence_789
```

---

# 31. Entity Split

An incorrectly merged entity may need to be split.

Example:

```text
Apple
```

was incorrectly treated as one entity.

The system may split it into:

```text
Apple Inc.
Apple fruit
```

Historical provenance must remain intact.

---

# 32. Entity Relationship

A relationship connects two entities.

Conceptually:

```text
Subject → Predicate → Object
```

Example:

```text
Apple Inc.
   → develops
iPhone
```

---

# 33. Relationship Types

Baseline relationship categories:

### Hierarchical

```text
is_a
part_of
contains
subcategory_of
```

### Associative

```text
related_to
compatible_with
alternative_to
complements
used_with
```

### Business

```text
offers
manufactures
serves
targets
competes_with
```

### Geographic

```text
located_in
operates_in
available_in
```

### Semantic

```text
describes
represents
mentions
supports
```

---

# 34. Relationship Direction

Relationships should be directional when semantics require direction.

Example:

```text
Company
   → offers
Service
```

is not identical to:

```text
Service
   → offers
Company
```

The model must preserve subject and object.

---

# 35. Symmetric Relationships

Some relationships may be symmetric.

Example:

```text
A related_to B
```

may imply:

```text
B related_to A
```

The system should explicitly declare whether a relationship is symmetric.

---

# 36. Relationship Inference

Some relationships may be inferred.

Example:

```text
Product
   → belongs_to
Category
```

could imply:

```text
Product
   → related_to
Category
```

Inferred relationships must be marked as inferred rather than presented as observed facts.

---

# 37. Relationship Strength

Relationships may carry strength.

Example:

```yaml
relationship:
  subject: ent_1
  predicate: related_to
  object: ent_2
  strength: 0.82
```

Strength must have a documented interpretation.

It must not be confused with confidence.

---

# 38. Relationship Confidence

Confidence answers:

> How confident are we that this relationship is correct?

Strength may answer:

> How strongly are the two entities related for a particular analytical purpose?

These concepts should remain separate.

---

# 39. Relationship Evidence

Every material inferred relationship should reference evidence.

Example:

```yaml
relationship:
  subject: entity_a
  predicate: compatible_with
  object: entity_b

  evidence:
    - evidence_123
    - evidence_456
```

---

# 40. Relationship Lifecycle

Relationships may be:

```text
candidate
observed
inferred
validated
deprecated
rejected
```

---

# 41. Attribute

An attribute describes a property of an entity.

Examples:

```text
price
weight
location
capacity
color
category
rating
availability
material
language
```

---

# 42. Attribute Identity

Attributes should have stable identifiers.

Example:

```yaml
attribute:
  id: attr_123
  name: price
```

This prevents inconsistent representations such as:

```text
price
product_price
cost
amount
```

being treated as four unrelated concepts without a defined relationship.

---

# 43. Attribute Types

Attributes may represent:

```text
numeric
text
boolean
date
datetime
duration
measurement
monetary
enumeration
entity_reference
list
structured
```

---

# 44. Attribute Domain

An attribute may have an expected entity domain.

Example:

```text
price
```

may apply to:

```text
Product
Service
Offer
```

but may not meaningfully apply to:

```text
Country
```

without additional context.

---

# 45. Attribute Range

Attributes may also constrain the type of value they accept.

Example:

```text
located_in
```

may expect:

```text
Place
```

rather than:

```text
numeric
```

---

# 46. Attribute Ontology

Attributes may themselves have relationships.

Example:

```text
price
   → type_of
monetary_attribute
```

This enables reusable semantic rules.

---

# 47. Attribute Synonyms

Attributes may have aliases.

Example:

```text
price
aliases:
  - cost
  - pricing
  - rate
```

But synonyms must be validated within the domain.

"Rate" can have different meanings depending on context.

---

# 48. Value

A value is the concrete state associated with an attribute.

Example:

```text
Entity:
Product A

Attribute:
weight

Value:
1.4 kg
```

---

# 49. Literal Values

Values may be literal:

```text
100
true
"Paris"
2026-09-01
```

But literal values should retain semantic typing.

---

# 50. Entity Values

Values may reference other entities.

Example:

```text
Hotel A
   → located_in
Paris
```

Here:

```text
Paris
```

is an entity rather than a literal string.

---

# 51. Typed Value Representation

Preferred representation:

```yaml
value:
  type: monetary
  amount: 99
  currency: EUR
```

rather than:

```yaml
value: "€99"
```

---

# 52. Measurement Values

Measurements should preserve:

```text
amount
unit
normalized_unit
```

Example:

```yaml
value:
  type: measurement
  amount: 1.4
  unit: kg
  normalized:
    amount: 1400
    unit: g
```

---

# 53. Date and Time Values

Dates and times should preserve timezone and precision where relevant.

Example:

```yaml
value:
  type: datetime
  value: "2026-09-05T10:30:00+02:00"
```

---

# 54. Range Values

Some facts are ranges.

Example:

```text
Price: €100–€150
```

Representation:

```yaml
value:
  type: range
  min: 100
  max: 150
  currency: EUR
```

---

# 55. List Values

Attributes may contain multiple values.

Example:

```text
Hotel
 → amenities
 → [WiFi, Pool, Gym]
```

Each value should remain individually addressable when useful.

---

# 56. EAV Fact

An EAV fact represents a specific assertion:

```text
Entity + Attribute + Value
```

Example:

```yaml
fact:
  entity: hotel_123
  attribute: star_rating
  value: 5
```

---

# 57. Fact Metadata

Every material fact should support:

```text
fact_id
entity_id
attribute_id
value
source
observed_at
valid_from
valid_until
status
confidence
provenance
```

---

# 58. Fact Provenance

Example:

```yaml
fact:
  entity: product_123
  attribute: price
  value:
    amount: 1299
    currency: EUR

  provenance:
    source: website_456
    retrieved_at: 2026-09-05T08:00:00Z
```

---

# 59. Observed Fact

An observed fact comes directly from a source.

Example:

```text
Website states:
Price = €1,299
```

This should be stored as:

```text
observed
```

rather than inferred.

---

# 60. Inferred Fact

An inferred fact is derived.

Example:

```text
Product A
belongs to
Premium Product Category
```

if that classification was derived from several signals.

The fact must be marked:

```text
inferred
```

---

# 61. Estimated Fact

An estimated value may be derived from incomplete data.

Example:

```text
estimated_market_size
```

The model must preserve the estimated nature of the value.

---

# 62. Human-Approved Fact

A human may validate an inferred relationship or attribute.

Example:

```yaml
fact:
  status: human_approved
  approved_by: human_actor
```

This creates an explicit authority boundary.

---

# 63. Fact Status vs Confidence

Status and confidence are different.

Example:

```text
status = inferred
confidence = 0.95
```

means:

> The system is highly confident this is an inference.

It does not mean the fact is human-approved.

---

# 64. Temporal Facts

Facts may change.

Example:

```text
Product price:
€999 in January
€1099 in February
€1199 in March
```

The system should preserve each observation.

---

# 65. Fact History

Historical facts should not be overwritten.

Preferred:

```text
Fact A
valid_until → February

Fact B
valid_from → February
```

rather than replacing Fact A.

---

# 66. Contradictory Facts

The system may hold:

```text
Product A
price
€999

Product A
price
€1099
```

at overlapping times.

This is not automatically a database error.

It may indicate:

* different markets
* different currencies
* different offers
* stale information
* conflicting sources

---

# 67. Conflict Context

Facts should preserve context where relevant:

```text
market
country
language
currency
device
date
customer_segment
source
```

This can explain apparent contradictions.

---

# 68. Fact Conflict Resolution

The system may rank competing facts using:

```text
source reliability
recency
specificity
context match
corroboration
human validation
```

But the losing fact should generally remain historically available.

---

# 69. Entity Graph

The entity layer can be represented as:

```text
Entity
  │
  ├── Attribute → Value
  │
  ├── Relationship → Entity
  │
  ├── Evidence
  │
  └── Search / Topic Associations
```

---

# 70. Example Entity Graph

```text
                ┌──────────────┐
                │   Company    │
                └──────┬───────┘
                       │ offers
                       ▼
                ┌──────────────┐
                │   Product     │
                └──────┬───────┘
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       price         category     material
          │            │            │
          ▼            ▼            ▼
        €999         Laptop       Aluminum
                       │
                       ▼
                     Topic
                       │
                       ▼
                    Search
                       │
                       ▼
                     SERP
```

---

# 71. Entity–Topic Relationship

Entities should be connected to topics through typed relationships.

Examples:

```text
central_entity
supporting_entity
mentioned_entity
required_entity
related_entity
```

This supports topic modeling.

---

# 72. Entity–Query Relationship

A query may:

```text
refer_to
describe
compare
seek
modify
filter
```

an entity.

Example:

```text
"best hotels in Paris"

Query
 ├── refers_to → Hotel
 └── constrained_by → Paris
```

---

# 73. Entity–Intent Relationship

An entity may participate in different intents.

Example:

```text
Entity:
Laptop

Queries:
"what is a laptop?"
"best laptops"
"buy laptop"
"laptop repair"
```

The same entity participates in:

```text
informational
commercial
transactional
support
```

contexts.

---

# 74. Entity–SERP Relationship

Entities may be detected in SERP results.

The system can use this to understand:

* dominant entities
* related concepts
* competitor entities
* content patterns

These are observations rather than permanent truths.

---

# 75. Entity–Page Relationship

Pages may:

```text
represent
mention
describe
compare
support
sell
review
```

entities.

Example:

```text
Page A
 → represents → Product A
 → mentions → Brand A
 → compares_with → Product B
```

---

# 76. Primary vs Secondary Entities

A page may have:

```text
primary_entity
secondary_entities
```

The primary entity represents the main semantic subject.

Secondary entities provide context.

This distinction may be used by Page Architecture and Content analysis.

---

# 77. Entity Coverage

Entity coverage measures whether important entities in a domain are adequately represented.

Coverage may consider:

```text
entity presence
attribute completeness
relationship completeness
contextual relevance
page representation
```

Entity count alone is not a meaningful coverage metric.

---

# 78. Attribute Coverage

Attribute coverage asks:

> Are the important properties of the entity represented?

Example:

For a hotel:

```text
location
price
amenities
room types
policies
capacity
```

Missing attributes may indicate:

* content gaps
* incomplete product information
* weak semantic coverage

---

# 79. Relationship Coverage

A site may mention all required entities but fail to explain how they relate.

Example:

```text
Entity A
Entity B
```

are both present, but:

```text
A → compatible_with → B
```

is missing.

Relationship coverage may therefore be important.

---

# 80. Entity Salience

Entity salience may estimate how important an entity is within a document or topic.

Potential signals:

* prominence
* repetition
* structural placement
* contextual relevance
* relationship density
* business importance

Salience is an analytical signal, not an absolute ranking factor.

---

# 81. Entity Centrality

Within an entity graph, centrality may indicate how connected an entity is.

Example:

```text
Core Entity
   ├── related entity
   ├── attribute
   ├── product
   ├── service
   └── topic
```

Centrality may support prioritization but must not automatically determine SEO strategy.

---

# 82. Entity Importance

Entity importance may combine:

```text
business relevance
search relevance
graph centrality
user relevance
commercial importance
```

The exact scoring belongs to the Decision Engine.

---

# 83. Entity Discovery Sources

Entities may be discovered from:

```text
business input
website crawling
search queries
SERPs
competitor pages
structured data
documents
external databases
human input
LLM extraction
```

---

# 84. Entity Extraction

LLMs and NLP systems may identify candidate entities.

The extraction pipeline should be:

```text
Source
 ↓
Entity Extraction
 ↓
Normalization
 ↓
Resolution
 ↓
Validation
 ↓
Persistence
```

---

# 85. Extraction Is Not Validation

An LLM saying:

```text
"Entity X exists"
```

does not automatically establish:

```text
validated_entity
```

Extraction produces candidates.

Validation determines whether they should become trusted knowledge.

---

# 86. Entity Normalization

Normalization may include:

* capitalization
* punctuation
* whitespace
* spelling variants
* transliteration
* language forms
* abbreviations

Normalization must not erase meaningful distinctions.

---

# 87. Entity Canonicalization

Canonicalization selects a stable representation.

Example:

```text
"IBM"
"IBM Corp"
"International Business Machines"
```

may map to:

```text
International Business Machines
```

while retaining aliases.

---

# 88. Entity Deduplication

Deduplication should consider:

```text
identity
context
external IDs
relationships
attributes
aliases
```

rather than string similarity alone.

---

# 89. Semantic Duplicate vs Related Entity

Example:

```text
"SEO audit"
"technical SEO audit"
```

may be:

* related
* hierarchical
* overlapping
* distinct

The system must not automatically merge them.

---

# 90. Entity Contradictions

Entities themselves may contain contradictory attributes.

Example:

```text
Company A
founded_year = 2001

Company A
founded_year = 2004
```

Both observations should remain traceable.

---

# 91. Source Reliability

Different sources have different authority.

Possible reliability dimensions:

```text
authority
directness
freshness
specificity
consistency
independence
```

The system should store reliability metadata rather than hard-coding universal trust.

---

# 92. Evidence Hierarchy

A domain-specific hierarchy may look like:

```text
Direct business source
        ↓
Official source
        ↓
Authoritative external source
        ↓
Reliable third-party source
        ↓
Observed search evidence
        ↓
AI inference
```

The hierarchy must remain contextual.

For example, SERP observation is the authoritative source for what appeared in a specific SERP, even if it is not the authoritative source for a product's technical specification.

---

# 93. Source Context

A source should be evaluated for the specific claim it supports.

Example:

```text
Official product page
```

is strong evidence for:

```text
product specifications
```

but may not be strong evidence for:

```text
market-wide search demand
```

---

# 94. Entity Provenance

The system should preserve:

```text
where entity was discovered
how it was normalized
how it was resolved
which sources support it
which agent processed it
which version created it
```

---

# 95. Entity Versioning

Entities should support version history for material changes.

Examples:

```text
canonical name changed
type changed
relationships changed
attributes changed
identity merged
identity split
```

---

# 96. Entity Snapshot

A workflow may use a snapshot:

```yaml
entity_snapshot:
  entity_id: ent_123
  version: 7
  captured_at: 2026-09-05T08:00:00Z
```

This helps reproduce analytical decisions.

---

# 97. Entity Freshness

Entity identity may be relatively stable.

Entity attributes may be highly dynamic.

Therefore freshness should be attached primarily to facts and observations rather than assuming the entire entity becomes stale at once.

---

# 98. EAV Query Patterns

The system should support questions such as:

### Find entities with an attribute

```text
Entities where:
attribute = price
```

### Find a specific value

```text
Products where:
price < 1000 EUR
```

### Find related entities

```text
Products compatible_with Laptop_A
```

### Find incomplete EAV

```text
Products missing:
weight
material
```

---

# 99. EAV and Semantic Retrieval

EAV should work with vector retrieval.

Example:

```text
Structured filter:
entity_type = product

+
Semantic retrieval:
similar to "lightweight laptop"

+
Relationship filter:
category = laptop
```

This produces better contextual retrieval than embeddings alone.

---

# 100. EAV and Topic Discovery

Topic discovery can use EAV to identify:

```text
important attributes
attribute combinations
entity relationships
recurring questions
missing information
```

Example:

```text
Product
 ├── price
 ├── weight
 ├── battery
 └── display
```

may generate multiple search-oriented topic candidates.

---

# 101. EAV and Search Queries

Queries can express:

```text
entity
attribute
value
constraint
comparison
```

Example:

```text
"lightweight laptops under $1000"

Entity:
Laptop

Attribute:
Weight

Constraint:
Lightweight

Attribute:
Price

Value:
< $1000
```

This decomposition is useful for query understanding.

---

# 102. Query-to-EAV Mapping

The system may represent:

```yaml
query_interpretation:
  query: "5 star hotels in Paris"

  entity:
    - Hotel

  attributes:
    - star_rating

  values:
    - 5

  relationships:
    - located_in: Paris
```

This is an interpretation, not a direct transcription of the query.

---

# 103. EAV and Search Intent

Attribute/value combinations can provide intent signals.

Example:

```text
"best laptop for gaming"
```

may indicate:

```text
Entity: laptop
Use case: gaming
Intent: commercial investigation
```

The EAV representation supports intent analysis but does not determine it by itself.

---

# 104. EAV and SERP Analysis

SERP results may reveal which attributes users expect.

Example:

```text
Query:
best running shoes for flat feet

SERP pages repeatedly cover:
support
stability
cushioning
price
```

These can become candidate attribute relationships.

---

# 105. EAV and Content Gaps

If important entity attributes are repeatedly represented in SERPs but absent from a relevant page, the system may identify a potential content gap.

This requires evidence and contextual validation.

---

# 106. EAV and Cannibalization

Two pages may compete because they represent the same:

```text
entity
attribute combination
search need
intent
```

EAV can therefore support cannibalization analysis.

---

# 107. Entity Graph and Internal Linking

Internal links may be recommended where pages represent related entities.

Example:

```text
Page A
represents:
Laptop A

Page B
represents:
Laptop Accessories

Relationship:
compatible_with

Recommendation:
Page A → Page B
```

---

# 108. Entity Graph and Topical Maps

Topical maps organize topics.

Entity graphs explain the semantic objects underlying those topics.

The relationship is:

```text
Entity Graph
      ↓
Topic Discovery
      ↓
Topic Model
      ↓
Topical Map
```

The two must not be treated as interchangeable.

---

# 109. Entity Graph and Page Architecture

Page architecture can use entity structure to determine:

* primary page subjects
* supporting pages
* category boundaries
* relationships
* page differentiation

Entity structure informs page architecture but does not automatically determine it.

---

# 110. Entity Graph and Decision Engine

The Decision Engine may use:

```text
entity importance
attribute completeness
relationship strength
search demand
intent
SERP evidence
business value
page coverage
```

to make strategic recommendations.

---

# 111. Human Validation

Humans should be able to:

```text
approve entity
reject entity
merge entities
split entities
edit attributes
approve relationship
reject relationship
correct value
```

These actions must be recorded.

---

# 112. Human Correction

A human correction should not simply overwrite AI output.

It should create an auditable event:

```yaml
correction:
  object: entity_123
  field: entity_type
  previous: concept
  new: product
  reason: "Business owner clarification"
```

---

# 113. Learning from Entity Corrections

Repeated corrections may reveal:

* extraction problems
* resolution problems
* ontology weaknesses
* prompt issues
* domain-specific rules

These should become evaluation and improvement signals.

---

# 114. Entity Confidence

Confidence may be calculated from:

```text
source agreement
identifier match
context consistency
relationship consistency
attribute consistency
human validation
```

The exact scoring mechanism belongs to the Decision Engine.

---

# 115. Confidence Is Contextual

An entity may have:

```text
identity confidence = 0.99
```

but:

```text
price confidence = 0.60
```

Confidence should therefore exist at the fact/relationship level where necessary.

---

# 116. Entity Uncertainty

Valid uncertainty states include:

```text
identity_uncertain
type_uncertain
relationship_uncertain
attribute_uncertain
value_uncertain
source_conflict
```

---

# 117. Missing Knowledge

The system should distinguish:

```text
unknown
not researched
not applicable
not available
conflicting
```

Example:

```text
Product weight:
unknown
```

is not equivalent to:

```text
Product weight:
not applicable
```

---

# 118. Entity Deletion Policy

Entities should generally not be hard-deleted when historical analysis depends on them.

Preferred:

```text
deprecated
archived
superseded
merged
```

with historical relationships preserved.

---

# 119. Security and Isolation

Entity and EAV data must respect:

```text
organization
workspace
project
```

boundaries.

An entity created in Project A must not automatically appear in Project B.

---

# 120. Shared Global Entities

Some systems may eventually support globally shared entities.

If implemented, the architecture must distinguish:

```text
Global Entity
```

from:

```text
Project-specific Knowledge
```

Project-specific facts must never be overwritten by global assumptions.

---

# 121. MVP Entity Model

The MVP should support:

```text
Entity
Entity Type
Alias
Identifier
Relationship
Attribute
Typed Value
EAV Fact
Evidence
Confidence
Status
Temporal Metadata
Provenance
```

This is sufficient to establish the core semantic layer.

---

# 122. Future Entity Model

Future versions may add:

```text
ontology reasoning
advanced entity linking
external knowledge graph synchronization
entity embeddings
multi-market entity identity
entity evolution modeling
probabilistic graph inference
automated ontology induction
```

These must remain compatible with the baseline model.

---

# 123. Recommended Logical Schema

Conceptually:

```text
entities
    ↓
entity_aliases
    ↓
entity_identifiers

entities
    ↓
entity_relationships
    ↓
entities

entities
    ↓
eav_facts
    ↓
attributes
    ↓
typed_values

eav_facts
    ↓
evidence

entities
    ↓
topics
queries
pages
```

The exact database schema is governed by:

`06_DATA_ARCHITECTURE.md`

and implementation decisions belong to:

`07_TECHNICAL_ARCHITECTURE.md`.

---

# 124. Canonical EAV Example

```yaml
entity:
  id: ent_hotel_001
  canonical_name: "Example Hotel"
  type: hotel

facts:

  - attribute: star_rating
    value:
      type: integer
      value: 5
    state: observed

  - attribute: located_in
    value:
      type: entity_reference
      entity_id: ent_paris
    state: observed

  - attribute: price
    value:
      type: monetary
      amount: 180
      currency: EUR
    state: observed

  - attribute: suitable_for
    value:
      type: entity_reference
      entity_id: ent_business_traveler
    state: inferred
    confidence: 0.78
```

---

# 125. Canonical Relationship Example

```yaml
relationship:
  id: rel_001
  subject: ent_hotel_001
  predicate: located_in
  object: ent_paris

  state: observed

  evidence:
    - evidence_001

  provenance:
    source: official_hotel_website
```

---

# 126. Canonical Inferred Relationship Example

```yaml
relationship:
  id: rel_002
  subject: ent_hotel_001
  predicate: suitable_for
  object: ent_business_traveler

  state: inferred

  confidence:
    score: 0.78
    factors:
      - business_amenities
      - location
      - observed_page_content
```

---

# 127. Knowledge Lifecycle

The complete entity/EAV lifecycle is:

```text
Discover
   ↓
Extract
   ↓
Normalize
   ↓
Resolve
   ↓
Validate
   ↓
Enrich
   ↓
Attach Evidence
   ↓
Persist
   ↓
Use in Reasoning
   ↓
Monitor
   ↓
Update
```

---

# 128. Entity Quality Gates

Before an entity becomes validated:

```text
Identity Check
+
Type Check
+
Duplicate Check
+
Evidence Check
+
Context Check
```

Before an EAV fact becomes trusted:

```text
Entity Validity
+
Attribute Validity
+
Value Type Validity
+
Source Validation
+
Temporal Validation
```

---

# 129. EAV Quality Rules

The system should prevent:

* invalid attribute types
* impossible value types
* unresolved entity references
* duplicate facts without distinction
* unsupported relationships
* missing provenance for material derived facts
* silent overwrites
* cross-project leakage

---

# 130. Anti-Patterns

The following are prohibited:

### Keyword-as-Entity

Treating every keyword as an entity.

### String Matching as Identity

Merging entities because names are similar.

### EAV Without Types

Storing all values as strings.

### EAV Without Provenance

Storing facts without knowing where they came from.

### EAV Without Temporal Context

Overwriting changing values.

### Relationship Explosion

Creating meaningless links between everything.

### AI Fact Injection

Treating model-generated facts as observed facts.

### Global Contamination

Allowing project-specific facts to leak across projects.

### Similarity-Based Auto-Merge

Automatically merging entities solely because embeddings are similar.

---

# 131. Final Entity Model

The baseline semantic model is:

```text
                         ENTITY
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      ATTRIBUTES       RELATIONSHIPS     ALIASES
          │                │
          ▼                ▼
        VALUES          ENTITIES
          │
          ▼
       EAV FACTS
          │
          ▼
       EVIDENCE
          │
          ▼
      CONFIDENCE
          │
          ▼
      KNOWLEDGE
```

This semantic layer connects upward into:

```text
Entities
   ↓
Topics
   ↓
Search Needs
   ↓
Queries
   ↓
Intent
   ↓
SERPs
   ↓
Pages
   ↓
SEO Decisions
```

---

# 132. Final Design Principles

The Entity & EAV Model must remain:

### Identity-Centric

Entities have stable semantic identities.

### Relationship-Aware

Meaning comes from relationships as well as attributes.

### Typed

Values preserve their semantic types.

### Evidence-Based

Material facts have provenance.

### Temporal

Changing knowledge preserves history.

### Uncertainty-Aware

Ambiguity and conflicting evidence remain representable.

### Multilingual

Language expressions remain distinct from semantic identity.

### Search-Aware

Entities connect to queries, intent, SERPs, and pages.

### Business-Aware

Entities remain connected to real business offerings and priorities.

### Human-Governed

Important corrections and validations can be explicitly approved.

### Retrievable

The model supports structured, semantic, and relationship-based retrieval.

### Extensible

New entity types and attributes can be introduced without breaking the architecture.

---

# 133. Relationship to Other Documents

This document provides the detailed entity/EAV layer for:

```text
08_SEO_KNOWLEDGE_MODEL.md
    ↓
Defines the broader semantic knowledge model

06_DATA_ARCHITECTURE.md
    ↓
Defines persistence and data ownership

10_TOPIC_MODELING_AND_CLUSTERING.md
    ↓
Uses entities and relationships for topic construction

11_SEARCH_AND_SERP_INTELLIGENCE.md
    ↓
Connects entities to search reality

12_SEO_DECISION_ENGINE.md
    ↓
Uses entity knowledge for strategic decisions

13_AGENT_SPECIFICATIONS.md
    ↓
Defines agents operating on entity/EAV knowledge

15_HUMAN_IN_THE_LOOP.md
    ↓
Defines entity validation and correction workflows

16_OUTPUT_CONTRACTS.md
    ↓
Defines machine-readable entity/EAV outputs

25_CONTEXT_MANAGEMENT.md
    ↓
Defines retrieval of relevant entity context
```

---

# 134. Final Status

```yaml
document: 09_ENTITY_EAV_MODEL.md
status: APPROVED_AS_BASELINE_ENTITY_EAV_MODEL

core_model:
  entities: required
  entity_types: required
  aliases: required
  identifiers: supported
  relationships: required
  attributes: required
  typed_values: required
  eav_facts: required

identity:
  stable_ids: required
  entity_resolution: required
  ambiguity_handling: required
  merge_support: required
  split_support: required
  multilingual_labels: supported

knowledge:
  provenance: required
  evidence: required
  confidence: required_where_meaningful
  uncertainty: supported
  temporal_validity: required
  versioning: required
  contradiction_handling: required

seo_integration:
  topic_relationships: required
  query_relationships: required
  intent_relationships: supported
  serp_relationships: supported
  page_relationships: required
  content_gap_support: required
  cannibalization_support: required
  internal_link_support: required

retrieval:
  structured: required
  semantic: supported
  relationship_based: required
  hybrid: preferred

security:
  project_isolation: required
  scoped_access: required
  provenance: required
  auditability: required

mvp:
  dedicated_graph_database: not_required
  relational_representation: required
  vector_layer: supported
  graph_compatible_relationships: required
```

---

# 135. Final Principle

> **Entities define what the SEO system is talking about; EAV defines what is known about those entities; relationships define how they connect; evidence defines why the system believes those facts; and search context defines why that knowledge matters for SEO.**
