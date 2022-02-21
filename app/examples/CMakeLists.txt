#
# NOTE: add the executables
#
set(EXAMPLE_ONE "${PACKAGE_NAME}_example_one")

add_executable(${EXAMPLE_ONE} "${APP_EXAMPLES_SOURCE_DIR}/app_example.cpp")

target_include_directories(${EXAMPLE_ONE} PUBLIC ${CORE_INCLUDE_DIR})
target_link_libraries(${EXAMPLE_ONE} PRIVATE project_options project_warnings ${STARTER_CORE_LIB} stdc++fs)
