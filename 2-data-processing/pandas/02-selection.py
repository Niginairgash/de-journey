import pandas as pd

# Selection Tasks: worldcities.csv
df = pd.read_csv('worldcities.csv')

#Level 1: Basic Column Selection
#===============================================================
# Task 1.1: Select Single Columns
#===============================================================
# 1. Select only the 'city' column and show first 5 entries
city = df['city'].head(5)

# 2. Select the 'population' column and find its data type
population = df['population']
#print(type(population))

# 3. Select the 'country' column and count unique countries
country = df['country'].unique()
#print(country)

#===============================================================
# Task 1.2: Select Multiple Columns
#===============================================================
# 1. Select 'city' and 'country' columns together
country_with_city = df[['city', 'country']]

# 2. Select 'city', 'lat', 'lng' (geographic trio)
geographic_trio = df[['city', 'lat', 'lng']]

# 3. Select 'city_ascii', 'iso2', 'iso3' (identification columns)
identification_columns = df[['city_ascii', 'iso2', 'iso3']]


# Level 2: Row Selection
#===============================================================
# Task 2.1: Position-based Selection (.iloc)
#===============================================================
# 1. Select the first 10 rows of the dataset
first_10 = df.iloc[0:10]

# 2. Select rows 50 to 60 (inclusive of 50, exclusive of 60)
rows_50_60 = df.iloc[50:60]

# 3. Select every 100th row (0, 100, 200, ...)
every_100th = df.iloc[::100]

#===============================================================
# Task 2.2: Specific Row Access
#===============================================================
# 1. Get the 25th city's complete information
city_25 = df.iloc[24]

# 2. Select only rows 15, 30, and 45
specific_cities = df.iloc[[15,30,45]]

# 3. Get the last 5 cities in the dataset
last_cities = df.iloc[-5:]


# Level 3: Combined Row & Column Selection
#===============================================================
# Task 3.1: Specific Cells
#===============================================================
# 1. Get the population of the 10th city
population_10 = df['population'].iloc[9]

# 2. Get the country name of the 100th city
country_100 = df['country'].iloc[99]

# 3. Get latitude and longitude of the first city
first_city_coords = df.iloc[0][['lat','lng']]

#===============================================================
# Task 3.2: Range Selections
#===============================================================
# 1. Select 'city' and 'population' for rows 20-30
city_rows = df.iloc[20:31][['city', 'population']]

# 2. Get city names and countries for the first 15 capital cities

# 3. Select all columns for cities with population over 5 million (just show first 5)

#===============================================================
# 
#===============================================================
