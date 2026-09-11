"""Unit tests for the `User` domain entity (backend/app/domain/user/entity.py).

Backend-unit category (.ai/WBS.md §4, PHASE-0.8's category taxonomy).

Zero third-party imports (`backend.app.domain.user.entity` imports only
`dataclasses`, `datetime`, `enum`, and its own package — all stdlib), so
this file was actually executed this session, not just syntax-checked.
See the `if __name__ == "__main__"` block and .ai/PROJECT_STATE.md §14 for
this session's run record.

Correction to a claim in backend/tests/unit/test_error_hierarchy.py's own
docstring (session 7): running `python3 <path-to-this-file>` directly does
*not* put the repository root on `sys.path`, so a bare `from backend.app...`
import fails with `ModuleNotFoundError`. The invocation that actually
works (and is what this session used, verified directly rather than
assumed) is either:

    python3 -m backend.tests.unit.test_domain_user      # from repo root
    PYTHONPATH=. python3 backend/tests/unit/test_domain_user.py

Written in ordinary pytest style (bare `assert`, no fixtures) so it stays
real-pytest-compatible while also being directly runnable, same as
`test_error_hierarchy.py`.
"""

from datetime import datetime, timedelta, timezone

from backend.app.domain.user.entity import User, UserDomainError, UserStatus


def _new_user(**overrides: object) -> User:
    defaults: dict[str, object] = {
        "email": "person@example.com",
        "hashed_password": "not-a-real-hash",
        "display_name": "Ada Lovelace",
    }
    defaults.update(overrides)
    return User.register(**defaults)  # type: ignore[arg-type]


def test_register_produces_a_valid_active_user_with_a_stable_id() -> None:
    user = _new_user()
    assert user.status is UserStatus.ACTIVE
    assert user.is_active is True
    assert user.last_login_at is None
    assert len(user.id) == 36  # canonical UUID string form
    assert user.created_at == user.updated_at


def test_two_registrations_never_collide_on_id() -> None:
    first = _new_user()
    second = _new_user()
    assert first.id != second.id


def test_email_is_normalized_to_lowercase_and_stripped() -> None:
    user = _new_user(email="  Person@Example.COM  ")
    assert user.email == "person@example.com"


def test_email_without_an_at_sign_is_rejected() -> None:
    try:
        _new_user(email="not-an-email")
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


def test_empty_display_name_is_rejected() -> None:
    try:
        _new_user(display_name="   ")
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


def test_empty_hashed_password_is_rejected() -> None:
    try:
        _new_user(hashed_password="")
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


def test_record_login_returns_a_new_instance_and_advances_timestamps() -> None:
    user = _new_user()
    at = datetime.now(timezone.utc) + timedelta(minutes=5)
    logged_in = user.record_login(at=at)
    assert logged_in is not user  # frozen dataclass: never mutated in place
    assert user.last_login_at is None  # original untouched
    assert logged_in.last_login_at == at
    assert logged_in.updated_at == at


def test_disabled_user_cannot_record_a_login() -> None:
    user = _new_user().deactivate()
    try:
        user.record_login()
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


def test_deactivate_then_reactivate_round_trips_status() -> None:
    user = _new_user()
    disabled = user.deactivate()
    assert disabled.status is UserStatus.DISABLED
    assert disabled.is_active is False
    reactivated = disabled.reactivate()
    assert reactivated.status is UserStatus.ACTIVE


def test_deactivating_an_already_disabled_user_raises() -> None:
    disabled = _new_user().deactivate()
    try:
        disabled.deactivate()
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


def test_rename_updates_display_name_and_leaves_everything_else() -> None:
    user = _new_user()
    renamed = user.rename("Grace Hopper")
    assert renamed.display_name == "Grace Hopper"
    assert renamed.id == user.id
    assert renamed.email == user.email


def test_change_password_hash_updates_only_the_hash() -> None:
    user = _new_user()
    updated = user.change_password_hash("a-different-hash")
    assert updated.hashed_password == "a-different-hash"
    assert updated.email == user.email


def test_constructing_a_user_directly_with_a_malformed_id_is_rejected() -> None:
    # Guards repository hydration paths, not just `.register()`.
    try:
        User(id="not-a-uuid", email="a@b.com", hashed_password="x", display_name="X")
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


def test_constructing_a_user_directly_with_an_invalid_status_is_rejected() -> None:
    try:
        User(
            id="11111111-1111-1111-1111-111111111111",
            email="a@b.com",
            hashed_password="x",
            display_name="X",
            status="not-a-real-status",  # type: ignore[arg-type]
        )
        raise AssertionError("expected UserDomainError")
    except UserDomainError:
        pass


if __name__ == "__main__":
    test_functions = [
        test_register_produces_a_valid_active_user_with_a_stable_id,
        test_two_registrations_never_collide_on_id,
        test_email_is_normalized_to_lowercase_and_stripped,
        test_email_without_an_at_sign_is_rejected,
        test_empty_display_name_is_rejected,
        test_empty_hashed_password_is_rejected,
        test_record_login_returns_a_new_instance_and_advances_timestamps,
        test_disabled_user_cannot_record_a_login,
        test_deactivate_then_reactivate_round_trips_status,
        test_deactivating_an_already_disabled_user_raises,
        test_rename_updates_display_name_and_leaves_everything_else,
        test_change_password_hash_updates_only_the_hash,
        test_constructing_a_user_directly_with_a_malformed_id_is_rejected,
        test_constructing_a_user_directly_with_an_invalid_status_is_rejected,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
