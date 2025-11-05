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


2. Convert JSON String to Python Dictionary


      import json
      
      #JSON string
      json_data = '{"name": "Bob", "age": 30, "city": "London"}'
            
      #Convert to Python dictionary
      python_dict = json.loads(json_data)
      print(python_dict["name"])  # Output: Bob
