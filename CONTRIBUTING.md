# Contributing Guide

[← Back to README](README.md)

Rules for adding or editing entries in this repository.

## Which Section Does My Note Belong In?

| You are writing...                              | Put it in       |
|-------------------------------------------------|-----------------|
| A step-by-step technical how-to guide           | `docs/`         |
| Setup or config notes for a specific app        | `apps/`         |
| A one-page command or syntax quick reference    | `cheatsheets/`  |
| A dated bug fix or incident record              | `logs/`         |
| A random tip, trick, or personal observation    | `notes/`        |

## File Placement and Naming
- Use kebab-case for filenames. Start with an action verb.
  Examples: `setup-postgresql.md`, `install-neovim.md`, `fix-docker-permission.md`
- App entries under `apps/<category>/` live inside a dedicated directory named after the application: `apps/<category>/<app-name>/<app-name>.md` (e.g., `apps/cli/git/git.md`, `apps/developer/vscode/vscode.md`).
- One topic per file. Split long guides instead of merging unrelated steps.
- OS-specific steps go in separate files: `windows.md`, `linux.md`.
- Log entries use the date prefix: `YYYY-MM-DD-short-description.md`.

## Using Templates
Copy from `templates/` before writing anything new:

| Template | Use when writing... |
|---|---|
| [guide-template.md](templates/guide-template.md) | Step-by-step docs or app setup guides |
| [tool-entry-template.md](templates/tool-entry-template.md) | App-specific notes or tool reference pages |
| [troubleshooting-template.md](templates/troubleshooting-template.md) | A bug fix or incident log entry |

## Frontmatter
Every file must have frontmatter at the top:

```markdown
---
Title: Clear Action Title
Section: docs / apps / cheatsheets / logs / notes
Category: <subfolder path, e.g., it-fundamentals/networking>
Difficulty: Beginner / Intermediate / Advanced
Last verified: YYYY-MM-DD
Prerequisites: List any requirements here
Has screenshots: Yes / No
---
```

## Tags
Add a tags line immediately after the `# Title` heading:

```markdown
#docker #postgresql #deployment #has-screenshots
```

## Screenshots and Images
- Store images in `assets/images/<section>/<category>/<guide-name>/`.
- Name files to match step order: `01-login.png`, `02-config.png`.
- Use `.png` for UI screenshots, `.jpg` for hardware photos, `.gif` for short animated sequences.
- Crop tightly. Redact any passwords, tokens, or private IPs before saving.
- One screenshot per meaningful state change, not one per click.

## Writing Rules
- Short sentences. One idea per sentence.
- Skip intro fluff. Start with step 1 or the point.
- Skip installation steps for simple, single-command installs (e.g., `winget install git`). Only include an installation section or create a dedicated markdown guide if the installation requires a complex, multi-step technical process.
