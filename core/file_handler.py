# Import
import os

# Define functions
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def get_file_name(file_path):
    base_name = os.path.basename(file_path)
    return os.path.splitext(base_name)[0]