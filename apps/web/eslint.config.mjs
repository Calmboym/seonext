import { FlatCompat } from "@eslint/eslintrc";

// PHASE-0.8 (Testing Foundation & CI) wiring — apps/web/package.json's
// PHASE-0.6 comment deliberately deferred lint tooling to this subtask.
// FlatCompat is needed because `eslint-config-next` still ships a
// legacy-style shareable config; this is the standard bridge Next.js
// itself documents for ESLint 9's flat-config format.
const compat = new FlatCompat({
  baseDirectory: import.meta.dirname,
});

const eslintConfig = [...compat.extends("next/core-web-vitals", "next/typescript")];

export default eslintConfig;
