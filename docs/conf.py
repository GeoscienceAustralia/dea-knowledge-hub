import os
import datetime

project = 'DEA Docs'
copyright = f'{datetime.date.today().year}, Geoscience Australia'
author = 'Geoscience Australia'
version = '0.1'

html_static_path = ['_static', '_files']
templates_path = ['_layout', '_templates']
html_extra_path = ['robots.txt']
source_suffix = ['.rst', '.md']

exclude_patterns = [
    "**/_*",
    "**/*.scss",
    "**/unpublished-product",
]

if os.environ.get("BUILD_NOTEBOOKS") == "No" or os.environ.get("PRODUCTION_MODE") == "Yes":
    exclude_patterns.append("notebooks")

html_title = "DEA Docs"
html_baseurl = "https://docs.dea.ga.gov.au/"
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
    "sphinx_external_toc",
    "sphinx_sitemap",
]

myst_enable_extensions = ["colon_fence"]
myst_heading_anchors = 1

nbsphinx_execute = "never"

external_toc_path = "table_of_contents.yaml"

# rediraffe_redirects = "redirects.txt"

sitemap_url_scheme = "{link}"

html_css_files = [
    'styles/styles.css'
]

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["search-field"],
    "navbar_persistent": [],
    "secondary_sidebar_items": [],
    "footer_start": ["footer"],
    "footer_end": [],
    "navigation_with_keys": False,
    "search_bar_text": "Search ...",
    "show_prev_next": False,
    "header_links_before_dropdown": 3,
}

html_context = {
    'google_analytics_ga4_tag': 'G-0000000000', # G-4B9D450HR4
    'support_link': 'example-support.com'
}
