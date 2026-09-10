"""
Typed, validated-at-startup application configuration.

Per docs/07_TECHNICAL_ARCHITECTURE.md §58, configuration is split into three
categories:

    1. Application Configuration — feature flags, timeouts, limits,
       environment behavior. Safe to log; not secret.
    2. Secret Configuration — API keys, database credentials, signing
       secrets. Never logged, never given a hardcoded fallback.
    3. Runtime Configuration — model routing, provider availability, queue
       concurrency. Placeholders only at PHASE-0 — no AI runtime or queue
       exists yet to actually route to (see docs/07_TECHNICAL_ARCHITECTURE.md
       §§41-43, out of scope until a later phase); the fields exist so
       downstream phases don't have to re-plumb configuration loading.

Environment model (docs/07_TECHNICAL_ARCHITECTURE.md §59):
    development | test | staging | production

All three settings groups are pydantic-settings BaseSettings subclasses,
so instantiation itself performs validation — an invalid or missing
required value raises immediately at startup rather than failing later,
deep in a request path. No secret field carries a default value: a
missing secret must be a loud startup failure, never a silent fallback.

NOTE (PHASE-0.2, session 6): pydantic / pydantic-settings are declared in
pyproject.toml but were NOT installed or import-tested in the environment
this file was written in (no network access was available to this
session). This module has been syntax-checked (ast.parse) but not
runtime-executed. See .ai/PROJECT_STATE.md § 14 for the full verification
record — do not treat this as RUNTIME_VERIFIED.
"""

from enum import Enum
from functools import lru_cache

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    """The environment model from docs/07_TECHNICAL_ARCHITECTURE.md §59."""

    DEVELOPMENT = "development"
    TEST = "test"
    STAGING = "staging"
    PRODUCTION = "production"


class ApplicationSettings(BaseSettings):
    """Application Configuration — feature flags, timeouts, limits, environment
    behavior. Not secret; safe to log or expose in diagnostics."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    environment: Environment = Field(
        default=Environment.DEVELOPMENT,
        description="Selects environment-specific behavior via configuration, "
        "never via forked business logic (docs/20_PROJECT_STRUCTURE.md §59).",
    )
    debug: bool = Field(default=False)
    api_host: str = Field(default="0.0.0.0")
    api_port: int = Field(default=8000, ge=1, le=65535)
    request_timeout_seconds: float = Field(default=30.0, gt=0)
    log_level: str = Field(default="INFO")

    # Feature flags (docs/07_TECHNICAL_ARCHITECTURE.md §58 example category).
    # Empty by design at PHASE-0 — no feature exists yet to flag.
    feature_flags: dict[str, bool] = Field(default_factory=dict)

    @property
    def is_production(self) -> bool:
        return self.environment is Environment.PRODUCTION


class SecretSettings(BaseSettings):
    """Secret Configuration — API keys, database credentials, signing
    secrets. Never logged. No field below may carry a non-empty default:
    a missing secret must fail startup loudly, not silently fall back."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    # Required — no default. Instantiating SecretSettings() without this
    # set in the environment raises a pydantic ValidationError at startup.
    database_url: SecretStr = Field(
        ...,
        description="PostgreSQL connection string. See "
        "backend/app/infrastructure/database/session.py (PHASE-0.3).",
    )
    secret_key: SecretStr = Field(
        ...,
        description="Signing secret for session/token issuance. Consumed "
        "by backend/app/security/authentication/tokens.py (PHASE-0.5).",
    )

    def __repr__(self) -> str:  # pragma: no cover - defensive redaction
        # Never let a stray print()/log of a SecretSettings instance leak
        # values; SecretStr already redacts .__str__, but be explicit here
        # too since __repr__ is what most loggers/debuggers actually call.
        return "SecretSettings(**redacted**)"


class RuntimeSettings(BaseSettings):
    """Runtime Configuration — model routing, provider availability, queue
    concurrency. Per docs/07_TECHNICAL_ARCHITECTURE.md §58's own examples.
    Placeholder fields only: no AI runtime (§§41-43) or queue (§§21-23)
    exists yet at PHASE-0. Typed now so later phases consume, not invent,
    this contract."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        extra="ignore",
        case_sensitive=False,
    )

    default_model_provider: str | None = Field(
        default=None,
        description="Reserved for PHASE-2+ (AI runtime). Unused at PHASE-0.",
    )
    queue_concurrency: int = Field(
        default=1,
        ge=1,
        description="Reserved for a later phase's background-worker queue "
        "(docs/07_TECHNICAL_ARCHITECTURE.md §§21-23). No queue exists yet.",
    )


class Settings:
    """Aggregates the three configuration categories behind one object,
    so callers don't need to know the category split to get a value —
    but the split is preserved internally per docs/07_TECHNICAL_ARCHITECTURE.md
    §58, e.g. for redacting `secret` from diagnostic dumps."""

    def __init__(self) -> None:
        self.app = ApplicationSettings()
        self.secret = SecretSettings()
        self.runtime = RuntimeSettings()


@lru_cache
def get_settings() -> Settings:
    """Process-wide cached settings singleton. Constructing `Settings()`
    validates all three groups immediately — call this once, early, at
    application startup (see backend/app/main.py, PHASE-0.4), not lazily
    inside a request handler, so a misconfiguration is a startup failure."""

    return Settings()
