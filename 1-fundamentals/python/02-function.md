# *args (Variable Positional Arguments)
**What it is:** Allows a function to accept any number of positional arguments.

    def greet(*args):
      for name in args:
        print(f"Hello, {name}!")

    # You can pass any number of arguments
    greet("Alice")                    # Hello, Alice!
    greet("Alice", "Bob")             # Hello, Alice! Hello, Bob!
    greet("Alice", "Bob", "Charlie")  # Hello, Alice! Hello, Bob! Hello, Charlie!

**Think of it as:** A catch-all for extra positional arguments.

# **kwargs (Variable Keyword Arguments)
**What it is:** Allows a function to accept any number of keyword arguments.

    def create_profile(**kwargs):
      for key, value in kwargs.items():
          print(f"{key}: {value}")
  
    # You can pass any number of keyword arguments
    create_profile(name="Alice", age=25)
    # Output: name: Alice, age: 25
    
    create_profile(name="Bob", age=30, city="New York", job="Engineer")
    # Output: name: Bob, age: 30, city: New York, job: Engineer

**Think of it as:** A dictionary that collects extra keyword arguments.

# Using *args and **kwargs Together
    def flexible_function(*args, **kwargs):
        print("Positional arguments:", args)
        print("Keyword arguments:", kwargs)
    
    flexible_function(1, 2, 3, name="Alice", age=25)
    # Output:
    # Positional arguments: (1, 2, 3)
    # Keyword arguments: {'name': 'Alice', 'age': 25}

# Lambda Functions
**What it is:** A small anonymous function (without a name) that can take any number of arguments but can only have one expression.

    # Regular function
    def square(x):
        return x * x
    
    # Lambda equivalent
    square = lambda x: x * x
    
    print(square(5))  # Output: 25

# Common uses:
**1. With** _map()_ **- apply to each item:**

    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(squared)  # Output: [1, 4, 9, 16, 25]

**2. With** _filter()_ **- filter items:**

    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4, 6]

**3. With** _sort()_- **custom sorting:**

    students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
    # Sort by age
    students.sort(key=lambda student: student[1])
    print(students)  # Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]

# Quick Summary

* *args: For variable number of positional arguments → becomes a tuple
* **kwargs: For variable number of keyword arguments → becomes a dictionary
* lambda: For creating small, one-line functions without a formal definition
