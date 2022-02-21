set(PACKAGE_NAME "starter_app")

#
# NOTE: `get_version()` defines the variable `${${PACKAGE_NAME}_VERSION}` which is used below to set
# the version of the library  (see `cmake/utils.cmake`)
#
get_version()

# Rename `${${PACKAGE_NAME}_VERSION}` variable to `${PACKAGE_VERSION}` for easy reference in the
# current `CMakeLists.txt` file.
set(PACKAGE_VERSION ${${PACKAGE_NAME}_VERSION})

#
# NOTE: Set our source and include directory variables for use through the build
#
set(APP_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")
set(APP_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")
set(APP_TEST_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/tests")

#
# NOTE: add additional project options
#
option(STARTER_BUILD_APP_TESTING "Enable Test builds" ON)

#
# NOTE: Prevent in source builds (can't build in src/ or in project root)
#
if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_CURRENT_BINARY_DIR OR CMAKE_CURRENT_BINARY_DIR STREQUAL APP_SOURCE_DIR)
  print(
    FATAL_ERROR
    "In source builds are not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

#
# NOTE: bring in standard cmake includes
#
# include(CMakeDependentOption) include(GNUInstallDirs)

#
# NOTE: This is where 3rd party libraries should be installed via the light weight CPM dependancy
# management system. The CPM wiki is here: https://github.com/cpm-cmake/CPM.cmake/wiki/More-Snippets
#
# NOTE: Using `CPMFindPackage()` to install package only if it is not already installed.
if(STARTER_BUILD_APP_TESTING)
  cpmfindpackage(
    NAME
    Catch2
    GITHUB_REPOSITORY
    catchorg/Catch2
    VERSION
    2.13.7)
  if(Catch2_ADDED)
    # The current `CMakeLists.txt` file installed the Catch2 package
    print(STATUS "Catch2 configured correctly")
    set(Catch2_Installed
        ON
        PARENT_SCOPE)
  elseif(Catch2_Installed)
    # The package was previously installed to the project
    print(STATUS "Catch2 already installed")
  else()
    # The package was not succesfully installed to the project
    print(WARNING "Catch2 was not configured properly")
  endif()
endif()

#
# NOTE: Manually add all header files
#
set(APP_HEADERSS
    "${APP_INCLUDE_DIR}/version.hpp"
    )

#
# NOTE: Manually add source files
#
set(APP_SOURCES
    "${APP_SOURCE_DIR}/main.cpp"
    )

#
# NOTE: Build tests with catch2
#
if(STARTER_BUILD_APP_TESTING)
  enable_testing()
  print(STATUS "${PACKAGE_NAME} -- Tests Enabled")
  add_subdirectory("tests")
endif()

#
# NOTE: Add the src/ subdirectory to finish building the executable
#
add_subdirectory("src")
