extensions = []
templates_path = ["_templates"]
source_suffix = '.rst'
root_doc = "modules"
project = "htLib"
copyright = "2022, Harol"
author = "Harol Alvarado"

version = "1.0"
language = None
pygments_style="sphinx"
html_theme ="alabaster"
html_static_path=["_static"]

from sys import path

path.append("C:\\Users\\Harol\\Desktop\\HT\\desktop\\coding\\python\\libserial\\docs")

path.append("C:/Users/Harol/Desktop/HT/desktop/coding/python/libserial/src/htLib")

print(path)

extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.autodoc')
#extensions.append('sphinx.ext.autosummary')
extensions.append('sphinx.ext.intersphinx')
extensions.append('sphinx.ext.mathjax')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.graphviz')
extensions.append('sphinx.ext.napoleon')
