[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

| Field | Value |
|---|---|
| **Title** | Install Python on Windows and Check PATH |
| **Section** | docs |
| **Category** | programming-dev/languages |
| **Difficulty** | Beginner |
| **Last verified** | 2026-11-12 |
| **Prerequisites** | Windows 10 or 11 PC, internet connection |
| **Has screenshots** | No |

# Install Python on Windows and Check PATH

## Overview
Installing Python on Windows without adding it to your system `PATH` causes `'python' is not recognized as an internal or external command` errors in the terminal. This guide shows how to download the official installer, enable the PATH option during setup, and verify that both `python` and `pip` work from any terminal.

## Before You Start
- Know whether your Windows PC is 64-bit (most modern PCs) or ARM64.
- Close any open Command Prompt or PowerShell windows before starting the installation.

## Steps

### 1. Download the Official Python Installer
Download Python directly from the official Python Software Foundation website rather than third-party bundles.

1. Open your browser and visit `python.org/downloads/`.
2. Click **Download Python 3.x.x** (the latest stable Windows 64-bit installer).
3. Save the `.exe` installer file (for example, `python-3.12.x-amd64.exe`).

### 2. Run the Installer and Check "Add python.exe to PATH"
This is the most important step on Windows:

1. Double-click the downloaded `.exe` installer.
2. On the very first screen, **check the box at the bottom**:
   - `[x] Add python.exe to PATH`
3. *(Optional)* Also check **Use admin privileges when installing py.exe** if you want the Python Launcher available for all users.
4. Click **Install Now** and approve the Windows UAC prompt if asked.
5. On the final "Setup was successful" screen, click **Disable path length limit** if offered, then click **Close**.

### 3. Verify Python and PATH in a New Terminal
Open a **new** Command Prompt or PowerShell window (old terminals will not have the updated `PATH`) and run:

```cmd
python --version
pip --version
```

You should see output similar to:
```text
Python 3.12.7
pip 24.2 from C:\Users\<YourName>\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)
```

To inspect the exact folder Windows is resolving `python` from, run:
```cmd
where python
```

## Verification
Confirm that Python executes interactively and can run inline code:

```cmd
python -c "print('Python PATH is working!')"
```

Expected output:
```text
Python PATH is working!
```

## Common Errors
- `'python' is not recognized as an internal or external command` -> You forgot to check **Add python.exe to PATH** during installation, or you are using a terminal opened before installation. Open a new terminal and test `py --version`. If `py` works, re-run the `.exe` installer, choose **Modify**, ensure **Add Python to environment variables** is checked, and finish.
- `Running 'python' opens the Microsoft Store instead of Python.` -> Windows App Execution Aliases intercept `python.exe`. Open **Settings** > **Apps** > **Advanced app settings** > **App execution aliases**, and turn **Off** both `App Installer (python.exe)` and `App Installer (python3.exe)`.
