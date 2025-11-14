import pandas as pd

#===============================================================
# Task 1: Basic Setup
#===============================================================
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones', 'Tablet', 'Speaker'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Audio', 'Electronics', 'Audio'],
    'Price': [1200, 25, 80, 300, 150, 600, 120],
    'Stock': [15, 100, 45, 20, 75, 30, 50],
    'Rating': [4.5, 4.2, 4.0, 4.7, 4.8, 4.3, 4.6]
}
df = pd.DataFrame(data)
#print("Original DataFrame:")
#print(df)


#===============================================================
# Task 2: Basic Single Conditions**
#===============================================================
"""
2.1 Find all products with Price greater than $200  
2.2 Find all products in the 'Electronics' category  
2.3 Find products with stock less than 50
"""
print("Products with Price greater than $200 ")
expensive_products = df[df['Price'] > 200]
print(expensive_products)
print("\n Products in the 'Electronics' category")
category_electronics = df[df['Category']=='Electronics']
print(category_electronics)

#===============================================================
# Task 3: Multiple Conditions**
#===============================================================
"""
3.1 Find Electronics products priced under $1000  
3.2 Find products with Rating above 4.5 AND Stock above 40  
3.3 Find products that are either Audio OR Accessories
"""

#===============================================================
# Task 4: Using isin()**
#===============================================================
"""
4.1 Find products that are either 'Laptop', 'Tablet', or 'Monitor'  
4.2 Find products in categories 'Audio' or 'Accessories'
"""

#===============================================================
# Task 5: String Operations**
#===============================================================
"""
5.1 Find products whose names start with 'M'  
5.2 Find products whose names contain 'phone'  
5.3 Find products with names longer than 6 characters
"""

#===============================================================
# Task 6: Complex Combinations**
#===============================================================
"""
6.1 Find Electronics products with Price between $500 and $1500  
6.2 Find products with high rating (≥4.5) OR low stock (<30)  
6.3 Find Audio products that are NOT priced above $200
"""

#===============================================================  
# Task 7: Using query() Method**
#===============================================================
"""
Solve these using the `query()` method:  
7.1 Products with Price > 100 and Stock < 60  
7.2 Products in Electronics category with Rating ≥ 4.5  
7.3 Products that are not in Stock between 40 and 70
"""

#===============================================================
# Task 8: loc for Selective Filtering**
#===============================================================
"""
8.1 Get only Product names and Prices for items with Rating > 4.4  
8.2 Get Product, Category, and Stock for Electronics with Price < 800  
8.3 Get all columns except Rating for products with Stock > 50
"""

#===============================================================
# Task 9: Real Business Scenarios**
#===============================================================
"""
9.1 Find products that need restocking (Stock < 30)  
9.2 Find premium products (Price > $500 AND Rating > 4.0)  
9.3 Find bargain products (Price < $100 AND Rating ≥ 4.5)
"""

#===============================================================
# Task 10: Challenge Tasks**
#===============================================================
"""
10.1 Find products where:  
- Category is Electronics OR Audio  
- Price between $100 and $800  
- Rating above 4.0  
- Stock at least 20

10.2 Create a "Deal Alert" filter: Products with high rating (≥4.5) but medium price (≤$300)
"""

