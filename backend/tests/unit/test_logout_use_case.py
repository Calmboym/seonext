"""Unit test for `backend/app/application/commands/auth/logout.py`. Zero
third-party imports. See test_domain_user.py's docstring for the
invocation note.
"""

from backend.app.application.commands.auth.logout import logout_user


def test_logout_accepts_a_user_id_and_returns_none() -> None:
    """Documents the current contract exactly (see logout.py's module
    docstring for why this is a real, honest implementation for a
    stateless-JWT architecture, not a stub): logout does not raise, does
    not need to look anything up, and returns nothing for the route to
    act on beyond "this succeeded"."""

    result = logout_user(user_id="11111111-1111-1111-1111-111111111111")
    assert result is None


if __name__ == "__main__":
    test_functions = [test_logout_accepts_a_user_id_and_returns_none]
    for test_function in test_functions:
        test_function()
        print(f"PASS: {test_function.__name__}")
    print(f"\n{len(test_functions)} tests passed.")
