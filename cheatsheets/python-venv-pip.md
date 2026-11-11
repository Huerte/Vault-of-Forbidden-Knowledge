[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)

# Python venv and pip Cheatsheet (Quick Reference)

A simple, practical reference sheet for creating virtual environments and managing packages on Windows, macOS, and Linux.

## 1. Creating a Virtual Environment

```bash
python -m venv .venv                             # Create a virtual environment named .venv (Windows)
python3 -m venv .venv                            # Create a virtual environment named .venv (macOS/Linux)
```

## 2. Activating the Environment

```bash
# Windows (Command Prompt)
.venv\Scripts\activate.bat                       # Activate environment in Windows cmd.exe

# Windows (PowerShell)
.venv\Scripts\Activate.ps1                       # Activate environment in PowerShell

# macOS and Linux (bash/zsh)
source .venv/bin/activate                        # Activate environment in terminal
```

## 3. Verifying the Active Environment

```bash
where python                                     # Verify active Python path (Windows)
which python                                     # Verify active Python path (macOS/Linux)
python -V                                        # Check the Python version of the active environment
```

## 4. Installing and Managing Packages with pip

```bash
python -m pip install --upgrade pip              # Upgrade pip to the latest version
pip install requests                             # Install the latest version of a package
pip install requests==2.31.0                     # Install a specific package version
pip install -r requirements.txt                  # Install all dependencies listed in a file
pip install -e .                                 # Install current project in editable/development mode
```

## 5. Inspecting Installed Packages

```bash
pip list                                         # List all installed packages and their versions
pip show requests                                # Show metadata, location, and dependencies of a package
pip check                                        # Verify installed packages have compatible dependencies
```

## 6. Saving and Exporting Dependencies

```bash
pip freeze > requirements.txt                    # Save pinned package versions to requirements.txt
```

## 7. Removing Packages and Leaving the Environment

```bash
pip uninstall requests -y                        # Remove a package without confirmation prompt
deactivate                                       # Exit the virtual environment and return to system Python
```
