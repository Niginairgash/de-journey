import datetime
# Python Text File Tasks
# Beginner Tasks
#===============================================================
# Task 1: Create a Simple Diary
#===============================================================
# Create a program that lets users write diary entries
# Each entry should be timestamped and saved to "diary.txt"

def simple_diary():
    print("=== SIMPLE DIARY ===")
    entry = input("Write your diary entry: ")

    # Get current date and time
    now = datetime.date
    timestamp = now.strftime("%Y-%m-%d %H:%:%S")

    # Save to file
    with open('diary.txt', 'a', newline='') as file:
        file.writelines(f"[{timestamp}] {entry}")

simple_diary()


#===============================================================
# Task 2: Word Counter
#===============================================================
# Write a program that counts:
# - Total words in a file
# - Total lines in a file
# - Most common word


#===============================================================
# Task 3: To-Do List Manager
#===============================================================
# Create a simple to-do list that can:
# - Add new tasks
# - View all tasks
# - Mark tasks as completed
# - Save to "todo.txt"


#===============================================================
# Task 4: Simple Config Reader
#===============================================================
# Read a config file with key=value pairs
# Example config.txt:
# username=john
# language=python
# level=beginner
