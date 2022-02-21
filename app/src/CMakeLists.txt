#
# NOTE: Output build param information
#
print(STATUS "Building ${PACKAGE_NAME}_v${PACKAGE_VERSION} [${CMAKE_BUILD_TYPE}]")

#
# NOTE: Name the executable here
#
set(BINARY_NAME "${PACKAGE_NAME}.bin")

#
# NOTE: Add the executable, target all directories and link the libraries
#
add_executable(${BINARY_NAME} ${APP_SOURCES})
target_include_directories(${BINARY_NAME} PUBLIC ${APP_INCLUDE_DIR})
target_link_libraries(${BINARY_NAME} PRIVATE project_options project_warnings ${STARTER_CORE_LIB})
