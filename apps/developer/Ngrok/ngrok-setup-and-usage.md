[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Ngrok: How to Share Your Local Website with Anyone Online |
| **Section** | apps |
| **Category** | developer |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | A free account on ngrok.com |
| **Has screenshots** | No |

---

# Ngrok: How to Share Your Local Website with Anyone Online

## What It Does

When you build a website or API on your computer, it usually runs at `http://localhost:3000`. Only you can see it on your own machine. A friend, client, or smartphone on another Wi-Fi network cannot open it.

**Ngrok** creates a secure, temporary link (like `https://something.ngrok-free.app`) that points directly to your computer. Anyone in the world can click that link and see the website running on your laptop in real time.

---

## First Run / Initial Setup

Follow these steps once to install and connect Ngrok:

### Step 1: Create a Free Account
1. Open your browser and go to `https://ngrok.com`.
2. Click **Sign Up** and create a free account.

---

### Step 2: Install Ngrok on Windows

**Option A: Using Windows Package Manager (Fastest)**
1. Press the **Windows Key**, type `powershell`, and press **Enter**.
2. Type this command and press **Enter**:
   ```powershell
   winget install ngrok.ngrok
   ```

**Option B: Manual Download**
1. Download the ZIP file from the Ngrok website dashboard.
2. Unzip it and place `ngrok.exe` into a folder (like `C:\tools\ngrok`).
3. Add that folder to your Windows PATH so you can type `ngrok` anywhere.

---

### Step 3: Connect Your Secret Authtoken

1. Go to your Ngrok online dashboard: `https://dashboard.ngrok.com/get-started/your-authtoken`.
2. Copy your personal **Authtoken** (a long text code).
3. In your terminal, type:
   ```cmd
   ngrok config add-authtoken YOUR_LONG_TOKEN_HERE
   ```
4. Press **Enter**.
5. You will see: `Authtoken saved to configuration file`.

---

## How to Use Ngrok

### Step 1: Start Your Local Website
Make sure your local web app is running in one terminal (for example, on port `3000` or `5173`).

---

### Step 2: Open the Tunnel in a Second Terminal
1. Open a new, separate terminal window.
2. If your website is running on port 3000, type:
   ```cmd
   ngrok http 3000
   ```
3. Press **Enter**.

---

### Step 3: Share the Forwarding Link
The terminal screen changes into a dashboard. Look for the line that says **Forwarding**:

```text
Forwarding   https://a1b2-c3d4-e5f6.ngrok-free.app -> http://localhost:3000
```

1. Select and copy the `https://...ngrok-free.app` URL.
2. Send this URL to your friend, test it on your phone, or paste it into a webhook settings page.
3. As long as you leave the terminal window open, the link works. When you press `Ctrl + C`, the link closes.

---

## The Secret Web Inspector Screen

While Ngrok is running, open this URL in your web browser:

```text
http://127.0.0.1:4040
```

This opens a live inspection dashboard. Every single request, image, or form sent to your website will appear on screen. You can inspect headers, see error messages, and click the **Replay** button to test the same request again.

---

## Good Things to Know (Gotchas)

- **The URL changes every time you restart:** On the free plan, each time you close and reopen Ngrok, you get a new random web address.
- **The Free Warning Banner:** When someone opens the link in a browser, Ngrok displays a blue warning page asking them to click "Visit Site". This is normal on the free plan to prevent abuse.
