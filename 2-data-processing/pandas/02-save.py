##  **Task 1: Basic File Saving**
# Create and save a simple DataFrame

""" python
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
    'Price': [999.99, 25.50, 75.00, 299.99],
    'Stock': [15, 100, 50, 25],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics']
})

# todo:
# 1. Save as CSV without index
# 2. Save as Excel file
# 3. Save as JSON with pretty formatting
"""


##  **Task 2: Save Processed Data**
# Read, clean, and save modified data

"""python
# Start with this "messy" data
messy_sales = pd.DataFrame({
    'OrderID': [101, 102, 103, 104, 105],
    'Customer': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Amount': [150.0, 200.0, None, 300.0, 180.0],  # Contains missing value
    'Date': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19']
})

# Your tasks:
# 1. Fill missing values with the average amount
# 2. Filter orders above $170
# 3. Save the cleaned data as CSV
# 4. Save only Customer and Amount columns as Excel
"""


## 📊 **Task 3: Multiple DataFrames to One File**
# Create and save multiple sheets in one Excel file

"""python
# Create sample data for different departments
hr_data = pd.DataFrame({
    'Employee': ['John', 'Sarah', 'Mike', 'Lisa'],
    'Position': ['Manager', 'Analyst', 'Developer', 'Designer'],
    'Salary': [70000, 55000, 65000, 60000]
})

it_data = pd.DataFrame({
    'Employee': ['Tom', 'Emma', 'Alex'],
    'Project': ['Website', 'Mobile App', 'Database'],
    'Deadline': ['2024-03-01', '2024-04-15', '2024-02-28']
})

sales_data = pd.DataFrame({
    'Employee': ['Rachel', 'Kevin'],
    'Region': ['North', 'South'],
    'Target': [100000, 120000]
})

# Your tasks:
# 1. Save all three DataFrames to one Excel file, each in separate sheets
# 2. Name the sheets: 'HR', 'IT', 'Sales'
# 3. Don't include index in any sheet
"""


##  **Task 4: Real Dataset Processing**
# Download and process a real dataset

"""python
# Use this URL or any dataset you have
url = "https://raw.githubusercontent.com/datasets/iris/master/data/iris.csv"

# todo:
# 1. Read the iris dataset from the URL
# 2. Save it locally as CSV
# 3. Filter only 'setosa' species
# 4. Save the filtered data as Excel
# 5. Calculate average measurements per species and save as JSON
"""



##  **Task 5: Advanced Formatting**
# Save with custom formatting and conditions

"""python
# Sample financial data
financial_data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Revenue': [50000, 52000, 48000, 55000, 60000, 58000],
    'Expenses': [35000, 36000, 38000, 37000, 39000, 38500],
    'Profit': [15000, 16000, 10000, 18000, 21000, 19500]
})

# Your tasks:
# 1. Calculate profit margin (Profit/Revenue) and add as new column
# 2. Save as CSV with only 2 decimal places for numeric columns
# 3. Create two separate files: 
#    - High performance months (Profit > 17000)
#    - Low performance months (Profit <= 17000)
# 4. Save summary statistics as JSON
"""


##  **Task 6: Data Pipeline Simulation**
# Complete data processing pipeline

"""python
# Simulate a real-world scenario
raw_customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice Smith', 'Bob Johnson', 'Charlie Brown', None, 'Eve Wilson', 'Frank Davis'],
    'email': ['alice@email.com', 'bob@email.com', 'charlie@email.com', 'diana@email.com', 'eve@email.com', 'frank@email.com'],
    'age': [25, 35, 28, 42, 31, None],
    'city': ['New York', 'London', 'New York', 'Paris', 'Tokyo', 'London'],
    'purchase_amount': [150.0, 200.0, 75.0, 300.0, 125.0, 180.0]
})

# Your tasks:
# 1. Clean the data: remove rows with missing names or ages
# 2. Create a summary DataFrame with:
#    - Total customers per city
#    - Average purchase amount per city
# 3. Save:
#    - Cleaned customer data as CSV
#    - City summary as Excel
#    - Both as separate sheets in one Excel file
#    - JSON file with city statistics
"""


## **Task 7: Error Handling & Best Practices**
# Practice robust file operations**

"""python
# Create sample data
inventory = pd.DataFrame({
    'item_id': ['A001', 'A002', 'A003', 'A004'],
    'item_name': ['Widget X', 'Gadget Y', 'Tool Z', 'Device W'],
    'quantity': [100, 50, 75, 200],
    'price': [19.99, 29.99, 9.99, 49.99]
})

# Your tasks:
# 1. Save with error handling (try-except blocks)
# 2. Check if file already exists before saving
# 3. Create a backup system: save with timestamp in filename
# 4. Save with different encodings (utf-8, latin1)
"""


##  **Solution Checklist**
"""
After each task, verify:
- [ ] File was created successfully
- [ ] No unnecessary index column
- [ ] Data looks correct when reopened
- [ ] File sizes are reasonable
- [ ] Special characters handled properly
"""

##  **Bonus Challenge**
"""
Create your own dataset about something you're interested in (movies, games, sports) and:
1. Save it in 3 different formats
2. Create filtered versions
3. Generate summary files
4. Package everything in one Excel file with multiple sheets
"""

## **Need Help? Use This Template:**
"""python
import pandas as pd
import os
from datetime import datetime


# Example of timestamped backup:
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
df.to_csv(f'backup_data_{timestamp}.csv', index=False)
"""
