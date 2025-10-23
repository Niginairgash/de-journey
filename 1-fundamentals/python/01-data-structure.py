#TASK 1: Create a Grocery List
groceries = [ "bread", "milk", "eggs" ] # Create a list called groceries with: "bread", "milk", "eggs"
groceries.append("butter")              # Add "butter" to the list
groceries.remove("milk")                # Remove "milk" from the list
#print(groceries)                        # Print the final list

# TASK 2: Student Grades Dictionary
grades = {                              # Create a dictionary called grades with:
    "Alice": 85,                        # - "Alice": 85
    "Bob": 92,                          # - "Bob": 92  
    "Charlie": 78                       # - "Charlie": 78
    } 
grades["Diana"] = 88                    # Add "Diana" with grade 88
grades["Bob"] = 95                      # Update Bob's grade to 95
#print(grades["Charlie"])                # Print Charlie's grade

# TASK 3: Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 4, 5]      # You have a list: [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)           # Convert it to a set to remove duplicates
final_numbers = list(unique_numbers)    # Then convert back to a list
#print(final_numbers)                    # Print the result