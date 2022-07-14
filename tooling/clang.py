"""
Wrap up clang tooling functionality
"""

# standard lib
from pathlib import Path
from typing import List, Dict

# local package
from tooling import settings
from tooling.utils import Log, Shell


class Clang:
    def __init__(self, cxx_formatter: Dict[str, str], cmake_formatter: Dict[str, str], linter: Dict[str, str]):
        self._shell = Shell()
        self._cxx_formatter: str = cxx_formatter["name"]
        self._cxx_formatter_flags: str = cxx_formatter["flags"]
        self._cmake_formatter: str = cmake_formatter["name"]
        self._cmake_formatter_flags: str = cmake_formatter["flags"]
        self._linter: str = linter["name"]
        self._linter_flags: str = linter["flags"]

        # gather all cpp/hpp files for all projects
        self._source_files: List[Path] = []
        # gather all cmake files for formatting
        self._cmake_files: List[Path] = []
        for project in settings.PROJECTS:
            for cpp in project.rglob("**/*.cpp"):
                self._source_files.append(cpp)
            for hpp in project.rglob("**/*.hpp"):
                self._source_files.append(hpp)
            for cmake in project.rglob("**/*.txt"):
                # BUG: Possible bug here, as regular text files
                # could be mistaken for CMakeLists.txt files.
                # it shouldn't actually break anything, but rather
                # give an unwanted outcome
                self._cmake_files.append(cmake)

    def format(self):
        """
        @desc Run clang format on all the files found in self.files
        @raises Exception if name values are None or Empty
        """
        # gather all the cmake files
        Log.info(f"Formatting all files")
        for file in self._source_files:
            if file in settings.FORMAT_IGNORE:
                Log.warn(f"Ignoring {file}")
                continue
            self._shell.execute(f"{self._cxx_formatter} {self._cxx_formatter_flags} {file}")

        print()
        for file in self._cmake_files:
            if file in settings.FORMAT_IGNORE:
                Log.warn(f"Ignoring {file}")
                continue
            self._shell.execute(f"{self._cmake_formatter} {self._cmake_formatter_flags} {file}")

    def lint(self):
        """
        @desc
        """
        Log.info(f"Statically analyzing all files")
        files = ""
        for file in self._source_files:
            if file in settings.ANALYZE_IGNORE:
                Log.warn(f"Ignoring {file}")
                continue
            files += f"{file} "
        self._shell.execute(f"{self._linter} {self._linter_flags} {files}")
