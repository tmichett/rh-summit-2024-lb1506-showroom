import re
import os
import sys

# Ensure a file is provided as an argument
if len(sys.argv) < 2:
    print("Usage: python script.py <input_file>")
    sys.exit(1)

# Get the input file from command line
input_file = sys.argv[1]

# Validate input file existence
if not os.path.isfile(input_file):
    print(f"Error: File '{input_file}' not found.")
    sys.exit(1)

# Define the block to be removed
remove_pattern = r"= Documentation Book\nAuthor Name\nv1\.0\n:sectnums:\n:toc:\n:pdf-page-size: A4\n\n"

# Read the file content
with open(input_file, "r") as file:
    content = file.read()

# Remove the block if it exists
updated_content = re.sub(remove_pattern, "", content)

# Write the updated content back to the file
with open(input_file, "w") as file:
    file.write(updated_content)

print(f"Updated '{input_file}' by removing the specified block if present.")
