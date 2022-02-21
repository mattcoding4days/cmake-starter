set(PACKAGE_NAME "starter_core")

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
set(CORE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/src")
set(CORE_TEST_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/tests")
set(CORE_EXAMPLES_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/examples")
set(CORE_INCLUDE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/include")

# NOTE: add additional project options
option(STARTER_BUILD_CORE_TESTING "Enable Test builds" ON)
option(STARTER_BUILD_CORE_EXAMPLES "Enable example builds" ON)

#
# NOTE: Prevent in source builds (can't build in src/ or in project root)
#
if(CMAKE_CURRENT_SOURCE_DIR STREQUAL CMAKE_CURRENT_BINARY_DIR OR CMAKE_CURRENT_BINARY_DIR STREQUAL
                                                                 CORE_SOURCE_DIR
)
  print(
    FATAL_ERROR
    "In source builds are not allowed. Please make a new directory (called a build directory) and run CMake from there."
  )
endif()

#
# NOTE: This is where 3rd party libraries should be installed via the light weight CPM dependancy
# management system. The CPM wiki is here: https://github.com/cpm-cmake/CPM.cmake/wiki/More-Snippets
#
# NOTE: Using `CPMFindPackage()` to install package only if it is not already installed.
if(STARTER_BUILD_CORE_TESTING)
  CPMFindPackage(
    NAME Catch2
    GITHUB_REPOSITORY catchorg/Catch2
    VERSION 2.13.7
  )
  if(Catch2_ADDED)
    # The current `CMakeLists.txt` file installed the Catch2 package
    print(STATUS "Catch2 configured correctly")
    set(Catch2_Installed
        ON
        PARENT_SCOPE
    )
  elseif(Catch2_Installed)
    # The package was previously installed to the project.
    #
    # Where `<dependency>_BINARY_DIR` is the path to the build directory of the dependency.
    print(STATUS "Catch2 already installed")
  else()
    # The package was not succesfully installed to the project
    print(WARNING "Catch2 was not configured properly")
  endif()
endif()

#
# NOTE: Output build param information
#
print(STATUS "Building ${PACKAGE_NAME}-${PACKAGE_VERSION} [${CMAKE_BUILD_TYPE}]")

#
# HACK: glob src files and header files (some people may not like this)
#
file(GLOB_RECURSE CORE_GLOBBED_HEADERS CONFIGURE_DEPENDS
     "${CORE_INCLUDE_DIR}/${PACKAGE_NAME}/*.hpp"
)
file(GLOB_RECURSE CORE_GLOBBED_SOURCES CONFIGURE_DEPENDS "${CORE_SOURCE_DIR}/*.cpp")

#
# NOTE: Build tests with catch2
#
if(STARTER_BUILD_CORE_TESTING)
  enable_testing()
  print(STATUS "${PACKAGE_NAME} -- Tests Enabled")
  add_subdirectory("tests")
endif()

#
# NOTE: Build project examples, mostly useful for shared/static libraries
#
if(STARTER_BUILD_CORE_EXAMPLES)
  print(STATUS "${PACKAGE_NAME} -- Examples Enabled")
  add_subdirectory("examples")
endif()

#
# NOTE: Add core as a interfaced library into our project, as it is header only
#
print(STATUS "\nAdding the ${PACKAGE_NAME} library")
add_library(${PACKAGE_NAME} SHARED ${CORE_GLOBBED_HEADERS} ${CORE_GLOBBED_SOURCES})
target_include_directories(${PACKAGE_NAME} PUBLIC ${CORE_INCLUDE_DIR})
target_link_libraries(${PACKAGE_NAME} PRIVATE project_options project_warnings stdc++fs)

#
# NOTE: Install all shared libraries
#
install(TARGETS ${PACKAGE_NAME} LIBRARY DESTINATION lib)
install(DIRECTORY "${CORE_INCLUDE_DIR}/" DESTINATION include)

set_target_properties(
  ${PACKAGE_NAME} PROPERTIES VERSION ${${PACKAGE_NAME}_VERSION} SOVERSION ${${PACKAGE_NAME}_VMAJOR}
)

# Set the name of the library in the top level `CMakeLists.txt` file.
#
# This allows us to use `STARTER_CORE_LIB` to link against in the 'app' project
set(STARTER_CORE_LIB
    ${PACKAGE_NAME}
    PARENT_SCOPE
)
