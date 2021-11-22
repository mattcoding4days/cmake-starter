#include <fmt/color.h>

#include <CLI/CLI.hpp>
#include <functional>
#include <iostream>
#include <map>
#include <starter/addition.hpp>
#include <starter/version.hpp>

using namespace fmt;

auto main(int argc, const char **argv) -> int32_t {
  auto getVersion = []() -> std::string {
    std::string v{to_string(STARTER_VMAJOR)};
    v += "." + std::to_string(STARTER_VMINOR) + "." +
         std::to_string(STARTER_VPATCH);
    return v;
  };

  CLI::App app;
  CLI11_PARSE(app, argc, argv);

  print("Version: {}", getVersion());
  print(fg(color::crimson) | emphasis::bold, "\n2 + 2 = {}!\n",
        starter::add(2, 2));
}
