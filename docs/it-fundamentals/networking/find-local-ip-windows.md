[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

---

| Field | Value |
|---|---|
| **Title** | Find Your Local IP Address on Windows |
| **Section** | docs |
| **Category** | it-fundamentals/networking |
| **Difficulty** | Beginner |
| **Last verified** | 2026-10-15 |
| **Prerequisites** | A Windows PC |
| **Has screenshots** | No |

---

# Find Your Local IP Address on Windows

## Overview
Your local (private) IPv4 address identifies your PC on your home or office network. You need it for things like file sharing, remote desktop, port forwarding, or telling a colleague which machine to connect to.

## Before You Start
- A Windows 10 or 11 PC connected to a network.

## Steps

### 1. Open Command Prompt
Press `Win + R`, type `cmd`, and press Enter.

### 2. Run `ipconfig`
At the prompt, type:

```bat
ipconfig
```

Press Enter. Windows prints one section per network adapter.

### 3. Find the IPv4 address
Look for the line starting with `IPv4 Address` under the adapter you are using:

- **Wi-Fi**: the section titled `Wireless LAN adapter Wi-Fi`
- **Ethernet cable**: the section titled `Ethernet adapter Ethernet`

The address looks like `192.168.1.42` (or `10.0.x.x` / `172.16.x.x`). That is your local IP.

> Tip: if the output scrolls past, run `ipconfig | more` to page through it, or `ipconfig > %USERPROFILE%\Desktop\ip.txt` to save it to your desktop.

## Verify It Worked
The address is in one of the private ranges (`192.168.x.x`, `10.x.x.x`, `172.16–31.x.x`). An address starting with `169.254` means the adapter did not get an address from the network — reconnect or check the router.

## Common Issues
- **Multiple adapters, many addresses**: use the one in the section of the connection you actually use; ignore `Media disconnected` sections.
- **Want the public IP instead**: that is your router's address as seen from the internet — search "what is my IP" in a browser, or run `curl ifconfig.me` in PowerShell.

## See Also
- `ipconfig /all` shows DNS servers and the MAC address too.
