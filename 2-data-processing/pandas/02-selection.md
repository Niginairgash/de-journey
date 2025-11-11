#  Pandas Selection: The Simple Guide
Think of selection like picking items from a menu or finding people in a photo album!

## 1. The Two Main Ways to Select
**By Label (using ._loc[ ]_)**
* Like using someone's name to find them
* "Show me Sarah's grades"
* "Get data from row 2 to row 5"

**By Position (using _.iloc[ ]_)**
* Like using position numbers
* "Show me the 3rd person in line"
* "Get the first 5 rows"

 ## 2. Selecting Columns (Easiest!)

```python
import pandas as pd
  
# Sample DataFrame
data = {
   'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
   'Age': [25, 30, 35, 28],
   'City': ['NYC', 'London', 'Tokyo', 'Paris'],
   'Salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print(df)
```
  Output:
  
            Name  Age    City  Salary
      0    Alice   25     NYC   50000
      1      Bob   30  London   60000
      2  Charlie   35   Tokyo   70000
      3    Diana   28   Paris   55000

**Select Single Column - returns a Series**

```python
# Method 1: Square brackets (most common)
names = df['Name']
print("Names column:")
print(names)
    
# Method 2: Dot notation (works for simple column names)
ages = df.Age
print("\nAges column:")
print(ages)
```

**Select Multiple Columns - returns a DataFrame**

```python
# Select Name and City columns
name_city = df[['Name', 'City']]
print("Name and City columns:")
print(name_city)
    
# Select Name, Age, and Salary
subset = df[['Name', 'Age', 'Salary']]
print("\nName, Age, Salary:")
print(subset)
```

## 3. Selecting Rows
**By Position with _.iloc[ ]_**

```python
# Single row (position 2 - third row)
print("Third row:")
print(df.iloc[2])
    
# Multiple rows (first 3 rows)
print("\nFirst 3 rows:")
print(df.iloc[0:3])
    
# Specific rows (first and third)
print("\nFirst and third rows:")
print(df.iloc[[0, 2]])
```

**By Label with _.loc[ ]_**

```python
# Single row (index label 2)
print("Row with index 2:")
print(df.loc[2])
    
# Multiple rows (index 1 and 3)
print("\nRows with index 1 and 3:")
print(df.loc[[1, 3]])
```

## 4. Selecting Specific Cells (Row + Column)

```python
# Bob's Age using .loc (label-based)
bob_age = df.loc[1, 'Age']  # Row 1, Column 'Age'
print(f"Bob's age: {bob_age}")
    
# Charlie's Salary using .iloc (position-based)
charlie_salary = df.iloc[2, 3]  # Row 2, Column 3
print(f"Charlie's salary: {charlie_salary}")
```

**Key Learning Points:**
- `df[['col1', 'col2']]` - Double brackets for multiple columns → returns DataFrame
- `df.iloc[start:end]` - Position-based slicing (end is exclusive)
- `df.iloc[[1, 5, 10]]` - Specific positions using list of indices
- `df.iloc[-5:]` - Negative indexing for last rows
- `df.iloc[::100]` - Step selection (every 100th row)
