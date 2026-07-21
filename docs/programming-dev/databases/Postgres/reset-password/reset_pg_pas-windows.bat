@echo off
setlocal

set "PGDATA=C:\Program Files\PostgreSQL\18\data"
set "PGBIN=C:\Program Files\PostgreSQL\18\bin"

echo === Step 1: Stopping PostgreSQL ===
net stop postgresql-x64-18

echo === Step 2: Backing up pg_hba.conf (your safety net) ===
copy "%PGDATA%\pg_hba.conf" "%PGDATA%\pg_hba.conf.bak" /Y

echo === Step 3: Temporarily allowing passwordless local login ===
powershell -Command "(Get-Content '%PGDATA%\pg_hba.conf') -replace '^(local\s+all\s+all\s+)scram-sha-256', '$1trust' -replace '^(host\s+all\s+all\s+127\.0\.0\.1/32\s+)scram-sha-256', '$1trust' -replace '^(host\s+all\s+all\s+::1/128\s+)scram-sha-256', '$1trust' | Set-Content '%PGDATA%\pg_hba.conf'"

echo === Step 4: Starting PostgreSQL with trust auth ===
net start postgresql-x64-18

echo.
echo === Step 5: Set your new password ===
echo (Letters and numbers only - avoid %%, ^^, ^&, ^|, quotes)
set /p NEWPASS=Enter NEW password for user postgres: 

echo === Step 6: Applying new password ===
"%PGBIN%\psql" -U postgres -c "ALTER USER postgres WITH PASSWORD '%NEWPASS%';"

echo === Step 7: Restoring original secure pg_hba.conf ===
copy "%PGDATA%\pg_hba.conf.bak" "%PGDATA%\pg_hba.conf" /Y

echo === Step 8: Restarting PostgreSQL with secure auth restored ===
net stop postgresql-x64-18
net start postgresql-x64-18

echo.
echo Done. Username stays "postgres", password is now what you entered.
echo Secure scram-sha-256 authentication is back in place.
pause