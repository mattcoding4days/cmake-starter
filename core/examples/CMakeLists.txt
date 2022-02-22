#
# NOTE: add the executables
#
set(EXAMPLE_ONE "${PACKAGE_NAME}_example_one.bin")

add_executable(${EXAMPLE_ONE} "${CORE_EXAMPLES_SOURCE_DIR}/core_example.cpp" ${CORE_SOURCE_DIR}/add.cpp)

target_include_directories(${EXAMPLE_ONE} PUBLIC ${CORE_INCLUDE_DIR})
target_link_libraries(${EXAMPLE_ONE} PRIVATE project_options project_warnings stdc++fs)
