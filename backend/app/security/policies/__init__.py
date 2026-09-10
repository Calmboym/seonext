"""Security policy definitions (password complexity rules, token
lifetime policy, lockout thresholds, etc.) — the configurable-rules layer
that authentication/, authorization/, and permissions/ would each read
from, rather than hardcoding their own thresholds.

Reserved for PHASE-1+. PHASE-0.5's authentication/ module hardcodes its
two constants (`ACCESS_TOKEN_EXPIRE_MINUTES`,
`PASSWORD_RESET_TOKEN_EXPIRE_MINUTES`) directly rather than reading them
from here — introducing a policy-configuration layer for two constants
would be premature; revisit once a third or fourth policy value exists
and the duplication actually hurts.
"""
