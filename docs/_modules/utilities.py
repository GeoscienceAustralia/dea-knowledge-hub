import os
import sys
import glob
import re
import datetime

def current_year():
    return datetime.date.today().year

def optional_exclude_pattern(environment_variable, exclude_pattern):
    if (
        os.environ.get(environment_variable) == "No"
        and not os.environ.get("BUILD_MODE") in ["demo", "production"]
    ):
        return [exclude_pattern]
    else:
        return []

def source_redirects(file_paths_glob):
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
