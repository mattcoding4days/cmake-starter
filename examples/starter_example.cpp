#include <iostream>
#include <starter/rest.hpp>

/* This is just an example of how to link and build external code, other
 * that catch2 driven tests. Examples could easily be end to end tests,
 * integration tests etc.
 * */
auto main() -> int32_t {
  starter::request("http://www.httpbin.org/get");
}
