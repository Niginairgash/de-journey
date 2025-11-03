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

filter_people()


#===============================================================
# Task 3: Create a CSV File
#===============================================================
# Create a new CSV file for a bookstore with columns:
# Title,Author,Price,Quantity
# Add at least 5 books and save to 'books.csv'

#===============================================================
#
#===============================================================


#===============================================================
#
#===============================================================


#===============================================================
#
#===============================================================


#===============================================================
#
#===============================================================


#===============================================================
#
#===============================================================
