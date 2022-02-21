#
# NOTE: determine required cmake here (use 'pip install cmake')
#
cmake_minimum_required(VERSION 3.10...3.22)

#
# NOTE: Set the C++ standard
#
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

#
# NOTE: Import get_version() function from utils, and set up project name
#
include(cmake/utils.cmake)

#
# NOTE: Set project name, and language.
#
# Sub-project versions are defined in their respective `CMakeLists.txt` files, by calling
# `get_version()`.
project(
  starter
  VERSION 0.1.0
  DESCRIPTION "Starter Project with shared library and seperate binary application using the CPM package manager"
  HOMEPAGE_URL "https://github.com/mattcoding4days/cmake-starter-lib"
  LANGUAGES CXX C)

#
# NOTE: Link this 'library' to set the c++ standard / compile-time options requested
#
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_${CMAKE_CXX_STANDARD})
add_library(project_warnings INTERFACE)

#
# NOTE: Include our own cmake scripts, and the CPM package manager
# and add compiler warnings
#
include(cmake/CPM.cmake)
include(cmake/print.cmake)
include(cmake/StandardProjectSettings.cmake)
include(cmake/CompilerWarnings.cmake)
set_project_warnings(project_warnings)

#
# NOTE: add additional project options
#
option(STARTER_ENABLE_PCH "Enable Precompiled Headers" ON)
option(STARTER_BUILD_CORE "Build the core shared library" ON)
option(STARTER_BUILD_APP "Build the application" ON)

#
# NOTE: This sets a global PCH parameter, each project will build its own PCH, which is a good idea
# if any #define's change consider breaking this out per project as necessary. Modify as needed for
# your project
#
if(STARTER_ENABLE_PCH)
  target_precompile_headers(
    project_options
    INTERFACE
    <algorithm>
    <bitset>
    <chrono>
    <condition_variable>
    <cstdint>
    <cstdlib>
    <deque>
    <exception>
    <filesystem>
    <fstream>
    <iostream>
    <memory>
    <mutex>
    <optional>
    <sstream>
    <string_view>
    <thread>
    <variant>
    <vector>)
endif()

#
# NOTE: Add sub-projects to the project
#
if(STARTER_BUILD_CORE)
  add_subdirectory("core")
endif()

if(STARTER_BUILD_APP)
  add_subdirectory("app")
endif()

#
# NOTE: bring in standard cmake includes
#
include(CMakeDependentOption)
include(GNUInstallDirs)
