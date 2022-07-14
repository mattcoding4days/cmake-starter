"""
Application wide settings are here
"""

from pathlib import Path
from typing import Dict, List

import distro

# Set the Project root directory
PROJECT_ROOT = Path(__file__).resolve(strict=True).parent.parent

# Set the build directory
PROJECT_BUILD_DIR = PROJECT_ROOT / "build"

# All c++ projects must be added to this list
PROJECTS: List[Path] = [
    PROJECT_ROOT / "app",
    PROJECT_ROOT / "core"
]

# Package configurations, used for building a debian, slackware, or rpm package,
# change your information accordingly
PACKAGE_CONFIG: Dict[str, str] = {
    "BACKEND": "checkinstall",
    "LICENSE": "GPL-3.0",
    "MAINTAINER": "mattcoding4days",
    "REQUIRES": "",
    "RELEASE": f"{distro.codename()}-{distro.version()}"
}

# Cmake stuff

# Expected programs, here compilers are specified so different versions
# can easily be swapped in and out by editing this file
CMAKE_PROGRAMS: Dict[str, Dict[str, str]] = {
    # cmake is here incase a different version is being used,
    # using flags should not be necessary
    "CMAKE": {
        "name": "cmake",
        "flags": "",
    },
    # customize formatting and clang tidy through the flags
    "CLANG_FORMATTER": {
        "name": "clang-format",
        "flags": "-i"
    },
    "CMAKE_FORMATTER": {
        "name": "cmake-format",
        "flags": "-i"
    },
    "CLANG_ANALYZER": {
        "name": "clang-tidy",
        "flags": f"-p {PROJECT_BUILD_DIR} --config-file={PROJECT_ROOT / '.clang-tidy'}"
    },
    # modify your compiler versions here, flags should not be necessary
    "CLANG_CXX_COMPILER": {
        "name": "clang++",
        "flags": "",
    },
    "CLANG_C_COMPILER": {
        "name": "clang",
        "flags": "",
    },
    "GNU_CXX_COMPILER": {
        "name": "g++",
        "flags": "",
    },
    "GNU_C_COMPILER": {
        "name": "gcc",
        "flags": "",
    }
}

# Files that should be ignored for formatting (clang-format, cmake-format)
FORMAT_IGNORE: List[Path] = [
    PROJECT_ROOT / 'app' / 'src' / 'example_file.cpp',
    PROJECT_ROOT / 'app' / 'src' / 'some_other_file.cpp'
]

# Files that should be ignored for clang-tidy
ANALYZE_IGNORE: List[Path] = [
    PROJECT_ROOT / 'app' / 'tests' / 'hello_test.cpp',
    PROJECT_ROOT / 'core' / 'tests' / 'add_test.cpp'
]
