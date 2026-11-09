---
Title: Set Up SSH Keys for GitHub on Linux and macOS
Section: docs
Category: it-fundamentals/security-privacy
Difficulty: Beginner
Last verified: 2026-11-09
Prerequisites: A Linux or macOS terminal; a GitHub account; OpenSSH
Has screenshots: No
---

[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md) | [Windows guide](ssh-key-setup-windows.md)

# Set Up SSH Keys for GitHub on Linux and macOS
#ssh #github #linux #macos #security

## Overview

SSH keys let you authenticate Git operations without entering your GitHub password. You give GitHub the **public** key (`.pub`), while the **private** key stays on your computer. For Windows, use the [separate SSH setup guide](ssh-key-setup-windows.md).

## Before You Start

- Open Terminal on macOS, or your terminal app on Linux.
- Check that OpenSSH is installed with `ssh -V`.
- If `~/.ssh/id_ed25519` already exists, do **not** overwrite it. Keep the existing key or choose a different filename when generating another one.

## Steps

### 1. Generate a new Ed25519 key pair

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

Replace the example address with an email used for your GitHub account. Accept the default path (`~/.ssh/id_ed25519`) **only if it does not overwrite an existing key**. Use a strong passphrase when prompted; it protects a stolen private-key file.

The command creates `id_ed25519` (private; never share it) and `id_ed25519.pub` (public; safe to upload to GitHub).

### 2. Start `ssh-agent` and load your key

On **Linux**:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

On **macOS**:

```bash
eval "$(ssh-agent -s)"
ssh-add --apple-use-keychain ~/.ssh/id_ed25519
```

The macOS command can remember the passphrase in Keychain. If your version of `ssh-add` does not recognize `--apple-use-keychain`, use `ssh-add ~/.ssh/id_ed25519` instead. These steps load the key into the agent for your current session; startup behavior depends on your OS and shell configuration.

### 3. Copy only the public key

On **macOS**, copy it to the clipboard:

```bash
pbcopy < ~/.ssh/id_ed25519.pub
```

On **Linux**, print the public key and copy the entire single line from the terminal:

```bash
cat ~/.ssh/id_ed25519.pub
```

It starts with `ssh-ed25519`. **Never copy or upload `id_ed25519` without `.pub`.**

### 4. Register the key with GitHub

1. In GitHub, open **Settings → SSH and GPG keys → New SSH key**.
2. Give it a descriptive title (for example, `My Linux Laptop`).
3. Select **Authentication Key** and paste the public key into the **Key** field.
4. Click **Add SSH key** and complete any confirmation GitHub asks for.

### 5. Test authentication

```bash
ssh -T git@github.com
```

On your first connection, SSH may display GitHub's host-key fingerprint. Compare it with [GitHub's current published SSH fingerprints](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) **before** accepting. Do not accept an unfamiliar fingerprint without checking it.

Expected message: `Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.` GitHub may return a nonzero exit status even when authentication succeeds, because shell access is disabled.

## Verification

Run `ssh-add -l` to check that the key is loaded. Run `git remote -v` inside a project: SSH remotes have the form `git@github.com:OWNER/REPO.git`. HTTPS remotes do not use your SSH key.

## Common Errors

- **`Permission denied (publickey)`:** Check `ssh-add -l`, confirm that you uploaded the matching `.pub` file to the correct GitHub account, and check your remote URL.
- **`Bad permissions` or `UNPROTECTED PRIVATE KEY FILE`:** Restrict the private key with `chmod 600 ~/.ssh/id_ed25519`.
- **`Could not open a connection to your authentication agent`:** Run `eval "$(ssh-agent -s)"` again before `ssh-add`.
- **You created a key with a different filename:** Substitute that path in the `ssh-add`, `cat`/`pbcopy`, and verification steps.

For OS-specific passphrase guidance, see [GitHub's SSH key instructions](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases).
