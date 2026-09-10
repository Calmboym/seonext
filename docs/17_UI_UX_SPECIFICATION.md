# 17 — UI/UX Specification

**Document:** `17_UI_UX_SPECIFICATION.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Product UI/UX Specification
**Status:** `APPROVED_AS_BASELINE_UI_UX_SPECIFICATION`
**Authority:** Baseline specification for user experience, information architecture, navigation, interaction patterns, research workspaces, decision workflows, AI interaction, evidence presentation, human review, visualization, accessibility, localization, responsive behavior, and UX quality.

---

## 1. Purpose

This document defines the user experience and interface behavior of the SEO Research & Strategy Copilot / SEO Decision Engine.

The UI must make complex SEO research understandable, inspectable, actionable, and controllable without hiding important uncertainty behind simplified dashboards.

The product is not primarily a keyword table.

It is an environment in which users can:

* understand a business and its market;
* explore entities and relationships;
* inspect attributes and values;
* discover and validate topics;
* understand search intent;
* inspect SERPs and search reality;
* cluster topics and queries;
* map topics to pages;
* design page architecture;
* identify content gaps;
* detect cannibalization;
* design internal linking;
* evaluate competitors;
* review AI-generated recommendations;
* approve, reject, modify, or defer decisions;
* inspect evidence and provenance;
* monitor workflows;
* maintain a living SEO knowledge model.

The interface must therefore represent **relationships, evidence, uncertainty, decisions, and state**, not only lists and metrics.

---

# 2. Core UX Philosophy

The product follows:

> **Human Strategy + AI Research + AI Analysis + Human Validation**

The UI must reinforce this operating model.

The system should never visually imply:

> AI discovered something → therefore it is true → therefore it is approved.

Instead, the interface should communicate:

> Evidence → Analysis → Recommendation → Review → Decision → Action → Outcome.

---

# 3. Primary UX Principles

## 3.1 Decision-first, not metric-first

The interface should help answer:

* What should we do?
* Why?
* Based on what evidence?
* How confident are we?
* What conflicts exist?
* What happens if we act?
* Has a human approved it?

Metrics support decisions; they are not the product's final purpose.

---

## 3.2 Progressive disclosure

Complex information should be revealed progressively.

Default view:

* concise;
* decision-oriented;
* visually scannable.

Expanded view:

* evidence;
* relationships;
* assumptions;
* confidence;
* methodology;
* historical context;
* raw source information.

Users should not be forced to inspect every technical detail, but important evidence must remain accessible.

---

## 3.3 Evidence before assertion

Whenever the system presents an AI-derived recommendation, users should be able to identify:

1. what was observed;
2. what was inferred;
3. what was estimated;
4. what was recommended;
5. what was approved by a human.

The UI must not collapse these states into a generic "AI insight."

---

## 3.4 Uncertainty must be visible

The interface must represent:

* high confidence;
* medium confidence;
* low confidence;
* unknown;
* conflicted;
* stale;
* incomplete.

Uncertainty is information.

It must not be hidden merely to make the interface appear cleaner.

---

## 3.5 Relationships over isolated objects

SEO knowledge is highly relational.

For example:

```text
Entity
   ↓
Attribute
   ↓
Value
   ↓
Topic
   ↓
Query
   ↓
Intent
   ↓
SERP
   ↓
Page Candidate
   ↓
Architecture
   ↓
Internal Links
```

The UI should allow users to move through these relationships naturally.

---

## 3.6 AI should feel like a copilot

AI interaction should feel contextual rather than like a generic chatbot.

The system should understand:

* current workspace;
* selected entities;
* selected topics;
* selected pages;
* current project;
* current workflow;
* available evidence;
* user permissions;
* current decision state.

The user should not need to repeatedly explain what they are looking at.

---

## 3.7 No black-box decisions

The product may automate analysis.

It must not hide consequential decisions.

Recommendations must expose decision factors and evidence.

Private model chain-of-thought must never be displayed.

Instead, provide:

* rationale summaries;
* evidence;
* decision factors;
* confidence;
* assumptions;
* conflicts;
* methodology metadata.

---

# 4. Product UX Model

The application is organized around five conceptual areas:

```text
RESEARCH
    ↓
UNDERSTAND
    ↓
PLAN
    ↓
DECIDE
    ↓
EXECUTE / MONITOR
```

A more detailed representation is:

```text
Research
├── Business Research
├── Entity Research
├── EAV
├── Topic Discovery
├── Search Intelligence
└── Competitor Intelligence

Understand
├── Intent
├── SERP
├── Topic Relationships
├── Entity Relationships
└── Search Landscape

Plan
├── Topic Clusters
├── Topical Map
├── Page Candidates
├── Page Architecture
└── Internal Linking

Decide
├── Content Gaps
├── Cannibalization
├── Opportunities
└── Decision Center

Execute / Monitor
├── Approved Actions
├── Workflow Status
├── Historical Changes
└── Outcomes
```

---

# 5. Users and Roles

The MVP should primarily support SEO professionals and strategy-oriented users.

Potential roles:

### 5.1 SEO Strategist

Primary user.

Needs:

* research;
* topic modeling;
* intent;
* SERP analysis;
* topical maps;
* page architecture;
* strategic recommendations.

---

### 5.2 SEO Manager

Needs:

* project overview;
* decision monitoring;
* approvals;
* team coordination;
* opportunity prioritization;
* progress and outcomes.

---

### 5.3 Content Strategist

Needs:

* topic universe;
* intent;
* clusters;
* page candidates;
* content gaps;
* cannibalization;
* page architecture.

---

### 5.4 Analyst

Needs:

* raw search data;
* SERP evidence;
* competitors;
* metrics;
* historical comparisons;
* exportable research.

---

### 5.5 Reviewer / Approver

Needs:

* review queue;
* evidence;
* recommendation rationale;
* confidence;
* approve/reject/modify/defer controls.

---

# 6. Workspace and Project Model

The product must support explicit project isolation.

Conceptual hierarchy:

```text
Account
└── Workspace
    └── Project
        ├── Business Model
        ├── Knowledge Model
        ├── Research
        ├── Topics
        ├── Search Intelligence
        ├── Pages
        ├── Decisions
        └── Workflows
```

The current workspace and project must always be visually identifiable.

Users must never be uncertain about which project's data they are viewing or modifying.

---

# 7. Global Application Shell

The application shell should contain:

### Primary navigation

* Overview
* Research
* Knowledge
* Search Intelligence
* Topics
* Pages
* Opportunities
* Decisions
* Workflows

### Secondary contextual navigation

Context-dependent navigation may expose:

* Entities
* EAV
* Intent
* SERP
* Clusters
* Topical Map
* Page Architecture
* Internal Linking
* Content Gaps
* Cannibalization
* Competitors

### Global utilities

* Project switcher
* Search
* AI Assistant
* Notifications
* Help
* User/account controls

---

# 8. Navigation Principles

Navigation must preserve conceptual distinctions.

The UI must not present:

```text
Keywords
Topics
Pages
Intent
SERPs
```

as if they were interchangeable objects.

Each should retain its own conceptual identity.

---

# 9. Global Search

Global search should support finding:

* entities;
* attributes;
* values;
* topics;
* keywords/queries;
* pages;
* clusters;
* decisions;
* evidence;
* workflows.

Search results should be categorized.

Example:

```text
Search: "hotel"

Entities
  Hotel

Topics
  Best hotels in Mashhad

Queries
  hotels in mashhad
  mashhad hotel booking

Pages
  /hotels/mashhad

Decisions
  Create Mashhad hotel landing page
```

---

# 10. Dashboard / Project Overview

The dashboard should answer:

> "What is happening in this SEO project, and what deserves attention?"

It should not simply display vanity metrics.

Core sections:

### Project status

* research completeness;
* knowledge completeness;
* unresolved conflicts;
* pending reviews;
* stale datasets;
* workflow status.

### Strategic opportunities

Examples:

* high-value topic without a suitable page;
* strong topic cluster with insufficient coverage;
* potential cannibalization;
* missing entity coverage;
* emerging search demand;
* competitor gap.

### Decision queue

Show:

* pending recommendations;
* high-priority decisions;
* unresolved conflicts;
* decisions awaiting evidence;
* recently approved decisions.

### Research health

Examples:

```text
Entity coverage       82%
Topic coverage        71%
Search coverage       64%
Evidence quality      High
Pending validation    12
Stale SERPs           4
```

These percentages must always have a defined methodology.

---

# 11. Research Workspace

The Research workspace is the starting point for gathering business and market intelligence.

Core areas:

* Business Research
* Entity Discovery
* EAV
* Competitor Research
* Search Research

Users should see:

```text
What we know
What we inferred
What is missing
What is uncertain
What requires validation
```

---

# 12. Business Research Workspace

The Business Research interface should allow users to define:

* business;
* products;
* services;
* audiences;
* markets;
* differentiators;
* business goals;
* commercial priorities;
* geographic scope;
* language markets.

Important distinction:

> Business importance ≠ search demand.

The interface should allow both to be viewed independently and compared.

---

# 13. Entity Explorer

The Entity Explorer provides a structured view of the project's semantic model.

Primary views:

* entity list;
* entity detail;
* entity relationships;
* entity graph;
* entity evidence.

Entity detail should contain:

```text
Entity
├── Identity
├── Types
├── Names / Aliases
├── Attributes
├── Relationships
├── Topics
├── Queries
├── SERPs
├── Pages
├── Evidence
├── Confidence
└── History
```

---

# 14. Entity Graph

The graph should visualize relationships between entities.

Example:

```text
                 Destination
                     │
             ┌───────┴───────┐
             ↓               ↓
           Hotel           Airport
             │               │
             ↓               ↓
          Location        Transportation
```

Graph interaction should support:

* zoom;
* pan;
* node selection;
* relationship filtering;
* relationship strength;
* evidence inspection;
* expanding neighbors;
* path exploration.

The graph must not become decorative.

Every visible relationship should be traceable to underlying data.

---

# 15. EAV Explorer

The EAV interface should make attribute-value relationships understandable.

Example:

```text
Entity: Hotel

Attribute          Value
--------------------------------
Location            Mashhad
Star Rating         5
Price Range         Premium
Amenities           Spa
Target Audience     Business Travelers
```

Each fact should support:

* source;
* epistemic state;
* confidence;
* timestamp;
* evidence;
* conflicting values.

---

# 16. Topic Universe

The Topic Universe represents the discovered topic space before final page decisions.

The UI should distinguish:

```text
Discovered Topics
Validated Topics
Rejected Topics
Uncertain Topics
Merged Topics
Archived Topics
```

Topic cards or rows should expose:

* topic;
* parent/child relationships;
* entities;
* business relevance;
* search evidence;
* intent;
* opportunity signals;
* status;
* confidence.

---

# 17. Topic Discovery Workspace

Topic discovery should support multiple discovery sources:

* entity-driven;
* EAV-driven;
* search-driven;
* competitor-driven;
* user-provided;
* semantic expansion;
* journey-driven.

The UI should identify the source of each discovered topic.

Example:

```text
Topic: Best hotels in Mashhad

Sources:
✓ Entity relationship
✓ Search observation
✓ Competitor coverage
✓ User input
```

---

# 18. Topic Validation Workspace

Topic validation answers:

> "Should this topic exist in our strategic topic universe?"

Possible statuses:

* VALIDATED
* REJECTED
* NEEDS_REVIEW
* DUPLICATE
* MERGED
* INSUFFICIENT_DATA
* CONFLICTED

Validation factors may include:

* business relevance;
* entity relevance;
* search evidence;
* intent coherence;
* competitive landscape;
* content opportunity;
* uniqueness;
* existing coverage.

The UI should display these as decision factors rather than pretending that a single score explains the decision.

---

# 19. Intent Workspace

Intent should be represented as a structured model.

Potential dimensions:

* informational;
* commercial investigation;
* transactional;
* navigational;
* local;
* comparison;
* exploratory;
* problem-solving;
* audience-specific;
* journey stage.

The interface should support:

* dominant intent;
* mixed intent;
* intent distribution;
* confidence;
* evidence;
* intent changes over time.

---

# 20. SERP Intelligence Workspace

The SERP workspace is evidence-centric.

Primary views:

1. Query list
2. SERP snapshot
3. SERP comparison
4. SERP features
5. Result classification
6. Competitor landscape
7. Historical SERP changes

---

# 21. SERP Snapshot

A SERP snapshot should show:

```text
Query
Search Context
Timestamp
Provider
Features
Intent Signals
Results
```

Each result should expose:

* position;
* URL;
* domain;
* title;
* snippet;
* result type;
* page type;
* content format;
* relevant entities;
* observed features.

---

# 22. SERP Comparison

Users should be able to compare two or more queries.

Example:

```text
Query A          Query B
--------------------------------
Intent: 70%      Intent: 68%
SERP overlap: 82%
Entity overlap: 76%
Page-type overlap: 91%
```

The system may recommend that queries could potentially share a page.

It must not automatically conclude that they must share a page.

---

# 23. Topic Clustering Workspace

Clustering should be visualized through multiple representations.

### List view

```text
Cluster
├── Primary topic
├── Supporting topics
├── Queries
├── Intent
├── SERP similarity
├── Entity overlap
└── Confidence
```

### Graph view

Show relationships between topics.

### Matrix view

Show similarity across topics or queries.

### Hierarchical view

Show:

```text
Parent Topic
├── Subtopic
│   ├── Topic
│   └── Topic
└── Subtopic
```

Users should be able to inspect why items were grouped.

---

# 24. Topical Map

The Topical Map is a strategic representation of the topic universe.

It should not be confused with the site's final page architecture.

The UI must explicitly distinguish:

```text
Topical Map
        ↓
Page Candidates
        ↓
Page Architecture
        ↓
Information Architecture
```

The topical map interface should allow:

* topic hierarchy;
* relationships;
* cluster boundaries;
* supporting topics;
* business importance;
* search evidence;
* validation status.

---

# 25. Page Candidate Mapping

This workspace connects topics to potential pages.

A page candidate should expose:

* candidate title/name;
* target topic;
* supporting topics;
* primary intent;
* entities;
* expected content format;
* SERP evidence;
* existing-page overlap;
* cannibalization risk;
* confidence;
* recommendation state.

Possible mapping statuses:

* UNMAPPED
* CANDIDATE
* RECOMMENDED
* APPROVED
* REJECTED
* MERGED

---

# 26. Page Architecture Workspace

Page Architecture converts strategic topic decisions into page-level structure.

The UI should support:

```text
Site
├── Section
│   ├── Parent Page
│   │   ├── Child Page
│   │   └── Child Page
│   └── Parent Page
└── Section
```

Users should be able to:

* create candidate pages;
* reorder hierarchy;
* inspect topic relationships;
* identify overlaps;
* detect missing parents;
* inspect URL implications;
* compare alternative structures.

The system should clearly distinguish:

> recommended architecture

from:

> approved architecture.

---

# 27. Internal Linking Workspace

The internal linking interface should show:

* source page;
* target page;
* relationship;
* contextual reason;
* relevance;
* anchor recommendation;
* link confidence;
* approval status.

Graph visualization is appropriate.

Users should be able to filter:

* orphan pages;
* weakly connected pages;
* high-value pages;
* excessive outbound linking;
* missing contextual links.

---

# 28. Content Gap Workspace

A content gap should be represented as a structured finding.

Example:

```text
Gap
├── Topic
├── Entity
├── Search Evidence
├── Competitor Evidence
├── Existing Coverage
├── Opportunity
├── Confidence
├── Recommendation
└── Review Status
```

The UI must distinguish:

```text
No page exists
```

from:

```text
Page exists but coverage is insufficient
```

These are different gaps.

---

# 29. Cannibalization Workspace

Cannibalization should not be represented as a binary warning alone.

The interface should expose:

* affected pages;
* overlapping topics;
* overlapping queries;
* SERP overlap;
* intent similarity;
* content similarity;
* ranking history;
* business importance;
* recommended action;
* confidence.

Possible recommendations:

* no action;
* monitor;
* differentiate;
* consolidate;
* redirect;
* restructure;
* investigate.

Any consequential action requires appropriate authorization.

---

# 30. Competitor Intelligence Workspace

Competitors should be represented at multiple levels:

```text
Business Competitor
Search Competitor
Domain Competitor
Page Competitor
Topic Competitor
```

The UI should make these distinctions explicit.

Competitor analysis may show:

* topic coverage;
* entity coverage;
* SERP visibility;
* page types;
* content formats;
* topic gaps;
* structural patterns.

The system must not imply that copying competitor coverage is automatically strategically correct.

---

# 31. Decision Center

The Decision Center is a core product surface.

It should answer:

> "What decisions require attention?"

Each decision should include:

```text
Decision
├── Question
├── Recommendation
├── Evidence
├── Decision Factors
├── Confidence
├── Conflicts
├── Impact
├── Reversibility
├── Status
└── Human Decision
```

---

# 32. Decision Statuses

Suggested statuses:

```text
DRAFT
AI_RECOMMENDED
REQUIRES_REVIEW
UNDER_REVIEW
APPROVED
REJECTED
MODIFIED
DEFERRED
SUPERSEDED
ARCHIVED
```

The UI must never label an AI recommendation as "approved" without a valid approval event.

---

# 33. Human Review Queue

The Review Queue should prioritize decisions according to:

* strategic impact;
* uncertainty;
* confidence;
* reversibility;
* potential risk;
* evidence quality;
* business importance.

Example:

```text
HIGH PRIORITY
Potential cannibalization affecting 3 strategic pages

MEDIUM
Topic candidate requires validation

LOW
Low-impact metadata recommendation
```

---

# 34. Review Interface

The review screen should provide:

### Left

Object being reviewed.

### Center

Recommendation and decision factors.

### Right

Evidence and provenance.

### Actions

* Approve
* Reject
* Modify
* Defer
* Request More Evidence
* Add Note

The reviewer should be able to understand the decision without inspecting internal model reasoning.

---

# 35. Human Decision Recording

Every consequential human decision should capture:

* user;
* timestamp;
* decision;
* previous state;
* new state;
* optional rationale;
* evidence snapshot;
* related recommendation;
* affected objects.

Human decisions are first-class project data.

---

# 36. Evidence Viewer

Evidence should be accessible throughout the application.

An evidence panel may contain:

```text
Source
Source Type
Captured At
Observation
Relevant Data
Reliability
Freshness
Used By
```

Users should be able to navigate:

```text
Recommendation
    ↓
Claim
    ↓
Evidence
    ↓
Source
```

---

# 37. Provenance UX

The UI should make provenance visible without overwhelming the user.

Use compact indicators such as:

```text
Observed
Inferred
Estimated
Recommended
Human Approved
Conflicted
Unknown
```

Clicking the indicator should reveal supporting details.

---

# 38. Confidence UX

Confidence should never be represented solely by color.

It should include:

* label;
* numeric value where appropriate;
* confidence basis;
* uncertainty factors.

Example:

```text
Confidence: Medium

Primary signals:
✓ Strong SERP overlap
✓ Same dominant intent
△ Limited historical data
△ Mixed content formats
```

---

# 39. AI Assistant

The AI Assistant should be contextual.

Example prompts:

```text
Explain this cluster.
Why was this topic validated?
Show the evidence behind this recommendation.
What conflicts exist?
Compare these two page candidates.
What information is missing?
What should I review next?
```

The assistant should know the current context.

It should not claim access to information that is not available.

---

# 40. AI Actions

AI actions should be divided into:

### Read

* inspect;
* summarize;
* compare;
* explain;
* classify.

### Analyze

* cluster;
* infer;
* score;
* detect;
* recommend.

### Propose

* create topic candidate;
* propose page;
* suggest architecture;
* propose links.

### Execute

Only permitted when explicitly authorized and policy allows it.

The UI must distinguish proposals from executed actions.

---

# 41. Workflow Monitor

The Workflow Monitor should show:

```text
Workflow
├── Status
├── Progress
├── Current Step
├── Completed Steps
├── Failed Steps
├── Waiting for Review
└── Outputs
```

Example:

```text
Business Research       ✓
Entity Discovery        ✓
EAV Extraction          ✓
Topic Discovery         ✓
Topic Validation        ●
SERP Intelligence       ○
Clustering              ○
Human Review            ○
```

---

# 42. Workflow State UX

Supported visible states should include:

* QUEUED
* RUNNING
* WAITING
* WAITING_FOR_HUMAN
* PARTIAL
* FAILED
* RETRYING
* COMPLETED
* CANCELLED
* BLOCKED

The UI must clearly distinguish:

> waiting for data

from:

> waiting for human approval.

---

# 43. Loading States

Loading states should communicate what is happening.

Avoid generic:

> Loading...

Prefer:

```text
Collecting SERP evidence...
Analyzing 42 queries...
Building topic relationships...
Waiting for search provider...
```

Where appropriate, show progress.

---

# 44. Partial Results

Partial results must be explicit.

Example:

```text
Partial Result

42 of 50 queries analyzed.

8 queries could not be analyzed because
search data was unavailable.
```

Partial output must never appear visually identical to complete output.

---

# 45. Error UX

Errors should be:

* actionable;
* understandable;
* honest;
* contextual.

Example:

```text
SERP analysis could not be completed.

Reason:
Search provider rate limit reached.

Available:
✓ 38 of 50 queries
✗ 12 queries

Actions:
Retry
Continue with partial results
Change provider
```

Never fabricate missing results.

---

# 46. Stale Data UX

Stale information should be visually identifiable.

Example:

```text
SERP Snapshot
Captured: 21 days ago
Freshness: Stale

[Refresh]
```

The UI should distinguish:

* current;
* aging;
* stale;
* expired.

Freshness rules are defined by the underlying data model and search intelligence specifications.

---

# 47. Conflict UX

When evidence conflicts, display the conflict rather than silently selecting one source.

Example:

```text
CONFLICT DETECTED

Source A:
Price = €120

Source B:
Price = €145

No trusted resolution available.

[Inspect Evidence]
[Resolve Manually]
[Keep Both]
```

---

# 48. Empty States

Empty states should explain:

1. what is missing;
2. why it matters;
3. what the user can do next.

Example:

```text
No validated topics yet.

Topic validation is required before building
the topical map.

[Validate Topics]
```

---

# 49. Tables

Tables are appropriate for:

* topics;
* queries;
* SERP results;
* pages;
* decisions;
* evidence;
* competitors.

Tables should support:

* sorting;
* filtering;
* column configuration;
* pagination/virtualization;
* bulk selection;
* status filtering;
* search;
* export where permitted.

---

# 50. Cards

Cards should be used for:

* summaries;
* opportunities;
* decision previews;
* entity summaries;
* workflow states.

Cards should not replace tables when users need high-density comparison.

---

# 51. Graphs and Visualizations

Visualizations should answer specific questions.

Good uses:

* entity relationships;
* topic relationships;
* topical maps;
* page architecture;
* internal linking;
* competitor landscape;
* SERP similarity.

Avoid decorative visualizations.

Every graph should provide:

* legend;
* filtering;
* selection;
* details;
* accessible alternative representation.

---

# 52. Visualization Interaction

Graphs should support:

* zoom;
* pan;
* select;
* focus;
* expand;
* collapse;
* filter;
* search;
* reset.

Selecting an object should reveal its structured details.

The graph must always remain connected to the underlying model.

---

# 53. Information Density

SEO professionals often work with large datasets.

The UI should therefore support:

* compact density mode;
* comfortable reading mode;
* configurable columns;
* persistent filters;
* saved views;
* bulk actions.

Default density should optimize comprehension rather than maximum information density.

---

# 54. Bulk Actions

Bulk actions may include:

* validate topics;
* reject topics;
* merge topics;
* assign clusters;
* approve recommendations;
* request review;
* archive items.

Bulk consequential actions must respect authorization and review policy.

---

# 55. Undo and Reversibility

Where technically possible, reversible changes should provide:

* undo;
* rollback;
* version history.

Irreversible actions should require stronger confirmation.

The UI should clearly communicate consequence.

Example:

```text
This action will permanently remove the relationship.

[Cancel]
[Confirm]
```

---

# 56. Notifications

Notifications should focus on meaningful events:

* workflow completed;
* workflow failed;
* review required;
* important conflict detected;
* data became stale;
* provider failure;
* high-priority opportunity detected.

Avoid notification spam.

---

# 57. Activity and History

Users should be able to inspect project history.

History may include:

* research updates;
* topic changes;
* page mappings;
* decisions;
* approvals;
* rejected recommendations;
* workflow executions;
* model/version changes;
* evidence refreshes.

History should support filtering by object and event type.

---

# 58. Accessibility

Accessibility is a baseline requirement.

The interface should support:

* keyboard navigation;
* visible focus states;
* semantic HTML;
* screen-reader-compatible controls;
* accessible labels;
* sufficient contrast;
* non-color-only status indicators;
* reduced-motion preferences;
* accessible tables;
* accessible graph alternatives;
* meaningful error messages.

---

# 59. Keyboard UX

Power users should be able to navigate efficiently.

Potential shortcuts:

```text
/
Global Search

G → D
Dashboard

G → T
Topics

G → P
Pages

G → R
Research

G → C
Clusters

G → D
Decision Center
```

Exact shortcuts should be finalized during frontend implementation and must avoid conflicts with browser/system shortcuts.

---

# 60. Responsive Design

The product should support:

* desktop;
* laptop;
* tablet.

Desktop is the primary environment because of the analytical nature of the product.

Complex graph and table workflows may require larger screens.

On smaller screens:

* secondary panels may collapse;
* tables may become horizontally scrollable;
* graph controls may simplify;
* evidence panels may become drawers;
* navigation may become compact.

Mobile should not be treated as a miniature desktop.

---

# 61. Localization

The product must support multilingual UX.

Initial language architecture should accommodate:

* English;
* Persian;
* German.

The architecture must remain extensible to additional languages.

Localization must include:

* UI strings;
* dates;
* numbers;
* currencies;
* units;
* search contexts;
* AI output localization.

---

# 62. RTL / LTR

The UI must support both:

```text
LTR
```

and:

```text
RTL
```

without treating RTL as a superficial text-direction change.

Layout, icons, navigation, tables, graphs, drawers, and interaction patterns must remain usable in both directions.

---

# 63. International Search Context

Search intelligence interfaces should make search context explicit.

Example:

```text
Language: German
Country: Germany
Location: Frankfurt
Device: Desktop
Search Engine: Google
Captured: 2026-09-05
```

Users must not mistake localized search results for universal search reality.

---

# 64. AI Output Localization

AI-generated content should preserve structured semantics while localizing presentation.

For example:

```text
Epistemic State: INFERRED
```

may be translated for the UI, but the underlying enum must remain stable.

---

# 65. Design System Relationship

This document defines UX behavior and product-level interaction.

`19_DESIGN_SYSTEM.md` defines:

* visual tokens;
* typography;
* colors;
* spacing;
* components;
* elevation;
* borders;
* states;
* iconography;
* visual language.

`18_FRONTEND_ARCHITECTURE.md` defines implementation architecture.

Therefore:

```text
17_UI_UX_SPECIFICATION
        ↓
19_DESIGN_SYSTEM
        ↓
18_FRONTEND_ARCHITECTURE
```

should be interpreted as:

* UX defines behavior;
* Design System defines visual primitives;
* Frontend Architecture defines implementation.

---

# 66. Component Categories

The product will require reusable components for:

### Navigation

* Sidebar
* Breadcrumbs
* Tabs
* Project Switcher

### Data

* Data Table
* Filter Bar
* Search
* Sort Controls
* Pagination
* Data Cards

### AI

* AI Recommendation
* AI Insight
* Confidence Indicator
* Evidence Panel
* Rationale Summary

### Workflow

* Progress Stepper
* Workflow Status
* Review Queue
* Approval Dialog

### Knowledge

* Entity Card
* Relationship Viewer
* EAV Table
* Topic Card

### Visualization

* Entity Graph
* Topic Graph
* Architecture Tree
* Linking Graph
* Similarity Matrix

### System

* Toast
* Alert
* Modal
* Drawer
* Empty State
* Error State
* Loading State

**Relationship to the operational component taxonomy:** the categories above group components by *function/purpose* for UX specification, not by build order. The project separately maintains an operational FOUNDATION / SHARED / FEATURE taxonomy in `.ai/COMPONENT_MATRIX.md` for sequencing and ownership — these are different classification dimensions, not competing ones. Navigation and System components map largely to operational SHARED; Knowledge and Visualization components are largely FEATURE (domain-specific); AI and Workflow components split between SHARED and FEATURE depending on whether a given instance is domain-agnostic or domain-specific. See `.ai/COMPONENT_MATRIX.md` for the authoritative mapping.

---

# 67. UX State Model

Every major object should expose a consistent state model.

At minimum:

```text
Draft
AI Proposed
Validated
Under Review
Human Approved
Rejected
Superseded
Archived
```

The UI should not invent object states independently of the underlying domain model.

---

# 68. Permission-Aware UX

The UI must respect:

* workspace permissions;
* project permissions;
* role permissions;
* action authorization.

If the user cannot perform an action, the UI should explain why where appropriate.

The frontend must never be treated as the primary security boundary.

Authorization must be enforced server-side.

---

# 69. Data Privacy UX

Users should be able to understand:

* what data is being processed;
* which external provider is being used where relevant;
* what information is persisted;
* what is shared externally;
* what actions are irreversible.

Sensitive configuration and credentials must never be exposed through ordinary UI views.

---

# 70. AI Transparency

The product should communicate AI involvement without making the interface noisy.

Appropriate labels:

```text
AI Suggested
AI Inferred
Evidence Observed
Human Approved
```

Avoid vague labels such as:

```text
Smart Insight
Magic Score
AI Truth
```

---

# 71. Explainability Pattern

Recommended pattern:

```text
Recommendation
    ↓
Why?
    ↓
Decision Factors
    ↓
Evidence
    ↓
Confidence
    ↓
Conflicts / Assumptions
```

Do not expose private chain-of-thought.

Expose concise, verifiable decision rationale instead.

---

# 72. Opportunity Scoring UX

Scores should never appear without context.

Instead of:

```text
Opportunity Score: 92
```

show:

```text
Opportunity: High

Signals:
Business relevance      High
Search evidence         Strong
Competitive gap         Strong
Existing coverage       Low
Intent fit              High
Confidence              Medium
```

The exact scoring methodology belongs to the decision engine and data specifications.

---

# 73. Saved Views

Users should be able to save useful analytical configurations.

Examples:

```text
High-value unresolved topics
Pages with cannibalization risk
Topics awaiting validation
Stale SERP observations
Competitor gaps
Decisions awaiting approval
```

Saved views must be project-scoped unless explicitly designed otherwise.

---

# 74. Export UX

Export may support:

* CSV;
* JSON;
* reports;
* structured project artifacts.

Exports should preserve:

* object IDs;
* statuses;
* evidence references;
* timestamps;
* provenance where appropriate.

Export permissions must be respected.

---

# 75. Context Management UX

The user should not need to manually rebuild context.

The system should maintain contextual awareness of:

* project;
* current workspace;
* selected objects;
* workflow;
* previous validated decisions;
* available evidence.

However, users should be able to inspect the effective context when needed.

A compact context indicator may show:

```text
Context
Project: Travel SEO
Selected: 12 Topics
Evidence: 84 Sources
Workflow: Topic Validation
```

Detailed context retrieval behavior is defined in:

`25_CONTEXT_MANAGEMENT.md`.

---

# 76. Research Reuse

The UI should make previously collected knowledge reusable.

For example:

```text
Existing Entity Knowledge
        ↓
New Topic Research
        ↓
Existing SERP Data
        ↓
New Decision
```

The user should not be encouraged to repeatedly execute identical research when valid evidence already exists.

---

# 77. Freshness UX

Objects that depend on temporal information should expose freshness.

Example:

```text
Topic Analysis
Updated: 2 days ago

SERP
Updated: 4 hours ago

Competitor Data
Updated: 18 days ago
```

This allows users to judge whether a recommendation remains trustworthy.

---

# 78. Decision Impact UX

High-impact decisions should receive stronger visual emphasis.

Possible dimensions:

* affected pages;
* business importance;
* expected effort;
* reversibility;
* confidence;
* evidence quality.

This allows the review queue to prioritize intelligently.

---

# 79. Review Before Action

The UX must enforce:

```text
AI Recommendation
        ↓
Validation
        ↓
Human Review
        ↓
Authorization
        ↓
Action
```

where policy requires human approval.

The interface must not encourage users to skip review merely because a recommendation has high confidence.

---

# 80. Anti-Patterns

The following UX patterns are prohibited:

### 80.1 Keyword dashboard as the entire product

The product is not a keyword spreadsheet with AI attached.

### 80.2 AI magic scores

Scores without explanation are insufficient.

### 80.3 False certainty

Never visually present uncertain inference as established fact.

### 80.4 Hidden evidence

Recommendations must be traceable to evidence.

### 80.5 Confusing topics and pages

A topic is not automatically a page.

### 80.6 Confusing topical maps and page architecture

These are separate conceptual layers.

### 80.7 Autonomous-action illusion

AI recommendations must not look like completed actions.

### 80.8 Decorative graphs

Visualization must communicate analytical information.

### 80.9 Overloaded dashboards

The home screen should prioritize decisions and meaningful project health.

### 80.10 Generic chatbot UX

AI must be contextual to the research environment.

### 80.11 Color-only semantics

Status and confidence must not depend only on color.

### 80.12 Silent data failure

Missing, stale, partial, or conflicted data must be visible.

### 80.13 Excessive automation

Automation must not remove strategic control.

---

# 81. MVP UX Scope

The MVP should prioritize the smallest coherent decision-making experience.

Required:

1. Authentication and workspace/project shell
2. Dashboard
3. Business Research
4. Entity Explorer
5. EAV Explorer
6. Topic Universe
7. Topic Validation
8. Intent Workspace
9. SERP Intelligence
10. Topic Clustering
11. Page Candidate Mapping
12. Decision Center
13. Human Review Queue
14. Evidence Viewer
15. Workflow Monitor
16. AI contextual assistant
17. Search/filter/sort
18. Basic responsive behavior
19. Localization foundation
20. Accessible core interactions

Advanced graph and visualization capabilities may be introduced incrementally where implementation complexity is high.

---

# 82. Future UX Capabilities

Potential future capabilities:

* fully interactive knowledge graph;
* adaptive research planning;
* autonomous research workflows under policy;
* predictive opportunity detection;
* dynamic topical maps;
* historical search landscape visualization;
* advanced competitive intelligence;
* outcome-based recommendations;
* personalized strategist workspaces;
* multi-user collaborative research;
* comments and annotations;
* AI-assisted decision simulation;
* scenario comparison;
* strategy versioning;
* automated monitoring.

These must not be assumed to be MVP requirements.

---

# 83. UX Testing

UX quality must be validated through:

### Usability testing

Can users complete core SEO tasks?

### Comprehension testing

Can users distinguish:

* topic;
* keyword;
* page;
* intent;
* recommendation;
* decision?

### Evidence testing

Can users identify why a recommendation exists?

### Trust testing

Can users distinguish AI inference from observed data?

### Workflow testing

Can users understand where they are in a workflow?

### Review testing

Can users approve/reject/modify recommendations correctly?

### Accessibility testing

Can users operate the interface without relying on mouse or color?

---

# 84. Core UX Acceptance Scenarios

The MVP should validate scenarios such as:

### Scenario 1 — Topic discovery

User starts with a business and discovers a topic universe.

Expected:

* sources are visible;
* topics are distinguishable from keywords;
* uncertain topics are identifiable.

---

### Scenario 2 — Topic validation

User reviews a topic.

Expected:

* business relevance;
* search evidence;
* intent;
* competitive evidence;
* confidence;
* recommendation;
* validation controls.

---

### Scenario 3 — SERP investigation

User selects a query and investigates its SERP.

Expected:

* search context;
* timestamp;
* results;
* features;
* intent signals;
* evidence.

---

### Scenario 4 — Page decision

User reviews whether multiple topics should map to one page.

Expected:

* topic overlap;
* intent similarity;
* SERP similarity;
* entity overlap;
* recommendation;
* confidence;
* evidence;
* human decision.

---

### Scenario 5 — Cannibalization

User investigates potential cannibalization.

Expected:

* affected pages;
* overlapping queries;
* evidence;
* historical information;
* recommendation;
* review status.

---

### Scenario 6 — Human approval

User approves a recommendation.

Expected:

* explicit approval;
* identity;
* timestamp;
* state transition;
* audit event.

---

# 85. UX Quality Gates

A feature is not UX-complete until:

* conceptual distinctions are preserved;
* user goals are clear;
* states are visible;
* errors are understandable;
* uncertainty is represented;
* evidence is accessible;
* authorization is respected;
* loading/empty/error states exist;
* accessibility is considered;
* localization does not break layout;
* responsive behavior is defined;
* destructive actions are protected;
* AI recommendations are distinguishable from decisions;
* underlying output contracts are respected.

---

# 86. Relationship to Output Contracts

`16_OUTPUT_CONTRACTS.md` defines the structured outputs consumed by the UI.

Therefore:

```text
Agent
 ↓
Output Contract
 ↓
Validation
 ↓
Persisted Artifact
 ↓
API
 ↓
UI
```

The frontend must not reinterpret invalid or incomplete data as valid system state.

UI components should be designed around stable domain contracts rather than raw LLM responses.

---

# 87. Relationship to Human-in-the-Loop

`15_HUMAN_IN_THE_LOOP.md` defines:

* approval;
* rejection;
* modification;
* override;
* defer;
* review;
* escalation.

This document defines how those actions appear in the interface.

The UI is therefore the primary interaction surface for human strategic authority but is not the authorization authority itself.

---

# 88. Relationship to Agent Workflow

`14_AGENT_WORKFLOW.md` defines workflow execution.

The UI represents:

```text
Workflow
→ Steps
→ State
→ Evidence
→ Outputs
→ Review Gates
→ Completion
```

The UI must not fabricate progress merely because a workflow was started.

---

# 89. Relationship to SEO Decision Engine

`12_SEO_DECISION_ENGINE.md` defines decision logic.

The UI visualizes:

* recommendations;
* factors;
* confidence;
* evidence;
* conflicts;
* decisions;
* outcomes.

The UI must not independently implement strategic decision logic.

---

# 90. Relationship to Context Management

`25_CONTEXT_MANAGEMENT.md` defines context retrieval and lifecycle.

The UI should provide enough context awareness for users to understand what the AI is currently operating on.

It should avoid unnecessary context exposure while preserving transparency when context affects an important recommendation.

---

# 91. Relationship to Skills and Tooling

`26_SKILLS_AND_TOOLING_POLICY.md` defines:

* skill discovery;
* installation;
* permissions;
* security;
* validation.

The UI may expose tool activity where useful.

Example:

```text
Search Provider
SERP collection completed

Competitor Research
3 sources queried
```

Sensitive credentials and internal security details must never be exposed.

---

# 92. Frontend Architectural Constraint

The UI architecture must remain modular.

Conceptually:

```text
Pages
 ↓
Feature Modules
 ↓
Domain Components
 ↓
Shared Components
 ↓
Design System
```

Feature modules should correspond to meaningful product domains.

Examples:

```text
features/topics
features/entities
features/serp
features/decisions
features/workflows
features/pages
```

Exact implementation structure belongs to:

`18_FRONTEND_ARCHITECTURE.md`.

---

# 93. UX and Performance

The interface should remain responsive during:

* large table rendering;
* graph interactions;
* filtering;
* search;
* workflow monitoring;
* AI streaming;
* large evidence collections.

Potential techniques include:

* pagination;
* virtualization;
* lazy loading;
* progressive rendering;
* incremental graph expansion;
* cached queries;
* optimistic UI only where safe;
* background refresh.

Optimistic UI must never imply a consequential state transition before the server confirms it.

---

# 94. AI Streaming UX

Where AI responses stream:

* show generation state;
* allow cancellation where supported;
* preserve partial output appropriately;
* distinguish generated text from persisted artifacts;
* validate structured outputs before presenting them as trusted objects.

Streaming text should not automatically become canonical project state.

---

# 95. System Feedback

The application should provide feedback for important operations.

Examples:

```text
Topic validated.
Recommendation rejected.
Workflow paused for review.
SERP data refreshed.
3 conflicts require attention.
```

Feedback should be concise and non-blocking when possible.

---

# 96. Trust Model

The UI should progressively build trust through:

```text
Transparency
+
Evidence
+
Consistency
+
Validation
+
Human Control
+
History
```

The product should never attempt to manufacture trust through visual polish alone.

---

# 97. UX Definition of Done

A UX feature is complete when:

1. The user goal is explicitly defined.
2. The relevant domain objects are clearly represented.
3. Navigation is coherent.
4. Primary and secondary actions are defined.
5. Loading states exist.
6. Empty states exist.
7. Error states exist.
8. Partial-result states exist where relevant.
9. Stale/conflict states exist where relevant.
10. AI-generated information is clearly distinguished.
11. Evidence can be inspected.
12. Confidence and epistemic state can be understood.
13. Human review behavior is defined.
14. Authorization boundaries are respected.
15. Destructive actions are protected.
16. Accessibility requirements are addressed.
17. RTL/LTR behavior is addressed.
18. Responsive behavior is addressed.
19. Output contracts are respected.
20. The feature has a clear relationship to the domain model.
21. UX behavior can be tested.
22. The feature does not introduce a conceptual contradiction into the product.

---

# 98. Final UX Model

The product experience should ultimately feel like:

```text
                  ┌──────────────────┐
                  │      BUSINESS    │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │     RESEARCH     │
                  └────────┬─────────┘
                           ↓
             ┌────────────────────────────┐
             │  ENTITIES + EAV + TOPICS   │
             └─────────────┬──────────────┘
                           ↓
             ┌────────────────────────────┐
             │ SEARCH + INTENT + SERP     │
             └─────────────┬──────────────┘
                           ↓
             ┌────────────────────────────┐
             │ CLUSTERS + TOPICAL MAP     │
             └─────────────┬──────────────┘
                           ↓
             ┌────────────────────────────┐
             │ PAGE CANDIDATES +          │
             │ PAGE ARCHITECTURE          │
             └─────────────┬──────────────┘
                           ↓
             ┌────────────────────────────┐
             │ GAPS + CANNIBALIZATION +   │
             │ INTERNAL LINKING           │
             └─────────────┬──────────────┘
                           ↓
             ┌────────────────────────────┐
             │      DECISION CENTER       │
             └─────────────┬──────────────┘
                           ↓
                  ┌──────────────────┐
                  │  HUMAN REVIEW    │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │     APPROVAL     │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │     ACTION       │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │     OUTCOME      │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │     LEARNING     │
                  └──────────────────┘
```

The interface should make this lifecycle understandable without forcing the user to understand the underlying technical architecture.

---

# 99. Non-Negotiable UX Principles

1. **Human strategic authority remains explicit.**
2. **AI recommendations are not automatically decisions.**
3. **Topics, keywords, pages, intents, and SERPs remain distinct concepts.**
4. **Topical maps and page architecture remain distinct layers.**
5. **Evidence must remain accessible.**
6. **Uncertainty must remain visible.**
7. **Conflicts must not be silently resolved.**
8. **Partial results must be clearly labeled.**
9. **Stale data must be visible.**
10. **Consequential actions require authorization.**
11. **The frontend is not a security boundary.**
12. **Graphs must represent real underlying relationships.**
13. **Scores must be interpretable.**
14. **AI must not be presented as an oracle.**
15. **The UI must preserve output-contract semantics.**
16. **The UX must support human validation as a first-class workflow.**
17. **Accessibility is mandatory, not optional polish.**
18. **RTL/LTR must be structurally supported.**
19. **The interface must scale to professional SEO datasets.**
20. **The product must optimize for better SEO decisions, not more generated content.**

---

# 100. Document Control

```yaml
document:
  id: "17"
  filename: "17_UI_UX_SPECIFICATION.md"
  status: "APPROVED_AS_BASELINE_UI_UX_SPECIFICATION"
  product: "SEO Research & Strategy Copilot / SEO Decision Engine"
  authority: "baseline_ui_ux_specification"

ux:
  philosophy: "decision_first_evidence_first_human_control"
  operating_model: "human_strategy + ai_research + ai_analysis + human_validation"
  primary_users:
    - seo_strategist
    - seo_manager
    - content_strategist
    - analyst
    - reviewer

core_experiences:
  - business_research
  - entity_exploration
  - eav_exploration
  - topic_discovery
  - topic_validation
  - intent_analysis
  - serp_intelligence
  - topic_clustering
  - topical_mapping
  - page_candidate_mapping
  - page_architecture
  - internal_linking
  - content_gap_analysis
  - cannibalization_analysis
  - competitor_intelligence
  - decision_support
  - human_review
  - workflow_monitoring
  - evidence_inspection

core_epistemic_states:
  - OBSERVED
  - INFERRED
  - ESTIMATED
  - RECOMMENDED
  - HUMAN_APPROVED
  - CONFLICTED
  - UNKNOWN

core_object_states:
  - DRAFT
  - AI_PROPOSED
  - VALIDATED
  - UNDER_REVIEW
  - HUMAN_APPROVED
  - REJECTED
  - SUPERSEDED
  - ARCHIVED

design_principles:
  - evidence_first
  - decision_first
  - progressive_disclosure
  - explicit_uncertainty
  - conceptual_integrity
  - contextual_ai
  - human_control
  - accessibility
  - localization
  - responsive_design
  - professional_information_density

ai_ux:
  contextual: true
  chain_of_thought_exposure: false
  evidence_access: true
  confidence_visibility: true
  recommendation_vs_decision_distinction: true
  autonomous_action_illusion: false

architecture_relationships:
  output_contracts: "16_OUTPUT_CONTRACTS.md"
  human_in_the_loop: "15_HUMAN_IN_THE_LOOP.md"
  agent_workflow: "14_AGENT_WORKFLOW.md"
  seo_decision_engine: "12_SEO_DECISION_ENGINE.md"
  frontend_architecture: "18_FRONTEND_ARCHITECTURE.md"
  design_system: "19_DESIGN_SYSTEM.md"
  context_management: "25_CONTEXT_MANAGEMENT.md"
  skills_and_tooling_policy: "26_SKILLS_AND_TOOLING_POLICY.md"

localization:
  multilingual: true
  rtl_support: true
  ltr_support: true
  initial_languages:
    - en
    - fa
    - de

accessibility:
  keyboard_navigation: true
  screen_reader_support: true
  non_color_semantics: true
  reduced_motion: true
  accessible_visualization_alternatives: true

mvp:
  priority: "decision_making_experience"
  advanced_visualizations: "incremental"
  mobile_priority: "secondary_to_desktop"

security:
  frontend_is_security_boundary: false
  authorization_server_side: true
  consequential_actions_authorized: true

primary_design_rule:
  statement: "The UI must make evidence, uncertainty, recommendation, human decision, and resulting state distinguishable."

next_dependency:
  document: "18_FRONTEND_ARCHITECTURE.md"

related:
  - "12_SEO_DECISION_ENGINE.md"
  - "14_AGENT_WORKFLOW.md"
  - "15_HUMAN_IN_THE_LOOP.md"
  - "16_OUTPUT_CONTRACTS.md"
  - "18_FRONTEND_ARCHITECTURE.md"
  - "19_DESIGN_SYSTEM.md"
  - "25_CONTEXT_MANAGEMENT.md"
  - "26_SKILLS_AND_TOOLING_POLICY.md"
```
