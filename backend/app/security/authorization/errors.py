"""`AuthorizationDeniedError` — the plain exception every check in this
package raises, kept separate from
`backend.app.api.errors.exceptions.AuthorizationError` for exactly the
reason `backend.app.security.authentication.tokens.TokenError` and
`backend.app.application.errors.ApplicationError` already are (see either
of their module docstrings): the API layer depends on `security/`, not
the reverse (docs/07 §14), and a hard-import of `sqlalchemy`-dependent
repository types is avoided throughout this package for the same
zero-third-party-dependency testability reason `backend/app/application/
commands/auth/` uses `Protocol`s.

`backend/app/api/routes/*.py` is expected to catch this and translate it
into `AuthorizationError` (403) — the same "define locally, translate at
the API boundary" pattern this whole codebase now uses consistently.
"""

from __future__ import annotations


class AuthorizationDeniedError(Exception):
    """Raised when an authenticated user does not have sufficient
    membership/role to access a workspace or project. Carries no detail
    about *why* beyond the message (e.g. not "you have MEMBER but need
    ADMIN" in a machine-readable field) — docs/03 §109 combined with
    ordinary least-privilege practice: telling an unauthorized caller
    exactly what role they're missing, or that the resource exists at
    all versus them just not being a member, is information a 403
    doesn't need to hand out. `backend/app/api/routes/*.py` maps this to
    a generic `AuthorizationError` message, not this exception's own
    `str()`."""


class ProjectNotFoundError(Exception):
    """Raised by `backend.app.security.authorization.project.
    require_project_access` when the caller *is* a sufficiently-
    privileged member of the workspace, but no project with the given ID
    exists in it. Kept distinct from `AuthorizationDeniedError`
    deliberately: a workspace member requesting a nonexistent/mistyped
    project ID is a genuine 404, not a 403 — they are allowed to be in
    this workspace, this specific resource just isn't there. A
    *non*-member never reaches this check at all (`require_project_access`
    checks workspace membership first — see that module's docstring), so
    this exception being raised or not never depends on whether the
    caller had access to the workspace, only on whether the project
    exists once that's already established."""
