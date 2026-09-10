# SESSION_PROMPT.md — Session Entry Point

This file is a **protocol**, not a data store. It tells a new AI session how to find out what's going on; it does not itself contain the project's current state, task list, or documentation. If you find yourself copying content from `PROJECT_STATE.md`, `TASK_BOARD.md`, or `WBS.md` into this file, stop — reference them instead.

## Session Start Protocol

1. Read this file in full.
2. Read `.ai/PROJECT_STATE.md` — current phase, task, blockers, risks, and the authorization scope of the last session.
3. Read `.ai/TASK_BOARD.md` — identify which task (if any) is `AUTHORIZED`. **A task with Lifecycle Status `READY` is not authorized.** Only implement a task whose Authorization column explicitly says `AUTHORIZED`.
4. Read the relevant section of `.ai/WBS.md` for that task's dependencies and required documents.
5. Resolve dependencies: confirm every prerequisite in `WBS.md` is actually `DONE`, not just planned.
6. Determine required context using the procedure below (§ Context Retrieval) — do not load all 26 documents by default.
7. Check `.ai/COMPONENT_MATRIX.md` and `.ai/OWNERSHIP.md` if the task touches any UI component or cross-subsystem boundary.
8. Check `.ai/PROJECT_STATE.md` § Known Risks and § Blockers before starting.
9. Confirm the task is authorized (step 3). If not, stop and ask the human, exactly as `BOOTSTRAP-001` did.
10. Execute only that task.

## Context Retrieval Procedure (built on `25_CONTEXT_MANAGEMENT.md` — not duplicated here)

For the authorized task, classify documents as `REQUIRED` / `RECOMMENDED` / `OPTIONAL` / `EXCLUDED` following `25_CONTEXT_MANAGEMENT.md` §§ 9–24. Concretely:

- `REQUIRED`: `03_MASTER_RULES.md` (always) + the specific architecture/domain document(s) the task's WBS entry names + the relevant Output Contract section (`16`) if the task produces a contract-bound artifact.
- `RECOMMENDED`: the task's immediate parent's governing document, and `.ai/COMPONENT_MATRIX.md` / `.ai/OWNERSHIP.md` if components are involved.
- `OPTIONAL`: historical decisions in `.ai/PROJECT_STATE.md` § Active/Recent Decisions relevant to the task's domain.
- `EXCLUDED`: everything outside the task's declared dependency set in `WBS.md` — in particular, do not load frontend documents (`17`, `18`, `19`) for backend-only tasks or vice versa, unless the task is genuinely cross-cutting.

Example: a task to implement Entity Resolution would require `03, 06, 08, 09`, recommend `16`'s relevant contract section and `25` itself for the boundaries of this very procedure, and exclude `17, 18, 19`.

## Execution Procedure

Understand → Plan → Inspect existing implementation → Identify dependencies → Implement the smallest correct change → Test → Validate → Regression test → Verify → Document → Update state. (Full detail: `21_DEVELOPMENT_AND_DEBUG.md`, `22_TESTING_AND_VALIDATION.md` — referenced, not restated.)

## Testing Procedure

Follow `22_TESTING_AND_VALIDATION.md`. Never report a Verification Status of `TESTED` or `RUNTIME_VERIFIED` without evidence that tests actually ran. `IMPLEMENTED` + `UNVERIFIED` is a legitimate, honest combination — use it rather than overstating status.

## State Update Procedure

At the end of every meaningful task:
1. Update `.ai/TASK_BOARD.md` — both Lifecycle Status and Verification Status, independently (never conflate them — see Q2 in `PROJECT_STATE.md` § 10).
2. Update `.ai/PROJECT_STATE.md` — Current Task/Subtask, Completed/Verified/Unverified Work, Blockers, Required Next Action.
3. Update `.ai/WBS.md` only if the task changed the dependency graph or task hierarchy itself.
4. Update `.ai/COMPONENT_MATRIX.md` / `.ai/OWNERSHIP.md` only if components or ownership changed.
5. Record any new decision the same way Q1–Q7 are recorded in `PROJECT_STATE.md` § 10 — as a numbered, dated entry with what was decided and where it was applied.

## Handoff Procedure

Before ending a session, `PROJECT_STATE.md` must let the next session answer, without asking you: what was done, what was tested, what was verified, what remains, what's blocked, what changed and why, what task comes next, what it depends on, and what context it requires. If it can't answer all of those, the handoff is incomplete — finish updating the state files before stopping.

## Non-Negotiables for Every Session

- Never implement a task that is not explicitly `AUTHORIZED` on `.ai/TASK_BOARD.md`.
- Never claim `TESTED`, `VALIDATED`, or `RUNTIME_VERIFIED` without evidence.
- Never silently resolve a material architectural or terminology conflict — escalate to the human, the way Q1–Q7 were escalated.
- Never restate the authority hierarchy — it lives in `03_MASTER_RULES.md` § 2, referenced everywhere else.
- Treat this conversation as temporary; treat `.ai/*.md` as project continuity.
