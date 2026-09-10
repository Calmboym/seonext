import { defineConfig } from "vitest/config";

// Node environment, not jsdom — the only test suite that exists so far
// (tests/unit/health.test.ts) exercises a plain data-fetching function
// with no DOM interaction. Switch to `environment: "jsdom"` (and add the
// `jsdom` devDependency) once a component test needs to render anything.
export default defineConfig({
  test: {
    environment: "node",
    include: ["tests/**/*.test.ts", "tests/**/*.test.tsx"],
  },
});
