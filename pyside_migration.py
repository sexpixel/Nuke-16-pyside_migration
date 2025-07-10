#!/usr/bin/env python3
"""
PySide2 to PySide6 Migration Script for Nuke
Automatically updates import statements and references in Python files.
"""

import os
import re
import shutil
from pathlib import Path

def backup_file(file_path):
    """Create a backup of the original file"""
    backup_path = str(file_path) + '.bak'
    shutil.copy2(file_path, backup_path)
    return backup_path

def update_pyside_references(content):
    """Update PySide2 references to PySide6 in file content"""
    
    # Dictionary of replacements
    replacements = {
        # Import statements
        r'from PySide2': 'from PySide6',
        r'import PySide2': 'import PySide6',
        
        # Direct references
        r'PySide2\.': 'PySide6.',
        r'PySide2\b': 'PySide6',
        
        # Common module imports
        r'from PySide2\.QtCore': 'from PySide6.QtCore',
        r'from PySide2\.QtGui': 'from PySide6.QtGui',
        r'from PySide2\.QtWidgets': 'from PySide6.QtWidgets',
        r'from PySide2\.QtNetwork': 'from PySide6.QtNetwork',
        r'from PySide2\.QtOpenGL': 'from PySide6.QtOpenGL',
        r'from PySide2\.QtSql': 'from PySide6.QtSql',
        r'from PySide2\.QtSvg': 'from PySide6.QtSvg',
        r'from PySide2\.QtXml': 'from PySide6.QtXml',
        
        # Multi-line imports
        r'from PySide2\.QtCore\s+import': 'from PySide6.QtCore import',
        r'from PySide2\.QtGui\s+import': 'from PySide6.QtGui import',
        r'from PySide2\.QtWidgets\s+import': 'from PySide6.QtWidgets import',
    }
    
    updated_content = content
    changes_made = False
    
    for pattern, replacement in replacements.items():
        if re.search(pattern, updated_content):
            updated_content = re.sub(pattern, replacement, updated_content)
            changes_made = True
    
    return updated_content, changes_made

def process_python_file(file_path):
    """Process a single Python file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        updated_content, changes_made = update_pyside_references(content)
        
        if changes_made:
            # Create backup
            backup_path = backup_file(file_path)
            
            # Write updated content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            return True, backup_path
        
        return False, None
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False, None

def find_nuke_folder():
    """Find the .nuke folder in common locations"""
    home = Path.home()
    possible_paths = [
        home / '.nuke',
        home / 'Documents' / '.nuke',
        home / 'AppData' / 'Roaming' / '.nuke',  # Windows
    ]
    
    for path in possible_paths:
        if path.exists():
            return path
    
    return None

def main():
    print("PySide2 to PySide6 Migration Script for Nuke")
    print("=" * 50)
    
    # Find .nuke folder
    nuke_folder = find_nuke_folder()
    if not nuke_folder:
        print("Could not find .nuke folder automatically.")
        nuke_path = input("Please enter the path to your .nuke folder: ")
        nuke_folder = Path(nuke_path)
        
        if not nuke_folder.exists():
            print(f"Error: {nuke_folder} does not exist.")
            return
    
    print(f"Using .nuke folder: {nuke_folder}")
    
    # Confirm before proceeding
    confirm = input("\nThis will modify Python files in your .nuke folder. Continue? (y/n): ")
    if confirm.lower() != 'y':
        print("Operation cancelled.")
        return
    
    # Find all Python files
    python_files = list(nuke_folder.rglob('*.py'))
    
    if not python_files:
        print("No Python files found in the .nuke folder.")
        return
    
    print(f"\nFound {len(python_files)} Python files.")
    
    # Process files
    updated_files = []
    backup_files = []
    
    for py_file in python_files:
        print(f"Processing: {py_file.name}")
        was_updated, backup_path = process_python_file(py_file)
        
        if was_updated:
            updated_files.append(py_file)
            backup_files.append(backup_path)
    
    # Summary
    print("\n" + "=" * 50)
    print("MIGRATION COMPLETE")
    print("=" * 50)
    print(f"Files processed: {len(python_files)}")
    print(f"Files updated: {len(updated_files)}")
    print(f"Backup files created: {len(backup_files)}")
    
    if updated_files:
        print("\nUpdated files:")
        for file in updated_files:
            print(f"  - {file.name}")
        
        print("\nBackup files created (in case you need to revert):")
        for backup in backup_files:
            print(f"  - {backup}")
        
        print("\nNOTE: Test your Nuke installation after this migration.")
        print("If you encounter issues, you can restore from the .bak files.")
    else:
        print("\nNo files needed updating - all PySide references are already up to date!")

if __name__ == "__main__":
    main()