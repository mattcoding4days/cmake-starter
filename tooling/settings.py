"""
Application wide settings are here
"""

from pathlib import Path
from typing import Dict, List, Any

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
    "LICENSE": "MIT",
    "MAINTAINER": "mattcoding4days",
    "REQUIRES": "libssl-dev",
    "RELEASE": f"{distro.codename()}-{distro.version()}"
}

# Cmake stuff

# Expected programs, here compilers are specified so different versions
# can easily be swapped in and out by editing this file
CMAKE_PROGRAMS: Dict[str, Any] = {
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
        "name": "clang-tidy-13",
        "flags": f"-p {PROJECT_BUILD_DIR} --config-file={PROJECT_ROOT / '.clang-tidy'}"
    },
    # modify your compiler versions here
    "CLANG_CXX_COMPILER": "clang++-13",
    "CLANG_C_COMPILER": "clang-13",
    "GNU_CXX_COMPILER": "g++",
    "GNU_C_COMPILER": "gcc"
}

# Files that should be ignored
IGNORE: List[Path] = [
    PROJECT_ROOT / 'app' / 'src' / 'example_file.cpp',
    PROJECT_ROOT / 'app' / 'src' / 'some_other_file.cpp'
]
