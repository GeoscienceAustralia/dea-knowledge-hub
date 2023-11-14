import os
import sys
import glob
import re
import datetime

def current_year():
    return datetime.date.today().year

def optional_exclude_pattern(environment_variable, exclude_pattern):
    if os.environ.get(environment_variable) == "No" and not os.environ.get("PRODUCTION_MODE") == "Yes":
        return [exclude_pattern]
    else:
        return []

def source_redirects(file_paths_glob):
    redirect_syntax = r"\"?([^\"\s]*)\"?\s*\"?([^\"\s]*)\"?"
    comment_syntax = r"# .*"
    redirects = {}
    for file_path in glob.glob(file_paths_glob):
        with open(file_path, "r") as file:
            for line in file:
                if not re.match(comment_syntax, line):
                    from_file, to_file = re.match(redirect_syntax, line).groups()
                    redirects[from_file] = to_file
    return redirects
