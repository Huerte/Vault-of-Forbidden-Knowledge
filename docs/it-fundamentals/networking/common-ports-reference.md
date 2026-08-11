[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Common Network Ports Reference and How to Check Them |
| **Section** | docs |
| **Category** | it-fundamentals/networking |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | None |
| **Has screenshots** | No |

---

# Common Network Ports Reference and How to Check Them

## Overview

Think of an **IP address** like the street address of a big apartment building (your computer). 

A **Port** is like the specific apartment room number inside that building (like Room 80 or Room 443). Different programs listen at different room numbers so messages do not get mixed up.

When you play a game, open a website, or connect to a database, your computer uses a specific port number to talk to that service.

---

## The Most Common Ports You Will Meet

### 1. Web and Internet Ports (Everyday Use)

| Port Number | Name | What It Is Used For in Simple Words |
|---|---|---|
| **80** | HTTP | Normal websites without the lock icon (unencrypted plain text). |
| **443** | HTTPS | Secure websites with the green/grey lock icon in your browser (encrypted). |
| **53** | DNS | Translates website names like `google.com` into numbers. |
| **22** | SSH | Secure remote login to control Linux servers and Raspberry Pi boards. |
| **21** | FTP | Old file sending protocol used to upload files to web hosts. |
| **3389** | RDP | Windows Remote Desktop to see and control another Windows PC screen. |

---

### 2. Database Ports (For Programmers and Apps)

| Port Number | Database Name | What It Is in Simple Words |
|---|---|---|
| **5432** | PostgreSQL | A very popular database used by modern web apps. |
| **3306** | MySQL / MariaDB | The classic database used by WordPress and PHP apps. |
| **1433** | Microsoft SQL Server | Database system made by Microsoft for company apps. |
| **6379** | Redis | A super-fast temporary memory database for login sessions. |
| **27017** | MongoDB | Document database that stores data in JSON text format. |

---

### 3. Local Development Ports (When Building Apps)

| Port Number | Common Program | What It Is in Simple Words |
|---|---|---|
| **3000** | React / Node.js | Default local test website port when building web apps. |
| **5173** | Vite | Fast test server port used for modern frontend code. |
| **8000** | Django / Python | Default test website port for Python apps. |
| **8080** | Alternative Web | Backup web port when Port 80 or 3000 is already taken. |

---

## How to Check Which Ports are Open on Your Windows PC

### Method 1: Check If a Specific Port is in Use (Example: Port 5432)

1. Press the **Windows Key** on your keyboard.
2. Type: `cmd`
3. Click on **Command Prompt**.
4. Type this command and press **Enter**:

   ```cmd
   netstat -ano | findstr :5432
   ```

5. Look at the result:
   - **If you see lines ending in `LISTENING` followed by a number (like `4912`):** Port 5432 is currently active. The number at the far right is the Process ID (PID) using it.
   - **If the screen returns blank with no text:** Port 5432 is completely free and not being used by any program.

---

### Method 2: Find Which Program is Using a Port (Using PowerShell)

1. Press the **Windows Key**.
2. Type: `powershell`
3. Click on **Windows PowerShell**.
4. Type this command (replace `3000` with the port you want to check) and press **Enter**:

   ```powershell
   Get-Process -Id (Get-NetTCPConnection -LocalPort 3000).OwningProcess
   ```

5. Look at the result: It will show the exact program name (such as `node`, `postgres`, or `python`) holding that port.

---

### Method 3: Test if Another Computer Has a Port Open (Without Installing Extra Tools)

1. Open **PowerShell**.
2. Type this command and press **Enter**:

   ```powershell
   Test-NetConnection -ComputerName 192.168.1.50 -Port 22
   ```
   *(Replace `192.168.1.50` with the target IP address and `22` with the port number).*

3. Look at the last line:
   - `TcpTestSucceeded : True` -> The port is open and ready to connect.
   - `TcpTestSucceeded : False` -> The port is closed or blocked by a firewall.

---

## Common Problems with Ports

- **Error: "Port already in use" (EADDRINUSE):** This happens when you start a local app (like React on port 3000), but an older copy of the app is still running in the background. Use Method 2 to find the program and close it in Task Manager.
- **Port blocked by Windows Firewall:** If other computers on your home Wi-Fi cannot connect to your server, Windows Firewall is blocking incoming traffic. You must add an "Inbound Rule" in Windows Firewall to allow that port number.
