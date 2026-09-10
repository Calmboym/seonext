"""Unit tests for the `Workspace` domain entity
(backend/app/domain/workspace/entity.py).

Backend-unit category. Zero third-party imports — see
test_domain_user.py's docstring for the invocation note (`python3 -m
backend.tests.unit.test_domain_workspace` from repo root, or
`PYTHONPATH=.`), which applies identically here.
"""

from backend.app.domain.workspace.entity import Workspace, WorkspaceDomainError, WorkspaceStatus
from backend.app.domain.common.ids import new_id


def _owner_id() -> str:
    return new_id()


def test_create_produces_a_valid_active_workspace() -> None:
    owner = _owner_id()
    workspace = Workspace.create(name="Acme SEO", owner_user_id=owner)
    assert workspace.status is WorkspaceStatus.ACTIVE
    assert workspace.is_active is True
    assert workspace.owner_user_id == owner
    assert workspace.is_owned_by(owner) is True
    assert workspace.is_owned_by(_owner_id()) is False


def test_empty_name_is_rejected() -> None:
    try:
        Workspace.create(name="   ", owner_user_id=_owner_id())
        raise AssertionError("expected WorkspaceDomainError")
    except WorkspaceDomainError:
        pass


def test_malformed_owner_id_is_rejected() -> None:
    try:
        Workspace.create(name="Acme SEO", owner_user_id="not-a-uuid")
        raise AssertionError("expected WorkspaceDomainError")
    except WorkspaceDomainError:
        pass


def test_rename_returns_a_new_instance_with_the_same_id() -> None:
    workspace = Workspace.create(name="Acme SEO", owner_user_id=_owner_id())
    renamed = workspace.rename("Acme SEO — EU")
    assert renamed is not workspace
    assert renamed.id == workspace.id
    assert renamed.name == "Acme SEO — EU"
    assert workspace.name == "Acme SEO"  # original untouched


def test_archive_then_reactivate_round_trips_status() -> None:
    workspace = Workspace.create(name="Acme SEO", owner_user_id=_owner_id())
    archived = workspace.archive()
    assert archived.status is WorkspaceStatus.ARCHIVED
    assert archived.is_active is False
    reactivated = archived.reactivate()
    assert reactivated.status is WorkspaceStatus.ACTIVE


def test_archiving_an_already_archived_workspace_raises() -> None:
    archived = Workspace.create(name="Acme SEO", owner_user_id=_owner_id()).archive()
    try:
        archived.archive()
        raise AssertionError("expected WorkspaceDomainError")
    except WorkspaceDomainError:
        pass


def test_reactivating_an_already_active_workspace_raises() -> None:
    workspace = Workspace.create(name="Acme SEO", owner_user_id=_owner_id())
    try:
        workspace.reactivate()
        raise AssertionError("expected WorkspaceDomainError")
    except WorkspaceDomainError:
        pass


if __name__ == "__main__":
    test_functions = [
        test_create_produces_a_valid_active_workspace,
        test_empty_name_is_rejected,
        test_malformed_owner_id_is_rejected,
        test_rename_returns_a_new_instance_with_the_same_id,
        test_archive_then_reactivate_round_trips_status,
        test_archiving_an_already_archived_workspace_raises,
        test_reactivating_an_already_active_workspace_raises,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
