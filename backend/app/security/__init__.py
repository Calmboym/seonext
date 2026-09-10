"""Security boundary: authN/authZ primitives, tenant isolation, secret
handling touchpoints. See docs/07_TECHNICAL_ARCHITECTURE.md §§53-56,
docs/20_PROJECT_STRUCTURE.md §23.

Populated starting PHASE-0.5 (Authentication Foundation, session 7):
`authentication/` — session/token issuance, secure password storage.
`authorization/`, `permissions/`, `tenancy/`, `secrets/`, `audit/`,
`policies/` remain reserved placeholders (PHASE-1+) — each explains why
in its own `__init__.py`. PHASE-0.5 deliberately implements only the
authentication mechanism, not the rest of this boundary (.ai/WBS.md §4
acceptance criterion 4).
"""
