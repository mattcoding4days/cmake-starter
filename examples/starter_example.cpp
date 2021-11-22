#include <iostream>
#include <starter/addition.hpp>

/* This is just an example of how to link and build external code, other
 * that catch2 driven tests. Examples could easily be end to end tests,
 * integration tests etc.
 * */
auto main() -> int32_t {
  auto sum = starter::add(2, 2);
  std::cout << "2 + 2 = " << sum << '\n';
}
