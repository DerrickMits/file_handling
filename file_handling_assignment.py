# Step 1: File Creation
with open("my_file.txt", 'w') as file:
    file.write("Hello, World!\n")
    file.write("Learning Python file handling.\n")
    file.write("Line number: 3\n")

# Step 2: File Reading and Display
with open("my_file.txt", 'r') as file:
    content = file.read()
    print("File content after initial write:")
    print(content)

# Step 3: File Appending
with open("my_file.txt", 'a') as file:
    file.write("This is an appended line.\n")
    file.write("File handling is important.\n")
    file.write("Appending is done!\n")

# Read and display the content after appending
with open("my_file.txt", 'r') as file:
    content = file.read()
    print("File content after appending:")
    print(content)
