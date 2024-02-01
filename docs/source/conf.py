# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os
# The code of the modules can be found at the root of the repository
sys.path.insert(0, os.path.abspath('../..'))

project = 'assignment-1'
copyright = '2024, Dante Astorga Castillo, Rasmus Danielsson, Sebastian Montén, Ludvig Skare, Victor Stenmark'
author = 'Dante Astorga Castillo, Rasmus Danielsson, Sebastian Montén, Ludvig Skare, Victor Stenmark'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
