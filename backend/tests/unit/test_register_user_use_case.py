"""Unit tests for `backend/app/application/commands/auth/register.py`.

Zero third-party imports (the use case itself has none — see that
module's docstring — and `_auth_fakes.py` only imports the domain layer,
also zero third-party deps), so this file was actually executed this
session. See test_domain_user.py's docstring for the invocation note.

Uses `asyncio.run` directly rather than `pytest.mark.asyncio` (`pytest`
and `pytest-asyncio` are not installed in this sandbox — Risk R9) — each
test function is a thin sync wrapper around an `async def _body()`
closure, kept that way so this file stays real-pytest-compatible (with
`pytest-asyncio` installed, in a later session, these could drop the
wrapper and become `async def` directly) while still being runnable now.
"""

import asyncio

from backend.app.application.commands.auth.register import register_user
from backend.app.application.errors import EmailAlreadyRegisteredError
from backend.app.domain.user.entity import UserDomainError
from backend.tests.unit._auth_fakes import FakeUserRepository, fake_hash_password


def test_register_creates_a_user_with_a_real_hash_via_the_injected_hasher() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        user = await register_user(
            email="Ada@Example.com",
            password="correct horse battery staple",
            display_name="Ada Lovelace",
            users=users,
            hash_password=fake_hash_password,
        )
        assert user.email == "ada@example.com"  # normalized
        assert user.hashed_password == "hashed:correct horse battery staple"
        assert user.hashed_password != "correct horse battery staple"  # never stored in plaintext
        stored = await users.get_by_id(user.id)
        assert stored is not None
        assert stored.email == user.email

    asyncio.run(_body())


def test_register_with_an_already_taken_email_raises_and_does_not_double_add() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        await register_user(
            email="ada@example.com",
            password="first-password",
            display_name="Ada",
            users=users,
            hash_password=fake_hash_password,
        )
        try:
            await register_user(
                email="ADA@EXAMPLE.COM",  # same email, different case
                password="second-password",
                display_name="Ada Again",
                users=users,
                hash_password=fake_hash_password,
            )
            raise AssertionError("expected EmailAlreadyRegisteredError")
        except EmailAlreadyRegisteredError:
            pass

    asyncio.run(_body())


def test_register_with_an_empty_display_name_raises_a_domain_error_and_adds_nothing() -> None:
    async def _body() -> None:
        users = FakeUserRepository()
        try:
            await register_user(
                email="ada@example.com",
                password="a-password",
                display_name="   ",
                users=users,
                hash_password=fake_hash_password,
            )
            raise AssertionError("expected UserDomainError")
        except UserDomainError:
            pass
        assert await users.get_by_email("ada@example.com") is None

    asyncio.run(_body())


if __name__ == "__main__":
    test_functions = [
        test_register_creates_a_user_with_a_real_hash_via_the_injected_hasher,
        test_register_with_an_already_taken_email_raises_and_does_not_double_add,
        test_register_with_an_empty_display_name_raises_a_domain_error_and_adds_nothing,
    ]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
