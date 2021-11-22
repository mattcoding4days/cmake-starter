include(CTest)

file(GLOB_RECURSE GLOBBED_TESTS CONFIGURE_DEPENDS "${TEST_SOURCE_DIR}/*.cpp")

add_library(catch_main STATIC catch_main.cpp)
target_link_libraries(catch_main PUBLIC Catch2::Catch2)
target_link_libraries(catch_main PRIVATE project_options)

# set(TEST_BINARY "${PROJECT_NAME-unittests}")

add_executable(unittests ${GLOBBED_TESTS} ${SOURCE_DIR}/addition.cpp)
target_include_directories(unittests PUBLIC ${INCLUDE_DIR})
target_link_libraries(unittests PRIVATE project_options catch_main Catch2::Catch2)

add_test(NAME TestSuite COMMAND unittests)
