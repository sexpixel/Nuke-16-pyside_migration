# Nuke-16-pyside_migration
This script will update all of your Pyside2 references to Pyside6. 
This will help python scripts made prior to the release of Nuke 16 to execute correctly.

# PySide Migration Script - Execution Guide

## Prerequisites
- **Close Nuke completely** before running this script
- Make sure you have Python installed on your system
- Ensure you have administrator/write permissions to your .nuke folder

## Step-by-Step Instructions

### Step 1: Save the Script
1. Copy the Python script from the previous message
2. Open a text editor (Notepad++, VS Code, or even regular Notepad)
3. Paste the script code
4. Save the file as `pyside_migration.py` 
   - Choose a location you can easily find (Desktop, Documents, etc.)
   - Make sure the file extension is `.py` (not `.txt`)

### Step 2: Open Command Prompt/Terminal

**Windows:**
1. Press `Win + R` to open Run dialog
2. Type `cmd` and press Enter
3. OR: Press `Win + X` and select "Command Prompt" or "PowerShell"

**Mac:**
1. Press `Cmd + Space` to open Spotlight
2. Type `Terminal` and press Enter

**Linux:**
1. Press `Ctrl + Alt + T`
2. OR: Open your distribution's terminal application

### Step 3: Navigate to Script Location
Use the `cd` command to navigate to where you saved the script:

**Example (Windows):**
```
cd C:\Users\YourUsername\Desktop
```

**Example (Mac/Linux):**
```
cd ~/Desktop
```

### Step 4: Run the Script
Type the following command and press Enter:

```
python pyside_migration.py
```

**If you get a "python not found" error, try:**
```
python3 pyside_migration.py
```

### Step 5: Follow the Script Prompts
1. The script will try to find your .nuke folder automatically
2. If it can't find it, you'll be prompted to enter the path manually
3. **Common .nuke folder locations:**
   - **Windows:** `C:\Users\YourUsername\.nuke`
   - **Mac:** `/Users/YourUsername/.nuke`
   - **Linux:** `/home/yourusername/.nuke`
4. When prompted, type `y` to confirm you want to proceed
5. The script will process all Python files and show progress

### Step 6: Review Results
The script will show you:
- How many files were processed
- Which files were updated
- Where backup files were created

### Step 7: Test Nuke
1. Start Nuke normally
2. Check that it starts without PySide2 errors
3. Test your custom scripts/tools to ensure they work
4. If everything works, you can delete the `.bak` backup files later

## Troubleshooting

### "Python not found" Error
- **Windows:** Install Python from python.org or try `py` instead of `python`
- **Mac:** Try `python3` or install Python via Homebrew
- **Linux:** Install Python via your package manager

### "Permission Denied" Error
- **Windows:** Run Command Prompt as Administrator
- **Mac/Linux:** Try adding `sudo` before the command (use cautiously)

### Script Can't Find .nuke Folder
- Manually locate your .nuke folder in your file explorer
- Copy the full path and paste it when prompted
- Make sure to use forward slashes `/` or escape backslashes `\\` in the path

### If Something Goes Wrong
1. **Don't panic** - the script creates backups
2. Navigate to your .nuke folder
3. Look for files ending in `.bak`
4. Rename them back to `.py` to restore originals
5. Example: rename `my_script.py.bak` back to `my_script.py`

## Alternative: Manual Path Entry
If the automatic detection doesn't work, you can modify the script to use your specific path:

1. Find the line that says: `nuke_folder = find_nuke_folder()`
2. Replace it with: `nuke_folder = Path(r"C:\Users\YourUsername\.nuke")` (use your actual path)
3. Save and run the script

## Final Notes
- Keep the backup files until you're confident everything works
- Some third-party plugins might need separate updates
- Consider running this on a copy of your .nuke folder first if you're nervous
