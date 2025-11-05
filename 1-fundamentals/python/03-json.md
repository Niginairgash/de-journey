# JSON in Python
JSON (JavaScript Object Notation) is a way to store and exchange data that looks very similar to Python dictionaries.

# What is JSON?
* A lightweight data format that's easy for humans to read and write
* Commonly used for APIs, config files, and data storage
* Looks like this: {"name": "John", "age": 30, "city": "New York"}

# Basic JSON Operations in Python
**1. Convert Python Dictionary to JSON String**

    import json
    
    # Python dictionary
    person = {
        "name": "Alice",
        "age": 25,
        "is_student": True
    }
    
    # Convert to JSON string
    json_string = json.dumps(person)
    print(json_string)
    # Output: {"name": "Alice", "age": 25, "is_student": true}


**2. Convert JSON String to Python Dictionary**


      import json
      
      #JSON string
      json_data = '{"name": "Bob", "age": 30, "city": "London"}'
            
      #Convert to Python dictionary
      python_dict = json.loads(json_data)
      print(python_dict["name"])  # Output: Bob

**3. Read JSON from File**

    import json

    # Read from file
    with open("data.json", "r") as file:
        data = json.load(file)
        print(data)

**4. Write JSON to File**

    import json
    
    data = {
        "users": [
            {"name": "John", "age": 28},
            {"name": "Sarah", "age": 32}
        ]
    }
    
    # Write to file
    with open("output.json", "w") as file:
        json.dump(data, file, indent=4)  # indent makes it pretty

# Key Differences to Remember
* JSON uses true/false (lowercase), Python uses True/False (capital)
* JSON uses null, Python uses None
* JSON keys must be in double quotes " "

**Simple Example**

    import json
    
    # Python data
    student = {
        "name": "Tom",
        "grades": [85, 92, 78],
        "graduated": False
    }
    
    # Convert to JSON
    json_output = json.dumps(student, indent=2)
    print(json_output)
