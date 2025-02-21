import glob
import re

def source_redirects_in_custom_format(file_paths_glob):
    comment_syntax = r"# .*"
    redirect_syntax = r"\"?([^\"\s]*)\"?\s*\"?([^\"\s]*)\"?"
    redirects = {}
    for file_path in glob.glob(file_paths_glob):
        with open(file_path, "r") as file:
            for line in file:
                if not re.match(comment_syntax, line):
                    from_file, to_file = re.match(redirect_syntax, line).groups()
                    if from_file and to_file:
                        redirects[from_file] = to_file
    return redirects
