import os
import glob
import pandas as pd
from pathlib import Path

def check_csv_files():
    """
    Check for CSV files in the current directory and provide information about them.
    """
    current_dir = os.getcwd()
    print(f"Checking for CSV files in: {current_dir}")
    print("-" * 50)
    
    # Method 1: Using glob to find CSV files
    csv_files = glob.glob("*.csv")
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return
    
    print(f"Found {len(csv_files)} CSV file(s):")
    print()
    
    for i, csv_file in enumerate(csv_files, 1):
        file_path = Path(csv_file)
        file_size = file_path.stat().st_size
        
        print(f"{i}. File: {csv_file}")
        print(f"   Size: {file_size} bytes")
        print(f"   Path: {file_path.absolute()}")
        
        # Try to read the CSV and show basic info
        try:
            df = pd.read_csv(csv_file)
            print(f"   Rows: {len(df)}")
            print(f"   Columns: {len(df.columns)}")
            print(f"   Column names: {list(df.columns)}")
            
            # Show first few rows
            print(f"   First few rows:")
            print(df.head().to_string(index=False))
            
        except Exception as e:
            print(f"   Error reading file: {e}")
        
        print("-" * 30)

def check_csv_files_alternative():
    """
    Alternative method using os.listdir() to find CSV files
    """
    print("\nAlternative method - using os.listdir():")
    print("-" * 50)
    
    current_dir = os.getcwd()
    all_files = os.listdir(current_dir)
    csv_files = [f for f in all_files if f.lower().endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found using alternative method.")
        return
    
    print(f"Found {len(csv_files)} CSV file(s):")
    for csv_file in csv_files:
        print(f"  - {csv_file}")

def check_csv_files_with_details():
    """
    Check CSV files with more detailed information
    """
    print("\nDetailed CSV file analysis:")
    print("-" * 50)
    
    csv_files = glob.glob("*.csv")
    
    for csv_file in csv_files:
        print(f"\nAnalyzing: {csv_file}")
        
        try:
            # Read CSV without pandas first to check basic structure
            with open(csv_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f"  Total lines: {len(lines)}")
                if lines:
                    print(f"  First line (header): {lines[0].strip()}")
                    print(f"  Number of data rows: {len(lines) - 1}")
            
            # Now use pandas for detailed analysis
            df = pd.read_csv(csv_file)
            print(f"  DataFrame shape: {df.shape}")
            print(f"  Data types:")
            for col, dtype in df.dtypes.items():
                print(f"    {col}: {dtype}")
            
            # Check for missing values
            missing_values = df.isnull().sum()
            if missing_values.sum() > 0:
                print(f"  Missing values:")
                for col, missing in missing_values.items():
                    if missing > 0:
                        print(f"    {col}: {missing}")
            else:
                print(f"  No missing values found")
                
        except Exception as e:
            print(f"  Error analyzing file: {e}")

if __name__ == "__main__":
    # Main check
    check_csv_files()
    
    # Alternative method
    check_csv_files_alternative()
    
    # Detailed analysis
    check_csv_files_with_details() 