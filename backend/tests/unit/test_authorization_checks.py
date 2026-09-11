"""Tests for `backend/app/security/{authorization,tenancy,permissions}`
(`PHASE-1.3`).

Directly implements `.ai/WBS.md` §4B's `PHASE-1.3` acceptance criteria:
- (1) "a user cannot read or modify a workspace/project they are not a
  member of — proven by a negative test, not merely asserted":
  `test_non_member_cannot_access_a_workspace_they_are_not_in`.
- (4) "at least one privilege-escalation test and one cross-project-
  leakage test exist":
  `test_a_member_cannot_use_a_lower_role_to_pass_a_higher_role_gate` and
  `test_member_of_workspace_a_cannot_reach_a_project_that_belongs_to_workspace_b`.

Zero third-party imports (the checks under test have none — see their
own module docstrings — and `_authorization_fakes.py` only imports the
domain layer). See test_domain_user.py's docstring for the invocation
note and the `asyncio.run` wrapper convention (same as
test_register_user_use_case.py — `pytest-asyncio` is not installed).
"""

import asyncio

from backend.app.domain.common.ids import new_id
from backend.app.domain.membership.entity import Membership, Role
from backend.app.domain.project.entity import Project
from backend.app.security.authorization.errors import AuthorizationDeniedError, ProjectNotFoundError
from backend.app.security.authorization.project import require_project_access
from backend.app.security.authorization.workspace import require_workspace_access
from backend.app.security.permissions.roles import role_meets_minimum
from backend.app.security.tenancy.membership import get_role, is_member
from backend.tests.unit._authorization_fakes import FakeMembershipRepository, FakeProjectRepository


# ---------------------------------------------------------------------------
# permissions.roles — role ranking
# ---------------------------------------------------------------------------


def test_role_hierarchy_is_owner_above_admin_above_member() -> None:
    assert role_meets_minimum(Role.OWNER, Role.MEMBER) is True
    assert role_meets_minimum(Role.OWNER, Role.ADMIN) is True
    assert role_meets_minimum(Role.OWNER, Role.OWNER) is True
    assert role_meets_minimum(Role.ADMIN, Role.MEMBER) is True
    assert role_meets_minimum(Role.ADMIN, Role.OWNER) is False
    assert role_meets_minimum(Role.MEMBER, Role.ADMIN) is False
    assert role_meets_minimum(Role.MEMBER, Role.OWNER) is False


def test_a_role_always_meets_its_own_minimum() -> None:
    for role in Role:
        assert role_meets_minimum(role, role) is True


# ---------------------------------------------------------------------------
# tenancy.membership — lookups
# ---------------------------------------------------------------------------


def test_get_role_returns_none_for_a_user_with_no_membership() -> None:
    async def _body() -> None:
        memberships = FakeMembershipRepository()
        role = await get_role(memberships=memberships, workspace_id=new_id(), user_id=new_id())
        assert role is None

    asyncio.run(_body())


def test_is_member_reflects_get_role() -> None:
    async def _body() -> None:
        memberships = FakeMembershipRepository()
        workspace_id, user_id = new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.ADMIN))

        assert await is_member(memberships=memberships, workspace_id=workspace_id, user_id=user_id) is True
        assert await is_member(memberships=memberships, workspace_id=workspace_id, user_id=new_id()) is False

    asyncio.run(_body())


# ---------------------------------------------------------------------------
# authorization.workspace — require_workspace_access
# ---------------------------------------------------------------------------


def test_a_member_can_access_their_own_workspace() -> None:
    async def _body() -> None:
        memberships = FakeMembershipRepository()
        workspace_id, user_id = new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.MEMBER))

        role = await require_workspace_access(user_id=user_id, workspace_id=workspace_id, memberships=memberships)
        assert role is Role.MEMBER

    asyncio.run(_body())


def test_non_member_cannot_access_a_workspace_they_are_not_in() -> None:
    """PHASE-1.3 acceptance criterion 1's negative test: a user with NO
    membership row at all for this workspace must be rejected."""

    async def _body() -> None:
        memberships = FakeMembershipRepository()
        workspace_id, outsider_id = new_id(), new_id()
        # Deliberately no membership added for outsider_id in workspace_id.

        try:
            await require_workspace_access(user_id=outsider_id, workspace_id=workspace_id, memberships=memberships)
            raise AssertionError("expected AuthorizationDeniedError")
        except AuthorizationDeniedError:
            pass

    asyncio.run(_body())


def test_a_member_of_one_workspace_cannot_access_a_different_workspace_they_did_not_join() -> None:
    """The lateral-movement variant of the negative test: having a real,
    valid membership in workspace A must not grant any access to
    workspace B — the check must look up B specifically, not just "does
    this user have *a* membership somewhere"."""

    async def _body() -> None:
        memberships = FakeMembershipRepository()
        workspace_a, workspace_b, user_id = new_id(), new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_a, user_id=user_id, role=Role.OWNER))

        # Legitimate access to A:
        await require_workspace_access(user_id=user_id, workspace_id=workspace_a, memberships=memberships)

        # No membership in B at all — must be rejected despite being an
        # OWNER elsewhere.
        try:
            await require_workspace_access(user_id=user_id, workspace_id=workspace_b, memberships=memberships)
            raise AssertionError("expected AuthorizationDeniedError")
        except AuthorizationDeniedError:
            pass

    asyncio.run(_body())


def test_a_member_cannot_use_a_lower_role_to_pass_a_higher_role_gate() -> None:
    """PHASE-1.3 acceptance criterion 4's privilege-escalation test: a
    real MEMBER-level membership must not satisfy an ADMIN-or-higher
    gate. There is no client-supplied "role" parameter anywhere in this
    call — the role comes only from the looked-up Membership row — so
    the only way this could fail is the rank comparison itself being
    wrong."""

    async def _body() -> None:
        memberships = FakeMembershipRepository()
        workspace_id, user_id = new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.MEMBER))

        try:
            await require_workspace_access(
                user_id=user_id, workspace_id=workspace_id, memberships=memberships, minimum_role=Role.ADMIN
            )
            raise AssertionError("expected AuthorizationDeniedError")
        except AuthorizationDeniedError:
            pass

        # Sanity: an ADMIN-role membership DOES pass the same gate, so
        # the test above is failing for the right reason (role too low),
        # not because the gate is simply broken/always-deny.
        await memberships.add(Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.ADMIN))
        role = await require_workspace_access(
            user_id=user_id, workspace_id=workspace_id, memberships=memberships, minimum_role=Role.ADMIN
        )
        assert role is Role.ADMIN

    asyncio.run(_body())


# ---------------------------------------------------------------------------
# authorization.project — require_project_access
# ---------------------------------------------------------------------------


async def _seed_project(projects: FakeProjectRepository, *, workspace_id: str, name: str = "Acme SEO") -> Project:
    project = Project.create(workspace_id=workspace_id, name=name)
    await projects.add(project)
    return project


def test_a_member_can_access_a_project_in_their_own_workspace() -> None:
    async def _body() -> None:
        memberships, projects = FakeMembershipRepository(), FakeProjectRepository()
        workspace_id, user_id = new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_id, user_id=user_id))
        project = await _seed_project(projects, workspace_id=workspace_id)

        resolved_project, role = await require_project_access(
            user_id=user_id,
            workspace_id=workspace_id,
            project_id=project.id,
            projects=projects,
            memberships=memberships,
        )
        assert resolved_project.id == project.id
        assert role is Role.MEMBER

    asyncio.run(_body())


def test_member_of_workspace_a_cannot_reach_a_project_that_belongs_to_workspace_b() -> None:
    """PHASE-1.3 acceptance criterion 4's cross-project-leakage test: a
    legitimate member of workspace A, who supplies workspace A's own ID
    alongside a project ID that actually belongs to workspace B, must
    not be able to read that project — proving `require_project_access`
    genuinely composes with `ProjectRepository`'s tenant-scoping rather
    than trusting the caller's claimed workspace_id/project_id pairing
    at face value (docs/03 §109)."""

    async def _body() -> None:
        memberships, projects = FakeMembershipRepository(), FakeProjectRepository()
        workspace_a, workspace_b, user_id = new_id(), new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_a, user_id=user_id, role=Role.OWNER))
        project_in_b = await _seed_project(projects, workspace_id=workspace_b, name="Someone Else's Project")

        try:
            await require_project_access(
                user_id=user_id,
                workspace_id=workspace_a,  # the user's OWN, legitimate workspace
                project_id=project_in_b.id,  # but someone else's project ID
                projects=projects,
                memberships=memberships,
            )
            raise AssertionError("expected ProjectNotFoundError")
        except ProjectNotFoundError:
            pass

    asyncio.run(_body())


def test_non_member_is_rejected_before_any_project_lookup_even_for_a_real_project_id() -> None:
    """Confirms the membership-first ordering documented in project.py:
    a non-member of workspace_b must get `AuthorizationDeniedError`, not
    `ProjectNotFoundError`, even when the project ID they supply is a
    real one that exists *somewhere* (just not in workspace_b) — proving
    the project lookup never ran for them at all. Using a project ID
    that doesn't exist in workspace_b (rather than one that legitimately
    does) is deliberate: if the two checks ran in the opposite order,
    the project lookup would fail first and produce
    `ProjectNotFoundError` instead, which is exactly the distinction this
    test needs to be capable of catching — a project that genuinely
    exists in workspace_b would reach the same final exception either
    way and prove nothing about ordering."""

    async def _body() -> None:
        memberships, projects = FakeMembershipRepository(), FakeProjectRepository()
        workspace_a, workspace_b, outsider_id = new_id(), new_id(), new_id()
        # A real project, but in workspace_a, not workspace_b.
        real_project_elsewhere = await _seed_project(projects, workspace_id=workspace_a)
        # Deliberately no membership added for outsider_id in workspace_b.

        try:
            await require_project_access(
                user_id=outsider_id,
                workspace_id=workspace_b,
                project_id=real_project_elsewhere.id,
                projects=projects,
                memberships=memberships,
            )
            raise AssertionError("expected AuthorizationDeniedError, not ProjectNotFoundError")
        except AuthorizationDeniedError:
            pass
        except ProjectNotFoundError:
            raise AssertionError(
                "got ProjectNotFoundError instead of AuthorizationDeniedError — the project "
                "lookup ran before the membership check, which is the exact ordering bug this "
                "test exists to catch"
            )

    asyncio.run(_body())


def test_a_member_requesting_a_genuinely_nonexistent_project_gets_not_found_not_denied() -> None:
    async def _body() -> None:
        memberships, projects = FakeMembershipRepository(), FakeProjectRepository()
        workspace_id, user_id = new_id(), new_id()
        await memberships.add(Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.OWNER))

        try:
            await require_project_access(
                user_id=user_id,
                workspace_id=workspace_id,
                project_id=new_id(),  # no such project was ever created
                projects=projects,
                memberships=memberships,
            )
            raise AssertionError("expected ProjectNotFoundError")
        except ProjectNotFoundError:
            pass

    asyncio.run(_body())


if __name__ == "__main__":
    test_functions = [
        test_role_hierarchy_is_owner_above_admin_above_member,
        test_a_role_always_meets_its_own_minimum,
        test_get_role_returns_none_for_a_user_with_no_membership,
        test_is_member_reflects_get_role,
        test_a_member_can_access_their_own_workspace,
        test_non_member_cannot_access_a_workspace_they_are_not_in,
        test_a_member_of_one_workspace_cannot_access_a_different_workspace_they_did_not_join,
        test_a_member_cannot_use_a_lower_role_to_pass_a_higher_role_gate,
        test_a_member_can_access_a_project_in_their_own_workspace,
        test_member_of_workspace_a_cannot_reach_a_project_that_belongs_to_workspace_b,
        test_non_member_is_rejected_before_any_project_lookup_even_for_a_real_project_id,
        test_a_member_requesting_a_genuinely_nonexistent_project_gets_not_found_not_denied,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
