# Adds metadata to pages based on the Git version history. It sources information from the 'last updated' commit and the 'created at' commit for each page. Metadata includes the date of the commit and the name of its author. This metadata can be used in layouts and templates, for example: {{ page_version_history_metadata.last_updated_date }}

import os
import subprocess
import traceback

def run_git_log(command):
    result = subprocess.run(
        command,
        check=True,
        encoding="UTF-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )

    return result.stdout.strip().split('|')

def handle_exception(error):
    print(error)
    traceback.print_exc()
    pass

def page_version_history_metadata(app, pagename, templatename, context, doctree):
    page_filepath_absolute_with_extension_glob = os.path.join(app.srcdir, pagename + ".*")

    context["page_version_history_metadata"] = {
        "last_updated_hash": None,
        "last_updated_date": None,
        "last_updated_author_name": None,
        "last_updated_subject": None,
        "created_at_hash": None,
        "created_at_date": None,
        "created_at_author_name": None,
        "created_at_subject": None,
    }

    try:
        git_log_results = run_git_log(
            [
                "git",
                "log",
                "-1",
                "--date=format:%-d %b %Y",
                "--pretty=format:%H|%ad|%an|%s",
                "--",
                page_filepath_absolute_with_extension_glob,
            ]
        )

        print(git_log_results) # TODO Remove this after testing

        context["page_version_history_metadata"]["last_updated_hash"] = git_log_results[0]

        context["page_version_history_metadata"]["last_updated_date"] = git_log_results[1]

        context["page_version_history_metadata"]["last_updated_author_name"] = git_log_results[2]

        context["page_version_history_metadata"]["last_updated_subject"] = git_log_results[3]

    except (ValueError, Exception) as e:
        handle_exception(e)

    try:
        git_log_results = run_git_log(
            [
                "git",
                "log",
                "-1",
                "--follow",
                "--diff-filter=A",
                "--date=format:%-d %b %Y",
                "--pretty=format:%H|%ad|%an|%s",
                "--",
                page_filepath_absolute_with_extension_glob,
            ]
        )

        print(git_log_results) # TODO Remove this after testing

        context["page_version_history_metadata"]["created_at_hash"] = git_log_results[0]

        context["page_version_history_metadata"]["created_at_date"] = git_log_results[1]

        context["page_version_history_metadata"]["created_at_author_name"] = git_log_results[2]

        context["page_version_history_metadata"]["created_at_subject"] = git_log_results[3]

    except (ValueError, Exception) as e:
        handle_exception(e)

def setup(app):
    app.connect('html-page-context', page_version_history_metadata)

    return {
        "version": "1"
    }
