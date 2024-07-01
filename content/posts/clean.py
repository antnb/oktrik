import os
import re

# Path to the directory containing the .md files
directory = r'C:\Users\timur\Documents\GitHub\bdkalkuntrik\oktrik\content\posts'

# Regex pattern to match the old filename format
pattern = re.compile(r'^\d{4}-\d{2}-\d{2}-[a-z0-9]{4}-(.+\.md)$')

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Match the filename against the pattern
    match = pattern.match(filename)
    if match:
        # Extract the new filename from the regex match
        new_filename = match.group(1)
        # Construct the full old and new file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_filename}')
