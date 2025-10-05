import os
filename = "sample.txt"
try:
    with open(filename, 'r') as file:
        print("Reading file content:")
        line_number = 1

        for line in file:

            print(f"Line {line_number}: {line.strip()}")
            line_number += 1
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
