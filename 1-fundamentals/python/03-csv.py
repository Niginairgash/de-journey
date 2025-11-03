import csv
# Beginner Level
#===============================================================
# Task 1: Basic Reading and Display
#===============================================================
# Create a CSV file with this data:
# Name,Age,City
# Alice,25,New York
# Bob,30,London
# Charlie,35,Paris

#Create the CSV file
def create_sample_csv_dictionary():
    data = [
        {'Name': 'Alice', 'Age': '25', 'City': 'New York'},
        {'Name': 'Bob', 'Age': '30', 'City': 'London'},
        {'Name': 'Charlie', 'Age': '35', 'City': 'Paris'}
    ]
    print("Have started create file ......")
    with open('people.csv', 'w', newline='') as file:
        fieldnames = ['Name', 'Age', 'City']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
        print("\n Successfully created")

def create_sample_csv():
    data = [
        ['Name','Age','City' ],
        ['Alice',25,'New York'],
        ['Bob',30,'London'],
        ['Charlie',35,'Paris']
    ]
    print("\n Have started create file ......")
    with open('people2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        print("\n Successfully created")

def read_csv():
    with open('people.csv', 'r') as file:
        reader = csv.reader(file)
        for item in reader:
            print(item)

def read_csv_formatted():
    with open('people.csv', 'r') as file:
        reader = csv.DictReader(file)
        people = list(reader)
    print(people)


#create_sample_csv_dictionary()
#create_sample_csv()
#read_csv()
#read_csv_formatted()

#===============================================================
# Task 2: Simple Data Filtering
#===============================================================
# Using the same CSV, find and print:
# - All people older than 28
# - People from London
# - Just the names of all people
def filter_people():
    # Read CSV file
    with open('people.csv', 'r') as file:
        reader = csv.DictReader(file)
        people = list(reader)

    print("=== All People ===")
    for person in people:
        print(f"Name: {person['Name']}, Age: {person['Age']}, City: {person['City']}")
    
    print("\n=== People older than 28 ===")
    for person in people:
        if int(person['Age']) > 28:
            print(f"{person['Name']} is {person['Age']} years od")

    print("\n=== People from London ===")
    for person in people:
        if person['City'] == 'London':
            print(f"{person['Name']} lives in London")

    print("\n=== Just the names of all people ==")
    for person in people:
        print(f"{person['Name']}")

#filter_people()


#===============================================================
# Task 3: Create a CSV File
#===============================================================
# Create a new CSV file for a bookstore with columns:
# Title,Author,Price,Quantity
# Add at least 5 books and save to 'books.csv'
def create_csv_bookstore():
    bookstore = [
        ["Title", "Author", "Price", "Quantity"],
        ["To Kill a Mockingbird", "Harper Lee", 12.99, 15],
        ["1984", "George Orwell", 10.50, 22],
        ["Pride and Prejudice", "Jane Austen", 8.99, 18],
        ["The Great Gatsby", "F. Scott Fitzgerald", 11.25, 12],
        ["The Catcher in the Rye", "J.D. Salinger", 9.75, 8]
    ]

    with open('books.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(bookstore)

# Create CSV file using csv.DictWriter
def create_csv_use_dictwriter():
    bookstore = [
        {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Price": 12.99, "Quantity": 15},
        {"Title": "1984", "Author": "George Orwell", "Price": 10.50, "Quantity": 22},
        {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Price": 8.99, "Quantity": 18},
        {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Price": 11.25, "Quantity": 12},
        {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Price": 9.75, "Quantity": 8}
    ]

    with open('book.csv', 'w', newline='') as file:
        fieldnames = ["Title", "Author", "Price", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bookstore)

#create_csv_bookstore()
#create_csv_use_dictwriter()


# Intermediate Level
#===============================================================
# Task 4: Student Grade Calculator
#===============================================================
# Given students.csv:
# Name,Math,Science,English
# Alice,85,90,78
# Bob,72,88,95
# Charlie,90,85,92

# Calculate and add a new column 'Average'
# Save to 'students_with_grades.csv'

#===============================================================
# Task 5: Data Analysis
#===============================================================
# Using the bookstore CSV, calculate:
# - Total value of inventory (price * quantity for each book)
# - Most expensive book
# - Total number of books in stock
# - Average book price

#===============================================================
# Task 6: Data Cleaning
#===============================================================
# Clean this messy data:
# Name,Age,Email
# "Alice, Jr",25,alice@email.com
# Bob,30,bob@email
# Charlie,,charlie@email.com
# Dana,35,INVALID_EMAIL

# Remove rows with invalid data and fix formatting


# Advanced Level
#===============================================================
# Task 7: CSV to JSON Converter
#===============================================================
# Convert your bookstore CSV to JSON format:
# [
#   {"Title": "Book1", "Author": "Author1", "Price": 20, "Quantity": 5},
#   ...
# ]
# Save as 'books.json'

#===============================================================
# Task 8: Sales Report Generator
#===============================================================
# Create a sales system:
# 1. Read products from 'products.csv' (ID,Name,Price,Stock)
# 2. Process sales from 'sales.csv' (ProductID,Quantity,Date)
# 3. Update stock levels and generate sales report


#===============================================================
# Task 9: Data Merger
#===============================================================
# Merge two CSV files:
# employees1.csv: ID,Name,Department
# employees2.csv: ID,Salary,JoinDate

# Create merged_employees.csv with all information
