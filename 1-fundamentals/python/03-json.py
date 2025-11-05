# JSON Python Tasks
# Beginner Tasks

# Task 1: Basic Conversion

# Create a Python dictionary with your information (name, age, city)
# Convert it to JSON string and print it
# Then convert back to Python and access one value
import json

# Starter for Task 1
def basic_conversion():
    # Your code here
    my_info = {
        "name": "Your Name",
        "age": 25,
        "city": "Your City"
    }
    
    # Convert to JSON
    json_data = json.dumps(my_info)
    print("JSON:", json_data)
    
    # Convert back to Python
    python_data = json.loads(json_data)
    print("Name:", python_data["name"])

basic_conversion()

# Task 2: Simple File Operations

# Create a dictionary of your favorite movies with ratings
# Save it to a JSON file called "movies.json"
# Then read it back and print the data


# Task 3: List of Dictionaries

# Create a list containing 3 dictionaries of friends' information
# Convert to JSON and save to "friends.json"
# Read back and find the oldest friend


# Intermediate Tasks

# Task 4: Configuration Manager

# Create a config.json file with:
# - app_name, version, settings (theme, language)
# - database connection info
# Write functions to read and update config values


# Task 5: Student Gradebook

# Create a gradebook system that:
# - Stores students (name, id, grades list)
# - Calculates average grade for each student
# - Saves/loads from "grades.json"
# - Can add new students and grades


# Task 6: Shopping Cart

# Build a shopping cart that:
# - Stores items (name, price, quantity)
# - Calculates total cost
# - Saves cart to JSON
# - Can load previous cart
# - Add/remove items


# Advanced Tasks

# Task 7: API Data Handler

# Simulate API responses:
# - Create mock user data (users.json)
# - Write functions to:
#   * Get user by ID
#   * Add new user
#   * Update user info
#   * Delete user
```

# Task 8: Inventory System

# Build a product inventory:
# - Products: name, category, price, stock, id
# - Functions to:
#   * Add new products
#   * Update stock
#   * Find products by category
#   * Low stock alert
#   * Save/load inventory


# Task 9: Task Manager with JSON

# Create a task management system:
# - Tasks: title, description, due_date, priority, completed
# - Features:
#   * Add/delete tasks
#   * Mark as complete
#   * Filter by priority/status
#   * Save progress automatically


# Challenge Tasks

# Task 10: Budget Tracker

# Build a personal budget tracker:
# - Income and expense categories
# - Monthly budget limits
# - Transaction history with dates
# - Generate monthly reports
# - Data visualization suggestions
```

# Task 11: Book Library System

# Create a library management system:
# - Books: title, author, isbn, available copies
# - Members: name, member_id, borrowed books
# - Functions for borrowing/returning books
# - Track due dates and fines


# Task 12: Weather Data Logger

# Simulate weather data collection:
# - Store temperature, humidity, timestamp
# - Calculate daily averages
# - Find min/max temperatures
# - Generate weekly reports in JSON
- Comment your code clearly

**Which task would you like to start with? I can provide more detailed instructions and help you with any task!** 🎯
