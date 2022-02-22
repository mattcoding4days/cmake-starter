#ifndef STARTER_CORE_ADD_HPP
#define STARTER_CORE_ADD_HPP

/**
 * @file add.hpp
 * @author Matt Williams (matt.k.williams@protonmail.com)
 * @date 2021-11-19
 */

#include <cstdint>

namespace starter::core {

/**
 * @brief add 2 numbers together
 *
 * @details this is just an example function to showcase a shared library
 * linking to another project
 *
 * @param a int32_t
 *
 * @param b int32_t
 *
 * @returns summation of a + b
 * */
[[nodiscard]] std::int32_t add(std::int32_t a, std::int32_t b);
}  // namespace starter::core

#endif
