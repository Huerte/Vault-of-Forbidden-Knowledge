[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | How to Undo Mistakes in Git: Simple Recovery Guide |
| **Section** | docs |
| **Category** | programming-dev/version-control |
| **Difficulty** | Intermediate |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | Basic Git knowledge |
| **Has screenshots** | No |

---

# How to Undo Mistakes in Git: Simple Recovery Guide

## Overview

Everyone makes mistakes in Git: you edited the wrong file, committed too early, wrote a typo in your message, or deleted something by accident.

This guide provides a quick "What is your problem?" table and shows the exact command to fix it without panic.

---

## Find Your Situation in This Table

| What You Did Wrong | What You Want to Happen | The Command to Run |
|---|---|---|
| I edited a file, broke it, and want it back to how it was | Throw away changes in that single file | `git restore filename.txt` |
| I edited 10 files and want to cancel all my changes today | Throw away all uncommitted edits everywhere | `git restore .` |
| I typed `git add .` by mistake | Unstage files so they are not saved yet | `git restore --staged .` |
| I saved a commit with a typo in the message | Change the last commit message | `git commit --amend -m "New text"` |
| I forgot to include a file in my last commit | Add the missing file to the last commit | `git add file.txt` then `git commit --amend --no-edit` |
| I saved a commit by mistake, but I want to keep my code | Undo commit, keep all files on screen | `git reset --soft HEAD~1` |
| I saved a bad commit and want to erase it completely | Erase the last commit and all its code | `git reset --hard HEAD~1` |
| I already pushed a bad commit to GitHub | Safely reverse the pushed commit | `git revert <commit-id>` |

---

## Step-by-Step Solutions

---

### Scenario 1: You Edited a File and Want to Cancel Your Changes

**Situation:** You opened `index.html`, typed some code that broke everything, and you just want the file to go back to the way it was before you started editing.

Run this command:
```bash
git restore index.html
```
*(Replace `index.html` with your actual file name. The file instantly returns to its clean saved state).*

If you edited many files and want to throw away changes on ALL of them at once:
```bash
git restore .
```

---

### Scenario 2: You Ran `git add .` by Accident

**Situation:** You ran `git add .`, but you do not want to save those files right now.

Run this command:
```bash
git restore --staged .
```
*(Your files will stay edited on your screen, but Git takes them out of the "ready to save" staging area).*

---

### Scenario 3: You Want to Fix the Last Commit Message

**Situation:** You committed with `git commit -m "add login"`, but realized you had a typo or wanted a better description.

Run this command:
```bash
git commit --amend -m "Add secure user login form"
```
*(Git updates the last snapshot with your new message without creating a duplicate commit).*

---

### Scenario 4: You Want to Undo the Last Commit (Keep Your Code)

**Situation:** You committed your work, but realized you were not finished yet. You want to undo the snapshot, but keep all your written code intact.

Run this command:
```bash
git reset --soft HEAD~1
```
*(The commit is deleted, but all the code you wrote remains safe and staged on your computer).*

---

### Scenario 5: You Already Pushed a Bad Commit to GitHub

**Situation:** You pushed a commit to GitHub and other teammates can see it. You want to cancel that commit safely without breaking anyone else's history.

1. Find the ID code of the bad commit by running:
   ```bash
   git log --oneline -n 5
   ```
2. Copy the 7-letter ID code (for example: `a1b2c3d`).
3. Run the revert command:
   ```bash
   git revert a1b2c3d
   ```
4. Git creates a brand new commit that does the exact opposite of the bad commit, cleanly removing the broken changes.
5. Push the fix to GitHub:
   ```bash
   git push
   ```

---

### Scenario 6: Panic Mode (You Ran `reset --hard` and Lost Good Code)

**Situation:** You ran `git reset --hard` and accidentally deleted good commits. Do not panic! Git remembers almost everything in a hidden diary called `reflog`.

1. In your terminal, type:
   ```bash
   git reflog
   ```
2. You will see a list of every move you made with numbers like `HEAD@{0}`, `HEAD@{1}`, `HEAD@{2}`.
3. Look for the line just BEFORE you made the mistake (example: `HEAD@{2}`).
4. Restore your project back to that exact moment by typing:
   ```bash
   git reset --hard HEAD@{2}
   ```
5. All your lost commits and files will instantly reappear!
