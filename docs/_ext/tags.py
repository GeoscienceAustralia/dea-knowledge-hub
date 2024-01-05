# A custom directive for adding tags to pages.

import os
import re
from fnmatch import fnmatch
from pathlib import Path
from typing import List
from docutils import nodes
from sphinx.errors import ExtensionError
from sphinx.util.docutils import Directive
from sphinx.util.logging import getLogger
from sphinx.util.rst import textwidth

# Configuration
tags_dir = "tags"
tags_heading = "Tags"

class Tags(Directive):
    def run(self):
        result = nodes.reference(refuri="https://google.com/", text="Test")

        return [result]

def setup(app):
    app.add_directive("tags", Tags)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }









