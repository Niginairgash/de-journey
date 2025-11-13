## What is Filtering?
Filtering means selecting specific rows from your DataFrame based on certain conditions - just like using a sieve to separate what you want from what you don't want.

## Basic Filtering Syntax
```python
filtered_data = dataframe[condition]
```

## Common Condition Operators
- `==` : equal to
- `!=` : not equal to
- `>` : greater than
- `<` : less than
- `>=` : greater than or equal to
- `<=` : less than or equal to

## Simple Examples

Let's create a sample DataFrame first:
```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'London', 'Paris', 'Tokyo'],
    'Salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print(df)
```

### 1. Single Condition Filtering
```python
# Get people older than 28
adults = df[df['Age'] > 28]
print(adults)

# Get people from London
london_people = df[df['City'] == 'London']
print(london_people)
```

### 2. Multiple Conditions
Use `&` for AND, `|` for OR, `~` for NOT

```python
# AND condition: Age > 25 AND Salary > 55000
result = df[(df['Age'] > 25) & (df['Salary'] > 55000)]
print(result)

# OR condition: From London OR Paris
result = df[(df['City'] == 'London') | (df['City'] == 'Paris')]
print(result)

# NOT condition: Not from New York
result = df[~(df['City'] == 'New York')]
print(result)
```

### 3. Using `isin()` for Multiple Values
```python
# People from specific cities
cities = ['London', 'Paris']
result = df[df['City'].isin(cities)]
print(result)
```

### 4. String Operations
```python
# Names starting with 'A'
result = df[df['Name'].str.startswith('A')]
print(result)

# Names containing 'li'
result = df[df['Name'].str.contains('li')]
print(result)
```

## Common Methods for Filtering

### `query()` method - More readable
```python
# Same as df[df['Age'] > 28]
result = df.query('Age > 28')

# Multiple conditions
result = df.query('Age > 25 and Salary > 55000')
```

### `loc` for filtering and selecting columns
```python
# Filter rows and select specific columns
result = df.loc[df['Age'] > 28, ['Name', 'Salary']]
print(result)
```

## Quick Tips:
1. **Use parentheses** for multiple conditions: `(condition1) & (condition2)`
2. **`&` means AND**, `|` means OR
3. **`isin()`** is great for checking multiple values
4. **`query()`** can be more readable for complex conditions

## Real-life Analogy:
Think of filtering like shopping online:
- "Show me shoes **AND** under $50" = `(category == 'shoes') & (price < 50)`
- "Show me shirts **OR** pants" = `(category == 'shirts') | (category == 'pants')`
- "Show me everything **EXCEPT** red items" = `~(color == 'red')`

