include(CTest)

file(GLOB_RECURSE STARTER_GLOBBED_TESTS CONFIGURE_DEPENDS "${STARTER_TEST_SOURCE_DIR}/*.cpp")

add_library(catch_main STATIC catch_main.cpp)
target_link_libraries(catch_main PUBLIC Catch2::Catch2)
target_link_libraries(catch_main PRIVATE project_options)

add_executable(unittests ${STARTER_GLOBBED_TESTS})
target_include_directories(unittests PUBLIC ${STARTER_INCLUDE_DIR})
target_link_libraries(unittests PRIVATE project_options catch_main Catch2::Catch2)

add_test(NAME StarterTestSuite COMMAND unittests)
