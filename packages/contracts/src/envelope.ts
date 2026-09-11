// Mirrors backend/app/contracts/api/envelope.py's `SuccessEnvelope` —
// see that file's docstring for the full rationale (why only
// status/data/created_at/request_id/contract_id/contract_version are
// present, and why AI-agent-specific envelope categories from
// docs/16_OUTPUT_CONTRACTS.md §12 are deliberately omitted here rather
// than stubbed out). Kept in sync with the Python side by hand — see
// this package's README for the manual-sync statement
// (`PHASE-1.4` acceptance criterion 3).

export interface SuccessEnvelope<TData> {
  contract_id: string;
  contract_version: string;
  status: "success";
  data: TData;
  request_id: string;
  /** ISO 8601 timestamp string over the wire (a JS `Date` on the client
   * side after `JSON.parse` + `new Date(...)`, same as every other
   * timestamp field in this package). */
  created_at: string;
}
