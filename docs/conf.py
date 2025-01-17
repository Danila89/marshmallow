# -*- coding: utf-8 -*-
#
# marshmallow documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import datetime as dt

import alabaster
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath(os.path.join('..', 'src')))
import marshmallow  # noqa
from marshmallow.compat import OrderedDict  # noqa

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'alabaster',
    'sphinx_issues',
    'versionwarning.extension',
]

primary_domain = 'py'
default_role = 'py:obj'

intersphinx_mapping = {
    'python': ('http://python.readthedocs.io/en/latest/', None),
}

issues_github_path = 'marshmallow-code/marshmallow'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'
# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'marshmallow'
copyright = ' {0:%Y} <a href="https://stevenloria.com">Steven Loria</a>'.format(
    dt.datetime.utcnow()
)

version = release = marshmallow.__version__

exclude_patterns = ['_build']

# THEME

html_theme_path = [alabaster.get_path()]
html_theme = 'alabaster'
html_static_path = ['_static']
templates_path = ['_templates']
html_show_sourcelink = False

html_theme_options = {
    'logo': 'marshmallow-logo.png',
    'description': 'Object serialization and deserialization, lightweight and fluffy.',
    'description_font_style': 'italic',
    'github_user': 'marshmallow-code',
    'github_repo': 'marshmallow',
    'github_banner': True,
    'github_type': 'star',
    'opencollective': 'marshmallow',
    'tidelift_url': 'https://tidelift.com/subscription/pkg/pypi-marshmallow?utm_source=marshmallow&utm_medium=referral&utm_campaign=docs ',
    'code_font_size': '0.8em',
    'warn_bg': '#FFC',
    'warn_border': '#EEE',
    # Used to populate the useful-links.html template
    'extra_nav_links': OrderedDict([
        ('marshmallow @ PyPI', 'http://pypi.python.org/pypi/marshmallow'),
        ('marshmallow @ GitHub', 'http://github.com/marshmallow-code/marshmallow'),
        ('Issue Tracker', 'http://github.com/marshmallow-code/marshmallow/issues'),
    ])
}

html_sidebars = {
    'index': [
        'about.html', 'donate.html', 'useful-links.html', 'searchbox.html',
    ],
    '**': ['about.html', 'donate.html', 'useful-links.html',
           'localtoc.html', 'relations.html', 'searchbox.html']
}

# sphinx-version-warning config
versionwarning_messages = {
    'latest': 'This document is for the development version. For the stable version documentation, see <a href="/en/stable/">here</a>.',
    'stable': 'This document is for the latest stable release. For the 3.0 pre-release documentation, see <a href="/en/3.0/">here</a>.',
    '3.0': 'This document is for the latest 3.0 pre-release. For the 2.x documentation, see <a href="/en/2.x-line/">here</a>.',
    '2.x-line': 'This document is for the 2.x release branch. For the 3.0 pre-release documentation, see <a href="/en/3.0/">here</a>.',
}
# Show warning at top of page
versionwarning_body_selector = 'div.document'
# For debugging locally
# versionwarning_project_version = '3.0'

# https://docs.readthedocs.io/en/latest/guides/adding-custom-css.html
def setup(app):
    app.add_stylesheet('css/versionwarning.css')
