#ifndef STARTER_APP_VERSION_HPP
#define STARTER_APP_VERSION_HPP

/**
 * @file starter_app/version.hpp
 * @author Matt Williams (matt.k.williams@protonmail.com)
 * @brief Adds version support for project, used by Cmake
 * @date 2021-11-19
 */

#include <string>

#define VMAJOR 0
#define VMINOR 1
#define VPATCH 0

namespace starter::app {
/**
 * @brief return the version in string format
 *
 * @returns std::string
 * */
[[maybe_unused]] inline static std::string get_version() {
  std::string version_string{std::to_string(VMAJOR)};
  version_string += "." + std::to_string(VMINOR) + "." + std::to_string(VPATCH);
  return version_string;
}
}  // namespace starter::app

#endif
