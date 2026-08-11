[← Back to README](../../../../../README.md) | [Contributing Guide](../../../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | How to Backup and Restore a PostgreSQL Database with pg_dump |
| **Section** | docs |
| **Category** | programming-dev/databases/Postgres |
| **Difficulty** | Intermediate |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | PostgreSQL installed on your computer |
| **Has screenshots** | No |

---

# How to Backup and Restore a PostgreSQL Database with pg_dump

## Overview

A database stores all your user accounts, products, and app data. If your computer crashes or an update breaks your tables, you need a safe copy of that data.

- **`pg_dump`**: A tool built into PostgreSQL that exports your database into a single file (called a **backup file**).
- **`psql` / `pg_restore`**: Tools that read that backup file and rebuild all your tables and data when you need them.

This guide walks you through creating a backup file and restoring it step by step.

---

## Step 1: Open Your Terminal and Set Your Password

Before running backup commands, tell your terminal your PostgreSQL password so it does not stop and ask you every time.

### On Windows PowerShell:
```powershell
$env:PGPASSWORD = "your_actual_postgres_password"
```

### On Windows Command Prompt (CMD):
```cmd
set PGPASSWORD=your_actual_postgres_password
```

---

## Step 2: How to Make a Backup (Export)

Pick one of the two backup types below based on your needs:

### Option A: Create a Plain SQL Backup File (Easiest to Read)
This makes a `.sql` text file that you can open in Notepad to inspect your data.

1. Run this command:

   ```bash
   pg_dump -U postgres -h localhost -p 5432 -d mydb -f my_backup.sql
   ```

   **What each part means in simple words:**
   - `-U postgres`: The database username (usually `postgres`).
   - `-h localhost`: The database runs on this computer.
   - `-p 5432`: The default PostgreSQL port number.
   - `-d mydb`: The name of the database you want to copy (replace `mydb` with your real database name).
   - `-f my_backup.sql`: The name of the file you want to save.

2. Look in your current folder: You will see a new file named `my_backup.sql`.

---

### Option B: Create a Compressed Custom Backup File (Best for Big Databases)
This creates a compressed `.dump` binary file that takes less disk space and restores faster.

Run this command:
```bash
pg_dump -U postgres -h localhost -p 5432 -F c -b -v -f my_backup.dump mydb
```

---

## Step 3: How to Restore a Database from Your Backup File (Import)

When you need to restore your saved data onto the same or another computer:

### If You Have a Plain SQL File (`.sql`):

1. First, create a new empty database to receive the data:
   ```bash
   psql -U postgres -h localhost -c "CREATE DATABASE mydb_restored;"
   ```

2. Load all tables and data into that database:
   ```bash
   psql -U postgres -h localhost -d mydb_restored -f my_backup.sql
   ```

3. Text will scroll on your screen as tables and rows are recreated.

---

### If You Have a Compressed Custom File (`.dump`):

1. Create the new empty database:
   ```bash
   psql -U postgres -h localhost -c "CREATE DATABASE mydb_restored;"
   ```

2. Restore using `pg_restore`:
   ```bash
   pg_restore -U postgres -h localhost -d mydb_restored -v my_backup.dump
   ```

---

## Verification: How to Check That Your Data Restored Correctly

1. Connect to your restored database using `psql`:
   ```bash
   psql -U postgres -d mydb_restored
   ```

2. List all tables by typing `\dt` and pressing **Enter**.
3. Count the rows in any table to verify data exists:
   ```sql
   SELECT count(*) FROM users;
   ```
4. Type `\q` and press **Enter** to exit.

---

## Common Problems and Fixes

- **Error: `FATAL: password authentication failed`:** The password you entered in Step 1 is incorrect. Check your password spelling.
- **Error: `'pg_dump' is not recognized`:** The PostgreSQL bin folder is not in your Windows PATH. Follow the [Windows Environment Variables Guide](../../../../docs/it-fundamentals/operating-systems/windows-environment-variables.md) to add `C:\Program Files\PostgreSQL\<version>\bin` to your PATH.
- **Error: `database "mydb" does not exist`:** Check that you typed the database name correctly with exact uppercase/lowercase letters.
