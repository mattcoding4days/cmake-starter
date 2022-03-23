#include <iostream>
#include <starter_app/version.hpp>
#include <starter_core/add.hpp>
#include <starter_core/version.hpp>

int main() {
  std::cout << "Starter core version: " << starter::core::get_version() << '\n';
  std::cout << "Starter app version: " << starter::app::get_version() << '\n';
  std::cout << "3 + 3 = " << starter::core::add(3, 3) << '\n';

  return 0;
}
