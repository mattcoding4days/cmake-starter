#include <cpr/cpr.h>

#include <iostream>
#include <starter/rest.hpp>

namespace starter {
void request(const std::string &pRequest) {
  cpr::Response r = cpr::Get(cpr::Url{pRequest});
  std::cout << r.url << std::endl;
  std::cout << r.status_code << std::endl;
  std::cout << r.header["content-type"] << std::endl;
  std::cout << r.text << std::endl;
}
}  // namespace starter
