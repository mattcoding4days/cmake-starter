function(get_version)
  # Note: The `include` folder containing `version.hpp` for each package should use the same name as
  # the value of `PACKAGE_NAME`, as defined in the package's `CMakeLists.txt`.
  # ie: `core/include/CortexCore/` should contain `Version.hpp` for the `core` package.
  file(READ "${CMAKE_CURRENT_SOURCE_DIR}/include/${PACKAGE_NAME}/version.hpp" file_contents)
  string(REGEX MATCH "VMAJOR ([0-9]+)" _ "${file_contents}")
  if(NOT CMAKE_MATCH_COUNT EQUAL 1)
    message(FATAL_ERROR "Could not extract the major version from version.hpp")
  endif()
  set(ver_major ${CMAKE_MATCH_1})

  string(REGEX MATCH "VMINOR ([0-9]+)" _ "${file_contents}")
  if(NOT CMAKE_MATCH_COUNT EQUAL 1)
    message(FATAL_ERROR "Could not extract the minor version from version.hpp")
  endif()
  set(ver_minor ${CMAKE_MATCH_1})

  string(REGEX MATCH "VPATCH ([0-9]+)" _ "${file_contents}")
  if(NOT CMAKE_MATCH_COUNT EQUAL 1)
    message(FATAL_ERROR "Could not extract the patch version from version.hpp")
  endif()
  set(ver_patch ${CMAKE_MATCH_1})

  set(${PACKAGE_NAME}_VMAJOR
      ${ver_major}
      PARENT_SCOPE
  )
  set(${PACKAGE_NAME}_VMINOR
      ${ver_minor}
      PARENT_SCOPE
  )
  set(${PACKAGE_NAME}_VPATCH
      ${ver_patch}
      PARENT_SCOPE
  )
  set(${PACKAGE_NAME}_VERSION
      "${ver_major}.${ver_minor}.${ver_patch}"
      PARENT_SCOPE
  )
endfunction()

