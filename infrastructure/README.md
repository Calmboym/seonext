# infrastructure/

Operational infrastructure concerns — distinct from `backend/app/infrastructure/` (in-process code such as the config loader and DB session factory). See `docs/20_PROJECT_STRUCTURE.md` §3.

| Subdirectory | Status |
|---|---|
| `database/` | Populated (`PHASE-0.3`) — migrations, seeds, fixtures, scripts. |
| `redis/` | Not yet created — no caching/queue layer is in scope until a later phase needs Redis (`docs/07_TECHNICAL_ARCHITECTURE.md` §38). |
| `vector/` | Not yet created — semantic retrieval vector store choice is deliberately deferred (Observation #2, `.ai/WBS.md` § 4; `docs/07_TECHNICAL_ARCHITECTURE.md` §32). |
| `object_storage/` | Not yet created — no phase has required object storage yet. |
| `deployment/` | Not yet created — deployment architecture is out of scope for local Phase-0 foundation work. |
