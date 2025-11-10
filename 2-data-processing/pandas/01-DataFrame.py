import pandas as pd
#===============================================================
# Task 1: Create a Basic DataFrame
#===============================================================
# Create a DataFrame for a book store with columns: 'Title', 'Author', 'Price', 'Stock'
# Add 3-4 books of your choice
# Solution
bookstore = pd.DataFrame({
    'Title': ['Python Basics', 'Data Science Guide', 'Machine Learning'],
    'Author': ['John Smith', 'Sarah Chen', 'Mike Johnson'],
    'Price': [29.99, 39.99, 49.99],
    'Stock': [15, 8, 12]
})
# print(bookstore)


#===============================================================
# Task 2: DataFrame from Dictionary
#===============================================================
# Create this data as a DataFrame:
data = {
    'City': ['New York', 'London', 'Tokyo', 'Paris'],
    'Population': [8419000, 8982000, 13960000, 2148000],
    'Country': ['USA', 'UK', 'Japan', 'France']
}

new_data = pd.DataFrame(data)


#===============================================================
# Task 3: DataFrame Inspection
#===============================================================
# Using the DataFrame from Task 2:
# 1. Display the first 2 rows
two_rows = new_data.head(2)

# 2. Get the shape (dimensions)
df_shape = new_data.shape

# 3. Get the column names
display_rows = new_data.columns.to_list()

# 4. Display the 'Population' column only
population = new_data['Population']


#===============================================================
# Task 4: Extract Series from DataFrame
#===============================================================
# From your bookstore DataFrame:
# 1. Extract the 'Price' column as a Series
extract_price = bookstore['Price']

# 2. Calculate the average price
bookstore[bookstore['Price'] > 30]

# 3. Find the most expensive book
max_price = bookstore['Price']
max_price.max()

#===============================================================
# Task 5: Filtering Data
#===============================================================
# From cities DataFrame:
df = pd.read_csv("worldcities.csv")

# 1. Find all cities with population greater than 5 million
# largest_cities = df[df['population'] > 5000000]
largest_cities = df.query('population > 5000000') # often more readable

# 2. Find cities in Europe (UK and France)
european_cities      = df[df['country'].isin(['UK', 'France'])]
european_cities_v2   = df.query('country in ["UK", "France"]')
european_cities_v3   = df[(df['country'] == 'UK') | (df['country'] == 'France')]
print(european_cities_v3)
#===============================================================
# Task 6: Adding New Columns
#===============================================================
# To your cities DataFrame, add:
# 1. A 'Density' column (assume area in sq km: [783.8, 1572, 2194, 105.4])
# 2. Calculate population density (population / area)

