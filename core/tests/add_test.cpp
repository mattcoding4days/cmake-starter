#include <gtest/gtest.h>

#include <starter_core/add.hpp>

/**
 * @brief Test our library
 *
 * */
TEST(AddTest, BasicAssertions) {
  // Expect equality.
  EXPECT_EQ(starter::core::add(3, 3), 6);
}
