"""
Uses checkinstall as a backend to create a debian package.
"""

# standard lib
from pathlib import Path

# local package
from tooling.settings import PACKAGE_CONFIG
from tooling.utils import Log, Shell


class Packager:
    """
    A simple class that uses checkinstall to build
    a debian package
    """

    def __init__(self, build_dir: Path, pkg_name: str, pkg_version: str, pkg_type: str):
        if not build_dir.exists():
            raise Exception(
                f"Build directory {build_dir} does not exist, aborting...")

        self.shell = Shell()
        self.backend = PACKAGE_CONFIG["backend"]
        if not self.shell.is_installed(self.backend):
            raise Exception(
                f"The packaging backend [{self.backend}] was not found on the system, please install and try again")
        self.license = PACKAGE_CONFIG["LICENSE"]
        self.maintainer = PACKAGE_CONFIG["MAINTAINER"]
        self.requires= PACKAGE_CONFIG["REQUIRES"]
        self.release = PACKAGE_CONFIG["RELEASE"]
        self.build_dir = build_dir
        self.name: str = pkg_name
        self.version: str = pkg_version
        self.type: str = pkg_type

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

    def build_pkg(self) -> None:
        """
        @description: build the package with parameters that were fed to us
        """
        self.shell.execute(
            f"cd {str(self.build_dir)} && sudo {self.backend} -y --pkgname={self.name} --pkgrelease={self.release}"
            f" --pkgversion={self.version} --pkglicense={self.license} --requires={self.requires}"
            f" --maintainer={self.maintainer} --type={self.type} --install=yes"
        )
