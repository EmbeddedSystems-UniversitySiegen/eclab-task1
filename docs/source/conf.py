# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
import os
import sys
from sphinx.ext import todo

# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EC-Lab-Task1'
copyright = '2024, University Siegen'
author = 'University Siegen'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx.ext.todo"
]

todo_include_todos = True

# conf.py``
myst_url_schemes = [
    "http",
    "https",
]  # Ensures that standard web protocols are recognized

myst_enable_extensions = [
    "dollarmath",  # Enables dollar symbol for inline math
    "amsmath",  # Allows more complex math formatting
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_favicon = "_static/unisiegen.png"

# Function to convert absolute paths to relative paths


def convert_todo_path(app, doctree, fromdocname):
    # Iterate over all nodes in the document tree
    for node in doctree.traverse(todo.todo_node):
        source_file = node.source
        if source_file:
            # Convert the absolute path to a relative path
            rel_path = os.path.relpath(source_file, start=app.srcdir)
            # Update the node's source attribute to the relative path
            node.source = rel_path


# Add the above function to the Sphinx setup
def setup(app):
    app.connect("doctree-resolved", convert_todo_path)
