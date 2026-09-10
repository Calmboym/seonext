# packages/ui

Shared frontend design-system components. See `docs/20_PROJECT_STRUCTURE.md` §27/§32 and `.ai/COMPONENT_MATRIX.md` (FOUNDATION/SHARED tiers) for the component inventory this package will eventually implement.

**Wired starting `PHASE-0.6` (session 7):** `package.json` + `src/index.ts` exist and `apps/web` depends on `@seonex/ui` as an npm workspace package (root `package.json`'s `workspaces` list), consumed via Next.js `transpilePackages` (`apps/web/next.config.mjs`) since this package ships raw TypeScript with no build step of its own. Still **empty of actual components** — `src/index.ts` exports nothing — per `PHASE-0.6`'s own acceptance criterion 4 ("no premature component implementation", `.ai/WBS.md` §4). Populated component-by-component starting whichever later phase needs the first one.
