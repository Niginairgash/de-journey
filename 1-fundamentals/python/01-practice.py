#===============================================================
# TASK 1: Two Sum Pairs 
#===============================================================
"""
Find all pairs (i, j) where nums[i] + nums[j] = target and i < j
"""
nums = [2, 7, 3, 6, 1, 5]
target = 8
# Expected: [(2,6), (3,5), (7,1)] because 2+6=8, 3+5=8, 7+1=8
# Solution:
pairs = [(nums[n], nums[x]) 
         for n in range(len(nums)) 
         for x in range(1+n, len(nums)) 
         if nums[n] + nums[x] == target]
#print(pairs)

#===============================================================
# TASK 2: Character Position Mapping
#===============================================================
"""
Create a dictionary mapping each character to list of positions it appears
"""
text = "hello world"

# Expected: {'h':[0], 'e':[1], 'l':[2,3,9], 'o':[4,7], ' ':[5], 'w':[6], 'r':[8], 'd':[10]}

# solution:
char_positions = {i : [x for x, y in enumerate(text) if y == i] for i in text}

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

# Solution:
diagonal = [matrix[i][i] for i in range(len(matrix))]

# print(diagonal)


#===============================================================
# TASK 4: Word Length Categorization
#===============================================================
"""
Categorize words by length: short (<5), medium (5-7), long (>7)
"""
words = ["apple", "hi", "banana", "programming", "a", "elephant"]

# Expected: {'short': ['hi', 'a'], 'medium': ['apple', 'banana'], 'long': ['programming', 'elephant']}

# Solution:
categories = {
    'short': [item for item in words if len(item) < 5],
    'medium': [item for item in words if 5 <= len(item) <= 7],
    'long': [item for item in words if len(item) > 7]
}

# print(categories)



"""
Calculate sum of all elements in nested lists (any depth)
But using only comprehensions (no recursion)
"""
nested_lists = [[1, 2], [3, [4, 5]], [6, [7, [8, 9]]]]

# This one is tricky! Hint: You might need multiple comprehensions
# Expected: 45 (1+2+3+4+5+6+7+8+9)

# Solution (simplified for 2 levels):
two_level = [[1, 2], [3, [4, 5]], [6, 7]]

# Solution:
total = [item  for sublist in two_level for item in (sublist if isinstance(sublist, list) else [sublist])]
print(total)