import sys
import os
sys.path.insert(0, os.path.abspath('.'))
from _modules import utilities
from _modules import mock_imports

project = "DEA Docs"
copyright = f"{utilities.current_year()}, Geoscience Australia"
author = "Geoscience Australia"
version = "0.1"

html_static_path = ["_static", "_files"]
templates_path = ["_layout", "_templates"]
html_extra_path = ["robots.txt"]
source_suffix = [".rst", ".md"]

exclude_patterns = [
    "**/.*",
    "**/_*",
    "**/*.scss",
    "**/unpublished-product",
    "notebooks/Scientific_workflows",
    "notebooks/DEA_notebooks_template.ipynb",
    "notebooks/USAGE.rst",
]
exclude_patterns += utilities.optional_exclude_pattern("ENABLE_KNOWLEDGE_HUB", "knowledge")
exclude_patterns += utilities.optional_exclude_pattern("ENABLE_DATA_PRODUCTS", "data")
exclude_patterns += utilities.optional_exclude_pattern("ENABLE_NOTEBOOKS", "notebooks")
exclude_patterns += utilities.optional_exclude_pattern("ENABLE_OLD_PRODUCT_VERSIONS", "data/old-version-product")

html_title = "DEA Docs"
html_baseurl = "https://docs.dea.ga.gov.au/"
html_logo = "_files/logos/ga-dea-combined-logo.svg"
html_favicon = "_static/favicons/dea-favicon.ico"
html_theme = 'pydata_sphinx_theme'
language = "en"

html_permalinks = False

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "myst_parser",
    "nbsphinx",
    "sphinx_design",
    "sphinxext.rediraffe",
    "sphinxcontrib.datatemplates",
    "sphinx_external_toc",
    "sphinx_sitemap",
    "sphinxext.opengraph",
]

myst_enable_extensions = [
    "colon_fence",
    "dollarmath"
]
myst_heading_anchors = 1

nbsphinx_execute = "never"

external_toc_path = "table_of_contents.yaml"

if os.environ.get("ENABLE_REDIRECTS") == "Yes" or os.environ.get("PRODUCTION_MODE") == "Yes":
    rediraffe_redirects = utilities.source_redirects("_redirects/*.txt")

sitemap_url_scheme = "{link}"

ogp_site_url = "https://docs.dea.ga.gov.au/"
ogp_image = "/_files/logos/dea-logo-inline.png"

sys.path.insert(0, os.path.abspath("./notebooks/Tools"))
autosummary_generate = ["./notebooks/Tools/index.rst"]
autodoc_default_options = {
    "members": True,
}
autodoc_mock_imports = mock_imports.mock_imports
autosummary_mock_imports = autodoc_mock_imports

napoleon_google_docstring = False
napoleon_numpy_docstring = True

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
