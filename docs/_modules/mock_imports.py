import os

mock_imports_file = "notebooks/mock_imports.txt"
comment_symbol = "#"

mock_imports = []
project_root = os.path.dirname(os.path.dirname(__file__))
mock_imports_file_path = os.path.join(project_root, mock_imports_file)

try:
    with open(mock_imports_file_path, 'r') as file:
        lines = file.read().splitlines()

        mock_imports = []

        for line in lines:
            line = line.split(comment_symbol)[0] # Strip text after the comment symbol
            line = line.strip() # Strip leading and trailing whitespace from each line
            if line != "": # Ignore blank lines
                mock_imports.append(line)

        print(f"Sourced {len(mock_imports)} mock imports from '{mock_imports_file_path}'")
except FileNotFoundError:
    print(f"Mock imports file not found at '{mock_imports_file_path}'")
