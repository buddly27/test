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
    build_path = doxygen.build()
    source_path = os.path.join(os.path.dirname(__file__), "..", "..")

    html_extra_path = ["./api"]

else:
    # variables provided by CMake if not using RTD.
    build_path = "@CMAKE_CURRENT_BINARY_DIR@/doc"
    source_path = "@PROJECT_SOURCE_DIR@"

# The suffix of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = u"Awesome Project"
copyright = u"2023, Jeremy Retailleau"

# Version
with open(os.path.join(source_path, "CMakeLists.txt")) as _version_file:
    _version = re.search(
        r"project\(.* VERSION ([\d\\.]+)", _version_file.read(), re.DOTALL
    ).group(1)

version = _version
release = _version

doxylink = {
    "awesome-project-cpp": (
        os.path.join(build_path, "awesome-project.tag"),
        "./doxygen"
    )
}

# -- HTML output --------------------------------------------------------------

html_theme = "sphinx_rtd_theme"

# If True, copy source rst files to output for reference.
html_copy_source = True
