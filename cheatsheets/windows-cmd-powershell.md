[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)

---

# Windows Command Prompt (CMD) vs PowerShell Cheatsheet

A side-by-side translation table comparing standard actions in Command Prompt (CMD) and Windows PowerShell.

---

## 1. Moving Around Folders and Files

| What You Want to Do | Command Prompt (CMD) | PowerShell |
|---|---|---|
| Show which folder you are in right now | `cd` | `pwd` |
| Go to a different folder | `cd myfolder` | `cd myfolder` |
| Go to another drive (like D:) | `cd /d D:\Projects` | `cd D:\Projects` |
| List all files in the current folder | `dir` | `ls` or `Get-ChildItem` |
| Show hidden files | `dir /a` | `Get-ChildItem -Force` |
| Create a new folder | `mkdir myfolder` | `mkdir myfolder` |
| Delete a folder and everything inside it | `rmdir /s /q myfolder` | `Remove-Item -Recurse -Force myfolder` |
| Copy a file to another folder | `copy file.txt dest\` | `Copy-Item file.txt -Destination dest\` |
| Move or rename a file | `move old.txt new.txt` | `Move-Item old.txt new.txt` |
| Read the text inside a file | `type file.txt` | `cat file.txt` or `Get-Content file.txt` |
| Clear the terminal screen | `cls` | `cls` |

---

## 2. Managing Programs and Processes

| What You Want to Do | Command Prompt (CMD) | PowerShell |
|---|---|---|
| Show all running programs | `tasklist` | `Get-Process` |
| Force close a program by name | `taskkill /f /im node.exe` | `Stop-Process -Name node -Force` |
| Force close a program by ID number | `taskkill /f /pid 1234` | `Stop-Process -Id 1234 -Force` |
| Find where a program is installed | `where git` | `Get-Command git` |

---

## 3. Network and Internet Checks

| What You Want to Do | Command Prompt (CMD) | PowerShell |
|---|---|---|
| Show your IP address and router address | `ipconfig` | `Get-NetIPConfiguration` |
| Show detailed network card information | `ipconfig /all` | `ipconfig /all` |
| Flush / clean your website DNS cache | `ipconfig /flushdns` | `Clear-DnsClientCache` |
| Test connection to an address | `ping 8.8.8.8` | `ping 8.8.8.8` |
| Check if a port is open on another PC | `telnet host 22` | `Test-NetConnection -ComputerName host -Port 22` |
| Check which program is using port 5432 | `netstat -ano \| findstr :5432` | `Get-NetTCPConnection -LocalPort 5432` |
