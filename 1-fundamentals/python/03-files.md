# 1. TXT Files (Plain Text)
**Simple text files - most basic format**

    # Writing to a text file
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a text file.\n")
        file.write("Line 3\n")
    
    # Reading from a text file
    with open("example.txt", "r") as file:
        content = file.read()
        print("Full content:")
        print(content)
    
    # Reading line by line
    with open("example.txt", "r") as file:
        print("\nLine by line:")
        for line in file:
            print(line.strip())  # strip() removes \n

# 2. CSV Files (Comma Separated Values)
**For tabular data - like Excel/spreadsheets**

**Writing CSV**
    
    import csv
    
    # Writing CSV data
    data = [
        ["Name", "Age", "City"],
        ["Alice", "25", "New York"],
        ["Bob", "30", "London"],
        ["Charlie", "35", "Tokyo"]
    ]
    
    with open("people.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

  **Reading CSV**

    import csv
  
    # Reading CSV as lists
    with open("people.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
    
    # Reading CSV as dictionaries (easier!)
    with open("people.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Name']} is {row['Age']} years old and lives in {row['City']}")

# 3. JSON Files (JavaScript Object Notation)
**For structured data - like Python dictionaries**

**Writing JSON**
    
    import json
    
    # Python dictionary
    person = {
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"],
        "is_student": True
    }
    
    # Write to JSON file
    with open("person.json", "w") as file:
        json.dump(person, file, indent=4)  # indent for pretty formatting

  **Reading JSON**

    import json
  
    # Reading JSON file
    with open("person.json", "r") as file:
        data = json.load(file)
        print(data)
        print(f"Name: {data['name']}")
        print(f"Hobbies: {', '.join(data['hobbies'])}")

# Complete Example: All Three Formats    

    import csv
    import json
    
    # Sample data
    employees = [
        {"name": "John", "department": "IT", "salary": 50000},
        {"name": "Sarah", "department": "HR", "salary": 45000},
        {"name": "Mike", "department": "Finance", "salary": 60000}
    ]
    
    # Save as TXT
    with open("employees.txt", "w") as file:
        for emp in employees:
            file.write(f"{emp['name']} works in {emp['department']} and earns ${emp['salary']}\n")
    
    # Save as CSV
    with open("employees.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "department", "salary"])
        writer.writeheader()
        writer.writerows(employees)
    
    # Save as JSON
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=2)
    
    print("Files created successfully!")


# Quick Tips:
* **TXT:** Use for simple text storage
* **CSV:** Use for Excel-like data
* **JSON:** Use for configuration files or API data
