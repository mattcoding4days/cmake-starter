"""
Compiler module
"""

from tooling import settings
from tooling.utils import Log, Shell


class Compiler:
    """
    @desc a very light wrapper around cmake compiler type,
    its mostly just to make command line compiling a bit easier and less cumbersome
    """

    def __init__(self, cxx_compiler: str, c_compiler: str):
        self.shell = Shell()
        self.cxx_compiler = cxx_compiler
        self.c_compiler = c_compiler

    def __init_build(self) -> bool:
        """
        @desc
        @return True if the command succeeds, False if otherwise
        """
        return self.shell.execute(
                f"cmake -B {settings.PROJECT_BUILD_DIR.stem} -D CMAKE_CXX_COMPILER={self.cxx_compiler} -D CMAKE_C_COMPILER={self.c_compiler}")


    def compile(self) -> bool:
        """
        @desc
        @returns True if compiling succeeds, false otherwise
        """
        Log.info("Configuring the project..")
        if not settings.PROJECT_BUILD_DIR.exists():
            if not self.__init_build():
                return False
            if not self.shell.execute(f"cmake --build {settings.PROJECT_BUILD_DIR.stem} -- -j$(nproc)"):
                return False

            Log.complete("Done..")
            return True

        # if the build dir already exists we are just going to recompile
        Log.warn(
            f"{settings.PROJECT_BUILD_DIR} already exists, re-compiling with existing settings")
        if not self.shell.execute(f"cmake --build {settings.PROJECT_BUILD_DIR.stem}"):
            return False

        Log.complete("Done..")
        return True
