"""Structural (not execution) verification that every Alembic migration
in this repository is reversible: every `op.create_table`/
`op.create_index` in `upgrade()` has a matching `op.drop_table`/
`op.drop_index` in `downgrade()`, in exact reverse order.

Originally written for `PHASE-1.1`'s migration only (session 9);
generalized the same session, once `PHASE-1.3` added a second real
migration, to check every migration file under `versions/` rather than
hardcoding one path — so a future migration gets this check for free
without a new near-duplicate test file.

No live database is reachable in this sandbox (Risk R9, .ai/
PROJECT_STATE.md §9), so `alembic upgrade head` / `alembic downgrade -1`
cannot actually be run against Postgres this session — this is a real,
mechanical substitute check, not a replacement for that: it proves each
migration file's `upgrade`/`downgrade` functions are structurally
symmetric (same tables, exact reverse order), which is a necessary but
not sufficient condition for "applies and reverts cleanly against a real
database". See each migration file's own docstring for what remains
`IMPLEMENTED / UNVERIFIED`.

Zero third-party imports (`ast`, `pathlib` — stdlib only), so this file
was actually executed this session. See test_domain_user.py's docstring
for the invocation note.
"""

import ast
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_VERSIONS_DIR = _REPO_ROOT / "infrastructure" / "database" / "migrations" / "versions"


def _migration_files() -> list[Path]:
    files = sorted(_VERSIONS_DIR.glob("*.py"))
    assert files, f"expected at least one migration file in {_VERSIONS_DIR}"
    return files


def _find_function(tree: ast.Module, name: str, *, source: Path) -> ast.FunctionDef:
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(f"function {name!r} not found in {source}")


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


def test_every_migration_s_created_tables_match_its_dropped_tables() -> None:
    checked = 0
    for path in _migration_files():
        tree = ast.parse(path.read_text())
        upgrade_fn = _find_function(tree, "upgrade", source=path)
        downgrade_fn = _find_function(tree, "downgrade", source=path)

        created = _op_calls(upgrade_fn, "create_table")
        if not created:
            continue  # e.g. 7ce776d78700, the framework-only PHASE-0.3 migration
        dropped = _op_calls(downgrade_fn, "drop_table")
        assert set(created) == set(dropped), (
            f"{path.name}: tables created {created!r} do not match tables dropped {dropped!r}"
        )
        checked += 1
    assert checked >= 2  # PHASE-1.1's and PHASE-1.3's migrations, at minimum


def test_every_migration_drops_tables_in_exact_reverse_creation_order() -> None:
    checked = 0
    for path in _migration_files():
        tree = ast.parse(path.read_text())
        upgrade_fn = _find_function(tree, "upgrade", source=path)
        downgrade_fn = _find_function(tree, "downgrade", source=path)

        created_order = _op_calls(upgrade_fn, "create_table")
        if not created_order:
            continue
        dropped_order = _op_calls(downgrade_fn, "drop_table")
        assert dropped_order == list(reversed(created_order)), (
            f"{path.name}: downgrade() must drop tables in exact reverse creation "
            f"order to respect foreign-key dependency direction both ways "
            f"(created: {created_order!r}, dropped: {dropped_order!r})"
        )
        checked += 1
    assert checked >= 2


def test_every_migration_s_created_indexes_match_its_dropped_indexes() -> None:
    checked = 0
    for path in _migration_files():
        tree = ast.parse(path.read_text())
        upgrade_fn = _find_function(tree, "upgrade", source=path)
        downgrade_fn = _find_function(tree, "downgrade", source=path)

        created = _op_calls(upgrade_fn, "create_index")
        if not created:
            continue
        dropped = _op_calls(downgrade_fn, "drop_index")
        assert set(created) == set(dropped), (
            f"{path.name}: indexes created {created!r} do not match indexes dropped {dropped!r}"
        )
        checked += 1
    assert checked >= 2


def test_users_table_created_first_and_dropped_last_in_its_own_migration() -> None:
    """`users` has no foreign keys pointing out of it (only into it), so
    in whichever migration creates it, it must be the first table created
    and the last one dropped — the opposite mistake would violate FK
    constraints on a real database. Scoped to the one migration that
    actually creates `users` (PHASE-1.1's), not all of them."""

    found = False
    for path in _migration_files():
        tree = ast.parse(path.read_text())
        upgrade_fn = _find_function(tree, "upgrade", source=path)
        created_order = _op_calls(upgrade_fn, "create_table")
        if "users" not in created_order:
            continue
        found = True
        downgrade_fn = _find_function(tree, "downgrade", source=path)
        dropped_order = _op_calls(downgrade_fn, "drop_table")
        assert created_order[0] == "users", f"{path.name}: users must be created first"
        assert dropped_order[-1] == "users", f"{path.name}: users must be dropped last"
    assert found, "no migration in versions/ creates a 'users' table"


def test_memberships_table_is_dropped_before_the_workspaces_and_users_tables_it_references() -> None:
    """`PHASE-1.3`-specific: `memberships` has foreign keys into both
    `workspaces` and `users`, so whichever migration creates it, it must
    also be the first thing that migration drops (or, in this project's
    case, the only thing that migration creates at all)."""

    for path in _migration_files():
        tree = ast.parse(path.read_text())
        upgrade_fn = _find_function(tree, "upgrade", source=path)
        created_order = _op_calls(upgrade_fn, "create_table")
        if "memberships" not in created_order:
            continue
        downgrade_fn = _find_function(tree, "downgrade", source=path)
        dropped_order = _op_calls(downgrade_fn, "drop_table")
        assert dropped_order[0] == "memberships", f"{path.name}: memberships must be dropped first"


if __name__ == "__main__":
    test_functions = [
        test_every_migration_s_created_tables_match_its_dropped_tables,
        test_every_migration_drops_tables_in_exact_reverse_creation_order,
        test_every_migration_s_created_indexes_match_its_dropped_indexes,
        test_users_table_created_first_and_dropped_last_in_its_own_migration,
        test_memberships_table_is_dropped_before_the_workspaces_and_users_tables_it_references,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
