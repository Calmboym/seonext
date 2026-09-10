/**
 * Frontend-unit tests for services/health.ts.
 *
 * frontend-unit category (.ai/WBS.md §4, PHASE-0.8's second named
 * category). Mocks `global.fetch` rather than hitting a real backend —
 * that round trip is `apps/web`'s own smoke test at render time
 * (app/page.tsx, PHASE-0.6), not this test's job. This file tests the
 * three branches getHealthStatus() has to get right: a healthy response,
 * an HTTP-error response, and a network failure — each maps to a
 * different `HealthCheckResult` shape that app/page.tsx branches on.
 *
 * NOTE (PHASE-0.8, session 7): requires `vitest` (newly declared
 * devDependency) — not installed in this session's sandbox, no
 * npm-registry access (Risk R9). Syntax-checked with the sandbox's
 * global `tsc` only, same as every other .ts/.tsx file this session.
 */

import { afterEach, describe, expect, it, vi } from "vitest";

import { getHealthStatus } from "../../services/health";

describe("getHealthStatus", () => {
  afterEach(() => {
    vi.unstubAllGlobals();
  });

  it("returns ok:true with the parsed body when the API responds 200", async () => {
    const mockFetch = vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => ({ status: "ok" }),
    });
    vi.stubGlobal("fetch", mockFetch);

    const result = await getHealthStatus();

    expect(result.ok).toBe(true);
    if (result.ok) {
      expect(result.data.status).toBe("ok");
    }
  });

  it("returns ok:false with the HTTP status when the API responds non-2xx", async () => {
    const mockFetch = vi.fn().mockResolvedValue({
      ok: false,
      status: 503,
      json: async () => ({}),
    });
    vi.stubGlobal("fetch", mockFetch);

    const result = await getHealthStatus();

    expect(result.ok).toBe(false);
    if (!result.ok) {
      expect(result.error).toBe("HTTP 503");
    }
  });

  it("returns ok:false with the error message when fetch itself throws (e.g. connection refused)", async () => {
    const mockFetch = vi.fn().mockRejectedValue(new Error("fetch failed: ECONNREFUSED"));
    vi.stubGlobal("fetch", mockFetch);

    const result = await getHealthStatus();

    expect(result.ok).toBe(false);
    if (!result.ok) {
      expect(result.error).toContain("ECONNREFUSED");
    }
  });

  it("requests the health path under the configured API base URL", async () => {
    const mockFetch = vi.fn().mockResolvedValue({
      ok: true,
      status: 200,
      json: async () => ({ status: "ok" }),
    });
    vi.stubGlobal("fetch", mockFetch);

    await getHealthStatus();

    const [calledUrl] = mockFetch.mock.calls[0] as [string, unknown];
    expect(calledUrl).toMatch(/\/api\/v1\/health$/);
  });
});
