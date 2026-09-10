import { getHealthStatus } from "../services/health";

// Health is fetched fresh on every request — this page exists to *prove*
// frontend↔API wiring (PHASE-0.6 acceptance criterion 3), not to cache a
// liveness check.
export const dynamic = "force-dynamic";

export default async function HomePage() {
  const health = await getHealthStatus();

  return (
    <main style={{ fontFamily: "system-ui, sans-serif", padding: "2rem", maxWidth: "40rem" }}>
      <h1>Seonex</h1>
      <p>SEO Research &amp; Strategy Copilot — Foundation placeholder page (PHASE-0.6).</p>

      <section>
        <h2>API health check</h2>
        <p>
          Status:{" "}
          <strong>{health.ok ? (health.data.status ?? "unknown") : "unreachable"}</strong>
        </p>
        {!health.ok && (
          <p style={{ color: "#b91c1c" }}>
            Could not reach the API at <code>{health.url}</code>: {health.error}
          </p>
        )}
      </section>
    </main>
  );
}
