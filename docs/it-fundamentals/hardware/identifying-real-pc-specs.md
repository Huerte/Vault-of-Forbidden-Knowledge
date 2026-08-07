# Identifying Real PC Specs

When checking a PC or laptop's specifications, especially when buying second-hand, it is common for the displayed specifications in the basic "System Properties" or "About your PC" screen to be spoofed or edited. 

To find the true hardware specifications and make it much harder to be fooled by a fake system, you can use built-in Windows diagnostic tools.

## 1. Using DirectX Diagnostic Tool (`dxdiag`)

The DirectX Diagnostic Tool provides detailed information about the DirectX components and drivers installed on your system. It is a quick and reliable way to check the CPU, RAM, and GPU.

### How to open:
1. Press `Windows Key + R` to open the Run dialog.
2. Type `dxdiag` and press `Enter`.
3. If a prompt appears asking to check if drivers are digitally signed, click **Yes**.

### What to check:
- **System Tab:** 
  - Check the **Processor** to verify the CPU model and speed.
  - Check the **Memory** to verify the amount of RAM installed.
- **Display Tab(s):** 
  - Check the **Name** under the Device section to verify the Graphics Processing Unit (GPU). If the laptop has both integrated and dedicated graphics, you may see multiple "Display" or "Render" tabs. Check all of them.

## 2. Using System Information (`msinfo32`)

For an even more detailed and robust check that is significantly harder to fake, use the System Information tool. This provides a comprehensive view of the hardware, system components, and software environment.

### How to open:
1. Press `Windows Key + R` to open the Run dialog.
2. Type `msinfo32` and press `Enter`.

### What to check:
- **System Summary:** 
  - **Processor:** Verify the exact CPU model, cores, and logical processors.
  - **Installed Physical Memory (RAM):** Verify the total RAM installed.
  - **BaseBoard Manufacturer/Product:** Check the motherboard details.
  - **System Model:** Verify the exact laptop or pre-built desktop model.
- **Components > Display:** 
  - Detailed information about the graphics card(s), including adapter RAM and driver versions.
- **Components > Storage > Disks:** 
  - Check the actual model, size, and type of the installed hard drives and SSDs.

> **Tip:** If you suspect the specs are still spoofed, booting the PC into the **BIOS/UEFI** is the ultimate way to verify hardware, as the BIOS reads directly from the physical hardware components and cannot be easily faked from within Windows.
