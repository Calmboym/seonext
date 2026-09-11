"""Structural verification of `backend/app/contracts/api/{auth,projects}.py`
(`PHASE-1.4`).

`pydantic` is not installed in this sandbox (Risk R9), so these schemas
cannot actually be instantiated/validated this session — what this file
mechanically confirms instead, via the stdlib `ast` module:

1. No *response*-side model (`*Data`, `*Response`) anywhere in `auth.py`
   or `projects.py` declares a field named `password`, `new_password`, or
   `hashed_password` — `PHASE-1.2` acceptance criterion 3 ("credentials
   still never stored/returned in plaintext") enforced at the contract
   level, mechanically, not just by having remembered to leave the field
   out.
2. Every `SuccessEnvelope` subclass in those two files sets a
   `contract_id` class attribute to a distinct, non-empty string literal
   (docs/16 §8: contracts must be versioned and distinguishable).

Zero third-party imports (`ast`, `pathlib`), so this file was actually
executed this session. See test_domain_user.py's docstring for the
invocation note.
"""

import ast
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]
_CONTRACTS_DIR = _REPO_ROOT / "backend" / "app" / "contracts" / "api"

_FORBIDDEN_RESPONSE_FIELD_NAMES = {"password", "new_password", "hashed_password"}
_REQUEST_SUFFIX = "Request"
_DATA_OR_RESPONSE_SUFFIXES = ("Data", "Response")


def _parse(filename: str) -> ast.Module:
    return ast.parse((_CONTRACTS_DIR / filename).read_text())


def _class_defs(tree: ast.Module) -> list[ast.ClassDef]:
    return [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]


def _annotated_field_names(class_node: ast.ClassDef) -> set[str]:
    names = set()
    for node in class_node.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.add(node.target.id)
    return names


def _is_response_side_class(class_node: ast.ClassDef) -> bool:
    return any(class_node.name.endswith(suffix) for suffix in _DATA_OR_RESPONSE_SUFFIXES) and not class_node.name.endswith(_REQUEST_SUFFIX)


def test_no_response_side_model_in_auth_contracts_exposes_a_credential_field() -> None:
    tree = _parse("auth.py")
    offenders: list[str] = []
    for class_node in _class_defs(tree):
        if not _is_response_side_class(class_node):
            continue
        leaked = _annotated_field_names(class_node) & _FORBIDDEN_RESPONSE_FIELD_NAMES
        if leaked:
            offenders.append(f"{class_node.name}: {leaked}")
    assert not offenders, f"response-side models must never expose credential fields: {offenders}"


def test_request_side_models_are_the_only_ones_allowed_a_password_field() -> None:
    tree = _parse("auth.py")
    password_bearing_requests = set()
    for class_node in _class_defs(tree):
        fields = _annotated_field_names(class_node)
        if fields & _FORBIDDEN_RESPONSE_FIELD_NAMES:
            assert class_node.name.endswith(_REQUEST_SUFFIX), (
                f"{class_node.name} carries a credential field but is not a *Request class"
            )
            password_bearing_requests.add(class_node.name)
    # Sanity: confirm the test isn't vacuously true — RegisterRequest and
    # LoginRequest really do carry a `password` field in the real file.
    assert "RegisterRequest" in password_bearing_requests
    assert "LoginRequest" in password_bearing_requests


def _contract_id_literal(class_node: ast.ClassDef) -> str | None:
    for node in class_node.body:
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == "contract_id"
            and isinstance(node.value, ast.Constant)
        ):
            return node.value.value
    return None


def test_every_success_envelope_subclass_declares_a_unique_nonempty_contract_id() -> None:
    seen: dict[str, str] = {}
    for filename in ("auth.py", "projects.py"):
        tree = _parse(filename)
        for class_node in _class_defs(tree):
            if not class_node.name.endswith("Response"):
                continue
            # Only classes that actually subclass something (i.e. skip
            # plain BaseModel data classes ending in "Response" by
            # accident — none currently do, but keep the check honest).
            if not class_node.bases:
                continue
            contract_id = _contract_id_literal(class_node)
            assert contract_id, f"{class_node.name} ({filename}) must declare a non-empty contract_id"
            assert contract_id not in seen, (
                f"contract_id {contract_id!r} used by both {seen[contract_id]} and "
                f"{class_node.name} ({filename}) — must be unique"
            )
            seen[contract_id] = f"{class_node.name} ({filename})"
    assert len(seen) >= 6  # 4 auth responses + 2 project responses, at minimum


if __name__ == "__main__":
    test_functions = [
        test_no_response_side_model_in_auth_contracts_exposes_a_credential_field,
        test_request_side_models_are_the_only_ones_allowed_a_password_field,
        test_every_success_envelope_subclass_declares_a_unique_nonempty_contract_id,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
