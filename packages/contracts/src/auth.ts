// Mirrors backend/app/contracts/api/auth.py exactly — see that file's
// docstring for the full rationale (no credentials ever echoed back,
// account-enumeration-safe password-reset messaging). Field names and
// nesting match the Python side field-for-field so a manual diff between
// the two files is enough to catch drift (`PHASE-1.4` acceptance
// criterion 3) until real schema generation exists (see README).

import type { SuccessEnvelope } from "./envelope";

// --- Register ---------------------------------------------------------

export interface RegisterRequest {
  email: string;
  password: string;
  display_name: string;
}

export interface RegisterData {
  id: string;
  email: string;
  display_name: string;
  created_at: string;
}

export type RegisterResponse = SuccessEnvelope<RegisterData>;

// --- Login --------------------------------------------------------------

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginData {
  access_token: string;
  token_type: "bearer";
  expires_in_minutes: number;
}

export type LoginResponse = SuccessEnvelope<LoginData>;

// --- Logout ---------------------------------------------------------------

// eslint-disable-next-line @typescript-eslint/no-empty-interface
export interface LogoutData {}

export type LogoutResponse = SuccessEnvelope<LogoutData>;

// --- Password recovery ------------------------------------------------

export interface PasswordResetRequestRequest {
  email: string;
}

export interface PasswordResetRequestData {
  message: string;
}

export type PasswordResetRequestResponse = SuccessEnvelope<PasswordResetRequestData>;

export interface PasswordResetConfirmRequest {
  reset_token: string;
  new_password: string;
}

export interface PasswordResetConfirmData {
  message: string;
}

export type PasswordResetConfirmResponse = SuccessEnvelope<PasswordResetConfirmData>;
