# 19 — Design System

**Document:** `19_DESIGN_SYSTEM.md`
**Product:** SEO Research & Strategy Copilot / SEO Decision Engine
**Document Type:** Design System Specification
**Status:** `APPROVED_AS_BASELINE_DESIGN_SYSTEM`
**Authority:** Baseline specification for visual language, design tokens, typography, color, spacing, layout, surfaces, components, interaction states, visualization styling, accessibility, motion, themes, RTL/LTR behavior, and design-system governance.

---

# 1. Purpose

This document defines the design system for the SEO Research & Strategy Copilot / SEO Decision Engine.

The design system provides the shared visual and interaction foundation used by the frontend architecture defined in:

`18_FRONTEND_ARCHITECTURE.md`

and the UX behavior defined in:

`17_UI_UX_SPECIFICATION.md`.

The design system exists to create:

* visual consistency;
* predictable interaction;
* scalable implementation;
* accessible interfaces;
* efficient product development;
* coherent AI interaction;
* clear representation of evidence, confidence, uncertainty, and decisions.

A design system is broader than a color palette or visual style guide. It includes principles, foundations, reusable components, interaction patterns, accessibility requirements, and implementation guidance.

---

# 2. Design Philosophy

The visual language should communicate:

> **Intelligent, calm, analytical, trustworthy, precise, and professional.**

The product should feel like a professional strategy environment rather than:

* a generic SaaS dashboard;
* a marketing website;
* an AI chatbot;
* a spreadsheet;
* a developer administration panel.

---

# 3. Design Personality

The design should balance:

```text
Analytical
    +
Calm
    +
Premium
    +
Technical
    +
Human
```

It should avoid:

```text
Noisy
Overly colorful
Gamified
Decorative
Over-animated
AI-hype driven
```

---

# 4. Core Design Principles

## 4.1 Clarity over decoration

Every visual element should improve:

* comprehension;
* navigation;
* comparison;
* decision-making;
* confidence.

Decorative UI should not compete with analytical information.

---

## 4.2 Hierarchy over density

The product will contain large amounts of information.

The answer is not to make everything visually dense.

Instead:

```text
Primary information
        ↓
Secondary information
        ↓
Supporting evidence
        ↓
Technical details
```

must have clear visual hierarchy.

---

## 4.3 Semantic design

Visual styles should communicate semantic roles.

For example:

```text
Primary Action
Secondary Action
Destructive Action
AI Recommendation
Observed Evidence
Human Approval
Conflict
Warning
Unknown
```

Components should use semantic variants rather than arbitrary visual names.

Prefer:

```text
variant="destructive"
```

over:

```text
variant="red"
```

---

## 4.4 Evidence should look different from inference

Observed information and AI inference should not have identical visual treatment.

The design should allow users to distinguish:

```text
OBSERVED
INFERRED
ESTIMATED
RECOMMENDED
HUMAN APPROVED
CONFLICTED
UNKNOWN
```

without relying only on color.

---

## 4.5 Calm confidence

The interface should communicate confidence through:

* typography;
* spacing;
* structure;
* labels;
* evidence;
* restrained visual emphasis.

It should not use excessive badges, gradients, animations, or giant scores to manufacture confidence.

---

# 5. Visual Language

The baseline visual language is:

```text
Clean
Grid-based
Whitespace-oriented
Layered
Subtle
Data-dense where necessary
Softly dimensional
```

The system may use restrained glass/surface treatments where they improve hierarchy, but glass effects must not become the identity of every component.

---

# 6. Surface System

The interface should use a small number of semantic surface levels.

Recommended model:

```text
Surface 0
Application background

Surface 1
Primary content surface

Surface 2
Elevated card / panel

Surface 3
Overlay / dialog / popover

Surface 4
Critical/high-emphasis overlay
```

The number of visual layers should remain limited.

---

# 7. Surface Semantics

Example:

```text
Application Background
    ↓
Workspace Surface
    ↓
Card / Panel
    ↓
Drawer / Dialog
```

Do not stack excessive translucent surfaces.

A surface should have a clear reason to exist.

---

# 8. Background

The primary application background should be visually quiet.

The background should support long analytical sessions.

Avoid:

* intense gradients;
* high-frequency patterns;
* animated backgrounds;
* excessive decorative illustrations.

---

# 9. Glass / Translucency

If glassmorphism is used, it must remain a supporting visual technique.

Recommended characteristics:

* subtle transparency;
* restrained blur;
* sufficient contrast;
* clear boundaries;
* no dependency on transparency for information comprehension.

Glass effects must degrade gracefully when unsupported.

---

# 10. Borders

Borders should establish structure without visually overwhelming the interface.

Use semantic border roles:

```text
Border / Default
Border / Subtle
Border / Strong
Border / Focus
Border / Destructive
```

Avoid using multiple unrelated border colors throughout the product.

---

# 11. Elevation

Elevation should communicate hierarchy.

Use a restrained scale:

```text
Elevation 0
Flat

Elevation 1
Card

Elevation 2
Raised panel

Elevation 3
Popover / dropdown

Elevation 4
Dialog / modal
```

Avoid excessive shadows.

---

# 12. Border Radius

Use a consistent radius scale.

Conceptually:

```text
radius-xs
radius-sm
radius-md
radius-lg
radius-xl
radius-full
```

Semantic component mapping should be documented.

Do not allow every component to invent its own radius.

---

# 13. Design Tokens

All foundational visual properties should be represented through tokens.

Token categories:

```text
Color
Typography
Spacing
Sizing
Radius
Border
Elevation
Motion
Opacity
Breakpoints
Z-index
```

Design tokens should provide a centralized vocabulary for component implementation.

---

# 14. Token Naming

Tokens should describe semantic roles.

Prefer:

```text
color.background.primary
color.text.primary
color.border.subtle
color.action.primary
```

over:

```text
color.blue
color.gray2
color.greenDark
```

Semantic naming makes future theme changes safer.

---

# 15. Color System

The color system should contain:

### Neutral palette

Used for:

* backgrounds;
* surfaces;
* borders;
* text;
* disabled states.

### Brand palette

Used for:

* primary actions;
* product identity;
* selected states.

### Semantic palette

Used for:

* success;
* warning;
* error;
* information;
* conflict.

### Analytical palette

Used cautiously for:

* charts;
* categorical visualization;
* comparison;
* data differentiation.

---

# 16. Color Usage Principle

Color should communicate meaning, not decoration.

Do not use:

```text
Blue = good
Red = bad
Green = approved
```

as the only semantic mechanism.

Each important state should include:

* label;
* icon or shape where appropriate;
* text;
* color as reinforcement.

---

# 17. Suggested Brand Direction

The product may use a restrained intelligent palette centered around a deep teal/blue-green primary tone with warm accent support.

A possible starting point:

```text
Primary:
Deep Teal

Accent:
Warm Amber

Neutrals:
Cool Gray / Slate family

Success:
Semantic Green

Warning:
Semantic Amber

Error:
Semantic Red

Information:
Semantic Blue
```

Exact production values must be finalized through contrast validation and visual testing.

The semantic token names must remain stable even if actual color values change.

---

# 18. Dark Theme

Dark mode should be a first-class theme.

It must not simply invert the light theme.

Dark mode requires independent consideration of:

* surface hierarchy;
* text contrast;
* borders;
* shadows;
* graph readability;
* status colors;
* chart colors;
* focus indicators.

---

# 19. Light Theme

Light mode should prioritize:

* readable text;
* subtle surface separation;
* comfortable analytical density;
* restrained borders;
* low visual noise.

---

# 20. Theme Tokens

Themes should override semantic tokens.

Conceptually:

```text
color.background.primary
        ↓
Light Theme Value

color.background.primary
        ↓
Dark Theme Value
```

Components should not directly reference theme-specific raw colors.

---

# 21. Typography

Typography must support long analytical sessions and dense professional interfaces.

The baseline typography direction is:

```text
Geist
+
Vazirmatn
```

where appropriate for Latin and Persian interfaces.

The system must remain capable of substituting fonts without changing component semantics.

---

# 22. Font Roles

Define roles such as:

```text
Display
Heading 1
Heading 2
Heading 3
Heading 4
Body
Body Small
Label
Caption
Code / Data
```

Each role should have:

* font family;
* size;
* weight;
* line height;
* letter spacing.

---

# 23. Typography Hierarchy

Recommended conceptual hierarchy:

```text
Page Title
    ↓
Section Title
    ↓
Subsection
    ↓
Body
    ↓
Supporting Metadata
```

Do not use font size alone.

Hierarchy may also use:

* weight;
* spacing;
* contrast;
* placement.

---

# 24. Numeric Typography

SEO products contain many metrics.

Numbers should be visually scannable.

Examples:

* search volume;
* CPC;
* rankings;
* confidence;
* percentages;
* dates.

Use consistent formatting.

Tabular numeric alignment should be used where useful for comparison.

---

# 25. Monospace Usage

Monospace typography should be reserved for:

* IDs;
* technical values;
* query strings where appropriate;
* code;
* raw provider responses;
* structured data.

Do not use monospace for ordinary UI copy.

---

# 26. Spacing System

Use a consistent spacing scale.

Conceptually:

```text
space-1
space-2
space-3
space-4
space-6
space-8
space-10
space-12
space-16
space-20
space-24
```

The exact numerical scale should be finalized during implementation.

---

# 27. Layout Grid

The application should use a consistent layout grid.

Desktop analytical layouts may use:

```text
Sidebar
+
Main Content
+
Optional Context Panel
```

Example:

```text
┌────────────┬───────────────────────────────┬─────────────┐
│            │                               │             │
│ Navigation │       Main Workspace          │  Context    │
│            │                               │  / Evidence │
│            │                               │             │
└────────────┴───────────────────────────────┴─────────────┘
```

---

# 28. Container Width

Content width should adapt to task complexity.

Examples:

* forms: narrower;
* decision review: medium;
* tables: wide;
* graphs: very wide;
* page architecture: full workspace.

Do not force every feature into one global max-width.

---

# 29. Responsive Breakpoints

The system should define semantic breakpoints.

Conceptually:

```text
Compact
Tablet
Desktop
Wide Desktop
```

Exact breakpoint values must be validated during implementation.

---

# 30. Responsive Behavior

Components must define how they behave when space decreases.

Examples:

```text
Three-column review
→ two-column
→ stacked

Large table
→ horizontal scroll

Evidence side panel
→ drawer

Sidebar
→ collapsed navigation
```

---

# 31. Component Architecture

Components should be:

* reusable;
* composable;
* accessible;
* predictable;
* semantically named;
* independently testable.

The component API should remain smaller than the number of edge cases it supports.

---

# 32. Component Layers

The design system should distinguish:

### Foundations

Tokens and primitives.

### Primitives

Basic components.

### Components

Reusable functional components.

### Patterns

Combinations of components solving recurring UX problems.

### Templates

Reusable page structures.

**Relationship to the operational component taxonomy:** the five layers above are a *design-system* classification describing composability and reuse depth. The project separately maintains an *operational* three-tier taxonomy — FOUNDATION / SHARED / FEATURE — in `.ai/COMPONENT_MATRIX.md`, used for build sequencing and ownership. These are different classification dimensions answering different questions, not competing or redundant definitions: Foundations + Primitives map to operational FOUNDATION; domain-agnostic Components/Patterns/Templates map to operational SHARED; domain-specific instances of any layer map to operational FEATURE. See `.ai/COMPONENT_MATRIX.md` for the authoritative mapping.

---

# 33. Foundation Components

Examples:

* Box/Layout
* Stack
* Grid
* Text
* Icon
* Separator
* VisuallyHidden

These should remain highly reusable.

---

# 34. Action Components

Required:

* Button
* IconButton
* Link
* ButtonGroup
* SplitButton where justified

Variants should be semantic.

Example:

```text
primary
secondary
ghost
destructive
```

---

# 35. Button States

Buttons should support:

```text
Default
Hover
Focus
Active
Disabled
Loading
Success where appropriate
```

Loading buttons should prevent accidental duplicate submissions.

---

# 36. Form Components

Required foundations:

* Input
* Textarea
* Select
* Combobox
* Checkbox
* Radio
* Switch
* Date/Time controls
* Search field

All interactive controls must have accessible names and predictable keyboard behavior.

Accessible behavior should be implemented at the component layer rather than repeatedly delegated to consumers.

---

# 37. Data Display Components

Required:

* Badge
* Tag
* Avatar
* Tooltip
* Table
* Data Grid where necessary
* Statistic
* Progress
* Timeline
* Empty State
* Skeleton
* Alert

---

# 38. Navigation Components

Required:

* Sidebar
* Breadcrumb
* Tabs
* Pagination
* Menu
* Dropdown
* Command/Search Palette

Navigation components must maintain keyboard accessibility and logical focus behavior.

---

# 39. Overlay Components

Required:

* Dialog
* Drawer
* Popover
* Tooltip
* Context Menu

Focus management must be handled consistently.

---

# 40. Dialog Rules

Dialogs should be used for:

* confirmation;
* focused decisions;
* short forms.

They should not contain entire complex workflows when a dedicated page would be clearer.

---

# 41. Drawer Rules

Drawers are preferred for contextual inspection.

Examples:

* evidence;
* entity details;
* topic details;
* SERP result details.

A drawer should preserve the user's primary analytical context.

---

# 42. Table Design

Tables should support:

* header hierarchy;
* sorting;
* filtering;
* row selection;
* pagination;
* column configuration;
* status indicators;
* responsive behavior.

Rows should not become visually overloaded with every possible field.

---

# 43. Table Density

Provide at least:

```text
Comfortable
Compact
```

density modes if the product's data volume justifies them.

Density settings must not compromise accessibility.

---

# 44. Status Components

The system should provide standardized status indicators.

Examples:

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

Status presentation must remain consistent throughout the application.

---

# 45. Epistemic State Components

Dedicated components should represent:

```text
Observed
Inferred
Estimated
Recommended
Human Approved
Conflicted
Unknown
```

These are not interchangeable with workflow statuses.

---

# 46. Confidence Component

The design system should provide a standardized confidence presentation.

Example:

```text
Confidence
Medium

[visual indicator]

Evidence quality:
Strong

Uncertainty:
Limited historical observations
```

Do not use a huge percentage number as the primary visual.

---

# 47. Evidence Component

Evidence should have a recognizable but restrained presentation.

Example:

```text
┌──────────────────────────────────────┐
│ Evidence                             │
│                                      │
│ Source: Search Provider              │
│ Captured: 2 hours ago                │
│ State: Observed                      │
│ Reliability: High                    │
│                                      │
│ [Inspect Source]                     │
└──────────────────────────────────────┘
```

---

# 48. Recommendation Component

AI recommendations should be visually distinct from canonical decisions.

Recommended structure:

```text
Recommendation
────────────────────
Create a dedicated page

Why:
• Strong intent alignment
• High SERP similarity
• No suitable existing page

Confidence:
Medium

[Review]
```

---

# 49. Decision Component

A decision component should visually communicate that the object represents an actual project decision.

Example:

```text
Decision
Approved

Action:
Create dedicated landing page

Approved by:
Human reviewer

Date:
2026-09-05
```

---

# 50. Conflict Component

Conflicts require high visibility but should not become visually alarming by default.

Example:

```text
Conflict detected

Two sources report different values.

[Inspect Evidence]
```

Use semantic warning/error styling as reinforcement.

---

# 51. Empty State

Empty states should contain:

* concise explanation;
* reason;
* next action.

Example:

```text
No validated topics yet.

Validate topics before building the topical map.

[Validate Topics]
```

---

# 52. Loading State

Loading states should preserve layout where possible.

Use:

* skeletons;
* progress indicators;
* contextual messages.

Avoid full-screen loading for local feature updates.

---

# 53. Skeleton Rules

Skeletons should resemble the expected content structure.

Do not use generic animated gray blocks everywhere.

---

# 54. Error State

Error states should communicate:

* what failed;
* why where known;
* what remains available;
* what the user can do.

Example:

```text
SERP refresh failed.

Existing data remains available.

[Retry]
[View Existing Snapshot]
```

---

# 55. Partial State

Partial state requires a distinct visual treatment.

Example:

```text
Partial

38 of 50 queries analyzed.

8 queries could not be processed.
```

---

# 56. Stale State

Stale data should have a consistent indicator.

Example:

```text
Stale
Last updated 21 days ago
```

The stale state should not visually imply that the data is invalid.

---

# 57. Disabled State

Disabled components should remain distinguishable while maintaining sufficient readability.

Do not rely on opacity alone when it makes text difficult to read.

---

# 58. Focus State

Every interactive component must have a visible focus state.

Never remove focus outlines without implementing an accessible replacement.

Focus indicators should have sufficient visual distinction.

---

# 59. Hover State

Hover should enhance interaction but must not be the only way to discover critical information.

Important information must remain available through keyboard and touch interaction.

---

# 60. Selection State

Selected objects should have a clear persistent visual state.

Examples:

* selected topic;
* selected entity;
* selected table row;
* selected graph node.

Selection must not depend only on color.

---

# 61. Destructive State

Destructive actions should use:

* semantic warning;
* clear label;
* confirmation when appropriate.

Avoid visually aggressive design that encourages impulsive action.

---

# 62. Icons

Icons should be:

* consistent;
* recognizable;
* semantically appropriate;
* accessible.

The icon library should be standardized.

A single icon should not represent multiple unrelated actions.

---

# 63. Icon + Text

For important actions, use icon + text when the icon alone may be ambiguous.

Examples:

```text
✓ Approve
× Reject
↻ Refresh
```

---

# 64. Icon Directionality

Directional icons must respect RTL/LTR context where their meaning depends on direction.

Examples:

* arrows;
* back/forward;
* hierarchy indicators.

Decorative icons may remain unchanged where semantically appropriate.

---

# 65. Charts

Charts should use semantic design tokens.

They should support:

* legends;
* labels;
* tooltips;
* accessible alternatives;
* keyboard-accessible data where practical.

---

# 66. Analytical Color Palette

Categorical charts should use distinguishable colors with sufficient contrast.

Do not use color palettes that depend on subtle shades users cannot reliably distinguish.

For critical states, use redundant encoding:

```text
Color
+
Label
+
Shape/Icon
```

---

# 67. Graph Design

Entity and topic graphs should prioritize:

* relationship clarity;
* node hierarchy;
* readable labels;
* selection;
* filtering.

Avoid:

* excessive glow;
* decorative shadows;
* unnecessary animation;
* overly dense node styling.

---

# 68. Graph States

Graph nodes may visually communicate:

```text
Selected
Highlighted
Filtered
Inactive
Unknown
Conflicted
```

However, node color must not be the only signal.

---

# 69. Architecture Tree

Page architecture should use a clear hierarchical visual language.

Recommended:

```text
Parent Page
  ├── Child Page
  │    ├── Subpage
  │    └── Subpage
  └── Child Page
```

Use indentation, connector lines, and labels consistently.

---

# 70. Internal Linking Visualization

Directed links should be visually distinguishable from hierarchy relationships.

The system should not use identical visual semantics for:

```text
Parent-child relationship
```

and:

```text
Internal link
```

---

# 71. AI Interaction Visual Language

AI-generated content should have a consistent visual identity.

Use subtle cues such as:

* AI icon;
* "AI Suggested" label;
* recommendation container;
* evidence indicators.

Avoid making the entire interface visually "AI themed."

---

# 72. Human Approval Visual Language

Human-approved states should communicate trust through status and metadata.

Example:

```text
✓ Human Approved
Reviewed by: [User]
Date: [Date]
```

Do not imply that human approval means the recommendation was objectively correct.

It means the authorized reviewer approved it.

---

# 73. Motion Principles

Motion should be:

* purposeful;
* short;
* subtle;
* interruptible where necessary.

Use motion for:

* navigation;
* state transitions;
* progressive disclosure;
* feedback.

Avoid motion for decoration.

---

# 74. Reduced Motion

Respect user reduced-motion preferences.

Animations that are not necessary for comprehension should be disabled or significantly reduced.

Accessibility guidance recommends avoiding excessive movement and providing ways to control motion.

---

# 75. AI Streaming Animation

AI streaming should communicate activity without creating distracting typing animations.

Prefer:

```text
Generating recommendation...
```

with progressive content rendering.

Avoid excessive cursor blinking or animated decorative effects.

---

# 76. Microinteractions

Use microinteractions for:

* confirmation;
* successful state changes;
* hover/focus feedback;
* drag/drop;
* filtering.

They should reinforce the user's action.

---

# 77. Toasts

Toasts should communicate transient outcomes.

Examples:

```text
Topic validated.
Recommendation rejected.
Workflow completed.
```

Critical information must not exist only in a toast.

---

# 78. Notifications

Notifications should use semantic severity:

```text
Info
Success
Warning
Error
```

Avoid using notification colors without text or icons.

---

# 79. Forms and Validation

Form errors should appear:

* near the affected field;
* with clear language;
* without relying only on color.

Server-side validation errors must be representable in the component system.

---

# 80. Search Interface

Search should have a consistent command/search pattern.

The global search should visually distinguish result categories:

```text
Entities
Topics
Queries
Pages
Decisions
Evidence
Workflows
```

---

# 81. Filters

Filter controls should use consistent:

* labels;
* chips;
* dropdowns;
* clear-all behavior.

Active filters must remain visible.

---

# 82. Filter Chips

Filter chips should clearly communicate:

```text
Status: Validated
Intent: Commercial
Cluster: Hotels
```

Each should support removal.

---

# 83. Data Freshness Indicator

Use standardized presentation:

```text
Fresh
Updated recently

Aging
May require refresh

Stale
Refresh recommended

Unknown
Freshness unavailable
```

---

# 84. Data Quality Indicator

Data quality should be visually distinct from confidence.

For example:

```text
Data Quality: High
Confidence: Medium
```

These are different concepts.

---

# 85. Confidence vs Data Quality

The design system must never collapse:

```text
Data Quality
```

and:

```text
AI Confidence
```

into one indicator.

High-quality evidence can still produce low-confidence conclusions.

---

# 86. Epistemic vs Workflow State

Likewise:

```text
Epistemic State
```

and:

```text
Workflow State
```

must remain separate.

Example:

```text
Topic:
INFERRED

Workflow:
UNDER_REVIEW
```

This is valid.

---

# 87. Semantic Tokens

Recommended semantic token categories:

```text
Background
Foreground
Surface
Border
Primary
Secondary
Accent
Success
Warning
Error
Info
Focus
Selection
Overlay
```

Components should consume semantic tokens.

---

# 88. Component API Principles

Component APIs should:

* use semantic variants;
* avoid prop explosion;
* support composition;
* support controlled state where appropriate;
* provide sensible defaults;
* expose accessible labels;
* avoid leaking implementation details.

A reusable component should expose a small, stable public API.

---

# 89. Controlled vs Uncontrolled Components

Interactive components should support controlled state when integration requires it.

Examples:

```text
Dialog
Select
Tabs
Popover
```

Uncontrolled behavior may be provided as a convenience.

The API should remain predictable across similar components.

---

# 90. Composition

Prefer composition over large configuration objects.

Example:

```text
Card
├── CardHeader
├── CardContent
└── CardFooter
```

rather than a single component with dozens of unrelated props.

---

# 91. Escape Hatches

Rare custom requirements should be supported through controlled extension mechanisms.

Potential mechanisms:

* class hooks;
* CSS custom properties;
* slots;
* composition;
* semantic variants.

Avoid creating a new prop for every visual edge case.

Component APIs should remain minimal and predictable.

---

# 92. Accessibility Contract

The design system should provide accessible behavior by default.

Interactive components should include appropriate:

* keyboard interaction;
* focus management;
* semantic roles;
* state attributes;
* accessible names;
* disabled behavior.

Accessibility is a system-level responsibility, not a final visual QA step.

---

# 93. Accessibility Baseline

Target:

> **WCAG 2.2 AA**

as the product accessibility baseline.

This includes consideration of:

* perceivable content;
* operable interaction;
* understandable behavior;
* robust implementation.

These four principles form the core W3C accessibility framework.

---

# 94. Keyboard Interaction

All core workflows must be usable through keyboard interaction.

Required:

* visible focus;
* logical tab order;
* no keyboard traps;
* keyboard-operable dialogs;
* keyboard-operable menus;
* keyboard-operable tabs;
* keyboard-operable forms.

ARIA Authoring Practices should inform component behavior where custom widgets are required.

---

# 95. Screen Reader Support

Components should provide:

* semantic structure;
* meaningful labels;
* state announcements;
* appropriate live regions where needed.

Dynamic workflow and AI updates should not create excessive screen-reader noise.

---

# 96. Color Contrast

Text and UI states must satisfy the selected accessibility baseline.

Contrast validation must cover:

* light theme;
* dark theme;
* disabled/active states where applicable;
* status colors;
* focus indicators;
* chart elements.

A design-system component being accessible in isolation does not guarantee that every composition is accessible; page-level validation remains necessary.

---

# 97. Non-Color Semantics

Never communicate critical meaning through color alone.

Example:

```text
✓ Approved
⚠ Conflict
○ Unknown
```

Color may reinforce the state.

---

# 98. RTL Design

The design system must support RTL structurally.

Use logical layout concepts where possible:

```text
margin-inline-start
padding-inline-end
inset-inline-start
```

rather than assuming physical left/right positions.

---

# 99. RTL Component Rules

Components requiring special RTL attention:

* navigation;
* breadcrumbs;
* tables;
* pagination;
* drawers;
* graphs;
* directional icons;
* trees;
* drag/drop;
* menus.

---

# 100. Localization

Components must accommodate:

* longer translated strings;
* different word lengths;
* different numeral systems where required;
* localized dates;
* localized units;
* translated status labels.

Do not design components around English-only string lengths.

---

# 101. Data Formatting

Formatting utilities should standardize:

* dates;
* times;
* numbers;
* percentages;
* currencies;
* large-number abbreviations.

Example:

```text
1,250,000
```

should follow locale-specific formatting rather than a hard-coded representation.

---

# 102. AI Text Formatting

AI-generated text may contain:

* Markdown;
* lists;
* tables;
* links;
* code;
* citations/evidence references.

The design system should provide safe rendering patterns.

Untrusted HTML must never be rendered without appropriate sanitization.

---

# 103. Evidence Citation Styling

Evidence references should be visually distinct from ordinary links.

They should support:

* source identity;
* timestamp;
* provenance;
* inspection.

---

# 104. Tooltip Rules

Tooltips should explain secondary information.

Do not hide critical information exclusively in tooltips.

Tooltips must be accessible through keyboard interaction.

---

# 105. Popover Rules

Popovers should contain contextual controls or information.

They should not become miniature application pages.

---

# 106. Command Palette

A command palette may support:

* global navigation;
* object search;
* actions;
* shortcuts.

It should respect permissions and current project context.

---

# 107. Drag and Drop

Drag-and-drop may be used for:

* page architecture;
* topic organization;
* ordering.

It must have an accessible alternative.

For example:

```text
Move Up
Move Down
Move To
```

---

# 108. Tables and Keyboard Navigation

Large analytical tables should support keyboard navigation where appropriate.

Focus behavior must remain predictable.

---

# 109. Graph Accessibility

Graphs must provide a structured alternative representation.

Example:

```text
Entity Graph
+
Relationship Table
```

A graph should never be the only way to access relationship information.

---

# 110. Data Visualization Accessibility

Charts should provide:

* text summaries;
* accessible labels;
* legends;
* meaningful data tables where necessary.

Important conclusions must not depend solely on visual interpretation.

---

# 111. Design Tokens and Themes

The token architecture should support future themes without rewriting components.

Conceptual structure:

```text
Raw Tokens
    ↓
Semantic Tokens
    ↓
Component Tokens
    ↓
Components
```

Example:

```text
Raw Teal
   ↓
Primary Action
   ↓
Button Primary
```

Components should depend on semantic roles rather than raw color values.

---

# 112. Component States Matrix

Every interactive component should document:

```text
Default
Hover
Focus
Active
Selected
Disabled
Loading
Error
Success
```

Only applicable states need to be implemented.

---

# 113. Component Documentation

Each component should document:

* purpose;
* when to use;
* when not to use;
* variants;
* states;
* accessibility;
* responsive behavior;
* RTL behavior;
* examples;
* API;
* known limitations.

A component library without usage guidance becomes difficult to scale.

---

# 114. Component Governance

New components should require:

1. identified product need;
2. design review;
3. accessibility review;
4. implementation review;
5. documentation;
6. test coverage.

Do not create duplicate components for the same conceptual purpose.

---

# 115. Component Naming

Use semantic names.

Prefer:

```text
EvidencePanel
DecisionCard
ConfidenceIndicator
ReviewQueue
```

Avoid:

```text
BlueCard
FancyPanel
BigBadge
MagicBox
```

---

# 116. Component Ownership

Each component should have an owner category:

```text
Foundation
Shared
Domain
Feature
```

Domain-specific components should not be promoted to the global design system without evidence of reuse.

---

# 117. Design System vs Feature UI

The design system provides reusable primitives.

Feature modules provide domain-specific compositions.

Example:

```text
Design System:
Table
Badge
Drawer
Button

Feature:
TopicValidationTable
DecisionReviewDrawer
SERPResultTable
```

The feature should compose the system rather than fork it.

---

# 118. Design System vs UX Specification

`17_UI_UX_SPECIFICATION.md` defines:

* what the user experience should do;
* user journeys;
* workflows;
* interaction patterns;
* information architecture.

This document defines:

* how the interface visually and behaviorally expresses those patterns.

---

# 119. Design System vs Frontend Architecture

`18_FRONTEND_ARCHITECTURE.md` defines:

* code organization;
* state;
* rendering;
* data access;
* frontend infrastructure.

This document defines:

* tokens;
* components;
* visual states;
* component APIs;
* interaction primitives.

---

# 120. Design System and Output Contracts

`16_OUTPUT_CONTRACTS.md` defines structured data semantics.

The design system defines how states such as:

```text
REQUIRES_REVIEW
CONFLICTED
PARTIAL
HUMAN_APPROVED
```

are visually represented.

The design system must not redefine their semantic meaning.

---

# 121. Design System and Human-in-the-Loop

`15_HUMAN_IN_THE_LOOP.md` defines decision authority.

This system defines the visual language for:

* review;
* approval;
* rejection;
* modification;
* defer;
* escalation.

---

# 122. Design System and Context

`25_CONTEXT_MANAGEMENT.md` defines context behavior.

This system may provide:

* ContextBadge;
* ContextPanel;
* SelectedObjects;
* ContextIndicator.

These components communicate context without owning the context system.

---

# 123. Design System and Skills

`26_SKILLS_AND_TOOLING_POLICY.md` governs tooling.

If tool execution is exposed in UI, use standardized:

```text
Tool
Status
Progress
Result
Failure
```

components.

Do not expose sensitive implementation details.

---

# 124. Design System Versioning

The design system must be versioned.

Changes should be classified as:

```text
Patch
Minor
Major
```

Examples:

### Patch

Bug fix without intended visual/API break.

### Minor

New optional component capability.

### Major

Breaking component API or semantic visual change.

---

# 125. Breaking Changes

Potential breaking changes:

* removing tokens;
* changing component API;
* changing component semantics;
* changing focus behavior;
* removing accessibility support;
* changing status meanings.

Accessibility regressions should be treated seriously as quality regressions rather than cosmetic changes.

---

# 126. Design Token Migration

When tokens change:

```text
Old Token
   ↓
Migration Mapping
   ↓
New Semantic Token
```

Avoid mass hard-coded replacements that bypass semantic architecture.

---

# 127. Visual Regression Testing

Visual regression should cover:

* foundations;
* shared components;
* critical states;
* themes;
* RTL;
* responsive layouts.

Important states include:

```text
Default
Focus
Error
Loading
Disabled
Selected
Dark
RTL
```

---

# 128. Accessibility Testing

Testing should include:

* automated accessibility scans;
* keyboard navigation;
* screen reader testing;
* zoom;
* reduced motion;
* touch interaction where applicable.

Automated testing is valuable but does not replace contextual manual testing.

---

# 129. Component Unit Testing

Components should test:

* rendering;
* variants;
* state changes;
* keyboard behavior;
* event handling;
* accessibility attributes.

---

# 130. Interaction Testing

Critical interactions should test:

```text
Open
→ Focus
→ Interact
→ Submit
→ Feedback
→ Close
→ Focus Return
```

This is especially important for dialogs, drawers, menus, and review workflows.

---

# 131. Cross-Theme Testing

Every important component should be tested in:

* light;
* dark.

Do not assume that a passing light theme automatically produces a valid dark theme.

---

# 132. RTL Testing

Critical components must be tested in both:

```text
LTR
RTL
```

including:

* alignment;
* spacing;
* icons;
* navigation;
* tables;
* drawers;
* trees;
* graphs.

---

# 133. Responsive Testing

Test:

* compact;
* tablet;
* desktop;
* wide desktop.

Complex analytical views must degrade gracefully.

---

# 134. Performance

The design system should avoid unnecessary runtime complexity.

Components should:

* minimize unnecessary re-renders;
* avoid heavy dependencies;
* support lazy loading for advanced modules;
* avoid excessive DOM complexity.

---

# 135. Animation Performance

Animation should use efficient browser-supported mechanisms.

Avoid animation that causes:

* layout thrashing;
* excessive repaint;
* long main-thread tasks.

---

# 136. Design System Dependencies

Dependencies should be minimized.

Before adding a component library or utility, evaluate:

* accessibility;
* bundle size;
* maintenance;
* licensing;
* API quality;
* RTL support;
* theme support;
* customization;
* compatibility.

---

# 137. No Duplicate UI Libraries

The project should avoid maintaining multiple overlapping component systems.

For example, do not simultaneously introduce:

```text
Library A Button
Library B Button
Custom Button
```

without a documented architectural reason.

---

# 138. Headless vs Styled Components

Where beneficial, behavior and accessibility may be separated from visual styling.

This can allow:

```text
Accessible Behavior
        +
Semantic Structure
        +
Design Tokens
        ↓
Visual Component
```

The chosen implementation pattern must be consistent across the system.

---

# 139. CSS Architecture

Styling should be:

* token-driven;
* predictable;
* scoped appropriately;
* compatible with themes;
* compatible with RTL;
* resistant to accidental leakage.

Avoid global selectors that unexpectedly affect unrelated components.

---

# 140. CSS Naming

Where class naming is required, use semantic names.

Avoid styling based on implementation-specific DOM structures.

---

# 141. Z-Index Architecture

Define a controlled z-index scale.

Conceptually:

```text
Base
Sticky
Dropdown
Popover
Drawer
Modal
Toast
Critical Overlay
```

Do not create arbitrary values such as:

```text
z-index: 999999;
```

throughout the application.

---

# 142. Scroll Behavior

Large analytical interfaces may contain:

* page scroll;
* panel scroll;
* table scroll;
* graph canvas scroll.

Scroll ownership should remain obvious.

Avoid nested scrolling where it harms usability.

---

# 143. Focus Restoration

When overlays close, focus should return to the triggering control where appropriate.

This is particularly important for:

* dialogs;
* drawers;
* command palettes;
* menus.

---

# 144. Accessibility Announcements

Dynamic events such as:

```text
Workflow completed
Decision approved
Error occurred
```

may require accessible announcements.

Use live regions carefully to avoid excessive announcements.

---

# 145. Content Tone

UI copy should be:

* concise;
* factual;
* professional;
* non-hyped;
* action-oriented.

Avoid:

```text
Amazing!
Magic!
Your AI knows exactly what to do!
```

Prefer:

```text
Recommendation ready for review.
```

---

# 146. AI Copy Tone

AI-generated interface copy should remain:

* precise;
* evidence-aware;
* appropriately uncertain.

Example:

```text
The available evidence suggests that these topics may share a page.

Confidence: Medium
```

not:

```text
These topics definitely belong on one page.
```

---

# 147. Error Copy

Errors should avoid technical jargon unless the user is expected to understand it.

Prefer:

```text
Search data could not be refreshed.
```

with technical details available in an expandable diagnostic area.

---

# 148. Confirmation Copy

Confirmation should describe consequences.

Prefer:

```text
Approve this recommendation?

This will mark the page mapping as human-approved.
```

rather than:

```text
Are you sure?
```

---

# 149. Design System Anti-Patterns

The following are prohibited:

### 149.1 One-off visual styles

Creating unique styles without system justification.

### 149.2 Raw color usage

Hard-coded colors throughout components.

### 149.3 Semantic overload

Using one visual style for unrelated states.

### 149.4 Color-only state

Communicating status solely through color.

### 149.5 Component prop explosion

Adding props for every edge case.

### 149.6 Duplicate components

Multiple components solving the same problem.

### 149.7 Accessibility afterthought

Adding accessibility after implementation.

### 149.8 Decorative AI branding

Making every component look "AI-powered."

### 149.9 Excessive glassmorphism

Using blur/transparency everywhere.

### 149.10 Excessive motion

Animations that reduce focus or readability.

### 149.11 Giant metric dashboards

Using oversized numbers as the primary product experience.

### 149.12 Visual certainty

Making uncertain AI recommendations look like established facts.

---

# 150. MVP Design System Scope

The MVP should include:

### Foundations

* color;
* typography;
* spacing;
* radius;
* borders;
* elevation;
* motion;
* breakpoints;
* themes.

### Core Components

* Button;
* Input;
* Select;
* Combobox;
* Checkbox;
* Switch;
* Tabs;
* Badge;
* Table;
* Card;
* Dialog;
* Drawer;
* Tooltip;
* Alert;
* Toast;
* Skeleton;
* Empty State;
* Error State;
* Progress.

### Product Components

* Confidence Indicator;
* Epistemic State;
* Evidence Panel;
* Recommendation Card;
* Decision Card;
* Review Queue;
* Workflow Stepper;
* Status Indicator.

### Visualization Foundations

* graph node;
* graph edge;
* legend;
* data visualization container;
* accessible alternative representation.

---

# 151. Future Design System Scope

Potential future additions:

* advanced graph primitives;
* collaborative cursors;
* annotation system;
* advanced data grids;
* scenario comparison;
* strategy simulation components;
* richer dashboard layouts;
* customizable workspace layouts.

These should be added only when justified by product requirements.

---

# 152. Design System Definition of Done

A component is complete when:

1. Its purpose is documented.
2. Its semantic role is defined.
3. Its variants are defined.
4. Its states are defined.
5. Its token dependencies are defined.
6. Its responsive behavior is defined.
7. Its RTL behavior is defined.
8. Its accessibility behavior is defined.
9. Keyboard behavior is tested where applicable.
10. Light theme is tested.
11. Dark theme is tested.
12. Visual regression coverage exists where appropriate.
13. Component tests exist.
14. Usage guidance exists.
15. API is documented.
16. No duplicate component already exists.
17. The component does not introduce arbitrary design values.
18. The component does not bypass established design tokens.
19. The component does not redefine domain semantics.
20. The component can be safely consumed by feature modules.

---

# 153. Final Design System Model

The design system should operate as:

```text
                    DESIGN PRINCIPLES
                           ↓
                    DESIGN TOKENS
                           ↓
                  FOUNDATIONAL PRIMITIVES
                           ↓
                     COMPONENTS
                           ↓
                     PATTERNS
                           ↓
                     TEMPLATES
                           ↓
                   PRODUCT FEATURES
                           ↓
                    USER EXPERIENCE
```

With accessibility integrated throughout:

```text
Accessibility
      ↓
Tokens
      ↓
Components
      ↓
Patterns
      ↓
Features
      ↓
Testing
```

Accessibility must be treated as a system-level concern because the quality of individual components, their integration, and the surrounding page context all contribute to the final accessible experience.

---

# 154. Non-Negotiable Design Principles

1. **Semantic tokens over raw visual values.**
2. **Accessibility by default.**
3. **WCAG 2.2 AA as the baseline target.**
4. **No color-only semantics.**
5. **Keyboard interaction is mandatory for core workflows.**
6. **RTL/LTR are first-class requirements.**
7. **Light and dark themes are first-class.**
8. **AI recommendations must look different from human-approved decisions.**
9. **Observed data must remain distinguishable from inference.**
10. **Confidence must not be confused with data quality.**
11. **Epistemic state must not be confused with workflow state.**
12. **Glass effects remain restrained and optional.**
13. **Motion must serve usability.**
14. **Reduced motion must be respected.**
15. **Components must be composable.**
16. **Component APIs must avoid prop explosion.**
17. **Feature modules compose the design system; they do not fork it.**
18. **Visualization is analytical, not decorative.**
19. **Every important visualization has an accessible alternative.**
20. **Design decisions must be documented.**
21. **New components require justification.**
22. **Duplicate UI primitives are prohibited without architectural justification.**
23. **The design system must not redefine backend/domain semantics.**
24. **The design system must support professional information density without sacrificing comprehension.**
25. **Visual polish must never be used to hide uncertainty, missing data, or system failure.**

---

# 155. Document Control

```yaml
document:
  id: "19"
  filename: "19_DESIGN_SYSTEM.md"
  status: "APPROVED_AS_BASELINE_DESIGN_SYSTEM"
  product: "SEO Research & Strategy Copilot / SEO Decision Engine"
  authority: "baseline_design_system"

design:
  philosophy: "intelligent_calm_analytical_precise"
  visual_language:
    - clean
    - grid_based
    - whitespace_oriented
    - layered
    - restrained
    - professional

foundations:
  - color
  - typography
  - spacing
  - sizing
  - radius
  - border
  - elevation
  - motion
  - opacity
  - breakpoints
  - z_index

themes:
  light: true
  dark: true
  semantic_tokens: true

typography:
  latin: "Geist"
  persian: "Vazirmatn"
  substitution_allowed: true

color:
  semantic_tokens: true
  color_only_semantics: false
  primary_direction: "deep_teal"
  accent_direction: "warm_amber"

surfaces:
  levels:
    - surface_0
    - surface_1
    - surface_2
    - surface_3
    - surface_4
  glass_effects:
    allowed: true
    default_usage: "restrained"

components:
  layers:
    - foundations
    - primitives
    - components
    - patterns
    - templates
  api_principles:
    - semantic_variants
    - composition
    - controlled_state_where_needed
    - accessibility_by_default
    - minimal_public_api
    - no_prop_explosion

accessibility:
  baseline: "WCAG_2.2_AA"
  keyboard_navigation: true
  screen_reader_support: true
  visible_focus: true
  no_color_only_semantics: true
  reduced_motion: true
  rtl_support: true
  accessible_visualization_alternatives: true

localization:
  multilingual: true
  rtl: true
  ltr: true
  initial_languages:
    - en
    - fa
    - de

state_representation:
  epistemic:
    - OBSERVED
    - INFERRED
    - ESTIMATED
    - RECOMMENDED
    - HUMAN_APPROVED
    - CONFLICTED
    - UNKNOWN
  workflow:
    - DRAFT
    - AI_PROPOSED
    - VALIDATED
    - UNDER_REVIEW
    - HUMAN_APPROVED
    - REJECTED
    - SUPERSEDED
    - ARCHIVED
  distinction_required: true

ai_ux:
  recommendation_distinct_from_decision: true
  evidence_visible: true
  confidence_visible: true
  visual_ai_hype: false
  chain_of_thought_exposure: false

visualization:
  analytical_first: true
  decorative_graphs: false
  accessible_alternative_required: true
  semantic_color_usage: true

governance:
  component_review_required: true
  accessibility_review_required: true
  documentation_required: true
  visual_regression_required_where_appropriate: true
  duplicate_components_prohibited: true
  semantic_token_usage_required: true

testing:
  component: true
  interaction: true
  accessibility: true
  visual_regression: true
  responsive: true
  rtl_ltr: true
  light_dark: true

dependencies:
  ux_specification: "17_UI_UX_SPECIFICATION.md"
  frontend_architecture: "18_FRONTEND_ARCHITECTURE.md"
  output_contracts: "16_OUTPUT_CONTRACTS.md"
  human_in_the_loop: "15_HUMAN_IN_THE_LOOP.md"
  seo_decision_engine: "12_SEO_DECISION_ENGINE.md"
  context_management: "25_CONTEXT_MANAGEMENT.md"
  skills_and_tooling_policy: "26_SKILLS_AND_TOOLING_POLICY.md"

primary_rule:
  statement: "The design system provides the shared visual and interaction language of the product while preserving semantic correctness, accessibility, evidence visibility, uncertainty, and human decision authority."

next_dependency:
  document: "20_PROJECT_STRUCTURE.md"
```
