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

class TagLinks(SphinxDirective):
    # Sphinx directive attributes
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True
    final_argument_whitespace = True

    # Custom attributes
    separator = ","

    def run(self):
        if not (self.arguments or self.content):
            raise ExtensionError("No tags passed to 'tags' directive.")

        tagline = []
        # Normalize white space and remove linebreaks
        if self.arguments:
            tagline.extend(self.arguments[0].split())
        if self.content:
            tagline.extend((" ".join(self.content)).strip().split())

        tags = [tag.strip() for tag in (" ".join(tagline)).split(self.separator)]

        tag_dir = Path(self.env.app.srcdir) / tags_dir
        result = nodes.paragraph()
        result["classes"] = ["tags"]
        result += nodes.inline(text=tags_heading)
        count = 0

        current_doc_dir = Path(self.env.doc2path(self.env.docname)).parent
        relative_tag_dir = Path(os.path.relpath(tag_dir, current_doc_dir))

        for tag in tags:
            count += 1

            file_basename = _normalize_tag(tag)

            if self.env.app.config.tags_create_badges:
                result += self._get_badge_node(tag, file_basename, relative_tag_dir)
                tag_separator = " "
            else:
                result += self._get_plaintext_node(tag, file_basename, relative_tag_dir)
                tag_separator = f"{self.separator} "
            if not count == len(tags):
                result += nodes.inline(text=tag_separator)

        # register tags to global metadata for document
        self.env.metadata[self.env.docname]["tags"] = tags

        return [result]

    def _get_plaintext_node(
        self, tag: str, file_basename: str, relative_tag_dir: Path
    ) -> List[nodes.Node]:
        """Get a plaintext reference link for the given tag"""
        link = relative_tag_dir / f"{file_basename}.html"
        return nodes.reference(refuri=str(link), text=tag)

    def _get_badge_node(
        self, tag: str, file_basename: str, relative_tag_dir: Path
    ) -> List[nodes.Node]:
        """Get a sphinx-design reference badge for the given tag"""
        from sphinx_design.badges_buttons import XRefBadgeRole

        # Required to set Inliner state, since we're directly creating a role object.
        # Typically this would be done when parsing the role from document text.
        text_nodes, messages = self.state.inline_text("", self.lineno)

        # Ref paths always use forward slashes, even on Windows
        tag_ref = f"{tag} <{relative_tag_dir.as_posix()}/{file_basename}>"
        tag_color = self._get_tag_color(tag)
        tag_badge = XRefBadgeRole(tag_color)
        return tag_badge(
            name=f"bdg-ref-{tag_color}",
            rawtext=tag,
            text=tag_ref,
            lineno=self.lineno,
            inliner=self.state.inliner,
        )[0]

    def _get_tag_color(self, tag: str) -> str:
        """Check for a matching user-defined color for a given tag.
        Defaults to theme's primary color.
        """
        tag_colors = self.env.app.config.tags_badge_colors or {}
        for pattern, color in tag_colors.items():
            if fnmatch(tag, pattern):
                return color
        return "primary"

















class Tags(Directive):
    def run(self):
        paragraph_node = nodes.paragraph(text='Tags ...')
        return [paragraph_node]

def setup(app):
    app.add_directive("tags", Tags)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }









