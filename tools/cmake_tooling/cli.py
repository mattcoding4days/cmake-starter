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
        parser.add_argument(
            "-l",
            "--list-sessions",
            help="show all vim session files in VIM_SESSIONS directory",
            action="store_true",
        )
        parser.add_argument(
            "-r", "--remove-session", help="remove a vim session file by name", type=str
        )
        parser.add_argument(
            "-o", "--open-session", help="open a vim session file by name", type=str
        )
        self.__args = parser.parse_args()

    @property
    def args(self) -> argparse.Namespace:
        """
        @description: Return the argparse object
        """
        return self.__args
