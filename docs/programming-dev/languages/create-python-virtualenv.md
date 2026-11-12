[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

| Field | Value |
|---|---|
| **Title** | Create and Activate a Python Virtual Environment |
| **Section** | docs |
| **Category** | programming-dev/languages |
| **Difficulty** | Beginner |
| **Last verified** | 2026-11-12 |
| **Prerequisites** | Python 3.8+ installed on Windows, macOS, or Linux |
| **Has screenshots** | No |

# Create and Activate a Python Virtual Environment

## Overview
A Python virtual environment (`venv`) gives each project its own isolated folder for installed packages and Python versions. Using a virtual environment prevents dependency conflicts between different projects on the same computer.

## Before You Start
- Confirm Python is installed by running `python --version` (Windows) or `python3 --version` (macOS/Linux).
- Open a terminal inside your project folder.

## Steps

### 1. Create the Virtual Environment
Run Python's built-in `venv` module to create a `.venv` folder inside your project directory:

```bash
# Windows
python -m venv .venv

# macOS / Linux
python3 -m venv .venv
```

### 2. Activate the Virtual Environment
Activate the environment so `python` and `pip` commands use `.venv` instead of your global system Python:

```bash
# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux (bash or zsh)
source .venv/bin/activate
```

Once activated, you will see `(.venv)` at the beginning of your terminal prompt.

### 3. Install a Package Inside the Environment
With `(.venv)` active, install packages normally using `pip`:

```bash
python -m pip install --upgrade pip
pip install requests
```

You can save your project's installed packages to a file so others can reproduce your environment:
```bash
pip freeze > requirements.txt
```

### 4. Deactivate the Virtual Environment
When you finish working on the project, return to your system Python by running:

```bash
deactivate
```

The `(.venv)` prefix disappears from your terminal prompt.

## Verification
While the environment is activated, verify that Python points inside `.venv`:

```bash
# Windows
where python

# macOS / Linux
which python
```

The output path should end with `.venv\Scripts\python.exe` (Windows) or `.venv/bin/python` (macOS/Linux).

## Common Errors
- `running scripts is disabled on this system` (Windows PowerShell) -> PowerShell's default execution policy blocks `.ps1` activation scripts. Run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` once in PowerShell, then retry `.venv\Scripts\Activate.ps1`.
- `No module named venv` (Ubuntu/Debian Linux) -> System Python omits the `venv` package by default. Run `sudo apt update && sudo apt install python3-venv`.
