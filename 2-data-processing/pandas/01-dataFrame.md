# DataFrame: The Entire Library (A Table)

Think of a DataFrame as the entire library, which is made of multiple bookshelves.
* **It's Two-Dimensional:** It has rows and columns, like a spreadsheet or a SQL table.
* **It has Row Labels and Column Labels:** Each row has an index, and each column has a name.
* **Each column is a Series!** The "Fruits" column is one Series, the "Prices" column is another Series. A DataFrame is a collection of Series that share the same index.

Example as a Pandas DataFrame:
```python
# Creating a DataFrame from a dictionary
data = {
  'Fruit': ['Apple', 'Banana', 'Cherry'],
  'Price': [1.50, 0.80, 3.00],
  'Quantity': [10, 15, 5]
}
      
df = pd.DataFrame(data)
print(df)
```
You can think of it as:
* The entire thing `df` is a DataFrame.
* The column `df['Fruit']` is a Series.
* The column `df['Price']` is another Series.
