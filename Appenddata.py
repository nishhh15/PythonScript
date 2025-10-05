FILE_NAME = 'output.txt'

print("Enter text to write to the file: ", end="")
initial_text = input()

try:
    with open(FILE_NAME, 'w') as file:
        file.write(initial_text + '\n')
    print("Data successfully written to output.txt.")
except IOError as e:
    print(f"Error writing to file: {e}")
    exit()

print("Enter additional text to append: ", end="")
append_text = input()

try:
    with open(FILE_NAME, 'a') as file:
        file.write(append_text + '\n')
    print("Data successfully appended.")
except IOError as e:
    print(f"Error appending to file: {e}")
    pass

print("\nFinal content of output.txt:")

try:
    with open(FILE_NAME, 'r') as file:
        final_content = file.read()

    print(final_content.strip())
except FileNotFoundError:
    print(f"Error: The file {FILE_NAME} was not found.")
except IOError as e:
    print(f"Error reading file: {e}")