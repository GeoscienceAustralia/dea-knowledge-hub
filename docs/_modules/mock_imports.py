import os

mock_imports_file = ".mock-imports"
comment_symbol = "#"

mock_imports = []
project_root = os.path.dirname(os.path.dirname(__file__))
mock_imports_file_path = os.path.join(project_root, mock_imports_file)

try:
    with open(mock_imports_file_path, 'r') as file:
        lines = file.read().splitlines()
        lines = [line.strip() for line in lines] # Strip leading and trailing whitespace from each line
        lines = [line for line in lines if line] # Ignore blank lines
        lines = [line for line in lines if not line.startswith(comment_symbol)] # Ignore commented lines
        mock_imports = lines
        print(f"Sourced {len(mock_imports)} mock imports from '{mock_imports_file_path}'")
except FileNotFoundError:
    print(f"Mock imports file not found at '{mock_imports_file_path}'")

