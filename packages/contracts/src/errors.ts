// Mirrors backend/app/api/schemas/errors.py's `ErrorResponse`/`ErrorBody`
// (established `PHASE-0.4`, reused unchanged here per `PHASE-1.4`
// acceptance criterion 2 — this is the first time it is mirrored into
// packages/contracts, since apps/web had no need for it before this
// session's auth/projects contracts existed for it to accompany).

export interface ErrorBody {
  /** Stable, machine-readable error code, e.g. "VALIDATION_FAILED". */
  code: string;
  /** Human-readable description. Safe to display to an end user. */
  message: string;
  /** Structured context (e.g. which fields failed validation). Never a raw stack trace. */
  details?: Record<string, unknown> | null;
  /** Correlates this response with server-side logs. */
  request_id: string;
  /** Whether retrying the same request might succeed. */
  retryable: boolean;
}

export interface ErrorResponse {
  error: ErrorBody;
}
