"""Observability: structured logging, metrics, tracing, audit, and event
surfaces. See docs/20_PROJECT_STRUCTURE.md §24 and docs/07_TECHNICAL_
ARCHITECTURE.md §3 (observability stack line: structured_logging, metrics,
tracing).

Populated starting PHASE-0.7 (Observability Foundation). AI-specific
observability fields (model/provider/model version/prompt version/token
usage/latency/tool calls/validation result/output status/cost estimate/
workflow-task identifiers — §24) are explicitly out of scope until an AI
runtime exists (a later phase) — nothing here fabricates those fields
ahead of time, per PHASE-0.7's own acceptance criterion 3
(.ai/WBS.md §4).

Submodules:
    logging/  — structured (JSON) application logging. See logging/core.py.
    metrics/  — request-count/duration metrics, Prometheus-exposition-
                format-compatible. See metrics/registry.py.
    tracing/  — lightweight in-process span tracking (contextvar-based, no
                external tracing backend wired yet). See tracing/tracer.py.
    audit/    — reserved for later phase. No audit-worthy domain action
                exists yet at PHASE-0 (no user accounts, no domain writes)
                — see audit/__init__.py.
    events/   — reserved for later phase. Distinct from the domain/
                application/integration event bus described in
                docs/20_PROJECT_STRUCTURE.md §50 (backend/app/events/, not
                yet created) — this events/ submodule is for observability-
                emitted analytics-style events, not the domain event bus.
                See events/__init__.py and .ai/WBS.md §4 Observation #4.
"""
