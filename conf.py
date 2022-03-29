# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = os.environ['PACKAGE']
copyright = '2022, ' + os.environ['AUTHORS']
author = os.environ['AUTHORS']
version = os.environ['VERSION']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
]

# Allow to create implicit reference to headings.
# See: https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#implicit-targets
myst_heading_anchors = 2

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = os.environ['LANGUAGE']

# Set by make.
languages = os.environ['LANGUAGES'].split(' ')

# Managed by make and gettext.
gettext_auto_build = False

# Use a single POT and PO file par language.
gettext_compact = 'package'

# Display the translated string even if it is marked fuzzy.
gettext_allow_fuzzy_translations = True

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = language == 'fr'

html_context = {
    'display_github': language == 'fr',
    'github_user': 'club-1',
    'github_repo': 'docs',
    'github_version': f'{version}/',
    'languages': [(lang, f'../{lang}/') for lang in languages],
}

html_theme_options = {
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': 'edit',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# The domain is used for code documentation, so no need for it here.
primary_domain = None
