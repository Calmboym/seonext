"""Unit tests for backend/app/security/authentication (PHASE-0.5).

Backend-unit category (.ai/WBS.md §4, PHASE-0.8). Authentication is
explicitly called out as a high-risk area requiring "stronger validation"
(docs/22_TESTING_AND_VALIDATION.md §108) — this is the substantively
important backend-unit test in this suite; test_error_hierarchy.py (the
other backend-unit file) is the one chosen for genuine same-session
execution because it has no third-party dependencies, not because it's
more important than this one.

NOTE (PHASE-0.8, session 7): requires `pydantic-settings` (via
`get_settings()`, transitively imported through
backend.app.security.authentication.tokens) and `bcrypt`, neither
installed in this session's sandbox (Risk R9) — this file is
syntax-checked (`ast.parse`) only, unlike test_error_hierarchy.py in the
same directory. It uses ordinary pytest idioms (`pytest.raises`) since
there is no benefit to hobbling it for standalone execution the way
test_error_hierarchy.py was — this file cannot run standalone regardless,
missing pydantic itself, not just pytest.

Every test below sets `SECRET_KEY`/`DATABASE_URL` via monkeypatch rather
than relying on a real `.env` file, so this suite runs the same way in
CI as on a fresh checkout with no local Postgres — consistent with
`get_settings()` being `@lru_cache`d (backend/app/infrastructure/config/
settings.py): each test clears the cache first so one test's monkeypatched
secret can't leak into the next via the cached Settings singleton.
"""

import time

import pytest


@pytest.fixture(autouse=True)
def _configured_settings(monkeypatch):
    """Provide the minimum environment `Settings()` needs to construct
    without touching a real database or real secret, and reset the
    `get_settings()` cache before and after so tests don't interfere with
    each other via the process-wide `@lru_cache`."""

    from backend.app.infrastructure.config.settings import get_settings

    monkeypatch.setenv("DATABASE_URL", "postgresql+asyncpg://test:test@localhost/test")
    monkeypatch.setenv("SECRET_KEY", "test-only-secret-key-do-not-use-in-production")
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


class TestPasswordHashing:
    def test_hash_password_never_returns_the_plaintext_password(self):
        from backend.app.security.authentication.passwords import hash_password

        plaintext = "correct horse battery staple"
        hashed = hash_password(plaintext)

        assert hashed != plaintext
        assert plaintext not in hashed

    def test_verify_password_accepts_the_correct_password(self):
        from backend.app.security.authentication.passwords import hash_password, verify_password

        plaintext = "correct horse battery staple"
        hashed = hash_password(plaintext)

        assert verify_password(plaintext, hashed) is True

    def test_verify_password_rejects_an_incorrect_password(self):
        from backend.app.security.authentication.passwords import hash_password, verify_password

        hashed = hash_password("correct horse battery staple")

        assert verify_password("wrong password", hashed) is False

    def test_verify_password_returns_false_for_a_malformed_hash_instead_of_raising(self):
        """A malformed hash (e.g. from data corruption, or a caller
        accidentally passing the plaintext instead of a hash) must fail
        closed, not crash the caller."""
        from backend.app.security.authentication.passwords import verify_password

        assert verify_password("anything", "not-a-real-bcrypt-hash") is False

    def test_hashing_the_same_password_twice_produces_different_hashes(self):
        """bcrypt salts each hash independently — two users with the same
        password must not be distinguishable by comparing hash strings."""
        from backend.app.security.authentication.passwords import hash_password

        first = hash_password("shared-password")
        second = hash_password("shared-password")

        assert first != second


class TestTokenIssuance:
    def test_create_access_token_round_trips_through_decode_access_token(self):
        from backend.app.security.authentication.tokens import create_access_token, decode_access_token

        token = create_access_token(subject="user-abc-123")

        assert decode_access_token(token) == "user-abc-123"

    def test_an_expired_access_token_is_rejected(self, monkeypatch):
        """docs/07_TECHNICAL_ARCHITECTURE.md §53's "session expiration"
        requirement — a token minted in the past with an already-elapsed
        expiry must not decode successfully."""
        from backend.app.security.authentication import tokens

        monkeypatch.setattr(tokens, "ACCESS_TOKEN_EXPIRE_MINUTES", -1)
        expired_token = tokens.create_access_token(subject="user-abc-123")

        with pytest.raises(tokens.TokenError, match="expired"):
            tokens.decode_access_token(expired_token)

    def test_a_password_reset_token_cannot_be_used_as_an_access_token(self):
        """Prevents a password-reset link from silently doubling as a
        full session token — the two token types must not be
        interchangeable even though they share one signing mechanism."""
        from backend.app.security.authentication.tokens import (
            TokenError,
            create_password_reset_token,
            decode_access_token,
        )

        reset_token = create_password_reset_token(subject="user-abc-123")

        with pytest.raises(TokenError, match="expected a 'access' token"):
            decode_access_token(reset_token)

    def test_a_token_signed_with_a_different_secret_is_rejected(self, monkeypatch):
        """Simulates a forged or replayed-from-another-environment token
        — the single most important property a signing mechanism has."""
        from backend.app.infrastructure.config.settings import get_settings
        from backend.app.security.authentication.tokens import TokenError, create_access_token, decode_access_token

        token = create_access_token(subject="user-abc-123")

        monkeypatch.setenv("SECRET_KEY", "a-completely-different-secret")
        get_settings.cache_clear()

        with pytest.raises(TokenError, match="invalid"):
            decode_access_token(token)

    def test_create_password_reset_token_round_trips_through_decode_password_reset_token(self):
        from backend.app.security.authentication.tokens import (
            create_password_reset_token,
            decode_password_reset_token,
        )

        token = create_password_reset_token(subject="user-abc-123")

        assert decode_password_reset_token(token) == "user-abc-123"

    def test_access_and_password_reset_tokens_have_different_expiry_windows(self):
        """Documents and protects the specific policy values
        (ACCESS_TOKEN_EXPIRE_MINUTES=30, PASSWORD_RESET_TOKEN_EXPIRE_MINUTES=15)
        — a reset link living as long as a session would weaken account
        recovery's security properties."""
        from backend.app.security.authentication import tokens

        assert tokens.PASSWORD_RESET_TOKEN_EXPIRE_MINUTES < tokens.ACCESS_TOKEN_EXPIRE_MINUTES

    def test_decode_access_token_does_not_check_any_permission(self):
        """Directly protects acceptance criterion 4 (.ai/WBS.md §4,
        PHASE-0.5): this module must not implement per-resource
        authorization. A subject that doesn't correspond to any real user
        yet still decodes successfully — there is nothing here to reject
        it on, by design."""
        from backend.app.security.authentication.tokens import create_access_token, decode_access_token

        token = create_access_token(subject="this-subject-does-not-exist-anywhere")

        assert decode_access_token(token) == "this-subject-does-not-exist-anywhere"
