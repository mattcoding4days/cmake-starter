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
        self.linter = settings.CMAKE_PROGRAMS["CLANG_ANALYZER"]

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
        Log.info("Formatting CXX files...")
        for file in self.source_files:
            self.shell.execute(f"{self.cxx_formatter} -i {file}")

        Log.complete(f"Done..\n")
        Log.info("Formatting CmakeLists files...")
        for file in self.cmake_files:
            self.shell.execute(f"{self.cmake_formatter} -i {file}")

        Log.complete(f"Done..")

    def lint(self):
        """
        @desc
        """
        for file in self.source_files:
            Log.info(f"Linting -> {file}")

        Log.complete(f"Linting complete..")
