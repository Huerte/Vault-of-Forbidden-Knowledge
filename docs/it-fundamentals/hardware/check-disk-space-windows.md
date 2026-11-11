[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

| Field | Value |
|---|---|
| **Title** | Check Free Disk Space and Storage Usage on Windows |
| **Section** | docs |
| **Category** | it-fundamentals/hardware |
| **Difficulty** | Beginner |
| **Last verified** | 2026-11-10 |
| **Prerequisites** | Windows 10 or 11 PC |
| **Has screenshots** | No |

# Check Free Disk Space and Storage Usage on Windows

## Overview
When your computer runs low on storage, system updates may fail, applications slow down, and virtual memory runs out. This guide explains how to check your available disk space, identify what files and programs are taking up the most room, and safely clean up unneeded data.

## Before You Start
- Close unnecessary open programs so temporary locks on cache files are released.
- Ensure you have standard user or administrator access on your Windows machine.

## Steps

### 1. Check Total and Free Space at a Glance
The fastest way to see the overall capacity of your drives:

1. Press `Windows Key + E` to open File Explorer.
2. Click **This PC** in the left sidebar.
3. Look at the **Devices and drives** section. Each drive displays a visual bar with free space (for example: `42.5 GB free of 475 GB`).

*(PowerShell Alternative)*:
Run this quick command to view free and used space across all drives:
```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{N="Used (GB)";E={[math]::Round($_.Used/1GB,2)}}, @{N="Free (GB)";E={[math]::Round($_.Free/1GB,2)}}
```

### 2. Inspect What Is Taking Up Space
Windows has built-in storage intelligence that categorizes disk consumption.

1. Press `Windows Key + I` to open **Settings**.
2. Navigate to **System** > **Storage** (or press `Windows Key + R`, type `ms-settings:storagesense`, and press `Enter`).
3. Under your main system drive (`C:`), Windows displays a categorized breakdown:
   - **Installed apps**: Games, development tools, and software.
   - **Temporary files**: Downloaded installation packages, recycle bin items, and crash logs.
   - **Other / Documents / Videos**: Personal user files and media.
4. Click on **Installed apps** or **Temporary files** to inspect the largest consumers sorted by size.

### 3. Safely Clean Up Disk Space
Free up several gigabytes without breaking your applications or deleting personal files:

1. In the **Storage** settings window, click on **Temporary files**.
2. Review the list of safe-to-delete categories:
   - **Recycle Bin**: Deleted files you no longer need.
   - **Windows Update Cleanup**: Previous version files kept for rollback after updates.
   - **Thumbnails & Temporary Internet Files**: Automatically regenerated caches.
3. Keep **Downloads** unchecked unless you have backed up any files in your user Downloads folder.
4. Click **Remove files**.

*(Automated Cleanup with Disk Cleanup)*:
You can also launch the classic Disk Cleanup utility:
```cmd
cleanmgr.exe
```
Select drive `C:`, check the temporary items you want to clean, and click **OK**.

## Verification
Confirm that free space has increased:

1. Return to File Explorer (`This PC`) or re-open **System** > **Storage**.
2. Confirm the available free space has increased.

## Common Errors
- `The drive bar in File Explorer is highlighted in red.` -> The drive has less than 10% free space remaining. Windows requires at least 10–15 GB of free space on `C:` to operate smoothly and install updates. Run the Temporary files cleanup or uninstall large unused apps.
- `Disk Cleanup does not remove Windows Update files.` -> You need administrator elevation to purge old update backups. In Disk Cleanup, click **Clean up system files**, wait for it to rescan, select **Windows Update Cleanup**, and click **OK**.
