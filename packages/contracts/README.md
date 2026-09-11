# packages/contracts

Shared API/output schemas consumed by more than one app (`apps/api`, `apps/web`, and eventually `apps/worker`). See `docs/20_PROJECT_STRUCTURE.md` §32, §54.

## Status (`PHASE-1.4`, session 9)

Populated for the first time: `src/envelope.ts` (`SuccessEnvelope<T>`), `src/errors.ts` (`ErrorResponse`/`ErrorBody`, moved here per this file's own prior note now that `apps/web` has a real reason to consume it), `src/auth.ts`, `src/projects.ts`.

**Synchronization strategy (`PHASE-1.4` acceptance criterion 3 — "packages/contracts and backend/app/contracts/api agree with each other, no drift"):** manual, by hand, field-for-field — not generated. `docs/20_PROJECT_STRUCTURE.md` §54 lists OpenAPI generation / generated TypeScript types as *options*, not a requirement, and none of that tooling can be installed in this project's current sandbox (no network access — see `.ai/PROJECT_STATE.md` §9, Risk R9). Every type in this package's `src/` has a one-line comment naming the backend Python file it mirrors; when either side changes a field, the other must be updated in the same change. This is a real limitation, disclosed rather than hidden: nothing currently *enforces* the two stay in sync beyond code review and this convention. A future session with package-install access should revisit this — likely via an OpenAPI-schema-to-TypeScript generation step wired into CI — rather than continuing hand-sync indefinitely.

**Verification:** unlike the backend Pydantic contracts (`pydantic` not installed in this sandbox — `IMPLEMENTED / UNVERIFIED`), this package's TypeScript **was genuinely compiled** this session (`tsc` and Node are available locally, no npm registry access needed for plain `.ts` interface files with zero external deps): `npx tsc -p tsconfig.json` from this directory exits 0. A deliberate type error was introduced in a scratch consuming file, confirmed to produce real `tsc` diagnostics, then removed — see `.ai/PROJECT_STATE.md` §14 for the full record. Verification status: `RUNTIME_VERIFIED` (compile-checked) for the type definitions themselves; there is of course no way to verify *semantic* agreement with the backend without both sides being exercised against the same real HTTP traffic, which needs `fastapi`/`pydantic` installed (Risk R9).

