#  Pandas Selection: The Simple Guide
Think of selection like picking items from a menu or finding people in a photo album!

# 1. The Two Main Ways to Select
**By Label (using ._loc[ ]_)**
* Like using someone's name to find them
* "Show me Sarah's grades"
* "Get data from row 2 to row 5"

**By Position (using _.iloc[ ]_)**
* Like using position numbers
* "Show me the 3rd person in line"
* "Get the first 5 rows"

 # 2. Selecting Columns (Easiest!)

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

  Output:
  
            Name  Age    City  Salary
      0    Alice   25     NYC   50000
      1      Bob   30  London   60000
      2  Charlie   35   Tokyo   70000
      3    Diana   28   Paris   55000

**Select Single Column - returns a Series**
