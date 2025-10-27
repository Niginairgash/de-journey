# Basic Syntax:
# Traditional way
squares_dict = {}
for x in range(5):
    squares_dict[x] = x*x

# Comprehension way
squares_dict = {x: x*x for x in range(5)}

#===============================================================
# TASK 1: Basic Dictionary Comprehension
#===============================================================
"""
Create a dictionary mapping numbers to their cubes for 0-4
"""
cubes = {}

cubes = {x: x**3 for x in range(5)}
#print(cubes)

#===============================================================
# TASK 2: Filter Dictionary
#===============================================================
"""
Given a dictionary of items and prices, create new dict with only items under $10
"""
prices = {"apple": 2.5, "laptop": 999, "banana": 1.5, "headphones": 50}

# solution:
cheap_items = { item:price for item, price in prices.items() if price < 10}

#print(cheap_items)  # {'apple': 2.5, 'banana': 1.5}

#===============================================================
# TASK 3: Transform Dictionary Keys/Values
#===============================================================
"""
Convert all prices to strings and add currency symbol
"""
prices = {'apple': 2.5, 'banana': 1.5, 'orange': 3.0}

# solution:
price_strings = { item:"$"+str(price) for item, price in prices.items()}

# print(price_strings) # {'apple': '$2.5', 'banana': '$1.5', 'orange': '$3.0'}

#===============================================================
# TASK 4: Character Frequency Counter (Meta)
#===============================================================
"""
Count frequency of each character in a string using dictionary comprehension
"""
text = "hello world"

# Your one-line solution:
char_count = {item:text.count(item) for item in text }

print(char_count)  # {'h':1, 'e':1, 'l':3, 'o':2, ' ':1, 'w':1, 'r':1, 'd':1}
