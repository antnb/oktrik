import os

def extract_titles(input_folder, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for filename in os.listdir(input_folder):
            if filename.endswith(".md"):
                file_path = os.path.join(input_folder, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                # Find the front matter section
                if lines[0].strip() == "---":
                    end_front_matter = None
                    for i in range(1, len(lines)):
                        if lines[i].strip() == "---":
                            end_front_matter = i
                            break

                    if end_front_matter is not None:
                        # Extract the front matter section
                        front_matter = lines[1:end_front_matter]
                        
                        # Find the title
                        for line in front_matter:
                            if line.startswith("title:"):
                                title = line.split("title:")[1].strip()
                                output.write(title + '\n')
                                break

if __name__ == "__main__":
    input_folder = "_posts"  # Folder where .md files are located
    output_file = "titles.txt"  # File to save the extracted titles
    extract_titles(input_folder, output_file)
