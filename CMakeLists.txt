#
# NOTE: determine required cmake here (use 'pip install cmake')
#
cmake_minimum_required(VERSION 3.10...3.21)

#
# NOTE: Import get_version() function from utils, and set up project name
#
include(cmake/utils.cmake)

get_version()
project(
  starter
  VERSION ${STARTER_VERSION}
  LANGUAGES CXX
)

#
# NOTE: Include our own cmake scripts, and the CPM package manager
#
include(cmake/CPM.cmake)
include(cmake/print.cmake)
include(cmake/StandardProjectSettings.cmake)

#
# NOTE: Link this 'library' to set the c++ standard / compile-time options requested
#
add_library(project_options INTERFACE)
target_compile_features(project_options INTERFACE cxx_std_17)
add_library(project_warnings INTERFACE)

#
# standard compiler warnings
#
include(cmake/CompilerWarnings.cmake)
set_project_warnings(project_warnings)

#
# NOTE: Set our source and include directory variables for use through the build
#
set(STARTER_SOURCE_DIR "${PROJECT_SOURCE_DIR}/src")
set(STARTER_TEST_SOURCE_DIR "${PROJECT_SOURCE_DIR}/tests")
set(STARTER_EXAMPLES_SOURCE_DIR "${PROJECT_SOURCE_DIR}/examples")
set(STARTER_INCLUDE_DIR "${PROJECT_SOURCE_DIR}/include")

#
# NOTE: Prevent in source builds (can't build in src/ or in project root)
#
if(PROJECT_SOURCE_DIR STREQUAL PROJECT_BINARY_DIR OR PROJECT_BINARY_DIR STREQUAL STARTER_SOURCE_DIR)
  print(
    FATAL_ERROR
    "In source builds are not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

#
# NOTE: bring in standard cmake includes
#
include(CMakeDependentOption)
include(GNUInstallDirs)

#
# NOTE: Set C/C++ parameters for all targets in this CMakeLists.txt
#
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra -pedantic --std=c++17 -fPIC")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -pedantic -fPIC")

#
# NOTE: This is where 3rd party libraries should be installed via the light weight CPM dependancy
# management system. The CPM wiki is here: https://github.com/cpm-cmake/CPM.cmake/wiki/More-Snippets
#
CPMAddPackage(
  Name Catch2
  GITHUB_REPOSITORY catchorg/Catch2
  VERSION 2.13.7
)
if(Catch2_ADDED)
  print(STATUS "Catch2 configured correctly")
else()
  print(WARNING "Catch2 was not configured properly")
endif()

CPMAddPackage(
  NAME cpr
  GIT_REPOSITORY https://github.com/whoshuu/cpr.git
  GIT_TAG f4622efcb59d84071ae11404ae61bd821c1c344b
  OPTIONS "CPR_BUILD_TESTS OFF"
)
if(cpr_ADDED)
  print(STATUS "cpr configured correctly")
else()
  print(WARNING "cpr was not configured properly")
endif()

#
# NOTE: add additional project options
#
option(STARTER_DEBUG "Building Debug version" OFF)
option(ENABLE_PCH "Enable Precompiled Headers" ON)
option(STARTER_TESTING "Enable Test builds" OFF)
option(STARTER_EXAMPLES "Enable example builds" OFF)

#
# NOTE: Build defaults to a release optimized build, cmake -DENABLE_DEBUG=ON will build debug
#
if(STARTER_DEBUG)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g")
else()
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
endif()

#
# NOTE: Output build param information
#
print(STATUS "Building ${PROJECT_NAME}-${PROJECT_VERSION} [${CMAKE_BUILD_TYPE}]")
print(STATUS "Building with CXX_FLAGS: ${CMAKE_CXX_FLAGS}")

#
# HACK: glob src files and header files (some people may not like this)
#
file(GLOB_RECURSE STARTER_GLOBBED_HEADERS CONFIGURE_DEPENDS
     "${STARTER_INCLUDE_DIR}/${PROJECT_NAME}/*.hpp"
)
file(GLOB_RECURSE STARTER_GLOBBED_SOURCES CONFIGURE_DEPENDS "${STARTER_SOURCE_DIR}/*.cpp")

#
# NOTE: This sets a global PCH parameter, each project will build its own PCH, which is a good idea
# if any #define's change consider breaking this out per project as necessary
#
if(ENABLE_PCH)
  target_precompile_headers(project_options INTERFACE <vector> <string> <map> <utility>)
endif()

#
# NOTE: Build tests with catch2
#
if(STARTER_TESTING)
  enable_testing()
  print(STATUS "Tests Enabled")
  add_subdirectory("tests")
endif()

#
# NOTE: Build project examples, mostly useful for shared/static libraries
#
if(STARTER_EXAMPLES)
  print(STATUS "Examples Enabled")
  add_subdirectory("examples")
endif()

#
# NOTE: declare libraries here all source should be placed into a single library, (whether they be
# shared or static)
#
add_library(${PROJECT_NAME} SHARED ${STARTER_GLOBBED_HEADERS} ${STARTER_GLOBBED_SOURCES})
target_include_directories(${PROJECT_NAME} PUBLIC ${STARTER_INCLUDE_DIR})
target_link_libraries(${PROJECT_NAME} PRIVATE stdc++fs cpr::cpr)

#
# NOTE: Install all shared libraries
#
install(TARGETS ${PROJECT_NAME} LIBRARY DESTINATION lib)
install(DIRECTORY "${STARTER_INCLUDE_DIR}/" DESTINATION include)

set_target_properties(
  ${PROJECT_NAME} PROPERTIES VERSION ${${PROJECT_NAME}_VERSION} SOVERSION
                                                                ${${PROJECT_NAME}_VERSION_MAJOR}
)
