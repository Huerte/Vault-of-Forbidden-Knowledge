[← Back to README](../../../README.md) | [Contributing Guide](../../../CONTRIBUTING.md)

| Field | Value |
|---|---|
| **Title** | Create a Windows Restore Point |
| **Section** | docs |
| **Category** | it-fundamentals/operating-systems |
| **Difficulty** | Beginner |
| **Last verified** | 2026-11-10 |
| **Prerequisites** | Windows 10 or 11 PC, Administrator account |
| **Has screenshots** | No |

# Create a Windows Restore Point

## Overview
A System Restore Point creates a saved snapshot of essential Windows system files, registry settings, and installed drivers. If an update, software installation, or system configuration change causes crashes or instability, you can roll back your system to this snapshot without losing personal files.

## Before You Start
- Make sure you are logged in as an Administrator.
- Save open work before proceeding.

## Steps

### 1. Enable System Protection
System Protection must be enabled on your Windows system drive (usually `C:`) before restore points can be saved.

1. Press `Windows Key + R`, type `SystemPropertiesProtection.exe`, and press `Enter`.
2. Under **Protection Settings**, select your system drive (`C:`) and click **Configure...**.
3. Select **Turn on system protection**.
4. Adjust the **Max Usage** slider (3% to 5% or about 5–10 GB is recommended).
5. Click **Apply**, then **OK**.

### 2. Create a Manual Restore Point
Once System Protection is turned on, create a snapshot before installing new drivers or editing system configurations.

1. In the **System Properties** window (on the **System Protection** tab), click **Create...**.
2. Type a clear descriptive name for the snapshot (for example: `Before Registry Edit` or `Before GPU Driver Update`). The current date and time are added automatically.
3. Click **Create**.
4. Wait a few moments until Windows shows: `The restore point was created successfully.`
5. Click **Close**, then **OK**.

*(PowerShell Alternative)*:
You can also create a restore point in an elevated PowerShell terminal (Run as Administrator):
```powershell
Checkpoint-Computer -Description "ManualRestorePoint" -RestorePointType "MODIFY_SETTINGS"
```

### 3. How to Roll Back Using System Restore
If your computer experiences issues later, use System Restore to roll back to your saved snapshot.

1. Press `Windows Key + R`, type `rstrui.exe`, and press `Enter` to open the System Restore wizard.
2. Click **Next**.
3. Choose the restore point you created from the list.
4. *(Optional)* Click **Scan for affected programs** to see which apps or drivers installed after the snapshot will be removed.
5. Click **Next**, review the restore details, and click **Finish**.
6. Windows will restart and restore system files to the selected point.

## Verification
To confirm that your restore point is saved and available:

1. Press `Windows Key + R`, type `rstrui.exe`, and press `Enter`.
2. Click **Next**; your newly created restore point should appear in the list with the exact description and timestamp you entered.
3. Click **Cancel** to close the wizard without rolling back.

## Common Errors
- `System Restore is turned off by your system administrator.` -> Group Policy or corporate management has locked System Protection. Run `gpedit.msc` and navigate to Computer Configuration > Administrative Templates > System > System Restore to enable it.
- `The restore point could not be created for the following reason: The specified object was not found. (0x80042306)` -> The Volume Shadow Copy service (VSS) is disabled. Press `Windows Key + R`, run `services.msc`, find **Volume Shadow Copy**, set its Startup Type to **Manual**, and start the service.
