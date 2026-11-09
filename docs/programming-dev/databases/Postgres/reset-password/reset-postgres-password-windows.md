---
Title: Reset a PostgreSQL Password on Windows
Section: docs
Category: programming-dev/databases/Postgres/reset-password
Difficulty: Intermediate
Last verified: 2026-11-09
Prerequisites: Windows administrator access; a local PostgreSQL 18 installation
Has screenshots: No
---

[← Back to README](../../../../../README.md) | [Contributing Guide](../../../../../CONTRIBUTING.md)

# Reset a PostgreSQL Password on Windows
#postgresql #windows #security #password-recovery

## Overview

The accompanying [Windows batch script](reset_pg_pas-windows.bat) resets the password for PostgreSQL's `postgres` role. It does so by **temporarily allowing passwordless local connections**. Read the entire script and this guide before running it.

## Before You Start

- Work on a machine you administer. Keep it disconnected from untrusted networks while authentication is relaxed.
- The script is hard-coded for PostgreSQL **18**: `C:\Program Files\PostgreSQL\18\data`, `C:\Program Files\PostgreSQL\18\bin`, and service `postgresql-x64-18`. Adjust all three for your installation.
- Make a separate backup of `pg_hba.conf` in a safe location. The script overwrites `pg_hba.conf.bak` without asking.
- Use an elevated Command Prompt. The commands stop and start a Windows service and modify its configuration.

## Steps: What the Script Does

### 1. Stops the PostgreSQL service

`net stop postgresql-x64-18` stops the database so the authentication file can be changed.

### 2. Backs up authentication settings

It copies `pg_hba.conf` to `pg_hba.conf.bak`. This backup is the route back to your original authentication policy.

### 3. Temporarily permits passwordless local login

A PowerShell command changes matching `scram-sha-256` entries to `trust` for local connections and the loopback addresses `127.0.0.1/32` and `::1/128`. It does **not** rewrite every possible `pg_hba.conf` layout or authentication method. With `trust`, matching connections do not need a password.

### 4. Restarts PostgreSQL with the temporary settings

`net start postgresql-x64-18` makes the modified authentication rules active. Minimize the time the database runs with `trust` enabled.

### 5. Prompts for the replacement password

The script asks for `NEWPASS` and inserts it into a SQL command. Its prompt tells you to use letters and numbers only; **it does not enforce that restriction or hide what you type**. Do not enter quotes or shell metacharacters, and do not reuse an important password.

### 6. Runs the password change

`psql -U postgres -c "ALTER USER postgres WITH PASSWORD '…';"` sets the replacement password. Check the command's actual output for success; the script does not stop automatically if `psql` fails.

### 7. Restores authentication and restarts the service

It copies `pg_hba.conf.bak` back to `pg_hba.conf`, stops PostgreSQL, and starts it again. **The final “Done” message is unconditional**: a failed copy or restart could leave passwordless authentication enabled.

## Verification

1. Open `pg_hba.conf` and confirm the original `scram-sha-256` entries have been restored. Compare it with your separate backup if possible.
2. Confirm the `postgresql-x64-18` service is running.
3. Reconnect from a new terminal using the updated password:

   ```powershell
   & "C:\Program Files\PostgreSQL\18\bin\psql.exe" -h 127.0.0.1 -U postgres -W -c "SELECT current_user;"
   ```

   The role should be `postgres`. Confirm independently that a wrong password is rejected under the restored authentication rules.

## Common Errors and Recovery

- **The service does not stop or start:** Verify the actual service name in Windows Services. Do not assume the password was changed.
- **`psql` still asks for the old password:** Your `pg_hba.conf` may not have matched the script's exact replacement patterns. Inspect the file rather than loosening additional rules blindly.
- **The script fails after enabling `trust`:** Stop PostgreSQL, manually restore the backed-up `pg_hba.conf`, restart the service, and verify that passwordless login is no longer permitted. Do this **before** another password-reset attempt.
- **A special character breaks the password command:** The script builds SQL from raw input. Prefer a reviewed, interactive `psql` recovery procedure for passwords containing punctuation; do not try to escape characters by guesswork.

For the exact commands and paths, see [reset_pg_pas-windows.bat](reset_pg_pas-windows.bat). This guide describes the current script; it does not make its error handling or temporary `trust` configuration inherently safe.
