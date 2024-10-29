# File Creation
try:
    with open('my_file.txt', 'w') as f:
        f.write('Line 1: This is a test line.\n')
        f.write('Line 2: Here is some more text.\n')
        f.write('Line 3: 12345\n')
except PermissionError:
    print("Permission Denied. Unable to create or write to the file.")
except Exception as e:
    print(f"Error occurred: {e}")

# File Reading and Display
try:
    with open('my_file.txt', 'r') as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("File not found. Please create the file before reading it.")
except Exception as e:
    print(f"Error occurred: {e}")

# File Appending
try:
    with open('my_file.txt', 'a') as f:
        f.write('Line 4: Appending some more text.\n')
        f.write('Line 5: 54321\n')
        f.write('Line 6: This is the end of the file.\n')
except PermissionError:
    print("Permission Denied. Unable to append to the file.")
except Exception as e:
    print(f"Error occurred: {e}")