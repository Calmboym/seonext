"""Domain layer: business and SEO domain rules (topic rules, entity relationships, decision states, recommendation rules, workflow domain rules, page relationships, validation rules). Must remain independent of HTTP, LLM providers, specific search providers, frontend frameworks, and infrastructure details. See docs/07_TECHNICAL_ARCHITECTURE.md §8.

Populated (`PHASE-1.1`, session 9): `user/`, `workspace/`, `project/` —
the platform-tenancy entities (User, Workspace, Project) that everything
else in this project is scoped under. `common/` holds cross-cutting
domain code (currently: stable-ID generation). Extended (`PHASE-1.3`,
session 9): `membership/` — who belongs to which Workspace, at what
Role; see that module's docstring for why it lives here rather than
directly under `backend/app/security/`. The SEO-domain submodules
docs/20_PROJECT_STRUCTURE.md §10 also lists (`business/`, `entity/`,
`eav/`, `topic/`, `keyword/`, `intent/`, `search/`, `serp/`, `page/`,
`competitor/`, `content_gap/`, `cannibalization/`, `internal_linking/`,
`topical_map/`, `decision/`, `evidence/`, `provenance/`, `workflow/`)
remain empty placeholders for the phases that introduce them."""
