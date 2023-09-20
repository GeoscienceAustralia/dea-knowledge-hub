project = 'DEA Docs'
copyright = '2023, Geoscience Australia'
author = 'Geoscience Australia'
version = '0.1'

html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ["**/_*.md", "notebooks"]
source_suffix = ['.rst', '.md']

html_title = "DEA Docs"
html_logo = "https://docs.dea.ga.gov.au/_images/dea-logo-inline.svg"
html_favicon = "https://docs.dea.ga.gov.au/_static/dea-favicon.ico"
html_theme = 'pydata_sphinx_theme'
language = "en"

extensions = [
    "m2r2",
    "nbsphinx",
    "sphinx_design",
    "sphinx_external_toc",
    "sphinxext.rediraffe",
    "sphinxcontrib.datatemplates",
    "sphinx_tags",
]

external_toc_path = "table_of_contents.yaml"

rediraffe_redirects = "redirects.txt"

tags_create_tags = True
tags_overview_title = "Tags"
tags_page_title = "Pages with tag"
tags_output_dir = "tags"
tags_extension = ["md", "rst"]
tags_create_badges = True

html_sidebars = {
    "index": [],
    "**": ["sidebar-nav-bs"],
}

html_css_files = [
    'styles-ga/theme.css',
    'styles-ga/global.css',
    'styles-ga/pages.css',
]

html_theme_options = {
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field"],
    "navbar_persistent": [],
    "secondary_sidebar_items": ["page-toc"],
    "footer_start": [
        "acknowledgement-of-country",
        "footer-links",
        "copyright"
    ],
    "footer_end": [],
    "navigation_with_keys": False,
    "search_bar_text": "Search ...",
    "show_nav_level": 1,
    "show_prev_next": False,
}
