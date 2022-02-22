include(CTest)

#
# NOTE: Add all test source files
#
set(CORE_TEST_SOURCES "${CORE_TEST_SOURCE_DIR}/catch_main.cpp" "${CORE_TEST_SOURCE_DIR}/constexpr_tests.cpp")

#
# NOTE: Set up Catch2 with a custom main function to act as a driving fixture for tests
#
set(PACKAGE_CATCH_MAIN "${PACKAGE_NAME}_catch_main")
add_library(${PACKAGE_CATCH_MAIN} STATIC catch_main.cpp)
target_link_libraries(${PACKAGE_CATCH_MAIN} PUBLIC Catch2::Catch2)
target_link_libraries(${PACKAGE_CATCH_MAIN} PRIVATE project_options)

#
# NOTE: Set up the executable and link all necessary files
#
set(PACKAGE_UNIT_TEST_NAME "${PACKAGE_NAME}_unittests")
add_executable(${PACKAGE_UNIT_TEST_NAME} ${CORE_TEST_SOURCES})
target_include_directories(${PACKAGE_UNIT_TEST_NAME} PUBLIC ${CORE_INCLUDE_DIR})
target_link_libraries(
  ${PACKAGE_UNIT_TEST_NAME}
  PRIVATE project_options
          project_warnings
          ${PACKAGE_CATCH_MAIN}
          Catch2::Catch2)

add_test(NAME "${PACKAGE_NAME}_test_suite" COMMAND ${PACKAGE_UNIT_TEST_NAME})
