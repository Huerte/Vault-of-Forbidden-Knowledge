[← Back to README](../README.md) | [Contributing Guide](../CONTRIBUTING.md)

---

# Git Command Cheatsheet (Quick Reference)

A simple, practical sheet of the Git commands you will use every day.

---

## 1. First Time Setup on Your Computer
```bash
git config --global user.name "Your Name"         # Set your name on your commits
git config --global user.email "you@example.com"  # Set your email on your commits
git config --global init.defaultBranch main       # Make "main" the default branch name
```

---

## 2. Starting a Project
```bash
git init                            # Turn the current folder into a Git repository
git clone https://github.com/...    # Download a project from GitHub to your PC
```

---

## 3. Checking What You Did
```bash
git status                          # Show which files were edited, added, or deleted
git diff                            # Show the exact lines you changed in your files
git log --oneline -n 10             # Show a clean list of the last 10 saves (commits)
```

---

## 4. Saving Your Work (The 3 Main Steps)
```bash
git add file.txt                    # Mark one file ready to be saved
git add .                           # Mark ALL edited files ready to be saved
git commit -m "Explain changes"     # Save a permanent snapshot with a short note
```

---

## 5. Working with Branches (Separate Workspaces)
```bash
git branch                          # Show all branches on your computer
git switch -c new-feature           # Create and jump into a new branch
git switch main                     # Jump back to the main branch
git branch -d old-feature           # Delete a branch you finished using
```

---

## 6. Sending and Getting Work Online
```bash
git pull                            # Download newest changes from GitHub
git push -u origin branch-name      # Upload your new branch to GitHub for the first time
git push                            # Upload your newest commits to GitHub
```

---

## 7. Temporary Hiding (Stash)
```bash
git stash                           # Hide your unsaved changes temporarily
git stash pop                       # Bring your hidden changes back
```

---

## 8. Undoing Mistakes (Emergency Fixes)
```bash
git restore file.txt                # Cancel unsaved changes in one file
git restore .                       # Cancel unsaved changes in all files
git restore --staged .              # Unstage files so they are not saved yet
git reset --soft HEAD~1             # Undo last commit, but KEEP all your written code
git reset --hard HEAD~1             # Delete last commit and ERASE all changes
git reflog                          # View history of all actions to recover lost work
```
