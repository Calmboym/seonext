# apps/

Runnable applications. See `docs/20_PROJECT_STRUCTURE.md` §5.1.

| App | Status | Notes |
|---|---|---|
| `api/` | Populated (`PHASE-0.4`) | FastAPI entrypoint (`main.py`), thin — imports `app` from `backend/app/main.py`. Must not contain core SEO reasoning. |
| `web/` | Populated (`PHASE-0.6`, session 7) | Next.js App Router shell (`app/layout.tsx`, `app/page.tsx`), consuming `apps/api`'s health endpoint as a smoke test. No feature/component implementation yet — see `apps/web/components/README.md` etc. for what's deliberately still empty. |
| `worker/` | Not yet created | Deferred — no phase has authorized background worker execution yet. |
