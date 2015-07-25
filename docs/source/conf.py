# -*- coding: utf-8 -*-
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

#needs_sphinx = '1.0'
extensions = [
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Raycrafter'
copyright = '2015, David Zuber'
author = 'David Zuber'

version = '0.1.0'
release = '0.1.0'

language = None
exclude_patterns = []
pygments_style = 'sphinx'
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']
htmlhelp_basename = 'Raycrafterdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}
latex_documents = [
  (master_doc, 'Raycrafter.tex', 'Raycrafter Documentation',
   'David Zuber', 'manual'),
]

# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'raycrafter', 'Raycrafter Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

texinfo_documents = [
  (master_doc, 'Raycrafter', 'Raycrafter Documentation',
   author, 'Raycrafter', 'One line description of project.',
   'Miscellaneous'),
]

# -- Intersphinx Config ----------------------------------------------------

intersphinx_mapping = {'python': ('https://docs.python.org/', None),
                       'ansible-raycrafter': ('http://ansibleraycrafter.readthedocs.org/en/latest/', None),
                       'clusterclienttest': ('http://clusterclienttest.readthedocs.org/en/latest/', None),
                       'clusterlogger': ('http://clusterlogger.readthedocs.org/en/latest/', None),
}
