# Basic Syntax:
# Traditional way
squares_dict = {}
for x in range(5):
    squares_dict[x] = x*x

# Comprehension way
squares_dict = {x: x*x for x in range(5)}

#===============================================================
# TASK 5: Basic Dictionary Comprehension
#===============================================================
"""
Create a dictionary mapping numbers to their cubes for 0-4
"""
cubes = {}

cubes = {x: x**3 for x in range(5)}
print(cubes)
#===============================================================
#===============================================================