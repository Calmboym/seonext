"""Unit tests for the `Project` domain entity
(backend/app/domain/project/entity.py).

Backend-unit category. Zero third-party imports — see
test_domain_user.py's docstring for the invocation note, which applies
identically here.
"""

from backend.app.domain.common.ids import new_id
from backend.app.domain.project.entity import Project, ProjectDomainError, ProjectStatus


def _workspace_id() -> str:
    return new_id()


def test_create_produces_a_valid_active_project_with_empty_business_fields_by_default() -> None:
    ws = _workspace_id()
    project = Project.create(workspace_id=ws, name="Acme.com SEO")
    assert project.status is ProjectStatus.ACTIVE
    assert project.workspace_id == ws
    assert project.belongs_to(ws) is True
    assert project.belongs_to(_workspace_id()) is False
    assert project.markets == ()
    assert project.industry is None


def test_empty_name_is_rejected() -> None:
    try:
        Project.create(workspace_id=_workspace_id(), name="")
        raise AssertionError("expected ProjectDomainError")
    except ProjectDomainError:
        pass


def test_malformed_workspace_id_is_rejected() -> None:
    try:
        Project.create(workspace_id="not-a-uuid", name="Acme.com SEO")
        raise AssertionError("expected ProjectDomainError")
    except ProjectDomainError:
        pass


def test_list_business_attributes_are_deduplicated_and_order_preserved() -> None:
    project = Project.create(
        workspace_id=_workspace_id(),
        name="Acme.com SEO",
        markets=["US", "UK", "US", "  ", "DE"],
    )
    assert project.markets == ("US", "UK", "DE")


def test_belongs_to_is_the_tenant_check_repositories_and_authorization_both_rely_on() -> None:
    ws_a, ws_b = _workspace_id(), _workspace_id()
    project = Project.create(workspace_id=ws_a, name="Acme.com SEO")
    assert project.belongs_to(ws_a) is True
    assert project.belongs_to(ws_b) is False


def test_update_business_profile_only_changes_the_fields_passed() -> None:
    project = Project.create(
        workspace_id=_workspace_id(),
        name="Acme.com SEO",
        industry="Retail",
        markets=["US"],
    )
    updated = project.update_business_profile(industry="E-commerce")
    assert updated.industry == "E-commerce"
    assert updated.markets == ("US",)  # untouched field preserved
    assert updated is not project
    assert project.industry == "Retail"  # original untouched


def test_update_business_profile_can_explicitly_clear_a_list_field() -> None:
    project = Project.create(workspace_id=_workspace_id(), name="Acme.com SEO", markets=["US"])
    cleared = project.update_business_profile(markets=[])
    assert cleared.markets == ()


def test_rename_preserves_id_and_workspace() -> None:
    ws = _workspace_id()
    project = Project.create(workspace_id=ws, name="Acme.com SEO")
    renamed = project.rename("Acme.com — Global SEO")
    assert renamed.id == project.id
    assert renamed.workspace_id == ws
    assert renamed.name == "Acme.com — Global SEO"


def test_archive_then_reactivate_round_trips_status() -> None:
    project = Project.create(workspace_id=_workspace_id(), name="Acme.com SEO")
    archived = project.archive()
    assert archived.status is ProjectStatus.ARCHIVED
    reactivated = archived.reactivate()
    assert reactivated.status is ProjectStatus.ACTIVE


def test_archiving_an_already_archived_project_raises() -> None:
    archived = Project.create(workspace_id=_workspace_id(), name="Acme.com SEO").archive()
    try:
        archived.archive()
        raise AssertionError("expected ProjectDomainError")
    except ProjectDomainError:
        pass


if __name__ == "__main__":
    test_functions = [
        test_create_produces_a_valid_active_project_with_empty_business_fields_by_default,
        test_empty_name_is_rejected,
        test_malformed_workspace_id_is_rejected,
        test_list_business_attributes_are_deduplicated_and_order_preserved,
        test_belongs_to_is_the_tenant_check_repositories_and_authorization_both_rely_on,
        test_update_business_profile_only_changes_the_fields_passed,
        test_update_business_profile_can_explicitly_clear_a_list_field,
        test_rename_preserves_id_and_workspace,
        test_archive_then_reactivate_round_trips_status,
        test_archiving_an_already_archived_project_raises,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
