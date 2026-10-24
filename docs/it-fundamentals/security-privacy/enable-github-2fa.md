[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Turn On Two-Factor Authentication for GitHub |
| **Section** | docs |
| **Category** | it-fundamentals/security-privacy |
| **Difficulty** | Beginner |
| **Last verified** | 2026-10-15 |
| **Prerequisites** | A GitHub account; a phone with an authenticator app (or a passkey/WebAuthn device, or SMS where supported) |
| **Has screenshots** | No |

---

# Turn On Two-Factor Authentication for GitHub

## Overview
Two-factor authentication (2FA) means a stolen password alone is not enough to get into your account. On GitHub it also unlocks contributing to many organizations that require it.

## Before You Start
- Install an authenticator app (e.g., a TOTP app) or have a passkey device ready. Prefer an app or passkey over SMS: SMS codes can be intercepted and are not available in every country.

## Steps

### 1. Open your settings
Click your avatar (top right) → **Settings** → **Password and authentication**.

### 2. Enable 2FA
Under "Two-factor authentication", click **Enable two-factor authentication** and pick a method:

- **Passkey / security key** (recommended): register a fingerprint, Face ID, or a hardware key.
- **Authenticator app (TOTP)**: GitHub shows a QR code; scan it with your app and enter the 6-digit code it generates.

### 3. Save your recovery codes
GitHub shows **16 recovery codes**. This is the step people skip and later regret:

- Download the codes (`.txt` file) **and** print them or store a copy in your password manager.
- Each code works once, if you lose your phone or change devices.
- Store them somewhere offline and safe — not in a plain note on the same phone.

### 4. Confirm and you are done
Follow the remaining prompts (GitHub may ask you to re-enter your password and confirm a code). Your account page now shows "Two-factor authentication: Enabled".

## Verify It Worked
Sign out and sign back in: after your password, GitHub asks for the second factor.

## Common Issues
- **New phone, old authenticator**: recovery codes get you in; then re-register the new device and regenerate codes.
- **Lost codes and lost device**: GitHub's account-recovery flow is slow by design. Avoid it: keep a second method (passkey + app) registered.
- **Git over HTTPS stops working**: passwords no longer authenticate Git operations — use a **Personal Access Token**, SSH, or the `gh` CLI instead.
