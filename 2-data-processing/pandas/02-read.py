import pandas as pd

# Task 1: Basic File Reading
# Create these CSV files and practice reading them:

# students.csv
"""
csv
Name,Age,Grade,Score
Alice,22,A,95
Bob,21,B,85
Charlie,23,A+,98
Diana,20,B+,87
"""


"""
# 1. Read the students.csv file
# 2. Display the first 3 rows
# 3. Check how many rows and columns it has
"""



# Task 2: Handle Different File Formats
# Create these files and read them:

# products.tsv (Tab Separated)
""" tsv
ID	Name	Price	Category
1	Laptop	999.99	Electronics
2	Book	19.99	Education
3	Headphones	149.99	Electronics
"""

# data.txt (Semicolon Separated)
""" txt
City;Population;Country
Tokyo;37400000;Japan
Delhi;28500000;India
Shanghai;25500000;China
"""

# Code tasks:
# 1. Read products.tsv using sep='\t'
# 2. Read data.txt using sep=';'
# 3. Compare the shapes of both DataFrames


# Task 3: Real Excel File Practice
# Create an Excel file `sales.xlsx` with two sheets:

# Sheet1 (January):
"""
Date,Product,Amount
2024-01-01,Widget A,1000
2024-01-02,Widget B,1500
"""

# Sheet2 (February):
"""
Date,Product,Amount
2024-02-01,Widget A,1200
2024-02-02,Widget C,800
"""

# Code tasks:
""" python
# 1. Read the January sheet
# 2. Read the February sheet
# 3. Read both sheets and combine them
"""



# Task 4: Problem Solving - Tricky Files

# Create this "messy" CSV file `messy_data.csv`:
""" csv
This is some header info
And more header lines
Name,Age,Salary,Department
John Doe,30,50000,IT
Jane Smith,25,45000,HR
,,,,,
Some footer text here
"""

# Code tasks:
""" python
# 1. Read the file skipping the first 2 lines
# 2. Read the file skipping the last 2 lines
# 3. Read only specific columns: Name and Department
"""



# Task 5: File Exploration**
"""
Download a real dataset and practice:
1. Go to [Kaggle](https://www.kaggle.com/datasets) and download any small CSV dataset
2. Or use this sample URL: https://github.com/Niginairgash/de-journey/blob/main/2-data-processing/pandas/iris.csv
"""
# Tasks:
# 1. Read the dataset from your computer
# 2. Display basic info about the data
# 3. Find out:
#    - How many rows and columns?
#    - What are the column names?
#    - What are the data types?


# Task 6: Advanced Challenges

# Create `employee_data.csv`
""" csv
ID,Name,Join_Date,Salary
1,John Doe,2020-01-15,50000
2,Jane Smith,2019-03-20,60000
3,Bob Johnson,2021-07-10,55000
"""

# Challenges:
# 1. Read the file and set 'ID' as the index
# 2. Read with specific data types: Salary as float
# 3. Handle missing values if any exist
# 4. Read only employees with Salary > 52000



# Solution Checklist
"""
After each task, ask yourself:
- [ ] Did I successfully read the file?
- [ ] Can I see the first few rows?
- [ ] Do I understand the structure (rows, columns)?
- [ ] Did I handle any file format issues?
"""

# Bonus Challenge**
Create your own CSV file with data about something you're interested in (movies, games, sports stats) and read it into Pandas!
