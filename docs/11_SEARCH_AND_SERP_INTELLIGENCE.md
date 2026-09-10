# 11 — Search and SERP Intelligence

**Document:** `11_SEARCH_AND_SERP_INTELLIGENCE.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Search Intelligence / SERP Analysis Specification
**Status:** `APPROVED_AS_BASELINE_SEARCH_AND_SERP_INTELLIGENCE`
**Authority:** Baseline specification for search acquisition, search context, SERP collection, SERP interpretation, search-intent inference, competitive search analysis, and search-reality modeling
**Depends On:** `08_SEO_KNOWLEDGE_MODEL.md`, `09_ENTITY_EAV_MODEL.md`, `10_TOPIC_MODELING_AND_CLUSTERING.md`
**Related To:** `12_SEO_DECISION_ENGINE.md`, `13_AGENT_SPECIFICATIONS.md`, `14_AGENT_WORKFLOW.md`, `16_OUTPUT_CONTRACTS.md`, `21_DEVELOPMENT_AND_DEBUG.md`, `22_TESTING_AND_VALIDATION.md`

---

# 1. Purpose

This document defines how the system collects, models, analyzes, validates, and uses search and SERP intelligence.

The Search & SERP Intelligence subsystem exists to answer:

* What are users searching for?
* In what context are they searching?
* What does the current search environment look like?
* What intent does the search environment suggest?
* What types of pages and content formats are being rewarded?
* Which entities and topics dominate the search results?
* Which competitors appear?
* How stable or volatile is the search environment?
* Which queries appear to belong together?
* Which queries appear to require separate pages?
* What opportunities or risks are visible in the current SERP?

The system must treat search data as **observed evidence about search reality**, not as an absolute representation of user intent or business value.

---

# 2. Core Principle

The search subsystem must move beyond:

```text
Keyword
↓
Search Volume
↓
Difficulty
```

toward:

```text
Query
+
Search Context
+
Search Demand
+
SERP
+
Intent Signals
+
Entity Signals
+
Content Format
+
Page Type
+
Competitive Landscape
+
Temporal Signals
+
Business Context
↓
Search Intelligence
```

Search volume remains useful, but it is only one signal.

---

# 3. Search Reality

The system must maintain a distinct representation of `Search Reality`.

Search reality consists of observed signals about how search engines respond to queries.

It may include:

```text
Queries
Search Metrics
SERPs
Ranking Results
SERP Features
Page Types
Content Formats
Entities
Intent Signals
Competitors
Search Trends
Historical SERPs
```

Search reality must remain separate from:

```text
Business Reality
```

because a query can be highly searched but strategically irrelevant to the business.

---

# 4. Search Intelligence Objectives

The subsystem must support:

1. Query discovery.
2. Query normalization.
3. Search-context modeling.
4. Search-demand analysis.
5. SERP acquisition.
6. SERP normalization.
7. SERP feature detection.
8. Search-intent inference.
9. Result-type classification.
10. Competitor identification.
11. SERP similarity analysis.
12. Query-to-query comparison.
13. SERP volatility detection.
14. Search-intent drift detection.
15. Topic validation.
16. Page-candidate validation.
17. Cannibalization analysis.
18. Content-gap discovery.
19. Opportunity analysis.
20. Historical search comparison.
21. Evidence-backed recommendations.
22. Search-data quality monitoring.

---

# 5. Search Intelligence Scope

The subsystem covers:

```text
Query Intelligence
Search Context
Search Demand
SERP Collection
SERP Analysis
Intent Signals
Result Analysis
SERP Features
Competitor Search Visibility
SERP Similarity
Search Volatility
Search Evolution
Search Evidence
```

It does not independently own:

```text
Business Strategy
Final Topic Strategy
Final Page Architecture
Final SEO Prioritization
Content Production
```

Those belong to other system layers.

---

# 6. Query

A `Query` represents a search expression.

The system must preserve:

```text
query_id
raw_query
normalized_query
language
locale
country
device
search_engine
source
observed_at
state
confidence
```

The original expression must never be discarded during normalization.

---

# 7. Raw Query vs Normalized Query

The system must preserve both:

```text
Raw Query
```

and:

```text
Normalized Query
```

Example:

```text
Raw:
Best Hotels In Paris!!!

Normalized:
best hotels in paris
```

Normalization may include:

* whitespace normalization;
* case normalization;
* punctuation handling;
* encoding normalization.

It must not remove semantic modifiers without explicit rules.

---

# 8. Query Canonicalization

Canonicalization attempts to identify semantically related search expressions.

Example:

```text
best hotels paris
best hotels in paris
top hotels in paris
best places to stay in paris
```

These may be related.

However:

```text
hotel paris
best hotel paris
cheap hotels paris
luxury hotels paris
```

may represent different:

* needs;
* audiences;
* intents;
* commercial positions;
* page requirements.

Canonicalization must therefore be evidence-driven.

---

# 9. Query Sources

Queries may come from:

```text
User Input
Business Vocabulary
Keyword Databases
Search APIs
Search Suggestions
Related Searches
SERP Features
Search Console
Analytics
Competitor Research
Website Content
Entity Expansion
EAV Expansion
Topic Expansion
AI-Generated Candidates
Human Input
```

Each query must retain its source and provenance.

---

# 10. Observed vs Generated Queries

The system must distinguish:

```text
OBSERVED_QUERY
```

from:

```text
GENERATED_QUERY
```

and:

```text
INFERRED_QUERY
```

An observed query has direct evidence.

A generated query is a hypothesis.

A generated query must not receive fabricated search metrics.

---

# 11. Search Context

Search data without context is incomplete.

A search observation should include, where available:

```text
Language
Country
Location
Device
Search Engine
Date
Time
Market
Audience
Query
```

Potentially:

```text
Personalization Context
Session Context
Seasonality
```

when legitimately available.

---

# 12. Search Context Identity

A search observation should conceptually be identified by:

```text
Query
+
Search Engine
+
Locale
+
Country
+
Device
+
Time
```

Two SERPs for the same query may represent different observations if their contexts differ.

---

# 13. Search Engine Provider

The architecture must support multiple search providers.

Conceptually:

```text
SearchProvider
├── Provider A
├── Provider B
├── Provider C
└── Future Provider
```

Provider-specific implementations must remain behind an adapter boundary.

The rest of the system should consume normalized search observations.

---

# 14. Provider Independence

The system must not embed provider-specific assumptions into:

* topic models;
* intent models;
* decision logic;
* page architecture;
* core data structures.

Provider-specific limitations must be represented explicitly.

---

# 15. Search Metrics

Potential search metrics include:

```text
Search Volume
Trend
Estimated Clicks
CPC
Competition
Impressions
CTR
Clicks
Ranking Position
Visibility
```

The system must preserve:

```text
Metric
+
Source
+
Timestamp
+
Context
+
Method
```

A metric without provenance should not be treated as verified.

---

# 16. Search Volume

Search volume is an input signal.

It must not be treated as:

```text
Demand
=
Search Volume
```

because search volume does not fully represent:

* business value;
* intent;
* conversion potential;
* relevance;
* SERP opportunity;
* audience quality;
* strategic importance.

---

# 17. Metric Provenance

Every externally sourced metric should retain:

```yaml
metric:
  name:
  value:
  unit:
  source:
  provider:
  observed_at:
  period:
  locale:
  country:
  methodology:
  confidence:
```

Provider estimates must remain identifiable as estimates.

---

# 18. Search Data Freshness

Search data must have freshness metadata.

Different signals require different refresh frequencies.

Example:

```text
SERP
→ High Frequency

Rankings
→ High Frequency

Search Trends
→ High Frequency

Search Volume
→ Medium Frequency

Keyword Difficulty
→ Medium Frequency

Historical Topic Data
→ Low/Medium Frequency
```

The exact refresh schedule belongs to operational configuration.

---

# 19. SERP Definition

A `SERP` is a structured observation of the search-result environment returned for:

```text
Query
+
Search Context
+
Timestamp
```

A SERP should contain:

```text
Query
Search Context
Timestamp
Provider
Organic Results
Paid Results
SERP Features
Result Metadata
Intent Signals
Entity Signals
Content Format Signals
```

---

# 20. SERP Snapshot

Every collected SERP should be treated as a snapshot.

Conceptually:

```yaml
serp_snapshot:
  serp_id:
  query_id:
  search_context:
  provider:
  observed_at:
  results:
  features:
  metadata:
  raw_source:
```

A later SERP observation must not silently overwrite an earlier snapshot.

---

# 21. Raw SERP Data

Where provider terms permit, the system should preserve raw SERP evidence.

Raw data provides:

* auditability;
* debugging;
* reprocessing;
* parser validation;
* historical comparison.

The normalized model should be derived from raw evidence where possible.

---

# 22. Normalized SERP

The system should transform provider-specific data into a normalized structure.

Example:

```text
Raw Provider Response
        ↓
Parser
        ↓
Normalized SERP
        ↓
SERP Features
        ↓
Result Classification
        ↓
Intent / Topic / Competitive Signals
```

Provider-specific fields may remain available as extensions.

---

# 23. SERP Result

Each result should contain, where available:

```text
result_id
position
url
domain
title
snippet
result_type
page_type
content_type
entity_signals
topic_signals
feature_membership
source
observed_at
```

The system should preserve enough evidence to reproduce important conclusions.

---

# 24. Result Position

Position should be represented carefully.

The system must distinguish:

```text
Organic Position
```

from:

```text
Absolute SERP Position
```

because SERPs may contain non-organic features.

Example:

```text
Ad
AI Feature
Organic Result
Organic Result
```

The first organic result is not necessarily the first visible element.

---

# 25. SERP Features

The model must support extensible SERP features.

Examples:

```text
Organic Results
Paid Results
Featured Snippet
People Also Ask
Knowledge Panel
Local Pack
Maps
Images
Videos
News
Shopping
Related Searches
Top Stories
Direct Answers
Other Search Features
```

The system must not assume that this list is permanent.

---

# 26. SERP Feature Metadata

A feature may contain:

```text
feature_type
position
size
source_urls
entities
queries
observed_at
visibility
```

Where exact visual measurements are unavailable, the system should represent the limitation rather than fabricate precision.

---

# 27. SERP Composition

The system should characterize the composition of a SERP.

Example:

```text
Organic Results:
10

Commercial Features:
Shopping

Informational Features:
People Also Ask

Local Features:
None

Media Features:
Images + Videos
```

This becomes an intent and opportunity signal.

---

# 28. Result-Type Classification

Results should be classified where possible.

Examples:

```text
Blog Article
Guide
Product Page
Category Page
Service Page
Landing Page
Homepage
Comparison
Review
Forum
Video
Tool
Directory
Marketplace
News
Documentation
```

Classification should retain confidence.

---

# 29. Page-Type Classification

The system should separately classify the architectural role of a result.

Example:

```text
Page Type:
Product

Content Format:
Product Detail

Intent Signal:
Transactional
```

Page type and content format are related but not identical.

---

# 30. Content Format

Content format may include:

```text
Listicle
Guide
How-To
Tutorial
Comparison
Review
Definition
Product Detail
Category
Landing Page
Tool
Calculator
Forum Discussion
Video
News Article
```

The system should detect dominant formats.

---

# 31. SERP Intent Signals

Intent should be inferred from multiple signals.

Potential signals include:

```text
Query Wording
Result Types
Page Types
Content Formats
SERP Features
Ranking Entities
Commercial Elements
Local Elements
Search Context
Historical SERPs
```

Intent classification should not rely solely on query modifiers.

---

# 32. Intent as a Distribution

A query may have multiple plausible intents.

The system should support:

```yaml
intent:
  primary:
  secondary:
  distribution:
    informational:
    commercial:
    transactional:
    navigational:
    local:
  confidence:
```

This prevents forced single-label classification.

---

# 33. Dominant Intent

A `Dominant Intent` represents the strongest currently observed intent signal.

Example:

```text
Query:
best CRM software

Dominant:
Commercial Investigation

Secondary:
Transactional

Confidence:
0.87
```

The dominant intent is an inference from evidence.

---

# 34. Mixed Intent

Some SERPs may contain several result types.

Example:

```text
Informational Results
+
Commercial Comparisons
+
Product Pages
```

The system should classify the SERP as mixed-intent when appropriate.

Possible representation:

```text
MIXED
```

with an intent distribution.

---

# 35. Intent Confidence

Confidence should depend on:

```text
SERP Consistency
Result-Type Consistency
Content-Format Consistency
Query Signals
Historical Stability
Search Context
```

Low consistency should reduce confidence.

---

# 36. Search Intent Drift

Intent may change over time.

Example:

```text
2025:
Informational

2026:
Commercial Investigation
```

The system must support detecting and representing this change.

It should not overwrite historical intent observations.

---

# 37. SERP Volatility

SERP volatility describes meaningful changes in observed search results over time.

Potential signals:

```text
Ranking URL Changes
Domain Changes
Page-Type Changes
SERP Feature Changes
Intent Distribution Changes
Result-Format Changes
```

Volatility should be measured relative to a defined observation window.

---

# 38. Volatility vs Intent Drift

These are different.

```text
SERP Volatility
=
Results changed.

Intent Drift
=
The meaning or expected result pattern appears to have changed.
```

A SERP can be volatile without intent changing.

Intent can gradually drift while individual results change incrementally.

---

# 39. Historical SERP Analysis

The system should support:

```text
SERP Snapshot A
       ↓
SERP Snapshot B
       ↓
SERP Snapshot C
```

and compare:

```text
Result Changes
Feature Changes
Intent Changes
Competitor Changes
Page-Type Changes
```

This supports temporal search intelligence.

---

# 40. SERP Similarity

SERP similarity compares two queries based on their observed search-result environments.

Possible signals:

```text
URL Overlap
Domain Overlap
Page-Type Overlap
Entity Overlap
Content-Format Overlap
Intent Similarity
SERP Feature Similarity
```

---

# 41. Query-to-Query SERP Similarity

SERP similarity can help answer:

> Should these queries potentially be represented by the same page?

Example:

```text
Query A
best running shoes

Query B
top running shoes
```

If their SERPs strongly overlap and intent is aligned, they may represent one page opportunity.

This is evidence, not an automatic decision.

---

# 42. SERP Similarity Thresholds

Thresholds must be configurable.

Conceptually:

```text
High Similarity
→ Strong consolidation signal

Medium Similarity
→ Review

Low Similarity
→ Likely separate search targets
```

Thresholds should be calibrated against real project data.

---

# 43. SERP Similarity and Topic Clustering

SERP similarity is one input to `10_TOPIC_MODELING_AND_CLUSTERING.md`.

The relationship is:

```text
Query
↓
SERP
↓
SERP Similarity
↓
Topic/Query Relationship
```

SERP similarity should not replace semantic/entity analysis.

---

# 44. SERP Similarity and Page Mapping

For page mapping, SERP similarity becomes particularly important.

Conceptually:

```text
High Semantic Similarity
+
High Intent Similarity
+
High SERP Similarity
+
Shared User Need
=
Strong Page Consolidation Candidate
```

The final page decision belongs to Page Architecture.

---

# 45. Competitor Intelligence

SERPs reveal search competitors.

The system should distinguish:

```text
Business Competitor
```

from:

```text
Search Competitor
```

A website may compete with a business in SERPs without being a direct commercial competitor.

---

# 46. Search Competitor

A `Search Competitor` is a domain, website, page, or entity that repeatedly competes for visibility for relevant queries.

Possible metrics:

```text
Query Overlap
Visibility
Ranking Distribution
Topic Coverage
Intent Coverage
SERP Presence
```

---

# 47. Competitor Entity vs Competitor Domain

The model should support:

```text
Organization
Domain
Subdomain
Page
Product
```

because competitive analysis may occur at different levels.

---

# 48. Competitor SERP Coverage

Competitor coverage may be represented as:

```text
Competitor
↓
Topics
↓
Queries
↓
SERPs
↓
Rankings
```

This enables topic-level competitive analysis.

---

# 49. Search Landscape

The system should be able to construct a search landscape:

```text
Query Universe
      ↓
Topic Universe
      ↓
SERP Universe
      ↓
Competitor Universe
      ↓
Page-Type Distribution
      ↓
Intent Distribution
```

This provides a strategic view of the search market.

---

# 50. Search Opportunity

Search opportunity represents a potential opening in the current search environment.

Possible signals:

```text
Business Relevance
Search Demand
Intent Fit
SERP Weakness
Competitive Strength
Content Quality Distribution
Existing Website Authority
Coverage Gap
```

Search opportunity is not identical to business opportunity.

---

# 51. SERP Weakness

A SERP may exhibit potential weakness when relevant results appear to have:

```text
Poor Intent Match
Weak Coverage
Outdated Content
Poor UX
Incomplete Information
Low Entity Coverage
Weak Format Match
Limited Topical Depth
```

Such observations must be evidence-backed.

The system must not declare a SERP "weak" simply because the user's page does not rank.

---

# 52. SERP Strength

A SERP may indicate strong competition through:

```text
Highly Relevant Results
Strong Domains
Stable Rankings
High-Quality Content
Strong Intent Alignment
Rich SERP Features
Strong Commercial Players
```

Strong SERP conditions should affect opportunity scoring.

---

# 53. Search Saturation

The system may estimate how saturated a query/topic is.

Potential signals:

```text
Strong Competitor Coverage
Stable Top Results
High Domain Strength
Low SERP Differentiation
Limited Result Diversity
```

Saturation is an analytical estimate and must carry uncertainty.

---

# 54. Search Diversity

The system should also measure result diversity.

For example:

```text
10 Results
=
10 Distinct Domains
```

versus:

```text
10 Results
=
3 Dominant Domains
```

This can provide competitive and SERP-structure signals.

---

# 55. SERP Result Diversity

Result diversity may consider:

```text
Domain Diversity
Page-Type Diversity
Content-Format Diversity
Entity Diversity
Intent Diversity
```

Low diversity may indicate a highly constrained search environment.

High diversity may indicate broader opportunity or mixed intent.

---

# 56. Search Landscape by Topic

For each topic, the system should be able to summarize:

```text
Queries
Intent Distribution
SERP Types
Page Types
Competitors
Search Demand
SERP Features
Volatility
Existing Coverage
```

This becomes an important input to topical strategy.

---

# 57. Search Landscape by Entity

Entity-centered search intelligence may include:

```text
Entity Queries
Entity Attributes
Entity Comparisons
Entity Alternatives
Entity Locations
Entity Problems
Entity Use Cases
Entity Commercial Queries
```

This connects search intelligence to the Entity/EAV model.

---

# 58. Entity-Query Relationship

A query may concern:

```text
Primary Entity
Secondary Entity
Attribute
Relationship
Need
```

Example:

```text
"best hotels near Eiffel Tower"

Primary Entity:
Hotels

Secondary Entity:
Eiffel Tower

Need:
Find suitable accommodation near a landmark
```

The relationship should be represented explicitly where possible.

---

# 59. Attribute-Driven Search

Attributes can generate search behavior.

Example:

```text
Product
├── Price
├── Size
├── Color
├── Material
└── Compatibility
```

Potential searches:

```text
cheap product
large product
blue product
leather product
product compatible with X
```

The system should connect these searches to EAV knowledge.

---

# 60. Search Journey

Queries may be connected into a journey.

Example:

```text
What is X?
   ↓
How does X work?
   ↓
Best X
   ↓
X vs Y
   ↓
Buy X
```

The search subsystem should identify potential journey relationships where evidence supports them.

---

# 61. Search Journey vs Intent

The system must preserve:

```text
Intent
=
Purpose of a specific search

Journey
=
Progression across multiple needs/searches
```

A user can move through multiple intent states within one journey.

---

# 62. Query Modifiers

Modifiers may provide intent clues.

Examples:

```text
what
how
why
guide
best
vs
review
alternative
price
buy
near me
login
```

These are signals, not deterministic rules.

The system must always allow SERP evidence to override simplistic modifier assumptions.

---

# 63. Modifier Limitations

A query containing:

```text
best
```

is not automatically commercial.

A query containing:

```text
how
```

is not automatically informational.

A query containing:

```text
buy
```

is a strong transactional signal, but context still matters.

The classifier must combine multiple signals.

---

# 64. Search Context and Localization

Search intelligence must be locale-aware.

The same query may produce different:

```text
SERP
Intent
Competitors
Result Types
Search Volume
Topics
```

across different markets.

Therefore:

```text
Query + Locale
```

must be treated as a distinct analytical context where required.

---

# 65. Multilingual Search Intelligence

The system must support:

```text
Language
Locale
Country
Search Engine
```

A translated query must not automatically inherit the original query's:

* search volume;
* intent;
* SERP;
* competitor set;
* page strategy.

Each locale requires appropriate evidence.

---

# 66. Search Engine Result Localization

Location may influence:

```text
Local Results
Businesses
Maps
Products
News
Language
SERP Features
```

The system should preserve location context where available.

---

# 67. Device Context

Search behavior and SERP presentation may vary by device.

The system should support:

```text
Desktop
Mobile
Tablet
Other
Unknown
```

Device-specific observations should not automatically overwrite one another.

---

# 68. Search Data Quality

Every search dataset should be evaluated for:

```text
Completeness
Freshness
Consistency
Provider Reliability
Locale Accuracy
Query Accuracy
SERP Parsing Accuracy
Duplicate Rate
Missing Fields
```

---

# 69. Search Provider Failure

If a search provider fails:

```text
Provider Failure
↓
Record Failure
↓
Retry According to Policy
↓
Fallback Provider if Authorized
↓
Otherwise Mark Data Unavailable
```

The system must never fabricate SERP data.

---

# 70. Partial SERP Data

If only partial SERP information is available, the system must explicitly record:

```text
PARTIAL_SERP
```

and identify missing components.

For example:

```text
Organic Results:
Available

SERP Features:
Unavailable

Paid Results:
Unavailable
```

Downstream agents must know the evidence limitation.

---

# 71. Stale Search Data

Stale search data should not silently appear current.

Every observation must include:

```text
observed_at
```

and where appropriate:

```text
freshness_status
```

Possible states:

```text
FRESH
AGING
STALE
UNKNOWN
```

---

# 72. Search Data Conflicts

Conflicts may occur between providers.

Example:

```text
Provider A:
Search Volume = 10,000

Provider B:
Search Volume = 6,500
```

The system should preserve both observations.

It may derive:

```text
ESTIMATED_RANGE
```

but must not falsely claim one value is objectively correct without evidence.

---

# 73. Search Evidence

A search conclusion should be traceable to:

```text
Query
Search Context
SERP Snapshot
Provider
Timestamp
Result Set
Analysis Version
```

This enables auditing.

---

# 74. Search Claim

Examples:

```text
"The query is primarily commercial."

"Query A and Query B likely represent the same page opportunity."

"Competitor X dominates this topic."

"The SERP has shifted toward product pages."

"This query currently has mixed intent."
```

Each claim must retain supporting evidence.

---

# 75. Search Intelligence State

Search-derived conclusions should use the project's epistemic states:

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

```text
SERP Result:
OBSERVED

Intent:
INFERRED

Search Volume:
ESTIMATED

Page Consolidation:
RECOMMENDED
```

---

# 76. SERP Analysis Pipeline

The canonical pipeline is:

```text
Query
 ↓
Search Context
 ↓
Provider Request
 ↓
Raw SERP
 ↓
Normalization
 ↓
Result Classification
 ↓
SERP Feature Extraction
 ↓
Entity / Topic Extraction
 ↓
Intent Analysis
 ↓
SERP Similarity
 ↓
Competitive Analysis
 ↓
Historical Comparison
 ↓
Search Intelligence
```

---

# 77. Search Intelligence Enrichment

Search intelligence should enrich the shared knowledge model.

Example:

```text
SERP
 ↓
Entities
 ↓
Topics
 ↓
Intent
 ↓
Competitors
 ↓
Page Types
 ↓
Relationships
```

These relationships must be persisted with provenance.

---

# 78. SERP-to-Topic Feedback

SERP analysis may reveal new topics.

Example:

```text
Query
 ↓
SERP
 ↓
Repeated Entity
 ↓
New Attribute
 ↓
Candidate Topic
```

The new topic should enter the topic-discovery lifecycle rather than being silently inserted as validated knowledge.

---

# 79. SERP-to-Entity Feedback

SERPs may reveal entities missing from the current entity model.

The system should be able to propose:

```text
NEW_ENTITY_CANDIDATE
```

with evidence.

The Entity Agent or relevant workflow then resolves and validates it.

---

# 80. Search-to-EAV Feedback

SERPs can reveal attributes associated with an entity.

Example:

```text
Entity:
Hotel

Repeated SERP Attributes:
Breakfast
Pool
Parking
Family Rooms
Location
```

These may become candidate EAV facts or attribute concepts.

Again:

```text
SERP Observation
≠
Verified Entity Fact
```

---

# 81. SERP-to-Page Mapping

Search intelligence should provide evidence for:

```text
Expected Page Type
Expected Content Format
Expected Scope
Expected Intent
Expected Entity Coverage
```

The final page architecture decision remains outside this subsystem.

---

# 82. Existing Page Evaluation

An existing page can be compared against a SERP.

Potential dimensions:

```text
Intent Alignment
Page Type Alignment
Content Format Alignment
Entity Coverage
Topic Coverage
SERP Feature Opportunities
Competitive Position
```

This supports optimization decisions.

---

# 83. Cannibalization Signals

Search intelligence may identify potential cannibalization when:

```text
Multiple Internal Pages
+
Same / Similar Queries
+
Same Intent
+
Same SERP
+
Overlapping Topic
```

This is evidence for a cannibalization analysis, not automatic proof.

---

# 84. Content Gap Signals

Search intelligence may reveal:

```text
Important Query
+
Relevant Topic
+
Strong Search Evidence
+
No Appropriate Existing Page
```

This can become a content-gap candidate.

---

# 85. Page Opportunity Signals

A page candidate becomes stronger when:

```text
Query Cluster
+
Shared Intent
+
Strong SERP Overlap
+
Coherent Topic
+
Business Relevance
+
Insufficient Existing Coverage
```

The Decision Engine ultimately determines priority.

---

# 86. Search Opportunity Matrix

A useful intermediate structure is:

| Query/Topic | Intent        | SERP Pattern | Competition | Existing Coverage | Business Relevance | Opportunity |
| ----------- | ------------- | ------------ | ----------- | ----------------- | ------------------ | ----------- |
| Topic A     | Commercial    | Comparison   | Medium      | Low               | High               | High        |
| Topic B     | Informational | Guides       | High        | High              | Medium             | Low         |
| Topic C     | Transactional | Product      | Medium      | None              | High               | High        |
| Topic D     | Mixed         | Mixed        | High        | Medium            | High               | Review      |

This is an analytical artifact, not the final decision.

---

# 87. Search Intelligence Confidence

Confidence should be calculated from evidence quality.

Potential factors:

```text
Data Completeness
Provider Reliability
SERP Stability
Result Consistency
Classification Agreement
Historical Agreement
Context Accuracy
```

Confidence must be separate from opportunity score.

---

# 88. Search Intelligence Explainability

The system should explain important conclusions through concise evidence.

Example:

```text
Conclusion:
Queries A and B likely map to one page.

Evidence:
- 8/10 overlapping ranking URLs
- same dominant intent
- same page format
- shared core entity
- same user need

Confidence:
0.91
```

The system should not expose private chain-of-thought.

---

# 89. Search Intelligence Output

A conceptual output structure:

```yaml
search_intelligence_result:
  project_id:
  query:
  search_context:
  observations:
    - query:
      metrics:
      serp:
      intent:
      competitors:
      features:
  relationships:
    - type:
      source:
      target:
      confidence:
  opportunities:
    - type:
      score:
      evidence:
  warnings:
    - type:
      message:
  provenance:
  version:
```

The canonical machine-readable contract belongs to `16_OUTPUT_CONTRACTS.md`.

---

# 90. Batch Search Analysis

The system should support analyzing many queries efficiently.

Batch processing should include:

```text
Query Deduplication
Context Grouping
Provider Batching
Caching
Parallel Collection
Rate Limiting
Failure Isolation
Result Normalization
```

A failure for one query must not invalidate unrelated queries.

---

# 91. Caching

Search data may be cached when:

* freshness requirements permit;
* provider terms permit;
* the query/context match;
* the cached observation is clearly marked.

Cache entries must not be presented as fresh observations when they are stale.

---

# 92. Rate Limits

Search providers may impose:

```text
Request Limits
Concurrency Limits
Daily Quotas
Credit Limits
```

The integration layer must enforce these constraints.

The search intelligence layer must receive explicit failure states rather than fabricated results.

---

# 93. Cost Control

Search acquisition may be expensive.

The orchestrator should support:

```text
Query Prioritization
Deduplication
Caching
Batching
Progressive Analysis
Selective SERP Depth
Provider Routing
```

The system should not collect expensive SERPs unnecessarily.

---

# 94. Search Acquisition Strategy

A practical strategy is:

```text
Broad Discovery
↓
Cheap Filtering
↓
High-Value Query Selection
↓
SERP Acquisition
↓
Deep Analysis
```

This reduces cost while preserving strategic quality.

---

# 95. Progressive SERP Analysis

Not every query requires identical analysis depth.

Possible levels:

```text
LEVEL 1
Basic SERP Snapshot

LEVEL 2
Result + Intent Analysis

LEVEL 3
Entity + Topic + Competitor Analysis

LEVEL 4
Historical + Similarity + Strategic Analysis
```

The orchestrator chooses the appropriate level based on task requirements.

---

# 96. Search Intelligence Agents

Potential specialized modules include:

```text
Query Discovery Agent
Search Data Agent
SERP Collection Agent
SERP Parsing Agent
Intent Agent
SERP Analysis Agent
Competitor Intelligence Agent
Search Similarity Agent
Search Trend Agent
```

These remain modular capabilities under the central orchestrator.

---

# 97. Agent Boundaries

Agents should not independently redefine:

```text
Entity Taxonomy
Topic Taxonomy
Intent Taxonomy
Business Strategy
Page Architecture Rules
```

They enrich and analyze the shared knowledge model.

---

# 98. Search Intelligence Workflow

A complete conceptual workflow:

```text
Receive Task
      ↓
Load Business Context
      ↓
Load Relevant Topics / Entities
      ↓
Acquire Query Set
      ↓
Normalize Queries
      ↓
Resolve Search Context
      ↓
Prioritize Queries
      ↓
Collect Search Data
      ↓
Collect SERPs
      ↓
Normalize SERPs
      ↓
Extract Features
      ↓
Classify Results
      ↓
Infer Intent
      ↓
Analyze Competitors
      ↓
Calculate SERP Similarity
      ↓
Compare Historical Data
      ↓
Detect Gaps / Risks / Opportunities
      ↓
Validate
      ↓
Persist Evidence
      ↓
Return Structured Output
```

---

# 99. Search Intelligence Failure Modes

The system must explicitly handle:

```text
Provider Failure
Rate Limit
Timeout
Malformed Response
Missing SERP
Partial SERP
Wrong Locale
Stale Data
Duplicate Data
Conflicting Providers
Parser Failure
Entity Ambiguity
Intent Ambiguity
SERP Volatility
Insufficient Evidence
```

Each failure should produce a structured status.

---

# 100. No-Fabrication Rule

The system must never invent:

```text
Search Volume
SERP Results
Ranking Positions
Competitor Presence
SERP Features
Search Trends
Provider Data
```

If unavailable:

```text
UNKNOWN
```

If incomplete:

```text
PARTIAL
```

If estimated:

```text
ESTIMATED
```

---

# 101. Search Intelligence Testing

Testing should cover:

### Query Tests

```text
Normalization
Canonicalization
Duplicate Detection
Locale Handling
Modifier Handling
```

### SERP Tests

```text
Parsing
Position Extraction
Feature Detection
Result Classification
Missing Fields
```

### Intent Tests

```text
Single Intent
Mixed Intent
Ambiguous Intent
Intent Drift
```

### Similarity Tests

```text
High Overlap
Medium Overlap
Low Overlap
False Similarity
```

### Provider Tests

```text
Timeout
Rate Limit
Malformed Response
Partial Response
Provider Conflict
```

---

# 102. Regression Testing

Historical SERP fixtures should be preserved for regression tests.

When parser or classifier logic changes, the system should verify that previously correct interpretations remain correct unless intentionally changed.

---

# 103. Search Intelligence Observability

The system should monitor:

```text
Provider Success Rate
SERP Collection Latency
Provider Cost
Query Throughput
Cache Hit Rate
Parse Failure Rate
Missing Data Rate
Intent Confidence
SERP Volatility
Classification Error Rate
```

---

# 104. Auditability

A search-intelligence result should be traceable to:

```text
Task
Query
Search Context
Provider
Raw Observation
Normalized Observation
Analysis Version
Model Version
Rules Version
Timestamp
```

This enables debugging and reproducibility.

---

# 105. Search Intelligence and Human Review

Human review may be required when:

```text
Intent Confidence is Low
SERP is Highly Mixed
Providers Conflict
Topic Boundary is Ambiguous
Page Mapping is Unclear
Competitive Interpretation is Uncertain
Data is Incomplete
```

The system should route such cases to review rather than force an automated decision.

---

# 106. Human Corrections

Humans may correct:

```text
Query Interpretation
Intent
Entity Association
Topic Association
Competitor Classification
SERP Classification
Page-Type Classification
```

Corrections should be stored as structured feedback.

---

# 107. Learning From Search Feedback

Historical human corrections may improve:

```text
Intent Classification
Entity Resolution
Topic Clustering
SERP Interpretation
Page Candidate Detection
```

However, learned behavior must remain versioned and evaluable.

---

# 108. Search Intelligence and Topical Mapping

Search intelligence informs topical mapping through:

```text
Query Universe
Intent Distribution
SERP Patterns
Entity Relationships
Competitor Coverage
Topic Demand
Page-Type Expectations
```

The topical map must not be generated from keyword volume alone.

---

# 109. Search Intelligence and Page Architecture

Search intelligence provides evidence for:

```text
Page Type
Content Format
Intent
Scope
Query Grouping
SERP Expectations
Competitive Environment
```

The Page Architecture subsystem determines how that evidence becomes website structure.

---

# 110. Search Intelligence and Decision Engine

The Decision Engine may consume:

```text
Search Demand
Intent
SERP Opportunity
Competition
SERP Stability
Existing Coverage
Topic Relevance
Business Relevance
```

The Search subsystem provides evidence.

The Decision Engine makes the strategic recommendation.

---

# 111. Search Intelligence and Living SEO Model

Search intelligence continuously updates the living knowledge system.

Conceptually:

```text
New Search Data
      ↓
New Evidence
      ↓
Updated Search Reality
      ↓
Updated Topics / Entities / Intent
      ↓
Updated Opportunities
      ↓
Updated Decisions
```

This is a core component of the product's long-term intelligence loop.

---

# 112. Search Intelligence Data Lifecycle

The lifecycle is:

```text
DISCOVER
   ↓
COLLECT
   ↓
VALIDATE
   ↓
NORMALIZE
   ↓
ANALYZE
   ↓
ENRICH
   ↓
PERSIST
   ↓
INDEX
   ↓
COMPARE
   ↓
REFRESH
```

Raw evidence should remain available according to retention policy.

---

# 113. Search Snapshot Lifecycle

A SERP snapshot may move through:

```text
REQUESTED
   ↓
COLLECTED
   ↓
NORMALIZED
   ↓
VALIDATED
   ↓
ANALYZED
   ↓
ACTIVE
   ↓
AGING
   ↓
STALE
```

A stale snapshot remains historically valuable.

---

# 114. Search Data Retention

Retention policies should consider:

```text
Raw SERPs
Normalized SERPs
Metrics
Historical Rankings
Search Trends
Provider Responses
Analysis Outputs
```

Retention should balance:

* cost;
* auditability;
* historical intelligence;
* provider terms;
* privacy requirements.

---

# 115. Security

Search intelligence may contain proprietary strategic information.

The system must protect:

```text
Search Research
Competitor Analysis
Business Queries
Strategic Decisions
Search Console Data
Analytics Data
Provider Credentials
API Keys
```

Credentials must never be stored as ordinary search knowledge.

---

# 116. Project Isolation

Search data must be scoped to:

```text
Workspace
Project
Locale
Business
```

unless explicitly shared through an authorized mechanism.

---

# 117. Search Intelligence Quality Gates

Before a search-analysis result becomes trusted project knowledge:

```text
Query Validated
Search Context Validated
Provider Recorded
Timestamp Recorded
Data Completeness Checked
SERP Normalized
Classification Validated
Confidence Recorded
Provenance Recorded
```

---

# 118. Minimum SERP Intelligence Object

A validated SERP observation should minimally contain:

```text
serp_id
query_id
search_context
provider
observed_at
results
features
raw_evidence_reference
state
confidence
```

---

# 119. Minimum Search Intelligence Result

A meaningful analysis should minimally provide:

```text
Query
Context
SERP Observation
Intent
Result-Type Distribution
SERP Features
Competitors
Relevant Topics
Confidence
Evidence
Warnings
```

---

# 120. Anti-Patterns

The system must not:

1. Treat search volume as complete demand.
2. Treat a keyword as a page.
3. Infer intent solely from modifiers.
4. Treat one SERP observation as permanent truth.
5. Overwrite historical SERPs.
6. Fabricate missing provider data.
7. Hide provider uncertainty.
8. Treat estimated metrics as observed facts.
9. Assume identical SERPs across locales.
10. Assume identical intent across locales.
11. Treat search competitors as business competitors automatically.
12. Declare SERP weakness without evidence.
13. Declare cannibalization from keyword overlap alone.
14. Declare content gaps from keyword absence alone.
15. Treat AI-generated queries as observed demand.
16. Ignore SERP features.
17. Ignore page types and content formats.
18. Use one intent label when evidence indicates mixed intent.
19. Allow every agent to create its own search taxonomy.
20. Use stale search observations as current without labeling them.

---

# 121. MVP Scope

The MVP should support:

```text
Query Management
Query Normalization
Search Context
Search Provider Adapter
Search Metrics
SERP Collection
Raw SERP Storage
Normalized SERP
Result Classification
SERP Feature Detection
Basic Intent Classification
SERP Similarity
Competitor Detection
Evidence / Provenance
Confidence
Historical Snapshots
Basic Search Opportunity Signals
Human Validation
Caching
Rate Limiting
Failure Handling
```

The MVP should prioritize reliability and evidence quality over maximum provider coverage.

---

# 122. Future Scope

Future capabilities may include:

```text
Real-Time SERP Monitoring
Advanced SERP Change Detection
Intent Drift Detection
Search Demand Forecasting
Automated Search Opportunity Discovery
Cross-Search-Engine Comparison
AI Search / Answer Engine Visibility
Advanced Competitor Intelligence
Search Journey Modeling
Probabilistic SERP Modeling
Adaptive Query Expansion
Search Market Simulation
Automated Strategic Alerts
```

These capabilities require separate validation and authorization.

---

# 123. Definition of Done

Search & SERP Intelligence is complete for a task when:

1. Relevant queries have been collected.
2. Query provenance is preserved.
3. Search context is defined.
4. Search metrics are sourced and timestamped.
5. SERPs have been collected where required.
6. Raw evidence is retained where permitted.
7. SERPs are normalized.
8. Results are classified.
9. SERP features are identified.
10. Intent signals are analyzed.
11. Competitors are identified where relevant.
12. SERP similarity is calculated where required.
13. Historical context is considered where relevant.
14. Uncertainty is represented.
15. Missing data is explicit.
16. Important claims have evidence.
17. Output conforms to the defined contract.
18. Search intelligence is persisted.
19. Human review is triggered where required.
20. Tests cover the relevant failure and regression cases.

---

# 124. Final Search Intelligence Model

The system should understand search as:

```text
QUERY
   +
SEARCH CONTEXT
   +
SEARCH DEMAND
   +
SERP
   +
SERP FEATURES
   +
RESULT TYPES
   +
CONTENT FORMATS
   +
ENTITIES
   +
TOPICS
   +
INTENT
   +
COMPETITORS
   +
TIME
   +
HISTORICAL CHANGE
        ↓
SEARCH INTELLIGENCE
        ↓
SEARCH REALITY
```

Search intelligence then feeds:

```text
Search Reality
        +
Business Reality
        +
Semantic Knowledge
        +
Website Reality
        +
Competitive Reality
        ↓
SEO Decision Engine
```

---

# 125. Non-Negotiable Principles

1. **Search data is evidence, not absolute truth.**
2. **SERP is an observation, not a permanent state.**
3. **Query ≠ Keyword ≠ Topic ≠ Intent ≠ Page.**
4. **Search context is part of search meaning.**
5. **SERP evidence is a major intent signal.**
6. **Intent must support mixed and uncertain states.**
7. **Search volume is one signal, not strategy.**
8. **Observed data must remain distinct from inferred data.**
9. **Generated queries must never receive fabricated demand.**
10. **Historical SERPs must remain recoverable.**
11. **SERP changes must be measurable over time.**
12. **Search competitors must remain distinct from business competitors.**
13. **SERP features are part of search reality.**
14. **Page type and content format are separate analytical dimensions.**
15. **SERP similarity informs page mapping but does not automatically determine it.**
16. **Search evidence must retain provenance.**
17. **Provider failures must never produce fabricated results.**
18. **Locale and language differences must be respected.**
19. **Search intelligence provides evidence; the Decision Engine makes strategic recommendations.**
20. **Human judgment remains authoritative for strategic decisions.**

---

# 126. Final Status

```yaml
document: 11_SEARCH_AND_SERP_INTELLIGENCE.md
status: APPROVED_AS_BASELINE_SEARCH_AND_SERP_INTELLIGENCE

purpose:
  - query intelligence
  - search context modeling
  - search demand analysis
  - SERP collection
  - SERP normalization
  - SERP feature analysis
  - search intent inference
  - competitor search intelligence
  - SERP similarity
  - search volatility
  - historical search analysis
  - evidence-backed search intelligence

core_objects:
  - query
  - keyword
  - search_context
  - search_metric
  - serp
  - serp_snapshot
  - serp_feature
  - search_result
  - competitor
  - intent
  - search_observation
  - search_claim
  - search_opportunity

epistemic_states:
  - observed
  - inferred
  - estimated
  - recommended
  - human_approved
  - conflicted
  - unknown

primary_signals:
  - query
  - search_context
  - search_demand
  - serp
  - serp_features
  - result_types
  - content_formats
  - entities
  - topics
  - intent
  - competitors
  - historical_change

architecture_role:
  search_intelligence_layer

provider_model:
  strategy: provider_independent_adapter
  raw_data: preserved_where_permitted
  normalized_data: required

temporal_model:
  serp_snapshots: required
  historical_comparison: supported
  freshness_tracking: required

human_control:
  strategic_decisions: human_authoritative

next_dependencies:
  - 12_SEO_DECISION_ENGINE.md
  - 13_AGENT_SPECIFICATIONS.md
  - 14_AGENT_WORKFLOW.md
  - 16_OUTPUT_CONTRACTS.md
  - 21_DEVELOPMENT_AND_DEBUG.md
  - 22_TESTING_AND_VALIDATION.md
```

**Final Status: `APPROVED_AS_BASELINE_SEARCH_AND_SERP_INTELLIGENCE`**
