# Working with Text Files in Python
Here's a simple guide to working with text files in Python:

# 1. Reading from a Text File
**Read the entire file at once:**

    # Open and read the whole file
    with open("myfile.txt", "r") as file:
        content = file.read()
        print(content)

**Read line by line:**

    # Read one line at a time
    with open("myfile.txt", "r") as file:
        for line in file:
            print(line.strip())  # strip() removes extra spaces/newlines

**Read all lines into a list:**

    # Get all lines as a list
    with open("myfile.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


# 2. Writing to a Text File

**Write new content (overwrites existing file):**

    # Write to file (creates new file or overwrites existing)
    with open("myfile.txt", "w") as file:
        file.write("Hello World!\n")
        file.write("This is a new line.")


**Add to existing content:**

    # Append to file (adds to end without deleting)
    with open("myfile.txt", "a") as file:
        file.write("\nThis line was appended.")

# 3. Different Ways to Open Files
* "r" - Read mode (default)
* "w" - Write mode (overwrites)
* "a" - Append mode (adds to end)
* "r+" - Read and write mode

# 4. Simple Examples
**Example 1: Create and write to a file**

    # Create a file with some text
    with open("notes.txt", "w") as file:
        file.write("My Notes:\n")
        file.write("- Learn Python\n")
        file.write("- Practice coding\n")

**Example 2: Read and display file content**

    # Read and display the file
    with open("notes.txt", "r") as file:
        print("File content:")
        print(file.read())


**Example 3: Count lines in a file**

    # Count how many lines in a file
    with open("notes.txt", "r") as file:
        lines = file.readlines()
        print(f"The file has {len(lines)} lines")


# 5. Important Tips
* Always use _with open()_ - it automatically closes the file
* _strip()_ removes spaces and newlines from strings
* _\n_ creates a new line
* If file doesn't exist, "w" or "a" will create it
* If file doesn't exist, "r" will give an error

# Quick Cheat Sheet:
    # Reading
    content = file.read()          # Read everything
    line = file.readline()         # Read one line
    lines = file.readlines()       # Read all lines as list
    
    # Writing
    file.write("text")            # Write text
    file.writelines(list)         # Write list of strings
