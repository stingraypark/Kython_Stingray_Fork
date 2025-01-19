# Import
import yaml

# Define functions
def read_yml(file_path):
    with open(file_path, encoding='utf-8') as file:
        return yaml.load(file, Loader=yaml.FullLoader)