[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | How to Find and Fix Internet Connection Problems on Windows |
| **Section** | docs |
| **Category** | it-fundamentals/networking |
| **Difficulty** | Beginner |
| **Last verified** | 2026-08-11 |
| **Prerequisites** | A Windows computer |
| **Has screenshots** | No |

---

# How to Find and Fix Internet Connection Problems on Windows

## Overview

When your computer cannot open websites, the problem can be in many places: your computer itself, your cable or Wi-Fi, your home router box, or your internet provider.

This guide gives you a step-by-step test list. You will run simple checks one by one to find the exact broken step and fix it.

---

## Key Terms Explained Simply

- **Command Prompt (CMD)**: A black window on Windows where you type text commands to talk directly to your computer.
- **Ping**: A test message your computer sends to another machine. If the other machine sends a reply back, the connection works.
- **Router / Gateway**: The box in your home with blinking lights that connects your devices to the internet.
- **IP Address**: The number address given to each device (like a phone number for your computer).
- **DNS**: The phonebook of the internet. It turns website names like `google.com` into numbers your computer understands.

---

## Before You Start: Open Command Prompt as Administrator

1. Press the **Windows Key** on your keyboard.
2. Type: `cmd`
3. Right-click on **Command Prompt** in the search list and click **Run as administrator**.
4. If a box pops up asking "Do you want to allow this app to make changes?", click **Yes**.
5. A black window opens with white text. You will type the commands from each step into this window.

---

## Steps

---

### Step 1: Check if Your Computer's Network Card Works

**Why:** Before checking the router or internet, test if the network chip inside your computer is alive.

1. In the black window, type this exact text:

   ```cmd
   ping 127.0.0.1
   ```

2. Press **Enter** on your keyboard.

3. Look at the text that appears:
   - **Good result:** You see 4 lines that say `Reply from 127.0.0.1: bytes=32 time<1ms`. At the bottom it says `Lost = 0 (0% loss)`. This means your computer hardware is working fine. Move to Step 2.
   - **Bad result:** It says `General failure` or `Destination host unreachable`. This means your computer network driver is turned off or broken. Restart your computer. If it still fails, reinstall your Wi-Fi or Ethernet driver.

---

### Step 2: Find Your Router's Address

**Why:** You need to know the number of your router box so you can test if your computer can talk to it.

1. In the black window, type:

   ```cmd
   ipconfig
   ```

2. Press **Enter**.

3. Scroll through the text and look for these lines:
   - **IPv4 Address**: This is your computer's address (example: `192.168.1.15`).
     > Note: If this number starts with `169.254.`, your computer is not getting an address from your router. Skip directly to Step 6 (Reset Network).
   - **Default Gateway**: This is your router box address (example: `192.168.1.1` or `192.168.0.1`). Write this number down.

---

### Step 3: Test the Connection to Your Router Box

**Why:** Check if your Wi-Fi signal or network cable is working between your PC and your router.

1. Type `ping` followed by a space, then the **Default Gateway** number you found in Step 2:

   ```cmd
   ping 192.168.1.1
   ```
   *(Replace `192.168.1.1` with your actual Default Gateway number).*

2. Press **Enter**.

3. Look at the result:
   - **Good result:** You see 4 lines saying `Reply from ...` with `0% loss`. Your computer can talk to your router box without problems. Move to Step 4.
   - **Bad result:** You see `Request timed out` or `Destination host unreachable`. Your computer cannot reach the router box.
     - If using Wi-Fi: Disconnect from Wi-Fi, turn Wi-Fi off and on, and reconnect.
     - If using a cable: Unplug the network cable from both the PC and the router, then plug it back in firmly until it clicks.

---

### Step 4: Test if the Internet Outside Your Home Works

**Why:** Check if your router is connected to the outside world, without testing website names yet.

1. In the black window, type:

   ```cmd
   ping 8.8.8.8
   ```

   *(Note: `8.8.8.8` is a public server run by Google that is always online).*

2. Press **Enter**.

3. Look at the result:
   - **Good result:** You see `Reply from 8.8.8.8: ... 0% loss`. You have real internet access. Move to Step 5.
   - **Bad result:** You see `Request timed out`. Your router cannot reach the internet. Unplug the power cable of your home router box, wait 30 seconds, and plug it back in. Wait 2 minutes for all lights to turn green.

---

### Step 5: Test if Website Names (DNS) Can Open

**Why:** If Step 4 worked but you still cannot open websites in your browser, your computer cannot translate names like `google.com` into numbers.

1. In the black window, type:

   ```cmd
   nslookup google.com
   ```

2. Press **Enter**.

3. Look at the result:
   - **Good result:** It shows `Name: google.com` and gives `Addresses:` below it. DNS is working normally.
   - **Bad result:** It says `DNS request timed out` or `Server failed`. Your DNS server is blocked or offline.

   **How to fix DNS:**
   - Press `Win + R`, type `ncpa.cpl`, and press **Enter**.
   - Right-click your active Wi-Fi or Ethernet connection and click **Properties**.
   - Click on **Internet Protocol Version 4 (TCP/IPv4)** to highlight it, then click **Properties**.
   - Click the circle for **Use the following DNS server addresses**.
   - In Preferred DNS server, type: `1.1.1.1` (Cloudflare).
   - In Alternate DNS server, type: `8.8.8.8` (Google).
   - Click **OK**, then click **Close**.

---

### Step 6: Full Network Reset Command List

**Why:** If your connection is still broken or frozen, this sequence cleans out all cached data and restarts the Windows network system.

Type these 5 commands into the black window one by one, pressing **Enter** after each:

```cmd
ipconfig /release
```
*(Tells the router to release your old address).*

```cmd
ipconfig /renew
```
*(Asks the router for a fresh new address. Wait 5 seconds for this to finish).*

```cmd
ipconfig /flushdns
```
*(Cleans out old corrupted website cache).*

```cmd
netsh winsock reset
```
*(Resets the internal Windows connection manager).*

```cmd
netsh int ip reset
```
*(Resets the TCP/IP network rules to factory default).*

After running all 5 commands, **restart your computer**.

---

## Verification: How to Check Everything Works

1. Open your web browser (Chrome, Edge, or Firefox).
2. Go to `https://www.google.com` and search for anything.
3. If the search results load quickly, your internet connection is fully fixed.

---

## Quick Summary Table

| What Step Failed | What It Means | What to Do |
|---|---|---|
| Step 1 (`ping 127.0.0.1`) | PC network card is broken or disabled | Restart PC or update network drivers |
| Step 2 gives `169.254.x.x` | Router refused to give your PC an IP | Run Step 6 reset commands or restart router |
| Step 3 (Ping Default Gateway) | PC cannot talk to your home router | Check Wi-Fi password or replug Ethernet cable |
| Step 4 (`ping 8.8.8.8`) | Router has no internet from provider (ISP) | Unplug router power for 30 seconds, call ISP if still red |
| Step 5 (`nslookup google.com`) | DNS cannot translate website names | Change DNS to `1.1.1.1` and `8.8.8.8` in network settings |
