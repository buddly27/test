# -*- coding: utf-8 -*-

"""Awesome Project documentation build configuration file."""

import os
import re

# -- General ------------------------------------------------------------------

# Extensions.
extensions = ["sphinxcontrib.doxylink", "lowdown"]

if os.environ.get("READTHEDOCS"):
    import doxygen

    doxygen.create_cmake_config()
    doxygen.build()

    html_extra_path = ["./api"]

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Awesome Project"
copyright = u"2023, Jeremy Retailleau"

_root = os.path.join(os.path.dirname(__file__), "..", "..")

# Version
with open(os.path.join(_root, "CMakeLists.txt")) as _version_file:
    _version = re.search(
        r"project\(.* VERSION ([\d\\.]+)", _version_file.read(), re.DOTALL
    ).group(1)

version = _version
release = _version

doxylink = {
    "awesome-project-cpp": (
        os.path.join(_root, "build", "doc", "doc", "awesome-project.tag"),
        os.path.join(_root, "build", "doc", "doc", "doxygen")
    )
}

# -- HTML output --------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

# If True, copy source rst files to output for reference.
html_copy_source = True
