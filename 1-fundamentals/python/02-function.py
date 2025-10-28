#===============================================================
# Task 1: Create a calculator function that can handle any number of inputs:
#===============================================================
def calculator(operation, *args):
    """
    operation: 'add', 'multiply', 'max', 'min'
    *args: numbers to operate on
    """
    if operation == 'add':
        result = 0
        for value in args:
            result += value
        return result
    elif operation == 'multiply':
        result = 1
        for value in args:
            result *= value
        return result
    elif operation == 'max':
        return max(args)
    elif operation == 'min':
        return min(args)

# print(calculator('add', 1, 2, 3))        # Should return 6
# print(calculator('multiply', 2, 3, 4))   # Should return 24
# print(calculator('max', 2, 3, 8))        # Should return 8
# print(calculator('min', 1, 3, 4))        # Should return 1

#===============================================================
# Task 2: Create a function that builds a user profile:
#===============================================================
def build_user_profile(**kwargs):
    """
    Create a user profile with any attributes.
    Must include at least 'name' and 'email'
    """
    # Check if reuired field are present
    if 'name' not in kwargs:
        return "Error: 'name' is required"
    if 'email' not in kwargs:
        return "Error: 'email' is required" 

    profile = "=== USER PROFILE ===\n"
    for key, value in kwargs.items():
        profile += f"{key}: {value}\n"
    profile += "======================="

    return profile
    
# print(build_user_profile(name="Alice", email="alice@email.com"))
# print(build_user_profile(name="Bob", age=30, city="NYC", job="Developer"))

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
sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)

# 2. Sort by age (youngest first)
sorted_by_age = sorted(students, key=lambda student: student["age"])

# 3. Sort by name length
sordet_by_len_name = sorted(students, key=lambda student: len(student["name"]) )



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
    newmassage = ''
    for massage in messages:
        newmassage += f"{massage} "
    
    print(f"[{level}]  {newmassage} |")


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
