#include <iostream>
#include <starter_core/add.hpp>
#include <starter_core/version.hpp>

/**
 * @brief An example of an example file :)
 * */

int main() {
  std::cout << "Starter core version: " << starter::core::get_version() << '\n';
  std::cout << "2 + 2 = " << starter::core::add(2, 2) << '\n';

  return 0;
}
