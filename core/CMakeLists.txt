set(PACKAGE_NAME "starter_core")

#
# NOTE: `get_version()` defines the variable `${${PACKAGE_NAME}_VERSION}` which is used below to set
# the version of the library  (see `cmake/utils.cmake`)
#
get_version()

#
# NOTE: Rename `${${PACKAGE_NAME}_VERSION}` variable to `${PACKAGE_VERSION}` for easy reference in the
# current `CMakeLists.txt` file.
#
set(PACKAGE_VERSION ${${PACKAGE_NAME}_VERSION})

#
# NOTE: Set our source and include directory variables for use through the build
#
set(CORE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")
set(CORE_TEST_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/tests")
set(CORE_EXAMPLES_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/examples")
set(CORE_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")

#
# NOTE: add additional project options
#
option(STARTER_BUILD_CORE_TESTING "Enable Test builds" ON)
option(STARTER_BUILD_CORE_EXAMPLES "Enable example builds" ON)

#
# NOTE: Prevent in source builds (can't build in src/ or in project root)
#
if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_CURRENT_BINARY_DIR OR CMAKE_CURRENT_BINARY_DIR STREQUAL CORE_SOURCE_DIR)
  print(
    FATAL_ERROR
    "In source builds are not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

#
# NOTE: This is where 3rd party libraries should be installed via the light weight CPM dependancy
# management system. The CPM wiki is here: https://github.com/cpm-cmake/CPM.cmake/wiki/More-Snippets
#
# NOTE: googletest version >= 3.11.0 now has google mock, and google benchmark libraries built into it,
# so we get 3 for 1
#
# NOTE: Using `CPMFindPackage()` to install package only if it is not already installed.
#
if(STARTER_BUILD_CORE_TESTING)
  cpmaddpackage(
    NAME
    googletest
    GITHUB_REPOSITORY
    google/googletest
    GIT_TAG
    release-1.11.0
    VERSION
    1.11.0
    OPTIONS
    "BUILD_GMOCK ON"
    "INSTALL_GTEST OFF"
    "gtest_force_shared_crt ON")
  if(googletest_ADDED)
    print(STATUS "gtest configured correctly")
    set(googletest_Installed
        ON
        PARENT_SCOPE)
  elseif(googletest_Installed)
    print(STATUS "gtest already installed")
  else()
    print(WARNING "gtest was not configured properly")
  endif()

  # add tests
  enable_testing()
  print(STATUS "${PACKAGE_NAME} -- Tests Enabled")
  add_subdirectory("tests")
endif()

#
# NOTE: Add the src directory to complete building the shared library
#
add_subdirectory("src")

#
# NOTE: Build project examples, mostly useful for shared/static libraries
#
if(STARTER_BUILD_CORE_EXAMPLES)
  print(STATUS "${PACKAGE_NAME} -- Examples Enabled")
  add_subdirectory("examples")
endif()

#
# NOTE: Set the name of the library in the top level `CMakeLists.txt` file.
#
# This allows us to use `STARTER_CORE_LIB` to link against in the 'app' project
#
set(STARTER_CORE_LIB
    ${PACKAGE_NAME}
    PARENT_SCOPE)
