import os
import datetime

def current_year():
    return datetime.date.today().year

def optional_exclude_pattern(environment_variable, exclude_pattern):
    if (
        os.environ.get(environment_variable) == "No"
        and not os.environ.get("BUILD_MODE") in ["pr-preview", "production"]
    ):
        return [exclude_pattern]
    else:
        return []

