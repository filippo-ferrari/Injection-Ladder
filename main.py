import re
import sys

# Get the file path from the command-line argument
file_path = sys.argv[1]

# Read the content of the Java file
with open(file_path, 'r') as file:
    java_code = file.read()

# Regular expression pattern to match @Autowired fields and their annotations
pattern = r'(\s+@Autowired\s+.*?;)'  # Matches @Autowired followed by any content up to a semicolon

# Find all @Autowired fields in the Java code
autowired_fields = re.findall(pattern, java_code)

# Sort the @Autowired fields in-place by their length
autowired_fields.sort(key=lambda x: len(x))

# Function to replace each match with the corresponding sorted @Autowired field
def replace_autowired(match):
    return autowired_fields.pop(0)

# Replace each @Autowired field individually
java_code = re.sub(pattern, replace_autowired, java_code)

# Write the modified code back to the file
with open(file_path, 'w') as file:
    file.write(java_code)

