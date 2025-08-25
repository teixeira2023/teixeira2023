import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os
import re
from pathlib import Path

class FeatureGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature File Generator")
        self.root.geometry("800x800")
        
        # Variables
        self.csv_file_path = tk.StringVar()
        self.feature_file_path = tk.StringVar()
        self.selected_name_keyword = tk.StringVar()
        self.selected_hobby_keyword = tk.StringVar()
        self.csv_data = None
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Feature File Generator", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # CSV File Selection
        ttk.Label(main_frame, text="1. Select CSV File:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.csv_file_path, width=50).grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 5))
        ttk.Button(main_frame, text="Browse", command=self.browse_csv_file).grid(row=1, column=2)
        
        # Feature File Selection
        ttk.Label(main_frame, text="2. Select Feature File:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.feature_file_path, width=50).grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(5, 5))
        ttk.Button(main_frame, text="Browse", command=self.browse_feature_file).grid(row=2, column=2)
        
        # Load Data Button
        ttk.Button(main_frame, text="Load Data", command=self.load_data).grid(row=3, column=0, columnspan=3, pady=10)
        
        # Keywords Selection Frame
        keywords_frame = ttk.LabelFrame(main_frame, text="Keyword Selection", padding="10")
        keywords_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        keywords_frame.columnconfigure(1, weight=1)
        
        # Name Keyword Selection
        ttk.Label(keywords_frame, text="3. Select Name Keyword:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.name_combobox = ttk.Combobox(keywords_frame, textvariable=self.selected_name_keyword, state="readonly")
        self.name_combobox.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        
        # Hobby Keyword Selection
        ttk.Label(keywords_frame, text="4. Select Hobby Keyword:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.hobby_combobox = ttk.Combobox(keywords_frame, textvariable=self.selected_hobby_keyword, state="readonly")
        self.hobby_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        
        # Context Preview
        ttk.Label(keywords_frame, text="5. Relevant Context:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.context_text = tk.Text(keywords_frame, height=4, width=50)
        self.context_text.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=(5, 0))
        
        # Add to Feature Button
        ttk.Button(main_frame, text="6. Add to Feature File", command=self.add_to_feature_file).grid(row=5, column=0, columnspan=3, pady=10)
        
        # Status Label
        self.status_label = ttk.Label(main_frame, text="Ready to start", foreground="blue")
        self.status_label.grid(row=6, column=0, columnspan=3, pady=5)
        
        # Preview Frame
        preview_frame = ttk.LabelFrame(main_frame, text="Feature File Preview", padding="10")
        preview_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        preview_frame.columnconfigure(0, weight=1)
        preview_frame.rowconfigure(0, weight=1)
        
        # Preview Text
        self.preview_text = tk.Text(preview_frame, height=10, width=80)
        preview_scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=self.preview_text.yview)
        self.preview_text.configure(yscrollcommand=preview_scrollbar.set)
        
        self.preview_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        preview_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Last Column Content Frame
        last_column_frame = ttk.LabelFrame(main_frame, text="Last Column Content", padding="10")
        last_column_frame.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        last_column_frame.columnconfigure(0, weight=1)
        last_column_frame.rowconfigure(0, weight=1)
        
        # Last Column Text
        self.last_column_text = tk.Text(last_column_frame, height=6, width=80)
        last_column_scrollbar = ttk.Scrollbar(last_column_frame, orient=tk.VERTICAL, command=self.last_column_text.yview)
        self.last_column_text.configure(yscrollcommand=last_column_scrollbar.set)
        
        self.last_column_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        last_column_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Configure main frame row weights
        main_frame.rowconfigure(7, weight=1)
        main_frame.rowconfigure(8, weight=1)
        
    def browse_csv_file(self):
        filename = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if filename:
            self.csv_file_path.set(filename)
            self.status_label.config(text=f"CSV file selected: {os.path.basename(filename)}")
            
    def browse_feature_file(self):
        filename = filedialog.askopenfilename(
            title="Select Feature File",
            filetypes=[("Feature files", "*.feature"), ("All files", "*.*")]
        )
        if filename:
            self.feature_file_path.set(filename)
            self.status_label.config(text=f"Feature file selected: {os.path.basename(filename)}")
            
    def load_data(self):
        if not self.csv_file_path.get():
            messagebox.showerror("Error", "Please select a CSV file first.")
            return
            
        try:
            self.csv_data = pd.read_csv(self.csv_file_path.get())
            
            # Check if required columns exist
            required_columns = ['name', 'hobbies', 'context']
            missing_columns = [col for col in required_columns if col not in self.csv_data.columns]
            
            if missing_columns:
                messagebox.showerror("Error", f"Missing required columns: {missing_columns}")
                return
            
            # Populate name combobox
            names = self.csv_data['name'].unique().tolist()
            self.name_combobox['values'] = names
            if names:
                self.name_combobox.set(names[0])
                
            # Populate hobby combobox
            all_hobbies = []
            for hobbies_str in self.csv_data['hobbies']:
                if pd.notna(hobbies_str):
                    hobbies_list = [h.strip() for h in str(hobbies_str).split(',')]
                    all_hobbies.extend(hobbies_list)
            
            unique_hobbies = list(set(all_hobbies))
            self.hobby_combobox['values'] = unique_hobbies
            if unique_hobbies:
                self.hobby_combobox.set(unique_hobbies[0])
                
            self.status_label.config(text=f"Data loaded successfully. Found {len(self.csv_data)} rows.")
            
            # Load feature file preview
            self.load_feature_preview()
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file: {str(e)}")
            
    def load_feature_preview(self):
        if not self.feature_file_path.get():
            return
            
        try:
            with open(self.feature_file_path.get(), 'r', encoding='utf-8') as f:
                content = f.read()
                self.preview_text.delete(1.0, tk.END)
                self.preview_text.insert(1.0, content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load feature file: {str(e)}")
            
    def find_relevant_context(self):
        if self.csv_data is None:
            return []
            
        name_keyword = self.selected_name_keyword.get()
        hobby_keyword = self.selected_hobby_keyword.get()
        
        if not name_keyword or not hobby_keyword:
            return []
            
        relevant_contexts = []
        
        for _, row in self.csv_data.iterrows():
            name = str(row['name']).lower()
            hobbies = str(row['hobbies']).lower()
            context = str(row['context'])
            
            # Check if both keywords match
            if (name_keyword.lower() in name and 
                hobby_keyword.lower() in hobbies):
                relevant_contexts.append(context)
                
        return relevant_contexts
        
    def get_last_column_content(self):
        if self.csv_data is None:
            return []
            
        name_keyword = self.selected_name_keyword.get()
        hobby_keyword = self.selected_hobby_keyword.get()
        
        if not name_keyword or not hobby_keyword:
            return []
            
        last_column_content = []
        
        for _, row in self.csv_data.iterrows():
            name = str(row['name']).lower()
            hobbies = str(row['hobbies']).lower()
            
            # Check if both keywords match
            if (name_keyword.lower() in name and 
                hobby_keyword.lower() in hobbies):
                # Get the last column content
                last_column_value = row.iloc[-1]  # Get the last column value
                last_column_content.append(str(last_column_value))
                
        return last_column_content
        
    def update_context_preview(self):
        relevant_contexts = self.find_relevant_context()
        last_column_content = self.get_last_column_content()
        
        self.context_text.delete(1.0, tk.END)
        if relevant_contexts:
            for i, context in enumerate(relevant_contexts, 1):
                self.context_text.insert(tk.END, f"{i}. {context}\n")
        else:
            self.context_text.insert(tk.END, "No relevant context found for selected keywords.")
            
        # Update last column content
        self.last_column_text.delete(1.0, tk.END)
        if last_column_content:
            for i, content in enumerate(last_column_content, 1):
                self.last_column_text.insert(tk.END, f"{i}. {content}\n")
        else:
            self.last_column_text.insert(tk.END, "No last column content found for selected keywords.")
            
    def add_to_feature_file(self):
        if not self.feature_file_path.get():
            messagebox.showerror("Error", "Please select a feature file first.")
            return
            
        relevant_contexts = self.find_relevant_context()
        
        if not relevant_contexts:
            messagebox.showwarning("Warning", "No relevant context found for selected keywords.")
            return
            
        try:
            # Read current feature file content
            with open(self.feature_file_path.get(), 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Find the last line to add Given statements
            last_line_index = len(lines) - 1
            
            # Add Given statements
            new_lines = []
            for context in relevant_contexts:
                # Extract the most relevant part of the context
                # Look for sentences that contain the hobby keyword
                hobby_keyword = self.selected_hobby_keyword.get()
                sentences = context.split(';')
                
                for sentence in sentences:
                    sentence = sentence.strip()
                    if hobby_keyword.lower() in sentence.lower():
                        # Format as Given statement
                        given_statement = f"    Given {sentence}\n"
                        new_lines.append(given_statement)
                        break
                else:
                    # If no specific sentence found, use the whole context
                    given_statement = f"    Given {context}\n"
                    new_lines.append(given_statement)
                    
            # Insert new lines before the last line
            lines[last_line_index:last_line_index] = new_lines
            
            # Write back to file
            with open(self.feature_file_path.get(), 'w', encoding='utf-8') as f:
                f.writelines(lines)
                
            # Update preview
            self.load_feature_preview()
            
            self.status_label.config(text=f"Added {len(new_lines)} Given statements to feature file.")
            messagebox.showinfo("Success", f"Added {len(new_lines)} Given statements to the feature file.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update feature file: {str(e)}")
            
    def on_name_keyword_change(self, event):
        self.update_context_preview()
        
    def on_hobby_keyword_change(self, event):
        self.update_context_preview()

def main():
    root = tk.Tk()
    app = FeatureGeneratorGUI(root)
    
    # Bind events for automatic context preview updates
    app.name_combobox.bind('<<ComboboxSelected>>', app.on_name_keyword_change)
    app.hobby_combobox.bind('<<ComboboxSelected>>', app.on_hobby_keyword_change)
    
    root.mainloop()

if __name__ == "__main__":
    main() 