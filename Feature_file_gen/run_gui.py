#!/usr/bin/env python3
"""
Launcher script for the Feature File Generator GUI
"""

import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from gui_feature_generator import main
    
    print("🚀 Starting Feature File Generator GUI...")
    print("=" * 50)
    print("Instructions:")
    print("1. Select your CSV file (must have 'name', 'hobbies', 'context' columns)")
    print("2. Select your .feature file")
    print("3. Click 'Load Data' to populate the dropdowns")
    print("4. Choose a name keyword from the CSV")
    print("5. Choose a hobby keyword from the CSV")
    print("6. Review the relevant context found")
    print("7. Click 'Add to Feature File' to insert Given statements")
    print("=" * 50)
    
    main()
    
except ImportError as e:
    print(f"❌ Error importing required modules: {e}")
    print("Make sure you have the following packages installed:")
    print("- tkinter (usually comes with Python)")
    print("- pandas")
    print("- pathlib")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    print("Please check that all required files are present in the same directory.") 