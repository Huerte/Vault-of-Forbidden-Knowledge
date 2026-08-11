[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Understanding Hidden Windows Folders: AppData, Temp, and Path Variables |
| **Section** | docs |
| **Category** | it-fundamentals/operating-systems |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | None |
| **Has screenshots** | No |

---

# Understanding Hidden Windows Folders: AppData, Temp, and Path Variables

## Overview

When installing programs or fixing computer issues, you often hear words like `%APPDATA%`, `%TEMP%`, or `%USERPROFILE%`.

These words with percent signs (`%...%`) are **Path Shortcuts** in Windows. Because every computer has a different username and sometimes different drive letters, Windows uses these shortcuts so instructions work on every PC.

This guide explains what each folder does in plain English and how to open them instantly.

---

## The Most Common Windows Shortcuts

| Shortcut | Where It Actually Takes You | What Lives Inside in Simple Words |
|---|---|---|
| **`%USERPROFILE%`** | `C:\Users\<YourName>` | Your main personal home folder (holds Desktop, Documents, Downloads). |
| **`%APPDATA%`** | `C:\Users\<YourName>\AppData\Roaming` | Settings for your installed programs (VS Code settings, Discord logins, game saves). |
| **`%LOCALAPPDATA%`** | `C:\Users\<YourName>\AppData\Local` | Big cache files, program temporary stores, and browser history. |
| **`%TEMP%`** | `C:\Users\<YourName>\AppData\Local\Temp` | Temporary scratch files that can safely be deleted when cleaning disk space. |
| **`%PROGRAMFILES%`** | `C:\Program Files` | Where standard 64-bit applications are installed. |
| **`%PROGRAMFILES(X86)%`** | `C:\Program Files (x86)` | Where older 32-bit applications are installed. |
| **`%PROGRAMDATA%`** | `C:\ProgramData` | Shared settings used by all user accounts on the computer. |

---

## What is AppData and Why is It Hidden?

Inside your user folder (`C:\Users\<YourName>`), there is a folder called **AppData**. 

By default, Windows makes AppData **hidden** so users do not accidentally delete their app settings or game saves.

Inside AppData, you will find three main subfolders:

```text
AppData\
├── Roaming\     -> Holds app settings that follow your profile (e.g. Discord, Spotify logins)
├── Local\       -> Holds machine-specific files, large cache files, and auto-updaters (e.g. Chrome cache)
└── LocalLow\    -> Special low-permission sandboxed folder (used by games and secure browser modes)
```

---

## Secret Run Box Shortcuts (Fastest Way to Open Folders)

You can jump to any of these folders in less than 2 seconds using the **Run** box:

1. Press **Windows Key + R** on your keyboard.
2. Type any of the words below into the box and press **Enter**:

- Type `%appdata%` -> Opens your `AppData\Roaming` folder immediately.
- Type `%localappdata%` -> Opens your `AppData\Local` folder immediately.
- Type `%temp%` -> Opens your temporary files folder.
- Type `.` (just a single dot) -> Opens your main User profile folder (`C:\Users\<YourName>`).
- Type `shell:startup` -> Opens the folder where Windows stores programs that start automatically when your PC boots up.

---

## How to Show Hidden Folders in Windows File Explorer

If you want to browse into these folders normally using your mouse:

### On Windows 11:
1. Open any folder in **File Explorer**.
2. Click the **View** button in the top menu bar.
3. Hover your mouse over **Show**.
4. Click on **Hidden items** so a checkmark appears next to it.

### On Windows 10:
1. Open **File Explorer**.
2. Click the **View** tab at the top.
3. Put a checkmark in the box that says **Hidden items**.

You will now see AppData and other system folders appear with slightly faded folder icons.
