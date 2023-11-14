import os
import sys
import glob
import re
import datetime

def current_year():
    return datetime.date.today().year

def optional_exclude_pattern(environment_variable, exclude_pattern):
    if os.environ.get(environment_variable) == "No" and not os.environ.get("PRODUCTION_MODE") == "Yes":
        return exclude_pattern
    else:
        return []

def source_redirects(filepath):
    redirects = {}
    for redirects_file in glob.glob(filepath):
        with open(redirects_file, "r") as redirects:
            for line in redirects:
                if not line.startswith("# "):
                    from_file, to_file = re.match(r"\"?([^\"\s]*)\"?\s*\"?([^\"\s]*)\"?", line).groups()
                    redirects[from_file] = to_file
    return redirects
