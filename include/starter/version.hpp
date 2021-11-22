#ifndef STARTER_VERSION_HPP
#define STARTER_VERSION_HPP

/**
 * @file version.hpp
 * @author Matt Williams (matt@dmgblockchain.com)
 * @brief Adds version support for project, used by Cmake
 * @date 2021-11-19
 */

#define STARTER_VMAJOR 0
#define STARTER_VMINOR 1
#define STARTER_VPATCH 0

#define STARTER_VERSION \
  (STARTER_VMAJOR * 1000 + STARTER_VMINOR * 100 + STARTER_VPATCH)


#endif // STARTER_VERSION_HPP
