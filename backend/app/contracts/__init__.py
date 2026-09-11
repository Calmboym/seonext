"""Backend-side output/response contract definitions, distinct from packages/contracts (shared, cross-app schemas). See docs/16_OUTPUT_CONTRACTS.md.

Populated (`PHASE-1.4`, session 9): `api/` — versioned request/response
schemas for the `/api/v1/auth` and `/api/v1/projects` groups
(docs/07 §15), plus the shared `SuccessEnvelope` (16 §12's success half).
Written before `PHASE-1.2`/`.5`'s endpoints, per docs/03 §97. Other
contract categories 20 §16 lists (`agents/`, `workflows/`, `decisions/`,
`evidence/`, `context/`, `common/`) remain empty placeholders for the
phases that introduce them."""
