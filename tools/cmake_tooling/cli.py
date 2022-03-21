"""
Command line interface code goes here
"""


import argparse


class Cli:
    """
    @description Wraps the built-in argparse library
    """

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog="cortex_tool",
            usage="%(prog)s [options]",
            description="Helper command line tool to be used by cortex developers and in the ci/cd pipeline",
            allow_abbrev=False,
        )

        # create subcommand parser
        sub_commands = parser.add_subparsers(help="Available subcommands")

        # create the clang tooling commands
        clang_commands = sub_commands.add_parser("clang", help="Execute linting and static analyzing with clang tooling")
        clang_commands.add_argument("--format", action="store_true", help="Format all projects recursively")
        clang_commands.add_argument("--lint", action="store_true", help="Lints all files")

        parser.add_argument(
            "-",
            "--list-sessions",
            help="show all vim session files in VIM_SESSIONS directory",
            action="store_true",
        )
        self.__args = parser.parse_args()

    @property
    def args(self) -> argparse.Namespace:
        """
        @description: Return the argparse object
        """
        return self.__args
