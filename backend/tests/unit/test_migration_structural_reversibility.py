"""Structural (not execution) verification that the `PHASE-1.1` migration
is reversible: every `op.create_table`/`op.create_index` in `upgrade()`
has a matching `op.drop_table`/`op.drop_index` in `downgrade()`, in exact
reverse order.

No live database is reachable in this sandbox (Risk R9, .ai/
PROJECT_STATE.md §9), so `alembic upgrade head` / `alembic downgrade -1`
cannot actually be run against Postgres this session — this is a real,
mechanical substitute check, not a replacement for that: it proves the
migration file's `upgrade`/`downgrade` functions are structurally
symmetric (same tables, exact reverse order), which is a necessary but
not sufficient condition for "applies and reverts cleanly against a real
database". See the migration file's own docstring for what remains
`IMPLEMENTED / UNVERIFIED`.

Zero third-party imports (`ast`, `pathlib` — stdlib only), so this file
was actually executed this session. See test_domain_user.py's docstring
for the invocation note.
"""

import ast
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_MIGRATION_PATH = (
    _REPO_ROOT
    / "infrastructure"
    / "database"
    / "migrations"
    / "versions"
    / "91ae40b03721_phase1_core_domain_tables.py"
)


def _find_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(f"function {name!r} not found in {_MIGRATION_PATH}")


def _op_calls(func: ast.FunctionDef, op_attr: str) -> list[str]:
    """Returns, in source order, the first string-literal argument of
    every `op.<op_attr>(...)` call in `func` — e.g. for `op_attr=
    "create_table"`, the table name of every `op.create_table("name", ...)`
    call. Handles both positional-first-arg and `table_name=`/first literal
    forms used by `op.drop_table`/`op.drop_index`."""

    names: list[str] = []
    for node in ast.walk(func):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == op_attr
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "op"
        ):
            literal = None
            if node.args and isinstance(node.args[0], ast.Constant):
                literal = node.args[0].value
            else:
                for kw in node.keywords:
                    if kw.arg == "table_name" and isinstance(kw.value, ast.Constant):
                        literal = kw.value.value
            if literal is not None:
                names.append(literal)
    return names


def test_every_created_table_has_a_matching_dropped_table() -> None:
    tree = ast.parse(_MIGRATION_PATH.read_text())
    upgrade_fn = _find_function(tree, "upgrade")
    downgrade_fn = _find_function(tree, "downgrade")

    created = _op_calls(upgrade_fn, "create_table")
    dropped = _op_calls(downgrade_fn, "drop_table")

    assert created, "expected at least one op.create_table in upgrade()"
    assert set(created) == set(dropped), (
        f"tables created {created!r} do not match tables dropped {dropped!r}"
    )


def test_downgrade_drops_tables_in_exact_reverse_order() -> None:
    tree = ast.parse(_MIGRATION_PATH.read_text())
    upgrade_fn = _find_function(tree, "upgrade")
    downgrade_fn = _find_function(tree, "downgrade")

    created_order = _op_calls(upgrade_fn, "create_table")
    dropped_order = _op_calls(downgrade_fn, "drop_table")

    assert dropped_order == list(reversed(created_order)), (
        "downgrade() must drop tables in exact reverse creation order to "
        "respect foreign-key dependency direction both ways "
        f"(created: {created_order!r}, dropped: {dropped_order!r})"
    )


def test_every_created_index_has_a_matching_dropped_index() -> None:
    tree = ast.parse(_MIGRATION_PATH.read_text())
    upgrade_fn = _find_function(tree, "upgrade")
    downgrade_fn = _find_function(tree, "downgrade")

    created = _op_calls(upgrade_fn, "create_index")
    dropped = _op_calls(downgrade_fn, "drop_index")

    assert created, "expected at least one op.create_index in upgrade()"
    assert set(created) == set(dropped), (
        f"indexes created {created!r} do not match indexes dropped {dropped!r}"
    )


def test_users_table_created_first_and_dropped_last() -> None:
    """`users` has no foreign keys pointing out of it (only into it), so
    it must be the first table created and the last one dropped — the
    opposite mistake would violate FK constraints on a real database."""

    tree = ast.parse(_MIGRATION_PATH.read_text())
    upgrade_fn = _find_function(tree, "upgrade")
    downgrade_fn = _find_function(tree, "downgrade")

    created_order = _op_calls(upgrade_fn, "create_table")
    dropped_order = _op_calls(downgrade_fn, "drop_table")

    assert created_order[0] == "users"
    assert dropped_order[-1] == "users"


if __name__ == "__main__":
    test_functions = [
        test_every_created_table_has_a_matching_dropped_table,
        test_downgrade_drops_tables_in_exact_reverse_order,
        test_every_created_index_has_a_matching_dropped_index,
        test_users_table_created_first_and_dropped_last,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
