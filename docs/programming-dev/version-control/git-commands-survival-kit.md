[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Git Commands Survival Kit: The Essential Guide for Daily Work |
| **Section** | docs |
| **Category** | programming-dev/version-control |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | Git installed on your computer |
| **Has screenshots** | No |

---

# Git Commands Survival Kit: The Essential Guide for Daily Work

## Overview

Think of **Git** like a super-smart camera system for your code and project files. 

Every time you make progress, you take a snapshot (called a **Commit**). If you make a mistake later, you can easily go back in time to any previous snapshot.

This guide explains the most important commands you need every day in plain English with clear examples.

---

## 1. Initial Setup: Tell Git Who You Are

When you install Git on a new computer, you must tell it your name and email. Git writes this information on every snapshot you take.

Open your terminal (PowerShell, Command Prompt, or Git Bash) and run these 3 commands:

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
git config --global init.defaultBranch main
```

---

## 2. Starting a Project

### Option A: Create a Brand New Empty Repository
If you have a folder on your computer that you want Git to start tracking:

1. Open your terminal inside that folder.
2. Type:
   ```bash
   git init
   ```
3. Git creates a hidden `.git` folder inside. It is now watching your project.

### Option B: Download an Existing Project from GitHub
If your project is already stored online on GitHub:

```bash
git clone https://github.com/username/my-project.git
```
*(Git downloads the entire project folder and its full history onto your computer).*

---

## 3. Daily 4-Step Routine (How You Save Your Work)

This is the exact sequence you will use 95% of the time:

```text
Step 1: Check what changed -> git status
Step 2: Pick files to save  -> git add .
Step 3: Save the snapshot   -> git commit -m "Explain what you did"
Step 4: Send to GitHub      -> git push
```

### Detailed Breakdown of the 4 Steps:

#### Step 1: See What Changed
```bash
git status
```
- **Red files:** Files you edited or added that are not yet marked for saving.
- **Green files:** Files ready to be saved in the next snapshot.

#### Step 2: Prepare Files to Save (Staging)
```bash
# Add one specific file:
git add index.html

# Or add ALL edited files at once:
git add .
```

#### Step 3: Take the Snapshot (Commit)
Always write a short, clear note in English inside the quotation marks explaining what you changed:
```bash
git commit -m "Add contact form to home page"
```

#### Step 4: Send Your Saved Changes to GitHub
```bash
git push
```
*(Uploads your commits from your computer up to GitHub).*

---

## 4. Working with Branches (Safe Experiments)

A **Branch** is like a duplicate copy of your project where you can build new features or try experiments safely without breaking the working `main` version.

### Create and Switch to a New Branch
```bash
git switch -c feature/new-button
```
*(Now any changes you make will only live on this branch).*

### Switch Back to the Main Branch
```bash
git switch main
```

### List All Branches on Your Computer
```bash
git branch
```
*(The branch with the green star `*` next to it is the one you are currently on).*

---

## 5. Getting Updates from Teammates

If someone else pushed changes to GitHub and you want to download them into your computer:

```bash
git pull
```

---

## 6. Temporarily Hiding Changes (Stash)

If you are in the middle of editing files, but need to quickly switch branches without saving a full snapshot:

```bash
# Put all your current work into a temporary hidden drawer:
git stash

# Later, when you want your edits back:
git stash pop
```

---

## 7. Looking at History

To see a neat, clean list of the last 10 snapshots:

```bash
git log --oneline -n 10
```

Each line shows a short ID code (like `7a8b9c0`) and the message you wrote when saving.
