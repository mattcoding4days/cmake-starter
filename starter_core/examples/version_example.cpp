#include <iostream>
#include <starter/version.hpp>

auto main() -> int32_t {
  auto getVersion = []() -> std::string {
    std::string v{std::to_string(STARTER_VMAJOR)};
    v.append(".")
        .append(std::to_string(STARTER_VMINOR))
        .append(".")
        .append(std::to_string(STARTER_VPATCH));
    return v;
  };

  std::cout << "Version: " << getVersion() << '\n';
}
