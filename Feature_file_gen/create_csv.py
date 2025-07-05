import csv
import pandas as pd

# Data from the notebook
name = "John"
age = 30
hobbies = ["reading", "traveling", "cooking"]
context = [     
    "John likes reading books",
    "John likes traveling twice a year",
    "John likes cooking for his family"]

# Method 1: Using csv module
def create_csv_with_csv_module():
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'age', 'hobbies', 'context']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerow({
            'name': name,
            'age': age,
            'hobbies': ', '.join(hobbies),  # Convert list to string
            'context': '; '.join(context)   # Convert list to string
        })
    
    print("CSV file created successfully using csv module!")

# Method 2: Using pandas (more convenient for data manipulation)
def create_csv_with_pandas():
    data = {
        'name': [name],
        'age': [age],
        'hobbies': [', '.join(hobbies)],
        'context': ['; '.join(context)]
    }
    
    df = pd.DataFrame(data)
    df.to_csv('data_pandas.csv', index=False)
    print("CSV file created successfully using pandas!")

if __name__ == "__main__":
    # Create CSV using both methods
    create_csv_with_csv_module()
    create_csv_with_pandas()
    
    # Display the created data
    print("\nData that was written to CSV:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies}")
    print(f"Context: {context}") 