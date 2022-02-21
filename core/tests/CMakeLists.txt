include(CTest)

file(GLOB_RECURSE CORE_GLOBBED_TESTS CONFIGURE_DEPENDS "${CORE_TEST_SOURCE_DIR}/*.cpp")

add_library(catch_main STATIC catch_main.cpp)
target_link_libraries(catch_main PUBLIC Catch2::Catch2)
target_link_libraries(catch_main PRIVATE project_options)

add_executable(unittests ${CORE_GLOBBED_TESTS})
target_include_directories(unittests PUBLIC ${CORE_INCLUDE_DIR})
target_link_libraries(unittests PRIVATE project_options catch_main Catch2::Catch2)

add_test(NAME "${PACKAGE_NAME}_test_suite" COMMAND unittests)
