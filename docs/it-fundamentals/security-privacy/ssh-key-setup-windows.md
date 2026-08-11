[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | How to Create and Set Up SSH Keys on Windows |
| **Section** | docs |
| **Category** | it-fundamentals/security-privacy |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | A Windows 10 or Windows 11 PC |
| **Has screenshots** | No |

---

# How to Create and Set Up SSH Keys on Windows

## Overview

When you connect to GitHub, GitLab, or a remote server, typing your username and password every single time is slow and annoying.

An **SSH Key** is a pair of two secret files that work like a **lock and a physical key**:

1. **The Public Key (`.pub` file):** This is the **lock**. You can freely give this file to GitHub or paste it onto any server. It is not a secret.
2. **The Private Key (no extension):** This is your **physical key**. It stays safely inside your computer. You must NEVER give this file to anyone or upload it online.

When your computer connects to GitHub, the two files talk to each other to prove who you are without sending any passwords over the internet.

---

## Step 1: Open PowerShell or Command Prompt

1. Press the **Windows Key** on your keyboard.
2. Type: `powershell`
3. Click on **Windows PowerShell**.

---

## Step 2: Generate Your New SSH Key Pair

1. In the blue PowerShell window, copy and paste this command:

   ```powershell
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
   *(Change `your_email@example.com` to your real email address).*

2. Press **Enter**.

3. You will see this prompt:
   ```text
   Enter file in which to save the key (C:\Users\YourName/.ssh/id_ed25519):
   ```
   **What to do:** Just press **Enter** on your keyboard to accept the default location.

4. Next, it will ask:
   ```text
   Enter passphrase (empty for no passphrase):
   ```
   **What to do:** If you want an extra security password when using the key, type a passphrase and press Enter. If you want it to log in automatically without any password prompt, just press **Enter** twice.

5. You will see a small text art box appear on the screen. This means your keys are successfully created!

---

## Step 3: Copy Your Public Key to Your Clipboard

You need to copy the text inside the `.pub` file so you can give it to GitHub or your server.

1. In PowerShell, paste this command and press **Enter**:

   ```powershell
   Get-Content -Path "$env:USERPROFILE\.ssh\id_ed25519.pub" | Set-Clipboard
   ```

2. Your public key is now copied to your clipboard (just like doing `Ctrl + C`).

---

## Step 4: Add the Key to Your GitHub Account

1. Open your web browser and log in to **GitHub** (`https://github.com`).
2. Click your **profile picture icon** in the top-right corner, then click **Settings**.
3. In the left sidebar, click **SSH and GPG keys**.
4. Click the green button that says **New SSH key**.
5. In the **Title** box, type a friendly name (for example: `My Windows Laptop`).
6. Click inside the big **Key** box and press **Ctrl + V** on your keyboard to paste the key you copied in Step 3.
7. Click **Add SSH key**.

---

## Step 5: Turn on the Windows SSH Agent Service

**Why:** Windows includes a background helper called `ssh-agent` that remembers your key so you never have to reload it.

1. Press the **Windows Key**.
2. Type: `powershell`
3. Right-click on **Windows PowerShell** and choose **Run as administrator**.
4. Paste these two lines one by one, pressing **Enter** after each:

   ```powershell
   Set-Service -Name ssh-agent -StartupType Automatic
   Start-Service -Name ssh-agent
   ```

5. Now add your private key to the agent by running:

   ```powershell
   ssh-add "$env:USERPROFILE\.ssh\id_ed25519"
   ```

6. You will see: `Identity added: ...`

---

## Step 6: Test the Connection (Verification)

1. Open a regular PowerShell or Command Prompt window.
2. Type this exact command and press **Enter**:

   ```powershell
   ssh -T git@github.com
   ```

3. If it asks:
   `Are you sure you want to continue connecting (yes/no/[fingerprint])?`
   Type `yes` and press **Enter**.

4. **Expected Success Output:**
   ```text
   Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

If you see this message with your GitHub username, your SSH key setup is 100% complete and working.

---

## Golden Rules for Safety

- **NEVER share the file named `id_ed25519` (without `.pub`):** That is your private key. Anyone with that file can pretend to be you.
- **You can safely share `id_ed25519.pub`:** The `.pub` file is meant to be shared.
