"""
Wrap up clang tooling functionality
"""

# standard lib
from pathlib import Path
from typing import List

# local package
from tooling import settings
from tooling.utils import Log, Shell


class Clang:
    def __init__(self):
        self.shell = Shell()
        self.cxx_formatter = settings.CMAKE_PROGRAMS["CLANG_FORMATTER"]["name"]
        self.cxx_formatter_flags = settings.CMAKE_PROGRAMS["CLANG_FORMATTER"]["flags"]
        self.cmake_formatter = settings.CMAKE_PROGRAMS["CMAKE_FORMATTER"]["name"]
        self.cmake_formatter_flags = settings.CMAKE_PROGRAMS["CMAKE_FORMATTER"]["flags"]
        self.linter = settings.CMAKE_PROGRAMS["CLANG_ANALYZER"]["name"]
        self.linter_flags = settings.CMAKE_PROGRAMS["CLANG_ANALYZER"]["flags"]

        # gather all cpp/hpp files for all projects
        self.source_files: List[Path] = []
        # gather all cmake files for formatting
        self.cmake_files: List[Path] = []
        for project in settings.PROJECTS:
            for cpp in project.rglob("**/*.cpp"):
                self.source_files.append(cpp)
            for hpp in project.rglob("**/*.hpp"):
                self.source_files.append(hpp)
            for cmake in project.rglob("**/*.txt"):
                # Possible bug here, as regular text files
                # could be mistaken for CMakeLists.txt files.
                # it shouldn't actually break anything, but rather
                # give an unwanted outcome
                self.cmake_files.append(cmake)

    def format(self):
        """
        @desc Run clang format on all the files found in self.files
        """
        # gather all the cmake files
        Log.info(f"Formatting all files")
        for file in self.source_files:
            if file in settings.FORMAT_IGNORE:
                Log.warn(f"Ignoring {file}")
                continue
            self.shell.execute(f"{self.cxx_formatter} {self.cxx_formatter_flags} {file}")

        print()
        for file in self.cmake_files:
            if file in settings.FORMAT_IGNORE:
                Log.warn(f"Ignoring {file}")
                continue
            self.shell.execute(f"{self.cmake_formatter} {self.cmake_formatter_flags} {file}")

    def lint(self):
        """
        @desc
        """
        Log.info(f"Statically analyzing all files")
        files = ""
        for file in self.source_files:
            if file in settings.ANALYZE_IGNORE:
                Log.warn(f"Ignoring {file}")
                continue
            files += f"{file} "
        self.shell.execute(f"{self.linter} {self.linter_flags} {files}")
