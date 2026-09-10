/**
 * Consumes the versioned health endpoint (PHASE-0.4,
 * backend/app/api/routes/health.py) as PHASE-0.6's smoke test that
 * frontend↔API wiring works (.ai/WBS.md §4, acceptance criterion 3).
 *
 * NOTE (PHASE-0.6, session 7): this has never actually been executed —
 * `next dev` cannot run in this session's sandbox (no network access to
 * install node_modules; see root README.md and .ai/PROJECT_STATE.md § 14
 * / Risk R9). Written against the health endpoint's known response shape
 * (`{"status": "ok"}`) but IMPLEMENTED / UNVERIFIED at runtime, matching
 * every other PHASE-0.x runtime claim this session.
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export interface HealthResponse {
  status: string;
}

export type HealthCheckResult =
  | { ok: true; url: string; data: HealthResponse }
  | { ok: false; url: string; error: string };

export async function getHealthStatus(): Promise<HealthCheckResult> {
  const url = `${API_BASE_URL}/api/v1/health`;

  try {
    const response = await fetch(url, { cache: "no-store" });
    if (!response.ok) {
      return { ok: false, url, error: `HTTP ${response.status}` };
    }
    const data = (await response.json()) as HealthResponse;
    return { ok: true, url, data };
  } catch (error) {
    return {
      ok: false,
      url,
      error: error instanceof Error ? error.message : "unknown error",
    };
  }
}
