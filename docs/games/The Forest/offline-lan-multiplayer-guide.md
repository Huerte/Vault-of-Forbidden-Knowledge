[← Back to README](../../README.md) | [Contributing Guide](../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Set Up Offline LAN Multiplayer in The Forest |
| **Section** | docs / games |
| **Category** | The Forest |
| **Difficulty** | Beginner |
| **Last Verified** | 2026-07-20 |
| **Prerequisites** | 2 Windows PCs with Steam installed, The Forest installed on both, 1 Smartphone with Mobile Hotspot |
| **Has Screenshots** | Yes (Placeholders) |

---

# Set Up Offline LAN Multiplayer in *The Forest*

## Overview

This guide walks you through playing *The Forest* together on two Windows computers using only your phone as a Wi-Fi hotspot. No active internet connection is needed once setup is complete.

Read each step in order. Do not skip phases. Every step includes a note on what you should see when it works correctly.

---

## Key Terms

- **HOST PC** — The computer that creates and runs the game world. This is where the server runs.
- **CLIENT PC** — The computer that connects to and joins the game world.
- **Dedicated Server** — A separate program (not the game itself) downloaded through Steam that manages the multiplayer session.
- **Hotspot** — Your phone acting as a Wi-Fi router so both computers can talk to each other without using the internet.

---

## Before You Start

Check all of these before proceeding:

- Both computers have **Steam** installed and are logged in.
- **The Forest** is installed and playable on both computers.
- You have a smartphone that can create a **Wi-Fi hotspot**.
- The **HOST PC** is connected to the internet right now (required for Phase 1 only).

> If any of the above are not met, resolve them before continuing. You only need internet for Phase 1. Everything after that runs offline.

---

# Steps

---

## Phase 1: Download Server Files (HOST PC Only — Internet Required)

**Who does this:** HOST PC only.  
**Why:** You need to download a separate program called "The Forest Dedicated Server" through Steam before going offline. This only needs to happen once.

1. Make sure the **HOST PC** is connected to the internet.

2. Open **Steam**.

3. Click **Library** at the top of the Steam window.

4. Look for a dropdown near the search bar that says **Games**. Click it.

5. A checklist appears. Find **Tools** and check the box next to it.

   ![Steam Library filter showing Tools checkbox checked](/assets/images/docs/games/the-forest/offline-lan-multiplayer-guide/01-steam-tools-filter.png)

   > **Expected result:** Your library now shows additional items alongside your games, including server tools.

6. In the search bar, type: `The Forest Dedicated Server`

7. When it appears in the list, click **Install** and wait for it to finish downloading.

   > **Expected result:** After installation, "The Forest Dedicated Server" appears in your Steam Library just like a game. You do not need to launch it yet.

---

## Phase 2: Switch Steam to Offline Mode (Both PCs)

**Who does this:** Both HOST PC and CLIENT PC. Do this on one computer, then switch to the other and repeat.  
**Why:** This stops Steam from trying to reach the internet during gameplay, which would cause errors when no internet is available.

1. Open **Steam** on the computer you are working on.

2. At the very top-left corner, click the word **Steam**.

3. In the dropdown menu that appears, click **Go Offline...**

   ![Steam menu showing Go Offline option](/assets/images/docs/games/the-forest/offline-lan-multiplayer-guide/03-steam-go-offline.png)

4. A confirmation box appears. Click **Restart in Offline Mode**.

   > **Expected result:** Steam closes and reopens. It now shows a banner or label saying it is in Offline Mode. You will not be able to browse the store or access friends until you go back online.

5. Switch to the **other computer** and repeat steps 1 through 4.

---

## Phase 3: Connect Both Computers to the Mobile Hotspot (Both PCs)

**Who does this:** Both HOST PC and CLIENT PC, plus the person with the phone.  
**Why:** The phone hotspot acts as a local Wi-Fi router so both computers can find each other. The internet is not used at all.

1. On your **smartphone**, open Settings and turn on **Mobile Hotspot** (sometimes called "Personal Hotspot" or "Tethering" depending on the phone).

2. Still on the smartphone, turn **OFF Cellular Data** (also called Mobile Data).

   > **Why turn off mobile data?** If mobile data stays on, the hotspot starts routing traffic through the internet, which causes disconnections during gameplay. The hotspot only needs to create a local wireless network, not provide internet.

   > **Expected result:** Your phone's hotspot Wi-Fi is on, but the phone itself shows no internet access.

3. On the **HOST PC**, click the Wi-Fi icon in the taskbar and connect to the hotspot network.

4. On the **CLIENT PC**, do the same — click the Wi-Fi icon and connect to the same hotspot network.

   > **Expected result:** Both computers show they are connected to the hotspot Wi-Fi. Neither one needs internet access from this point forward.

---

## Phase 4: Temporarily Disable Windows Firewall (Both PCs)

**Who does this:** Both HOST PC and CLIENT PC. Do this on one computer, then switch to the other and repeat.  
**Why:** Windows Firewall often blocks local network connections between the game and the server. Disabling it temporarily ensures both computers can communicate.

> **Safety note:** Only disable the firewall while playing this game on your private hotspot. Re-enable it after you finish playing. Instructions are in the "After You're Done Playing" section.

1. Click the **Windows Start button** and type: `Windows Defender Firewall`

2. Click the result that appears at the top.

3. On the left side of the window that opens, click **Turn Windows Defender Firewall on or off**.

   ![Windows Defender Firewall main window highlighting turn on or off link](/assets/images/docs/games/the-forest/offline-lan-multiplayer-guide/08-firewall-settings-menu.png)

4. Under **Private network settings**, select **Turn off Windows Defender Firewall (not recommended)**.

5. Under **Public network settings**, select **Turn off Windows Defender Firewall (not recommended)**.

   ![Firewall options setting both Private and Public to turned off](/assets/images/docs/games/the-forest/offline-lan-multiplayer-guide/09-firewall-turn-off.png)

6. Click **OK**.

   > **Expected result:** The Firewall window now shows that the firewall is off for both Private and Public networks. A red shield icon may appear — this is expected.

7. Switch to the **other computer** and repeat steps 1 through 6.

---

## Phase 5: Prepare Server Files (HOST PC Only)

**Who does this:** HOST PC only.  
**Why:** The server program needs to be told which game it belongs to. By default, it contains the wrong ID, which causes it to fail when launching.

1. Open **Steam**.

2. Click **Library** at the top.

3. Click the **Games** dropdown near the search bar and make sure **Tools** is checked. (This is the same step from Phase 1. If you already see "The Forest Dedicated Server" in your list, Tools is already enabled — skip to step 4.)

4. Find **The Forest Dedicated Server** in your library and right-click it.

5. In the menu that appears, hover over **Manage**, then click **Browse Local Files**.

   ![Right-click context menu on Steam showing Manage then Browse local files](/assets/images/docs/games/the-forest/offline-lan-multiplayer-guide/10-browse-local-files.png)

   > **Expected result:** A File Explorer window opens showing a folder full of server files.

6. In that folder, find the file named:

   ```
   steam_appid.txt
   ```

   > **Note:** Windows sometimes hides file extensions like `.txt`. If you see a file called `steam_appid` without the `.txt` part, that is the same file.

7. Right-click `steam_appid.txt`, hover over **Open with**, and click **Notepad**.

   > If you don't see Notepad in the list, click **Choose another app**, then select **Notepad** from there.

8. Delete everything inside the file and type only:

   ```
   242760
   ```

   ![Notepad editing steam_appid.txt with value 242760](/assets/images/docs/games/the-forest/offline-lan-multiplayer-guide/11-edit-steam-appid.png)

9. Save the file by pressing **Ctrl + S**, then close Notepad.

   > **Expected result:** The file now contains only the number `242760` with no extra spaces or blank lines.

10. Back in the File Explorer window, find and double-click:

    ```
    TheForestDedicatedServer.exe
    ```

    > This launches the server program for the first time to generate its settings files. It is not the game itself — you will not see anything playable.

11. A black console window opens and fills with text. **Do not close it.** Let it run for about **30 seconds**.

12. After 30 seconds, close it by clicking the **X** in the top-right corner of the console window.

    > **Expected result:** The console window opened, printed text for about 30 seconds, and then you closed it. This is correct. It has now created the configuration folder needed for the next phase.

---

## Phase 6: Edit Server Configuration (HOST PC Only)

**Who does this:** HOST PC only.  
**Why:** You need to tell the server which IP address to listen on. Setting it to `0.0.0.0` means "accept connections from any network adapter," which is required for the hotspot to work.

1. Press the **Windows key** and the **R key** at the same time. The Run box appears in the bottom-left corner of your screen.

2. Click inside the Run box and paste the following path exactly:

   ```
   %localappdata%low\SKS\TheForestDedicatedServer\ds
   ```

   > **Tip:** You can select the text above, copy it with **Ctrl + C**, click inside the Run box, and paste it with **Ctrl + V**.

3. Press **Enter**. A File Explorer window opens.

   > **Expected result:** You see a folder with several files inside, including one named `Server.cfg`. If this folder does not open, go back to Phase 5 and make sure the server ran for the full 30 seconds.

4. Find the file named `Server.cfg` in that folder.

5. Right-click `Server.cfg`, hover over **Open with**, and click **Notepad**.

   > If you don't see Notepad listed, click **Choose another app** and select Notepad from there.

6. Inside the file, scroll through and look for the line that starts with:

   ```
   serverIP
   ```

7. Change that entire line so it reads exactly:

   ```
   serverIP 0.0.0.0
   ```

   > **Important:** Do NOT add a port number or any other value after `0.0.0.0`.
   >
   > | Incorrect | Correct |
   > |---|---|
   > | `serverIP 0.0.0.0:27015` | `serverIP 0.0.0.0` |
   > | `serverIP 192.168.43.15` | `serverIP 0.0.0.0` |
   >
   > Adding a port number or a specific IP address here causes the error: `Error: You configure a invalid ip address`. The value `0.0.0.0` tells the server to accept connections from any network adapter automatically.

8. Save the file by pressing **Ctrl + S**, then close Notepad.

   > **Expected result:** The `serverIP` line in `Server.cfg` now reads exactly `serverIP 0.0.0.0`.

---

## Phase 7: Create a Server Shortcut (HOST PC Only)

**Who does this:** HOST PC only.  
**Why:** You need to launch the server with specific settings every time. A shortcut that already has those settings saves you from doing it manually each session.

1. Go back to the Dedicated Server installation folder. To open it again:
   - Open **Steam** → **Library** → right-click **The Forest Dedicated Server** → **Manage** → **Browse Local Files**.

2. In that folder, find the file:

   ```
   TheForestDedicatedServer.exe
   ```

3. Right-click it.

4. In the menu:
   - **On Windows 10:** Look for **Send to** in the menu.
   - **On Windows 11:** Click **Show more options** first, then look for **Send to**.

5. Hover over **Send to** and click **Desktop (create shortcut)**.

   > **Expected result:** A new shortcut icon appears on your Desktop, likely named `TheForestDedicatedServer.exe - Shortcut`.

6. Go to your **Desktop**. Right-click the new shortcut and click **Properties**.

7. In the Properties window, find the field labeled **Target**.

8. Click once inside the **Target** field to place your cursor there. Press the **End** key to jump to the very end of the text.

9. The text already ends with a closing quote mark (`"`). After that closing quote, type a space, then type:

   ```
   -nosteamclient -showlogs
   ```

   The full Target field should look like this when you're done:

   ```
   "C:\...\TheForestDedicatedServer.exe" -nosteamclient -showlogs
   ```

   > **Note:** The path inside the quotes (`C:\...`) is your actual installation path and will look different on your PC. You are only adding the text after the closing quote.

10. Click **Apply**, then click **OK**.

    > **Expected result:** The shortcut is now configured. Every time you launch the server using this shortcut, it will start with the correct settings automatically.

---

## Phase 8: Start the Server and Join the Game

### A. Launch the Dedicated Server (HOST PC)

**Who does this:** HOST PC only.

1. On the Desktop, find the shortcut you created in Phase 7.

2. Right-click it.

3. Click **Run as administrator**.

   > **Why run as administrator?** The server needs elevated permission to accept local network connections. Without it, the server may fail silently or players won't be able to connect.

   > If a User Account Control (UAC) box appears asking "Do you want to allow this app to make changes?" click **Yes**.

4. A black console window opens and starts printing lines of text. Do not close it. Leave it running in the background.

   > **Expected result:** After 10 to 30 seconds the text slows down and the server is running. The console window stays open on its own. This is correct.

---

### B. Join the Server (HOST PC and CLIENT PC)

**Who does this:** Both computers.

1. Open **The Forest** through Steam on the computer you are on. Launch it the same way you normally play the game.

2. On the main menu, click **Multiplayer**.

3. Click **Join Game**.

4. At the top of the screen, click the **Dedicated (LAN)** tab.

5. Wait a few seconds. Your server should appear in the list by the name set in `Server.cfg`.

6. Click on your server to select it.

7. Click **Join**.

   > **Expected result:** The game loads into the world. Both players appear in the same game session at the same time.

   > **Tip:** If the server does not appear in the list, wait 10 to 15 seconds and check again. If it still does not appear after 30 seconds, go to the troubleshooting section below.

8. Switch to the **other computer** and repeat steps 1 through 7.

---

# Verification

You have successfully set up offline LAN multiplayer when all of the following are true:

- Both players are in the same game world at the same time.
- Neither computer is connected to the internet.
- The server console window on the HOST PC stays open on its own without closing itself.

---

# Common Errors and Troubleshooting

Use this section only when something goes wrong. Find the error description that matches your situation and follow the fix steps.

---

## Error: "You configure a invalid ip address"

### What it looks like

The server console window shows:

```
Error: You configure a invalid ip address: 10.x.x.x:27015
```

Followed by repeated lines saying `Failed to connect to Steam`.

### Why it happens

The `serverIP` line in `Server.cfg` contains either a port number appended to the address (e.g., `:27015`) or a specific IP address instead of `0.0.0.0`.

### How to fix it

1. Press **Windows + R** to open the Run box.
2. Paste this path: `%localappdata%low\SKS\TheForestDedicatedServer\ds`
3. Press **Enter**.
4. Right-click `Server.cfg`, hover over **Open with**, and click **Notepad**.
5. Find the `serverIP` line and change it to read exactly:

   ```
   serverIP 0.0.0.0
   ```

6. Press **Ctrl + S** to save, then close Notepad.
7. Close the server console window if it is still open.
8. Right-click the server shortcut on your Desktop and click **Run as administrator**.

> **Expected result after fix:** The server starts and the console window stays open without the error message.

---

## Error: Version Mismatch / "Not Same Patch"

### What it looks like

Players cannot join, or they get kicked immediately after loading in. The screen or the console shows a message about a version mismatch or "not same patch."

### Why it happens

The Dedicated Server program and the game client on your PC are running different versions of the game. They need to be the exact same version to connect.

### How to fix it

1. Connect the **HOST PC** back to the internet temporarily.

2. Open **Steam** and click **Library**.

3. Click the **Games** dropdown and make sure **Tools** is checked so you can see the Dedicated Server.

4. Right-click **The Forest Dedicated Server** and click **Properties**.

5. Click **Installed Files** at the top of the Properties window.

6. Click **Verify integrity of tool files**.

7. Wait for Steam to finish checking and repairing the server files.

   > **Expected result:** Steam downloads any missing or outdated files and the verification completes.

8. Now right-click **The Forest** (the main game, not the server) and click **Properties**.

9. Click **Installed Files**, then click **Verify integrity of game files**.

10. Wait for that to complete as well.

11. Disconnect from the internet again and switch Steam back to **Offline Mode** (Phase 2).

12. Restart the server using the shortcut on your Desktop and try joining again.

> **Expected result after fix:** Players can connect and stay in the game without being kicked.

---

## Error: Server Does Not Appear Under "Dedicated (LAN)"

### What it looks like

After clicking the **Dedicated (LAN)** tab in the join menu, the list is empty or your server never shows up, even after waiting.

### Why it happens

- The server hasn't fully started yet.
- Windows Firewall is still on and blocking the connection.
- One or both computers are not connected to the same hotspot Wi-Fi network.

### How to fix it

Try each of these in order, checking the server list again after each one:

1. **Wait longer.** The server can take up to 60 seconds to appear after launching. Try waiting the full 60 seconds before assuming something is wrong.

2. **Check the Firewall.** Go back to Phase 4 and repeat the steps on both computers. Confirm both Private and Public firewalls are turned off.

3. **Check both computers are on the same Wi-Fi network.**
   - On the **HOST PC**, press **Windows + R**, type `cmd`, and press **Enter**.
   - In the black window, type `ipconfig` and press **Enter**.
   - Find the **IPv4 Address** line. Write down the number (example: `192.168.43.15`).
   - Do the same on the **CLIENT PC**.
   - Compare the two addresses. The first three groups of numbers must match (example: both should start with `192.168.43`). If they don't match, one computer is connected to the wrong Wi-Fi. Disconnect it and reconnect it to the correct hotspot.

4. Close the server console window and relaunch it using **Run as administrator** (right-click the shortcut on the Desktop).

> **Expected result after fix:** The server appears in the Dedicated (LAN) list within 30 to 60 seconds of launching.

---

## Error: Client Disconnects Immediately After Joining

### What it looks like

The CLIENT PC connects and the game starts loading, but then it drops back to the main menu almost immediately.

### Why it happens

- Mobile Data is still turned on on the smartphone, causing the hotspot to route traffic through the internet in a way that breaks the connection.
- The Wi-Fi signal between the phone and one of the computers is too weak.

### How to fix it

1. On your smartphone, confirm that **Mobile Data / Cellular Data is turned OFF**. The hotspot should still be on, but mobile data must be off.

2. Move both computers physically closer to the phone.

3. On both computers, click the Wi-Fi icon in the taskbar and confirm both are connected to the correct hotspot network. If either shows a different network, disconnect and reconnect to the hotspot.

4. Close the server console window on the HOST PC.

5. Right-click the server shortcut on the Desktop and click **Run as administrator**.

6. Once the server is running again, relaunch *The Forest* on the CLIENT PC and try joining again.

> **Expected result after fix:** The CLIENT PC loads into the game world and stays connected.

---

# After You're Done Playing

Do these steps when you finish your session.

1. Exit *The Forest* on both computers.

2. Close the server console window on the **HOST PC**.

3. Re-enable the Windows Firewall on **both computers**:
   - Click the **Windows Start button** and type `Windows Defender Firewall`.
   - Click the result.
   - Click **Turn Windows Defender Firewall on or off** on the left.
   - Select **Turn on Windows Defender Firewall** under both Private and Public settings.
   - Click **OK**.
   - Do this on both the HOST PC and the CLIENT PC.

4. Turn off the **Mobile Hotspot** on your phone.

5. On **both computers**, reconnect to your regular Wi-Fi.

6. On **both computers**, open Steam and click **Steam** (top-left) → **Go Online** to return to normal Steam mode.

> **Next time you want to play:** Start from Phase 2. You do not need to repeat Phase 1 again unless the server files were deleted or you reinstalled Windows.