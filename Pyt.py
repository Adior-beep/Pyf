def process_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: Cannot read the file '{filename}'.")
        return

    modified_content = content.upper()

    new_filename = "modified_" + filename
    try:
        with open(new_filename, 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to '{new_filename}'.")

if __name__ == "__main__":
    process_file()
