# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
from pathlib import Path

sys.path.insert(0, str(Path("../src").resolve()))

try:
    from wolpie._version import __version__
except ImportError:
    __version__ = "0.0.0"

version = __version__
release = __version__

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Wolpie"
project_copyright = "2025, Johandielangman"
author = "Johan Dielangman"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Use Markdown as the master document
master_doc = "index"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/johandielangman/wolpie",
    "use_repository_button": True,
    "use_issues_button": True,
    "path_to_docs": "docs",
    "use_edit_page_button": True,
    "show_navbar_depth": 2,
}

html_title = f"Wolpie Documentation v{version}"

# -- Extension configuration -------------------------------------------------

# Sphinx rST docstrings are handled natively - no Napoleon needed

# Autodoc settings - optimized for concise documentation
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
    "show-inheritance": True,
}

# Enable more concise autodoc output
autodoc_typehints = "description"
autodoc_typehints_description_target = "documented"

# Intersphinx configuration (disabled for faster builds)
# intersphinx_mapping = {
#     "python": ("https://docs.python.org/3/", None),
#     "requests": ("https://requests.readthedocs.io/en/latest/", None),
# }

# MyST parser configuration
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
