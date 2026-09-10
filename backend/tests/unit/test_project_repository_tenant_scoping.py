"""Structural verification that `ProjectRepository` enforces tenant
scoping by construction (`PHASE-1.1` acceptance criterion 4,
.ai/WBS.md §4B).

Not an execution test in the usual sense — `sqlalchemy` is not installed
in this sandbox (Risk R9), so `ProjectRepository.get()` cannot actually be
called against a real (or fake) session. What this file *can* do, and
does, is parse `project_repository.py`'s own source with the stdlib `ast`
module and mechanically check that every method claiming to be
project-scoped:

1. takes `workspace_id` as a required (no-default) parameter, and
2. references both `ProjectModel.workspace_id` and `ProjectModel.id` (or
   `.workspace_id`/`.id`) somewhere in its body,

so that a future edit which quietly drops the `workspace_id` filter (the
exact regression acceptance criterion 4 exists to prevent) fails this
check even without a database to catch it at query time. This file has
zero third-party imports (`ast`, `pathlib` — stdlib only), so — like
`test_domain_user.py` and friends — it was actually executed this
session, not just eyeballed. See test_domain_user.py's docstring for the
`python3 -m backend.tests.unit.test_project_repository_tenant_scoping`
invocation note.

This complements, and does not replace, a real integration test against
a live Postgres database with two workspaces and a project-ID guessing
attempt — that test is written in
backend/tests/api/test_project_isolation.py (IMPLEMENTED / UNVERIFIED,
same as every other test in this project that needs a real database or
`fastapi`/`httpx` installed) and should be run for real the first time
this project has package-install and Postgres access (Risk R9).
"""

import ast
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_SOURCE_PATH = _REPO_ROOT / "backend" / "app" / "infrastructure" / "repositories" / "project_repository.py"


def _load_class(class_name: str) -> ast.ClassDef:
    tree = ast.parse(_SOURCE_PATH.read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return node
    raise AssertionError(f"class {class_name!r} not found in {_SOURCE_PATH}")


def _find_method(class_node: ast.ClassDef, method_name: str) -> ast.AsyncFunctionDef:
    for node in class_node.body:
        if isinstance(node, ast.AsyncFunctionDef) and node.name == method_name:
            return node
    raise AssertionError(f"async method {method_name!r} not found on {class_node.name}")


def _required_arg_names(func: ast.AsyncFunctionDef) -> set[str]:
    """Names of every positional-or-keyword / keyword-only argument that
    has no default value (i.e. the caller *must* supply it). Excludes
    `self`."""

    args = func.args
    required: set[str] = set()

    positional = args.posonlyargs + args.args
    num_without_default = len(positional) - len(args.defaults)
    for arg in positional[:num_without_default]:
        if arg.arg != "self":
            required.add(arg.arg)

    for arg, default in zip(args.kwonlyargs, args.kw_defaults):
        if default is None:
            required.add(arg.arg)

    return required


def _references_attribute(func: ast.AsyncFunctionDef, owner: str, attribute: str) -> bool:
    """True if `func`'s body contains an `owner.attribute` access
    anywhere (e.g. `ProjectModel.workspace_id`)."""

    for node in ast.walk(func):
        if (
            isinstance(node, ast.Attribute)
            and node.attr == attribute
            and isinstance(node.value, ast.Name)
            and node.value.id == owner
        ):
            return True
    return False


def test_project_repository_class_exists_with_expected_methods() -> None:
    class_node = _load_class("ProjectRepository")
    method_names = {
        node.name for node in class_node.body if isinstance(node, ast.AsyncFunctionDef)
    }
    assert {"get", "list_for_workspace", "add", "save"} <= method_names


def test_get_requires_both_workspace_id_and_project_id() -> None:
    class_node = _load_class("ProjectRepository")
    get_method = _find_method(class_node, "get")
    required = _required_arg_names(get_method)
    assert "workspace_id" in required, "get() must require workspace_id — it must not be optional"
    assert "project_id" in required, "get() must require project_id"


def test_get_filters_on_both_workspace_id_and_id_in_its_query() -> None:
    class_node = _load_class("ProjectRepository")
    get_method = _find_method(class_node, "get")
    assert _references_attribute(get_method, "ProjectModel", "workspace_id"), (
        "get() must filter on ProjectModel.workspace_id — a query that only "
        "filters on the project id could return a project from any workspace"
    )
    assert _references_attribute(get_method, "ProjectModel", "id")


def test_list_for_workspace_requires_workspace_id() -> None:
    class_node = _load_class("ProjectRepository")
    method = _find_method(class_node, "list_for_workspace")
    assert "workspace_id" in _required_arg_names(method)


def test_no_unscoped_get_by_id_shortcut_exists_on_project_repository() -> None:
    """Guards against a future edit re-introducing a `get_by_id(project_id)`
    convenience method (like `UserRepository`/`WorkspaceRepository` have)
    that would bypass workspace scoping entirely for Project lookups."""

    class_node = _load_class("ProjectRepository")
    method_names = {
        node.name for node in class_node.body if isinstance(node, ast.AsyncFunctionDef)
    }
    assert "get_by_id" not in method_names


def test_save_checks_workspace_id_before_persisting() -> None:
    class_node = _load_class("ProjectRepository")
    save_method = _find_method(class_node, "save")
    assert _references_attribute(save_method, "row", "workspace_id") or _references_attribute(
        save_method, "project", "workspace_id"
    ), "save() must verify workspace_id before persisting an update"


if __name__ == "__main__":
    test_functions = [
        test_project_repository_class_exists_with_expected_methods,
        test_get_requires_both_workspace_id_and_project_id,
        test_get_filters_on_both_workspace_id_and_id_in_its_query,
        test_list_for_workspace_requires_workspace_id,
        test_no_unscoped_get_by_id_shortcut_exists_on_project_repository,
        test_save_checks_workspace_id_before_persisting,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
