"""Secure password storage.

Implements docs/07_TECHNICAL_ARCHITECTURE.md §53's "secure password
storage where passwords exist" requirement, satisfying PHASE-0.5
acceptance criterion (1): credentials are never stored in plaintext
(.ai/WBS.md §4). `hash_password`'s return value is the only thing a
caller should ever persist — nothing here stores, logs, or transmits a
raw password.

Uses `bcrypt` directly (newly declared in pyproject.toml) rather than a
wrapper library like `passlib` — bcrypt's own API is a two-function
surface (`hashpw`/`checkpw`) and needs no extra abstraction at this
foundation stage. A later phase can introduce algorithm-agility (e.g.
Argon2) behind these same two function signatures without changing call
sites — the same swappability principle backend/app/observability/logging
already applies to its formatter, and backend/app/observability/metrics
applies to prometheus_client.

Operates on raw strings only, never a User ORM model or any database
row — no user domain exists yet (PHASE-1 scope), and none is needed here.
Satisfies acceptance criterion (3): testable without a full user domain
existing.

NOTE (PHASE-0.5, session 7): `bcrypt` is newly declared in
pyproject.toml but was NOT installed or import-tested this session (no
network access — Risk R9, same limitation recorded for every other
dependency this project has declared). This module is syntax-checked
(`ast.parse`) only; its actual runtime behavior is UNVERIFIED.
"""

import bcrypt

_BCRYPT_ROUNDS = 12


def hash_password(plain_password: str) -> str:
    """Hash `plain_password` for storage. Returns a self-describing
    bcrypt hash string (algorithm identifier + cost factor + salt +
    digest, all encoded together per bcrypt's own format) — store exactly
    this return value. Nothing else about the original password is kept
    or needed."""

    salt = bcrypt.gensalt(rounds=_BCRYPT_ROUNDS)
    hashed = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check `plain_password` against a hash previously produced by
    `hash_password`. Returns `False` (never raises) for a malformed or
    foreign-format hash, matching bcrypt's own fail-closed posture —
    never reveals *why* a check failed, only whether it succeeded."""

    try:
        return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))
    except (ValueError, TypeError):
        return False
