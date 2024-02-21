import os

mock_imports_file = ".mock-imports"
comment_symbol = "#"

mock_imports = []

try:
    project_root = os.path.dirname(os.path.dirname(__file__))
    mock_imports_file_path = os.path.join(project_root, mock_imports_file)
    with open(mock_imports_file_path, 'r') as file:
        mock_imports = file.read().splitlines()
        mock_imports = [line.strip() for line in mock_imports] # Ignore blank lines
        mock_imports = [line for line in mock_imports if not line.startswith(comment_symbol)] # Ignore commented lines
        print(mock_imports)
except FileNotFoundError:
    print(f"File '{mock_imports_file}' not found in root folder of project.")

