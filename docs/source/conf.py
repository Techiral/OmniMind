# docs/source/conf.py
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

project = 'OmniMind'
copyright = '2025, Techiral'
author = 'Lakshya Gupta'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}