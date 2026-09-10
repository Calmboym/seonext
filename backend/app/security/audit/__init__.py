"""Security audit: policy around *what* security-relevant actions must
be recorded and reviewed (e.g. "every permission change must be
retained for N days") — distinct from
backend/app/observability/audit (PHASE-0.7), which is the generic
technical sink that would actually persist an audit-log entry once one
is emitted. This module would decide the *policy*; observability/audit
would be one of the things that policy writes to.

Reserved for PHASE-1+ — recorded here (Observation #5, .ai/WBS.md §4,
alongside the same module's secrets/__init__.py note) so a later phase
doesn't conflate this security-policy module with the observability
sink that shares the word "audit." Nothing here yet, matching
observability/audit/__init__.py: there is no security-relevant action to
have a retention policy for until PHASE-1's user/permission model exists.
"""
