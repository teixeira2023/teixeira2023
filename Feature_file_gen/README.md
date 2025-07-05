# Feature File Generator GUI

A graphical user interface application that helps you generate feature files by selecting relevant context from CSV data.

## Features

- **CSV File Selection**: Choose a CSV file with required columns (name, hobbies, context)
- **Feature File Selection**: Select an existing .feature file to modify
- **Keyword Selection**: Choose keywords from name and hobbies columns
- **Context Matching**: Automatically finds relevant context based on selected keywords
- **Feature File Update**: Adds Given statements to your feature file
- **Real-time Preview**: See the feature file content and changes in real-time

## Requirements

- Python 3.6 or higher
- tkinter (usually comes with Python)
- pandas
- pathlib

## Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Running the GUI

```bash
python run_gui.py
```

Or directly:
```bash
python gui_feature_generator.py
```

### Step-by-Step Instructions

1. **Select CSV File**: Click "Browse" to select your CSV file
   - Must contain columns: `name`, `hobbies`, `context`

2. **Select Feature File**: Click "Browse" to select your .feature file
   - Choose an existing feature file to modify

3. **Load Data**: Click "Load Data" to populate the dropdown menus
   - This will read your CSV and extract available names and hobbies

4. **Choose Keywords**:
   - Select a name keyword from the dropdown
   - Select a hobby keyword from the dropdown
   - The relevant context will be automatically displayed

5. **Add to Feature File**: Click "Add to Feature File" to insert Given statements
   - The application will find the most relevant context
   - Format it as "Given [context]" statements
   - Add them to your feature file

### CSV File Format

Your CSV file should have the following structure:

```csv
name,age,hobbies,context
John,30,"reading, traveling, cooking","John likes reading books; John likes traveling twice a year; John likes cooking for his family"
```

### Example Output

When you select:
- Name keyword: "John"
- Hobby keyword: "reading"

The application will find the relevant context and add:
```gherkin
    Given John likes reading books
```

## File Structure

```
Feature_file_gen/
├── gui_feature_generator.py    # Main GUI application
├── run_gui.py                  # Launcher script
├── create_csv.py              # CSV creation utility
├── check_csv_files.py         # CSV file checker
├── generate_feature.py        # Feature file generator
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── data.csv                   # Sample CSV file
└── data_pandas.csv           # Sample CSV file
```

## Troubleshooting

### Common Issues

1. **"Missing required columns" error**
   - Ensure your CSV has columns named exactly: `name`, `hobbies`, `context`

2. **"No relevant context found"**
   - Check that your selected keywords exist in the CSV data
   - Verify the spelling and case sensitivity

3. **GUI doesn't start**
   - Make sure tkinter is installed: `python -c "import tkinter"`
   - Install pandas: `pip install pandas`

### Error Messages

- **ImportError**: Missing required Python packages
- **FileNotFoundError**: Selected file doesn't exist
- **PermissionError**: No write permission for the feature file

## Contributing

Feel free to modify and improve this application. The main GUI class is in `gui_feature_generator.py`.

## License

This project is open source and available under the MIT License. 