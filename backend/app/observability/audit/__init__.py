"""Audit logging: a record of security/state-relevant actions (who did
what, when), distinct from ordinary application logging
(backend/app/observability/logging) which records operational request/
response flow. See docs/20_PROJECT_STRUCTURE.md §24.

Reserved for a later phase — empty at PHASE-0.7 by design, not oversight.
There is no audit-worthy action to record yet: no user accounts exist
(PHASE-0.5, if/when authorized, is a bare session/token mechanism with no
user records behind it — see .ai/WBS.md §4's own scope note on that
subtask), and no domain writes exist (backend/app/domain/ is empty).
Populate this once PHASE-1's user/workspace/project model introduces
actions worth auditing.
"""
