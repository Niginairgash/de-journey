#===============================================================
# Task 1: Create a calculator function that can handle any number of inputs:
#===============================================================
def calculator(operation, *args):
    """
    operation: 'add', 'multiply', 'max', 'min'
    *args: numbers to operate on
    """
    if operation == 'add':
        # Your code here - return sum of all numbers
        pass
    elif operation == 'multiply':
        # Your code here - return product of all numbers
        pass
    # Add more operations

# Test your function
print(calculator('add', 1, 2, 3))        # Should return 6
print(calculator('multiply', 2, 3, 4))   # Should return 24

#===============================================================
# Task 2: Create a function that builds a user profile:
#===============================================================
def build_user_profile(**kwargs):
    """
    Create a user profile with any attributes.
    Must include at least 'name' and 'email'
    """
    # Your code here
    # Check if required fields are present
    # Return a nicely formatted profile string

# Test cases
print(build_user_profile(name="Alice", email="alice@email.com"))
print(build_user_profile(name="Bob", age=30, city="NYC", job="Developer"))

#===============================================================
# Task 3: Sort this list of dictionaries in different ways:
#===============================================================
students = [
    {"name": "Alice", "grade": 85, "age": 20},
    {"name": "Bob", "grade": 92, "age": 22},
    {"name": "Charlie", "grade": 78, "age": 19}
]

# Your tasks:
# 1. Sort by grade (highest first)
# 2. Sort by age (youngest first)
# 3. Sort by name length

#===============================================================
# Task 4: Combined *args and **kwargs. Create a logger function
#===============================================================
def logger(level, *messages, **metadata):
    """
    level: 'INFO', 'WARNING', 'ERROR'
    *messages: one or more message strings
    **metadata: additional key-value pairs
    """
    # Your code here
    # Format: [LEVEL] message1 message2... | key1:value1, key2:value2

# Test
logger("INFO", "System started", "All services running", user="admin", timestamp="2024-01-01")
# Should output: [INFO] System started All services running | user:admin, timestamp:2024-01-01

#===============================================================
# Task 5: Lambda with Map/Filter. Process this data using lambda functions
#===============================================================
data = [15, 22, 8, 35, 42, 11, 27]

# Your tasks using lambda:
# 1. Square all numbers
# 2. Filter numbers greater than 20
# 3. Convert numbers to "Even" or "Odd" strings
# 4. Calculate which numbers are divisible by 3

#===============================================================
# Task 7: Create a flexible email sender
#===============================================================
def send_email(*recipients, **email_data):
    """
    recipients: one or more email addresses
    email_data: subject, body, cc, bcc, etc.
    """
    # Your code here
    # Validate that subject and body are provided
    # Format the output to show who the email is sent to and with what data

# Test
send_email("alice@email.com", "bob@email.com", 
          subject="Meeting", body="Hello team!", cc="boss@email.com")
