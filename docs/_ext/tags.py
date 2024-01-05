from docutils import nodes
from docutils.parsers.rst import Directive

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
