"""Unit tests for the `Membership` domain entity
(backend/app/domain/membership/entity.py).

Backend-unit category. Zero third-party imports — see
test_domain_user.py's docstring for the invocation note, which applies
identically here.
"""

from backend.app.domain.common.ids import new_id
from backend.app.domain.membership.entity import Membership, MembershipDomainError, Role


def _ids() -> tuple[str, str]:
    return new_id(), new_id()


def test_create_defaults_to_the_member_role() -> None:
    workspace_id, user_id = _ids()
    membership = Membership.create(workspace_id=workspace_id, user_id=user_id)
    assert membership.role is Role.MEMBER
    assert membership.belongs_to(workspace_id) is True
    assert membership.is_held_by(user_id) is True


def test_create_with_an_explicit_role() -> None:
    workspace_id, user_id = _ids()
    membership = Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.OWNER)
    assert membership.role is Role.OWNER


def test_malformed_workspace_id_is_rejected() -> None:
    try:
        Membership.create(workspace_id="not-a-uuid", user_id=new_id())
        raise AssertionError("expected MembershipDomainError")
    except MembershipDomainError:
        pass


def test_malformed_user_id_is_rejected() -> None:
    try:
        Membership.create(workspace_id=new_id(), user_id="not-a-uuid")
        raise AssertionError("expected MembershipDomainError")
    except MembershipDomainError:
        pass


def test_invalid_role_is_rejected() -> None:
    workspace_id, user_id = _ids()
    try:
        Membership(id=new_id(), workspace_id=workspace_id, user_id=user_id, role="not-a-real-role")  # type: ignore[arg-type]
        raise AssertionError("expected MembershipDomainError")
    except MembershipDomainError:
        pass


def test_change_role_to_something_invalid_is_rejected() -> None:
    workspace_id, user_id = _ids()
    membership = Membership.create(workspace_id=workspace_id, user_id=user_id)
    try:
        membership.change_role("not-a-real-role")  # type: ignore[arg-type]
        raise AssertionError("expected MembershipDomainError")
    except MembershipDomainError:
        pass


def test_change_role_returns_a_new_instance_with_the_same_id() -> None:
    workspace_id, user_id = _ids()
    membership = Membership.create(workspace_id=workspace_id, user_id=user_id, role=Role.MEMBER)
    promoted = membership.change_role(Role.ADMIN)
    assert promoted is not membership
    assert promoted.id == membership.id
    assert promoted.role is Role.ADMIN
    assert membership.role is Role.MEMBER  # original untouched


def test_belongs_to_and_is_held_by_distinguish_wrong_workspace_or_user() -> None:
    workspace_id, user_id = _ids()
    other_workspace_id, other_user_id = _ids()
    membership = Membership.create(workspace_id=workspace_id, user_id=user_id)

    assert membership.belongs_to(other_workspace_id) is False
    assert membership.is_held_by(other_user_id) is False


if __name__ == "__main__":
    test_functions = [
        test_create_defaults_to_the_member_role,
        test_create_with_an_explicit_role,
        test_malformed_workspace_id_is_rejected,
        test_malformed_user_id_is_rejected,
        test_invalid_role_is_rejected,
        test_change_role_to_something_invalid_is_rejected,
        test_change_role_returns_a_new_instance_with_the_same_id,
        test_belongs_to_and_is_held_by_distinguish_wrong_workspace_or_user,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
