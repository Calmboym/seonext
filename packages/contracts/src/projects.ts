// Mirrors backend/app/contracts/api/projects.py exactly. Written ahead
// of PHASE-1.5 (not authorized/started this session) per that file's own
// docstring and docs/03 §97.

import type { SuccessEnvelope } from "./envelope";

export interface ProjectCreateRequest {
  name: string;
  description?: string;
  industry?: string | null;
  markets?: string[];
  locations?: string[];
  business_model?: string | null;
  products?: string[];
  services?: string[];
  target_audiences?: string[];
  commercial_goals?: string[];
  strategic_priorities?: string[];
  website?: string | null;
}

// Every field optional: `undefined` means "leave unchanged" (mirrors the
// Python side's `None`-means-unchanged partial-update semantics — see
// projects.py's `ProjectUpdateRequest` docstring). To clear a list field,
// send `[]` explicitly, not `undefined`.
export interface ProjectUpdateRequest {
  name?: string;
  description?: string;
  industry?: string | null;
  markets?: string[];
  locations?: string[];
  business_model?: string | null;
  products?: string[];
  services?: string[];
  target_audiences?: string[];
  commercial_goals?: string[];
  strategic_priorities?: string[];
  website?: string | null;
}

export interface ProjectData {
  id: string;
  workspace_id: string;
  name: string;
  description: string;
  industry: string | null;
  markets: string[];
  locations: string[];
  business_model: string | null;
  products: string[];
  services: string[];
  target_audiences: string[];
  commercial_goals: string[];
  strategic_priorities: string[];
  website: string | null;
  status: string;
  created_at: string;
  updated_at: string;
}

export type ProjectResponse = SuccessEnvelope<ProjectData>;

export interface ProjectListData {
  items: ProjectData[];
  total: number;
}

export type ProjectListResponse = SuccessEnvelope<ProjectListData>;
