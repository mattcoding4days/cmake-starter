add_executable(example1 "${STARTER_EXAMPLES_SOURCE_DIR}/starter_example.cpp" ${STARTER_SOURCE_DIR}/rest.cpp)
target_include_directories(example1 PUBLIC ${STARTER_INCLUDE_DIR})
target_link_libraries(example1 PRIVATE stdc++fs cpr::cpr)

add_executable(example2 "${STARTER_EXAMPLES_SOURCE_DIR}/version_example.cpp")
target_include_directories(example2 PUBLIC ${STARTER_INCLUDE_DIR})
target_link_libraries(example2 PRIVATE stdc++fs cpr::cpr)
