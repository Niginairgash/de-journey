# Working with CSV Files in Python 
CSV (Comma Separated Values) files are like simple tables or spreadsheets. Here's how to work with them in Python:

# 1. Reading CSV Files
**Basic Reading:**

    import csv

    # Read a CSV file
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Each row is a list

**Reading as Dictionary (Recommended):**

    import csv
    
    with open('data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row['Name'], row['Age'])  # Access by column names

# 2. Writing CSV Files
**Basic Writing:**

    import csv
    
    data = [
        ['Name', 'Age', 'City'],
        ['Alice', 25, 'New York'],
        ['Bob', 30, 'London']
    ]
    
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

**Writing as Dictionary:**

    import csv
    
    data = [
        {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
        {'Name': 'Bob', 'Age': 30, 'City': 'London'}
    ]
    
    with open('output.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Age', 'City'])
        writer.writeheader()  # Write column names
        writer.writerows(data)

# 3. Simple Example - Complete Workflow

    import csv
    
    # Read data from CSV
    with open('students.csv', 'r') as file:
        reader = csv.DictReader(file)
        students = list(reader)  # Convert to list
    
    # Print all students
    for student in students:
        print(f"{student['Name']} is {student['Age']} years old")
    
    # Add a new student
    students.append({'Name': 'Charlie', 'Age': '22', 'Grade': 'A'})
    
    # Write back to CSV
    with open('students.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Age', 'Grade']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

Key Points to Remember:
* **Always use** with open() - it automatically closes the file
* **Use** newline='' when writing to avoid blank lines
* **DictReader/DictWriter** are easier to work with
* **pandas** is great for complex operations
