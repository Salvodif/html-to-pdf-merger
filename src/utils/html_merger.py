import os

def merge_html_files(directory):
    merged_content = ""
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='latin-1') as file:  # Change encoding if needed
                merged_content += file.read() + "\n"
    return merged_content