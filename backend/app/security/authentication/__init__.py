"""Session/token authentication mechanism.

See passwords.py (secure credential storage) and tokens.py (session/token
issuance, expiration, and the password-reset mechanism half of account
recovery). Scoped exactly to PHASE-0.5's Observation #1 interpretation
(.ai/WBS.md §4): a bare mechanism, independent of any user/workspace/
project record.

No FastAPI dependency (e.g. a `get_current_user`-style extractor) exists
yet here — wiring this into an actual protected route needs *something*
to look the decoded subject up against, which needs PHASE-1's user model.
Populate that wiring once that model exists; until then,
`decode_access_token` is the full extent of what a caller can do with an
incoming token (verify it and get back an opaque subject string).
"""

from .passwords import hash_password, verify_password
from .tokens import (
    TokenError,
    create_access_token,
    create_password_reset_token,
    decode_access_token,
    decode_password_reset_token,
)

__all__ = [
    "TokenError",
    "create_access_token",
    "create_password_reset_token",
    "decode_access_token",
    "decode_password_reset_token",
    "hash_password",
    "verify_password",
]
