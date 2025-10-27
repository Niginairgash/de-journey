# Basic Syntax:
# Traditional way
squares = []
for x in range(5):
    squares.append(x * x)

# Compehension way
squares = [x * x for x in range(5)]
# Result: [0, 1, 4, 9, 16]
#===============================================================
# TASK 1: Basic List Comprehension
#===============================================================
"""
Create a list of squares for numbers 0-9
"""
squares = []
squares = [x *x for x in range(10)]
#print(squares)

#===============================================================
# TASK 2: Filter with Condition
#===============================================================
"""
Get only even squares (numbers where square is even)
"""
even_squares = []
even_squares = [x **2 for x in range(9) if x**2 %2 == 0]
#print(even_squares)

#===============================================================
# TASK 3: Nested Loops
#===============================================================
"""
Create all combinations of (x, y) where x in [1,2,3] and y in [4,5,6]
"""
combinations = []
combinations = [(x,y) for x in range(1,4) for y in range(4,7)]
# print(combinations)

#===============================================================
# TASK 4: Real Interview Question
#===============================================================
"""
Flatten a 2D list into 1D
Example: [[1,2], [3,4], [5,6]] → [1,2,3,4,5,6]
"""
matrix = [[1,2], [3,4], [5,6]]

# solution 
flattened = [y for x in matrix for y in x]
#print(flattened)

#===============================================================
# TASK 5: Matrix Transpose
#===============================================================
"""
Transpose a matrix using nested list comprehension
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# solution:
transpose = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix))]

print(transpose)  
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
#===============================================================
# TASK 6: If-Else in Comprehension
#===============================================================
