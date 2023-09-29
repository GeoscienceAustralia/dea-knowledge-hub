import datetime

project = 'DEA Docs'
copyright = f'{datetime.date.today().year}, Geoscience Australia'
author = 'Geoscience Australia'
version = '0.1'

html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ["**/_*", "notebooks"]
source_suffix = ['.rst', '.md']

html_title = "DEA Docs"
html_logo = "https://docs.dea.ga.gov.au/_images/dea-logo-inline.svg"
html_favicon = "https://docs.dea.ga.gov.au/_static/dea-favicon.ico"
html_theme = 'pydata_sphinx_theme'
language = "en"

html_permalinks = False

extensions = [
    "myst_parser",
    "nbsphinx",
    "sphinx_design",
    "sphinxext.rediraffe",
    "sphinxcontrib.datatemplates",
]

myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 1

rediraffe_redirects = "redirects.txt"

html_sidebars = {
    "index": [],
    "**": ["sidebar-nav-bs"],
}

html_css_files = [
    'styles/themevars.css',
    'styles/global.css',
    'styles/pages.css',
]

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field"],
    "navbar_persistent": [],
    "secondary_sidebar_items": [],
    "footer_start": ["footer-v1"],
    "footer_end": [],
    "navigation_with_keys": False,
    "search_bar_text": "Search ...",
    "show_prev_next": False,
    "show_nav_level": 1,
    "header_links_before_dropdown": 1,
}

html_context = {
    'support_link': 'example-support.com',
}
