# apps/web/stores/

Global client-side state stores, scoped per `docs/20_PROJECT_STRUCTURE.md` §28's state-separation principle (Server State / UI State / Session State / Workflow State / Form State / Derived View State) — this directory is explicitly **not** a single global store containing all application state.

Empty at `PHASE-0.6` — no client state exists yet to manage. `app/page.tsx`'s health check reads server-fetched data directly (`services/health.ts`, an async Server Component); nothing here yet needs client-side state.
