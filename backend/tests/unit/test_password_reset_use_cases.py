"""Unit tests for `backend/app/application/commands/auth/password_reset.py`.
Same conventions as test_register_user_use_case.py — see that file's
docstring.
"""

import asyncio

from backend.app.application.commands.auth.password_reset import (
    confirm_password_reset,
    request_password_reset,
)
from backend.app.application.errors import InvalidOrExpiredResetTokenError
from backend.app.domain.user.entity import User
from backend.tests.unit._auth_fakes import (
    FakeTokenError,
    FakeUserRepository,
    fake_decode_reset_token,
    fake_hash_password,
    fake_issue_reset_token,
    fake_verify_password,
)


async def _seed_user(users: FakeUserRepository, *, email: str = "ada@example.com", password: str = "old-password") -> User:
    user = User.register(email=email, hashed_password=fake_hash_password(password), display_name="Ada")
    await users.add(user)
    return user


def test_request_password_reset_for_an_existing_active_account_returns_a_token_bound_to_the_user() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)

        token = await request_password_reset(
            email="ADA@EXAMPLE.COM", users=users, issue_reset_token=fake_issue_reset_token
        )

        assert token == f"reset-token:{user.id}"

    asyncio.run(_body())


def test_request_password_reset_for_an_unknown_email_returns_none_without_raising() -> None:
    """This is the account-enumeration-safety property under test — see
    password_reset.py's module docstring."""

    async def _body() -> None:
        users = FakeUserRepository()
        token = await request_password_reset(
            email="nobody@example.com", users=users, issue_reset_token=fake_issue_reset_token
        )
        assert token is None

    asyncio.run(_body())


def test_request_password_reset_for_a_disabled_account_also_returns_none() -> None:
    """Same outward result as "unknown email" — a disabled account must
    not be distinguishable from a nonexistent one via this endpoint
    either."""

    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)
        await users.save(user.deactivate())

        token = await request_password_reset(
            email="ada@example.com", users=users, issue_reset_token=fake_issue_reset_token
        )
        assert token is None

    asyncio.run(_body())


def test_confirm_password_reset_with_a_valid_token_updates_the_password_hash() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)
        token = f"reset-token:{user.id}"

        await confirm_password_reset(
            reset_token=token,
            new_password="brand-new-password",
            decode_reset_token=fake_decode_reset_token,
            users=users,
            user_writer=users,
            hash_password=fake_hash_password,
        )

        updated = await users.get_by_id(user.id)
        assert updated is not None
        assert updated.hashed_password == fake_hash_password("brand-new-password")
        assert fake_verify_password("old-password", updated.hashed_password) is False
        assert fake_verify_password("brand-new-password", updated.hashed_password) is True

    asyncio.run(_body())


def test_confirm_password_reset_with_a_malformed_token_propagates_the_decoders_own_exception() -> None:
    """The use case must not swallow or wrap this — it doesn't even
    import the real TokenError type (see password_reset.py's module
    docstring)."""

    async def _body() -> None:
        users = FakeUserRepository()
        try:
            await confirm_password_reset(
                reset_token="not-a-real-token",
                new_password="brand-new-password",
                decode_reset_token=fake_decode_reset_token,
                users=users,
                user_writer=users,
                hash_password=fake_hash_password,
            )
            raise AssertionError("expected FakeTokenError")
        except FakeTokenError:
            pass

    asyncio.run(_body())


def test_confirm_password_reset_for_a_token_whose_user_no_longer_exists_raises() -> None:
    async def _body() -> None:
        users = FakeUserRepository()  # deliberately empty — token references a user that isn't there
        token = "reset-token:00000000-0000-0000-0000-000000000000"
        try:
            await confirm_password_reset(
                reset_token=token,
                new_password="brand-new-password",
                decode_reset_token=fake_decode_reset_token,
                users=users,
                user_writer=users,
                hash_password=fake_hash_password,
            )
            raise AssertionError("expected InvalidOrExpiredResetTokenError")
        except InvalidOrExpiredResetTokenError:
            pass

    asyncio.run(_body())


def test_confirm_password_reset_for_a_now_disabled_account_raises() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)
        token = f"reset-token:{user.id}"
        await users.save(user.deactivate())  # disabled after the token was issued

        try:
            await confirm_password_reset(
                reset_token=token,
                new_password="brand-new-password",
                decode_reset_token=fake_decode_reset_token,
                users=users,
                user_writer=users,
                hash_password=fake_hash_password,
            )
            raise AssertionError("expected InvalidOrExpiredResetTokenError")
        except InvalidOrExpiredResetTokenError:
            pass

    asyncio.run(_body())


if __name__ == "__main__":
    test_functions = [
        test_request_password_reset_for_an_existing_active_account_returns_a_token_bound_to_the_user,
        test_request_password_reset_for_an_unknown_email_returns_none_without_raising,
        test_request_password_reset_for_a_disabled_account_also_returns_none,
        test_confirm_password_reset_with_a_valid_token_updates_the_password_hash,
        test_confirm_password_reset_with_a_malformed_token_propagates_the_decoders_own_exception,
        test_confirm_password_reset_for_a_token_whose_user_no_longer_exists_raises,
        test_confirm_password_reset_for_a_now_disabled_account_raises,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
