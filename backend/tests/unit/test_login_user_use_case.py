"""Unit tests for `backend/app/application/commands/auth/login.py`. Same
conventions as test_register_user_use_case.py — see that file's
docstring.
"""

import asyncio

from backend.app.application.commands.auth.login import login_user
from backend.app.application.errors import AccountDisabledError, InvalidCredentialsError
from backend.app.domain.user.entity import User
from backend.tests.unit._auth_fakes import (
    FakeUserRepository,
    fake_hash_password,
    fake_issue_access_token,
    fake_verify_password,
)

_EXPIRE_MINUTES = 30


async def _seed_user(users: FakeUserRepository, *, email: str = "ada@example.com", password: str = "correct-password") -> User:
    user = User.register(email=email, hashed_password=fake_hash_password(password), display_name="Ada")
    await users.add(user)
    return user


def test_login_with_correct_credentials_issues_a_token_bound_to_the_real_user_id() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)

        result = await login_user(
            email="ADA@EXAMPLE.COM",
            password="correct-password",
            users=users,
            user_writer=users,
            verify_password=fake_verify_password,
            issue_access_token=fake_issue_access_token,
            access_token_expire_minutes=_EXPIRE_MINUTES,
        )

        assert result.access_token == f"access-token:{user.id}"  # bound to the REAL user.id
        assert result.expires_in_minutes == _EXPIRE_MINUTES

    asyncio.run(_body())


def test_successful_login_records_last_login_at_via_the_domain_entity() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)
        assert user.last_login_at is None

        await login_user(
            email=user.email,
            password="correct-password",
            users=users,
            user_writer=users,
            verify_password=fake_verify_password,
            issue_access_token=fake_issue_access_token,
            access_token_expire_minutes=_EXPIRE_MINUTES,
        )

        updated = await users.get_by_id(user.id)
        assert updated is not None
        assert updated.last_login_at is not None

    asyncio.run(_body())


def test_login_with_unknown_email_raises_invalid_credentials() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        try:
            await login_user(
                email="nobody@example.com",
                password="whatever",
                users=users,
                user_writer=users,
                verify_password=fake_verify_password,
                issue_access_token=fake_issue_access_token,
                access_token_expire_minutes=_EXPIRE_MINUTES,
            )
            raise AssertionError("expected InvalidCredentialsError")
        except InvalidCredentialsError:
            pass

    asyncio.run(_body())


def test_login_with_wrong_password_raises_the_same_error_as_unknown_email() -> None:
    """The indistinguishability itself is the security property under
    test — see backend/app/application/errors.py's
    InvalidCredentialsError docstring."""

    async def _body() -> None:
        users = FakeUserRepository()
        await _seed_user(users)
        try:
            await login_user(
                email="ada@example.com",
                password="totally-wrong-password",
                users=users,
                user_writer=users,
                verify_password=fake_verify_password,
                issue_access_token=fake_issue_access_token,
                access_token_expire_minutes=_EXPIRE_MINUTES,
            )
            raise AssertionError("expected InvalidCredentialsError")
        except InvalidCredentialsError:
            pass

    asyncio.run(_body())


def test_login_for_a_disabled_account_raises_account_disabled_not_invalid_credentials() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await _seed_user(users)
        await users.save(user.deactivate())

        try:
            await login_user(
                email="ada@example.com",
                password="correct-password",
                users=users,
                user_writer=users,
                verify_password=fake_verify_password,
                issue_access_token=fake_issue_access_token,
                access_token_expire_minutes=_EXPIRE_MINUTES,
            )
            raise AssertionError("expected AccountDisabledError")
        except AccountDisabledError:
            pass

    asyncio.run(_body())


if __name__ == "__main__":
    test_functions = [
        test_login_with_correct_credentials_issues_a_token_bound_to_the_real_user_id,
        test_successful_login_records_last_login_at_via_the_domain_entity,
        test_login_with_unknown_email_raises_invalid_credentials,
        test_login_with_wrong_password_raises_the_same_error_as_unknown_email,
        test_login_for_a_disabled_account_raises_account_disabled_not_invalid_credentials,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
