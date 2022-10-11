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
from gettext import translation
from sphinx import __version__ as sphinx_version
from sphinx.util.logging import getLogger
from myst_parser import __version__ as myst_version
from sphinx_rtd_theme import __version__ as rtd_version
from docutils import __version__ as docutils_version
from importlib.util import find_spec
import sys
sys.path.insert(0, os.path.abspath('./_ext'))
logger = getLogger(__name__)


# -- Project information -----------------------------------------------------

project = os.environ['PACKAGE']
author = os.environ['AUTHORS']
version = os.environ['VERSION']
release = os.environ['RELEASE']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = os.environ['LOCALE']
languages = os.environ['LANGUAGES'].split(' ')

t = translation('package', './_locales', [language], fallback=True)
_ = t.gettext

title = _('Documentation %s') % project
copyright = _('%s, Membres de CLUB1') % '2022'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'french_typography',
    'term_tooltips',
    'index_role',
]

extensions_optionnal = {
    'sphinx-notfound-page': 'notfound.extension',
    'sphinx-last-updated-by-git': 'sphinx_last_updated_by_git',
}

for (package, module) in extensions_optionnal.items():
    if find_spec(module.split('.', 1)[0]) is not None:
        extensions.append(module)
    else:
        logger.info(f'package {package} is not installed, not using {module} extension')

# Allow to create implicit reference to headings up to level 6.
# See: https://docs.readthedocs.io/en/stable/guides/cross-referencing-with-sphinx.html#implicit-targets
myst_heading_anchors = 6

# Enable Some MyST extensions.
myst_enable_extensions = [
    'substitution',
]

# Define some substitution strings.
myst_substitutions = {
    'copyright': copyright,
    'sphinx_version': sphinx_version,
    'myst_version': myst_version,
    'rtd_version': rtd_version,
    'docutils_version': docutils_version,
}

# Strip everything after the last emdash in term's tooltips.
term_tooltips_apply_function = lambda s: s.rsplit('—', 1)[0].strip()

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Directory that contains the translated messages
locale_dirs = ['_locales']

# Managed by make and gettext.
gettext_auto_build = False

# Use a single POT and PO file par language.
gettext_compact = 'package'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'README*',
    'Thumbs.db',
    '.DS_Store',
]

# Enable smart quotes at Sphinx level to support localized quotes.
smartquotes = True

# Date formats for today, for instance in LaTeX.
# Use locale’s appropriate date representation.
today_fmt = '%x'

# Add numbers to figures
numfig = True

# List of downloads to include in the site version seletor.
downloads = []

if "DOWNLOADS" in os.environ:
    downloads = os.environ['DOWNLOADS'].split(' ')

# The domain is used for code documentation, so no need for it here.
primary_domain = None

# -- Options for HTML output -------------------------------------------------

# Used for canonical URLs and absolute links.
html_domain = 'https://club1.fr'
html_basedir = 'docs'
html_basepath = f'{html_domain}/{html_basedir}'

# Used for cannonical URLs.
html_baseurl = f'{html_basepath}/{language}'

html_favicon = '_static/favicon.ico'
# %s will be replaced by the project name
html_title = title

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'club1.css',
]

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

html_logo = '_static/club1logo.png'

# Do not copy source as the link to view source as been replaced by a link to
# GitHub.
html_copy_source = False

# Only show source link for french docs as other languages are stored in .po.
html_show_sourcelink = language == 'fr'

html_context = {
    'basepath': f'{html_basepath}',
    'version': release,
    'display_github': language == 'fr',
    'github_user': 'club-1',
    'github_repo': 'docs',
    'github_version': f'{version}/',
    'languages': [(lang, f'../{lang}/') for lang in languages],
    'downloads': [(dl.split('.')[-1], dl) for dl in downloads],
}

html_theme_options = {
    'logo_only': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': 'edit',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Format the date relative to the current locale.
html_last_updated_fmt = '%x'

# Use Paris timezone for display of last updated dates.
git_last_updated_timezone = 'Europe/Paris'

git_exclude_commits = [
    '130f8dd3322f42ceed64c706038e95ef15c96d97', # fix: markdownlint issues
    '2f1d07a2df3e1e83d94009ccac2d9005f55087d9', # docs: suppression de &nbsp; non nécessaires
]

git_exclude_patterns = [
    '**/docutils.conf',
]

# Base URL for 404 page's absolute links to resources.
notfound_urls_prefix = f'/{html_basedir}/{language}/'

# Template used for 404 error page.
notfound_template = '404.html'

# -- Options for MAN output --------------------------------------------------

# Show URLs after text in MAN output.
man_show_urls = True

# -- Options for EPUB output -------------------------------------------------

# Exclude files that are not needed in EPUB format.
epub_exclude_files = [
    # Favicon is only needed for HTML output.
    '_static/favicon.ico',
    # This file is downloaded from the website.
    '_static/tutos/mes-premiers-pas-sur-le-web/bonjour.txt', ]

# -- Options for LATEX output ------------------------------------------------

# Use LuaLaTeX for Unicode support, especially emojis.
latex_engine = 'lualatex'

latex_documents = [
    ('index', 'club1.tex', title, author.replace(',', r'\\'), 'manual'),
]

# Add footnote for external URLs, useful for printed copies.
latex_show_urls = 'footnote'

# Show pages for internal refs, useful for printed copies.
latex_show_pagerefs = True

latex_additional_files = ['_templates/club1.sty', '_templates/packages.sty']

latex_license = _(open('_templates/license.txt', 'r').read().strip()).replace('<', r'\url{').replace('>', '}')

latex_elements = {
    # Always use A4 paper.
    'papersize': 'a4paper',
    # Make sure to use babel instead of polyglossia.
    'babel': r'\usepackage{babel}',
    # Uniformization of chapter style, disable Sphinx default.
    'fncychap': '',
    # Use names for colors.
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames,table}{xcolor}',
    # Clear default font config.
    'fontpkg': '',
    # Packages to include before 'hyperref' and after 'sphinx'.
    'extrapackages': r'\usepackage{packages}',
    # Add custom preamble after 'hyperref' and 'sphinx'.
    'preamble': r'''
\usepackage{club1}
\newcommand\sphinxbackoftitlepage{\null\vfill
Copyright © %s.

%s}
''' % (copyright, latex_license),
}

# -- Options for linkcheck output --------------------------------------------

# Allow some redirects.
linkcheck_allowed_redirects = {
    r'https://github\.com/club-1/docs/edit/.*': r'https://github\.com/login\?return_to=https%3A%2F%2Fgithub\.com%2Fclub-1%2Fdocs%2Fedit%2F.*',
    r'https://gnu\.org/licenses/fdl\.html': r'https://www\.gnu\.org/licenses/fdl-[0-9]+\.[0-9]+\.html',
}

# -- Global setup ------------------------------------------------------------
def override_html_permalink_icon(app):
    app.config.html_permalinks_icon = "#"

def setup(app):
    app.connect('builder-inited', override_html_permalink_icon)
