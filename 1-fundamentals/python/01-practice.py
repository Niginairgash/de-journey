#===============================================================
# TASK 1: Two Sum Pairs 
#===============================================================
"""
Find all pairs (i, j) where nums[i] + nums[j] = target and i < j
"""
nums = [2, 7, 3, 6, 1, 5]
target = 8
# Expected: [(2,6), (3,5), (7,1)] because 2+6=8, 3+5=8, 7+1=8

#===============================================================
# TASK 2: Character Position Mapping
#===============================================================
"""
Create a dictionary mapping each character to list of positions it appears
"""
text = "hello world"

# Expected: {'h':[0], 'e':[1], 'l':[2,3,9], 'o':[4,7], ' ':[5], 'w':[6], 'r':[8], 'd':[10]}

# Your solution:
char_positions = 

print(char_positions)

#===============================================================
# TASK 3: Matrix Diagonal 
#===============================================================
"""
Extract the main diagonal from a matrix
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Expected: [1, 5, 9] (elements where row index == column index)

# Your solution:
diagonal = 

print(diagonal)


#===============================================================
# TASK 4: Word Length Categorization
#===============================================================
"""
Categorize words by length: short (<5), medium (5-7), long (>7)
"""
words = ["apple", "hi", "banana", "programming", "a", "elephant"]

# Expected: {'short': ['hi', 'a'], 'medium': ['apple', 'banana'], 'long': ['programming', 'elephant']}

# Your solution:
categories = 

print(categories)

#===============================================================
# TASK 5: Stock Profit Calculator
#===============================================================
"""
Calculate possible profits: (buy_day, sell_day, profit) where buy_day < sell_day
"""
prices = [7, 1, 5, 3, 6, 4]

# Expected: [(0,2,-2), (0,3,-4), (0,4,-1), ... (1,4,5)] 
# Format: (buy_index, sell_index, profit)

# Your solution:
profits = 
