[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Windows Environment Variables and PATH: Step-by-Step Guide |
| **Section** | docs |
| **Category** | it-fundamentals/operating-systems |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | Windows 10 or Windows 11 PC |
| **Has screenshots** | No |

---

# Windows Environment Variables and PATH: Step-by-Step Guide

## Overview

Have you ever typed a command in a terminal (like `python`, `git`, or `node`) and seen this error?

```text
'python' is not recognized as an internal or external command, operable program or batch file.
```

This error happens because Windows does not know which folder your program lives in. 

An **Environment Variable** is a small note that Windows keeps in memory. The most famous one is called **`PATH`**. `PATH` is a list of folders where Windows automatically looks whenever you type a command.

This guide shows you how to add any program to `PATH` step by step using the mouse or simple commands.

---

## The Difference: User Variables vs System Variables

When you open the settings screen, you will see two boxes:

1. **User Variables (Top Box):** Only affects the person currently logged in to the computer.
2. **System Variables (Bottom Box):** Affects all accounts on the computer and background services. If you are not sure, editing **System Variables** is the most common choice.

---

## Method 1: The Mouse and Window Method (Easiest)

Follow these exact steps to add a folder to your PATH:

### Step 1: Open the Environment Variables Window

1. On your keyboard, press the **Windows Key** and the **R** key together.
2. A small **Run** box opens in the bottom-left corner.
3. In the box, type this text:

   ```text
   sysdm.cpl ,3
   ```
   *(Make sure there is a space before the comma and three).*

4. Press **Enter** or click **OK**.
5. A window titled **System Properties** will appear with the **Advanced** tab already selected.
6. Look at the very bottom right and click the button that says **Environment Variables...**.

---

### Step 2: Edit the PATH List

1. Look at the bottom section labeled **System variables**.
2. Scroll down until you find the variable named **Path** (or **PATH**).
3. Click on **Path** once to highlight it in blue.
4. Click the **Edit...** button below the box.
5. A new smaller window opens showing a list of folder paths.

---

### Step 3: Add Your New Folder Path

1. On the right side of the window, click the **New** button.
2. A new blank line appears at the bottom of the list.
3. Paste or type the exact folder location where your program is installed.
   - *Example for Python:* `C:\Python312`
   - *Example for Node.js:* `C:\Program Files\nodejs`
   - *Example for Git:* `C:\Program Files\Git\cmd`
4. Click the **OK** button to close the edit window.
5. Click **OK** on the Environment Variables window.
6. Click **OK** on the System Properties window.

---

### Step 4: Close and Reopen Your Terminal

> **Crucial Rule:** Any Command Prompt or PowerShell window that was already open will NOT know about your changes. You must close all open terminal windows and open a fresh new one.

---

## Method 2: The Fast PowerShell Method

If you prefer typing a command instead of clicking through windows:

1. Press the **Windows Key**.
2. Type: `powershell`
3. Right-click on **Windows PowerShell** and select **Run as administrator**.
4. To add a folder (for example `C:\tools\bin`) to your user PATH permanently, copy and paste this command:

   ```powershell
   [Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\tools\bin", "User")
   ```
   *(Replace `C:\tools\bin` with your actual folder path).*

5. Press **Enter**.
6. Close PowerShell and open a new terminal window.

---

## Verification: How to Test That It Worked

1. Open a new **Command Prompt** or **PowerShell** window.
2. Type the command you wanted to use (for example, `git --version` or `python --version`).
3. Press **Enter**.

- **Success:** You will see the version number printed on the screen (such as `git version 2.45.0`).
- **Failure:** If it still says "not recognized", double-check that you did not make any spelling mistake in the folder path, and verify that the program `.exe` file actually sits inside that exact folder.

---

## Common Mistakes to Avoid

- **Do not add the file name, only the folder:** Add `C:\Program Files\Git\cmd`, not `C:\Program Files\Git\cmd\git.exe`.
- **Do not delete other lines:** In the Path window, never delete existing lines. Only click **New** and add your folder.
- **Spaces in paths:** If a folder name has spaces (like `Program Files`), Windows handles it automatically in the GUI list. You do not need to add extra quotation marks.
