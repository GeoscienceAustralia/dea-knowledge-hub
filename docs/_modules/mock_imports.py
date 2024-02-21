import os

mock_imports_file = ".mock-imports"
comment_symbol = "#"

mock_imports = []
project_root = os.path.dirname(os.path.dirname(__file__))
mock_imports_file_path = os.path.join(project_root, mock_imports_file)

try:
    with open(mock_imports_file_path, 'r') as file:
        lines = file.read().splitlines()
        lines = [line.strip() for line in mock_imports] # Ignore blank lines
        lines = [line for line in mock_imports if not line.startswith(comment_symbol)] # Ignore commented lines
        mock_imports = lines
except FileNotFoundError:
    print(f"File '{mock_imports_file}' not found in root folder of project.")

