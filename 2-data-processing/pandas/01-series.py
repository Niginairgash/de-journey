import pandas as pd
#===============================================================
# Task 1: Create a Basic Series
#===============================================================
# Create a Series of temperatures: [25, 28, 30, 22, 26]
# Use default index
# Print the series
temperatures = pd.Series([25, 28, 30, 22, 26])
print(temperatures)

#===============================================================
# Task 2: Series with Custom Index
#===============================================================
# Create a Series of student grades: [85, 92, 78, 96, 88]
# Use index: ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
# Print the series and access Diana's grade

student_grades = pd.Series([85, 92, 78, 96, 88], index=['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'])
print(student_grades)
student_grades['Diana']