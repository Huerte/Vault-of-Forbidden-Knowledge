[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

| Field | Value |
|---|---|
| **Title** | Kill the Process That Is Using a Port on Windows |
| **Section** | docs |
| **Category** | it-fundamentals/networking |
| **Difficulty** | Beginner |
| **Last verified** | 2026-11-10 |
| **Prerequisites** | Windows PC, Command Prompt or PowerShell (Run as Administrator) |
| **Has screenshots** | No |

# Kill the Process That Is Using a Port on Windows

## Overview
When starting a web server or database (like Node.js, Django, or PostgreSQL) fails because a port is already in use (`EADDRINUSE`), this guide shows how to find the process holding that port and terminate it cleanly.

## Before You Start
- Open Command Prompt or PowerShell as Administrator (Right-click Start > Terminal / Command Prompt (Admin)).
- Know the port number you want to free (for example: `3000`, `5432`, or `8080`).
- 
## Steps

### 1. Find the Process ID (PID) Using the Port
Run `netstat` to find which process is currently listening on your port.

```cmd
netstat -ano | findstr :<PORT>
```

For example, to find what is using port `3000`:
```cmd
netstat -ano | findstr :3000
```

Look at the rightmost column in the output. That number is the Process ID (**PID**):
```
  TCP    0.0.0.0:3000           0.0.0.0:0              LISTENING       14280
```
In this example, the PID is `14280`.

### 2. Identify What Program the PID Belongs To (Optional)
Before killing the process, check which application it is to make sure it is safe to close.

```cmd
tasklist /fi "pid eq <PID>"
```

Example:
```cmd
tasklist /fi "pid eq 14280"
```

Output:
```
Image Name                     PID Session Name        Session#    Mem Usage
========================= ======== ================ =========== ============
node.exe                     14280 Console                    1     45,212 K
```

### 3. Terminate the Process Using taskkill
Stop the process immediately using `taskkill` with the `/F` (force) and `/PID` flags.

```cmd
taskkill /PID <PID> /F
```

Example:
```cmd
taskkill /PID 14280 /F
```

Expected output:
```
SUCCESS: The process with PID 14280 has been terminated.
```

*(Alternative via Task Manager)*: You can also press `Ctrl + Shift + Esc`, open the **Details** tab, sort by **PID**, find the number, right-click it, and select **End task**.

## Verification
Confirm the port has been released by running the `netstat` check again.

```cmd
netstat -ano | findstr :<PORT>
```

If the port is now free, this command will return no output, and your development server can now bind to the port.

## Common Errors
- `ERROR: The process ... could not be terminated. Access is denied.` -> You ran Command Prompt without administrator privileges. Close it, right-click Command Prompt or Terminal, and choose **Run as administrator**.
- `ERROR: The process ... not found.` -> The process already closed or terminated on its own. Re-check `netstat` to confirm if the port is free.
