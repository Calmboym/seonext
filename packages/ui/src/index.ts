// Shared frontend design-system components (FOUNDATION/SHARED tiers per
// .ai/COMPONENT_MATRIX.md, docs/20_PROJECT_STRUCTURE.md §27: buttons,
// inputs, dialogs, tables, cards, badges, charts, graph primitives,
// evidence indicators, confidence indicators, state indicators).
//
// No components are implemented yet — this package exists starting
// PHASE-0.6 (Frontend Foundation) so it is importable in principle from
// apps/web, per that subtask's own scope ("makes them importable in
// principle, not built" — .ai/WBS.md §4, acceptance criterion 4: "no
// premature component implementation"). Populate component-by-component
// in later phases; each addition should be re-exported from this file so
// `import { X } from "@seonex/ui"` stays the one consumption pattern.

export {};
