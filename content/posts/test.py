import os
import re

# Path to the directory containing the .md files
directory = r'C:\Users\timur\Documents\GitHub\bdkalkuntrik\oktrik\content\posts'

# Regex pattern to match the front matter URL
url_pattern = re.compile(r'blogger_orig_url:\s*(https://www\.oktrik\.com/.+\.html)')

redirects = []

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".md"):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            match = url_pattern.search(content)
            if match:
                old_url = match.group(1)
                # Extract the URL path from the old URL
                old_path = re.sub(r'https://www\.oktrik\.com', '', old_url)
                # Create the new URL based on the filename
                new_url = f'https://www.oktrik.com/posts/{filename[:-3]}/'
                # Generate the Cloudflare Worker redirect code
                redirect_code = f"if (url.pathname === '{old_path}') {{\n    // Redirect '{old_path}' to '{new_url}' with a 301 status code\n    return Response.redirect('{new_url}', 301)\n}}\n"
                redirects.append(redirect_code)

# Write the redirects to an output file
output_file = 'redirects.js'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write('\n'.join(redirects))

print(f'Redirects written to {output_file}')
