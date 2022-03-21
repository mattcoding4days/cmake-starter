"""
Uses checkinstall as a backend to create a debian package.
"""

import argparse
import os
import subprocess as sp
from pathlib import Path
import distro

# local package
from cmake_tooling.utils import Log


class Packager:
    """
    A simple class that uses checkinstall to build
    a debian package
    """

    def __init__(self, args: argparse.Namespace):
        self.backend = "checkinstall"
        self.shell = str(os.getenv("SHELL"))
        self.pkg_build_dir = Path(args.build_dir)
        self.pkg_name: str = args.name
        self.pkg_version: str = args.version
        self.pkg_type: str = args.type
        self.pkg_license = "MIT"
        self.pkg_maintainer = "'mattcoding4days'"
        self.pkg_requires = "libssl-dev"
        self.pkg_release = f"{distro.codename()}-{distro.version()}"
        if not self.__configure_build_env():
            Log.error(f"{self.pkg_build_dir} is an invalid build directory")
        Log.info(f"Build directory resolved => {self.pkg_build_dir}")

    def __configure_build_env(self) -> bool:
        """
        @description: Make sure the build directory passed was valid
        @returns: True if a valid CMake build directory was found, False if not
        """
        # first check if the passed directory is correct
        found = False
        if "build" in self.pkg_build_dir.stem:
            found = True
        else:
            # the stem directory is not build, but it maybe up one more directory
            for receptacle in self.pkg_build_dir.iterdir():
                if receptacle.is_dir():
                    if "build" in receptacle.stem:
                        self.pkg_build_dir = receptacle
                        found = True
        return found

    def __exec_command(self, command: str) -> None:
        """
        @description: wrapper around subproccess, if a command fails to execute properly,
         error_msg will print, and promptly exit the entire script.
        @returns: None
        """
        Log.info(f"Running: {command}")
        try:
            sp.run(command, check=True, shell=True, executable=self.shell)
            Log.info("Done.. \n")
        except sp.CalledProcessError as error:
            Log.error(f"{error}")

    def __is_installed(self, command: str) -> bool:
        """
        @description: wrapper around subproccess, to test if a program is already installed,
         this will not work for libraries etc, but only for executables
        @returns: True, False
        """
        cmd = f"command -v {command}"
        ret: sp.CompletedProcess = sp.run(
            cmd, check=False, capture_output=True, shell=True
        )
        if ret.returncode != 0:
            # the program is not installed
            return False

        Log.info(f"Found: {command}")
        return True

    def build_pkg(self) -> None:
        """
        @description: build the package with parameters that were fed to us
        """
        if not self.__is_installed(self.backend):
            Log.error(
                f"{Path(__file__).resolve(strict=True).stem} uses {self.backend} as its backend, which is not installed on the system")

        self.__exec_command(
            f"cd {str(self.pkg_build_dir)} && sudo {self.backend} -y --pkgname={self.pkg_name} --pkgrelease={self.pkg_release}"
            f" --pkgversion={self.pkg_version} --pkglicense={self.pkg_license} --requires={self.pkg_requires}"
            f" --maintainer={self.pkg_maintainer} --type={self.pkg_type} --install=yes"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="buildpkg",
        description=f"Build a debian, slackware, or rpm package for C/C++ software that uses the CMake build system",
    )

    parser.add_argument(
        "-n",
        "--name",
        type=str,
        required=True,
        help="The name of the software you are packaging"
    )

    parser.add_argument(
        "-v",
        "--version",
        type=str,
        required=True,
        help="The current version of the software you are packaging",
    )

    parser.add_argument(
        "-b",
        "--build-dir",
        type=str,
        default=f"{Path.cwd()}",
        help="path to the build directory of your CMake build, if nothing is passed, the current working directory will be scanned"
    )

    parser.add_argument(
        "-t",
        "--type",
        type=str,
        default="debian",
        help="Choose the packaging system. Can be on of 'slackware', 'debian, or 'rmp', defaults to debian"
    )

    arguments = parser.parse_args()
    packager = Packager(arguments)
    packager.build_pkg()
