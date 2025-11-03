import datetime
import csv
import json
#===============================================================
# Task 1: Personal Diary System
#===============================================================
def add_diary_entry():
    entry_text = input("Write your diary entry: ")
    mood = input("How are feeling? (happy/sadsad/neutral): ")
    t = datetime.date.now()
    
    # count words in the entry
    word_count = len(entry_text)

    # Data for differernt format
    data_json = {
            "date" : f"{t}",
            "mood" : mood,
            "entry": entry_text,
            "word_count": word_count
    }

    data_csv = [t.strftime("%Y-%m-%d %H:%M:%S"), word_count, mood, entry_text[:50]] #first 50 char

    # which format to save in
    format_choice = input("Save format (txt/csv/json/all): ").lower()
    
    if format_choice == "txt":
        with open("diary_system.txt", "a") as f:
            f.write(f"Date: {t}\n")
            f.write(f"Mood: {mood}\n")
            f.write(f"Entry: {entry_text}\n")
            f.write("-" * 50 + "\n")
        print("Saved to TXT!")

    elif format_choice == "csv":
        with open("diary.csv", "a", newline="") as f:
            writer = csv.writer(f)
            #  Write header if file is empty
            if f.tell() == 0:
                writer.writerow(["Date", "WOrd Count", "Count", "Entry Preview"])
            writer.writerow(data_csv)
        print("Saved to CSV!")

    elif format_choice == json:
        # Read exisiting data, append new entry, and write back
        try: 
            with open("diary.json", "r") as file:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = {"entries": []}
        
        existing_data["entries"].append(data_json)

        with open("diary.json", "w") as f:
            json.dump(existing_data, file, indent=2)
        print("Saved to JSON!")

add_diary_entry()



#===============================================================
# Task 2: Student Grade Manager
#===============================================================
""" Requirements:
* Store student data in JSON: {"name": "John", "grades": [85, 90, 78]}
* Generate report cards in TXT format
* Export class statistics to CSV (average, highest, lowest grades)
"""
#===============================================================
# Task 3: Simple Inventory System
#===============================================================


#===============================================================
# Task 4: Weather Data Logger
#===============================================================


#===============================================================
# Task 5: Book Library Manager
#===============================================================


#===============================================================
# Task 6: Quiz Application
#===============================================================


#===============================================================
# Task 7: Expense Tracker
#===============================================================


#===============================================================
# Task 8: Music Playlist Manager
#===============================================================
