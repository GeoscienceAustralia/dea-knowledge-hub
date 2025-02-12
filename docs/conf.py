import os
import sys
sys.path.append(os.path.abspath("./_ext"))
sys.path.insert(0, os.path.abspath('.'))
from _modules import utilities
from _modules import mock_imports
from _modules import pr_preview

build_mode = os.environ.get("BUILD_MODE")
git_branch = os.environ.get("BRANCH")
enable_redirects = os.environ.get("LOCAL_ENABLE_REDIRECTS") == "Yes"
pr_preview_subdomain = os.environ.get("PR_PREVIEW_SUBDOMAIN")

current_year = utilities.current_year()

project = "DEA Knowledge Hub"
copyright = f"{current_year}, Geoscience Australia"
author = "Geoscience Australia"

html_static_path = ["_static", "_files"]
templates_path = ["_layouts", "_templates"]
html_extra_path = ["robots.txt"]
source_suffix = [".rst", ".md"]

is_production = build_mode == "production"
is_pr_preview = build_mode == "pr-preview"

exclude_patterns = [
    "**/.*",
    "**/_*",
    "**/*.scss",
    "_robots",
    "_components",
    "data/archive",
    "notebooks/Scientific_workflows",
    "notebooks/DEA_notebooks_template.ipynb",
    "notebooks/DEA_Sandbox.ipynb",
    "notebooks/USAGE.rst",
    "notebooks/Supplementary_data/*.md",
    "notebooks/Supplementary_data/*.rst",
    "notebooks/Supplementary_data/*.ipynb",
    "py-modindex/index.*",
]
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_USER_GUIDES", "guides")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_DATA_PRODUCTS", "data")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_VERSION_HISTORY", "data/version-history")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_NOTEBOOKS", "notebooks")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_NOTEBOOKS", "dea-notebooks")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_VALIDATION_REPORTS", "validation")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_OPERATIONAL_REPORTS", "operational-reports")
exclude_patterns += utilities.optional_exclude_pattern("LOCAL_ENABLE_TECH_ALERTS_CHANGELOG", "tech-alerts-changelog")

html_title = "DEA Knowledge Hub"
html_logo = "_files/logos/ga-dea-combined-logo.svg"
html_favicon = "_static/favicons/dea-favicon.ico"
html_theme = 'pydata_sphinx_theme'
language = "en"

if is_production: html_baseurl = "https://knowledge.dea.ga.gov.au/"
elif is_pr_preview: html_baseurl = f"https://{pr_preview_subdomain}.khpreview.dea.ga.gov.au/"
else: html_baseurl = ""

html_permalinks = False
html_last_updated_fmt = '%-d %B %Y' # E.g. 1 January 2020

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
    "notfound.extension",
    "sphinx_copybutton",
]

myst_enable_extensions = [
    "colon_fence",
    "attrs_inline",
    "attrs_block",
    "dollarmath",
]
myst_heading_anchors = 6
myst_all_links_external = True

nbsphinx_requirejs_path = ""
nbsphinx_execute = "never"

external_toc_path = "table_of_contents.yaml"

if (
    is_production or is_pr_preview or enable_redirects
): rediraffe_redirects = utilities.source_redirects("_redirects/*.txt")

sitemap_url_scheme = "{link}"

ogp_site_url = "https://knowledge.dea.ga.gov.au/"
ogp_image = "/_files/logos/dea-logo-inline.png"

sys.path.insert(0, os.path.abspath("./notebooks/Tools"))
autosummary_generate = ["./notebooks/Tools/index.rst"]
autodoc_default_options = {
    "members": True,
}
autodoc_mock_imports = mock_imports.mock_imports
autosummary_mock_imports = mock_imports.mock_imports

napoleon_google_docstring = False
napoleon_numpy_docstring = True

notfound_template = "404-not-found.html"
notfound_pagename = "404-not-found"
notfound_urls_prefix = ""

html_css_files = [
    'styles/styles.css'
]

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": [
        "navbar-logo",
        "navbar-nav",
        "search-field",
    ],
    "navbar_end": [],
    "navbar_persistent": [],
    "secondary_sidebar_items": [],
    "footer_start": ["footer"],
    "footer_end": [],
    "navigation_with_keys": False,
    "search_bar_text": "Search ...",
    "show_prev_next": False,
    "header_links_before_dropdown": 5, # The number of header menu items to display before the rest are nested inside the 'More' dropdown.
    "logo": {
        "link": "/"
    },
}

if is_pr_preview:
    html_theme_options["announcement"] = pr_preview.banner()

html_context = {
    "default_mode": "light",
    "meta_keywords": "DEA, Digital Earth Australia, GA, Geoscience Australia, Knowledge, Documentation, Content, Learn, Learning, Data Products, Metadata, User Guides, DEA Notebooks, Notebooks, Open Data Cube, CMI, Content Management Interface, Developer, Python, Jupyter",
    "current_year": current_year,
}

if is_production: html_context["google_analytics_ga4_tag"] = "G-4B9D450HR4"

suppress_warnings = [
    # "etoc.toctree"
]
