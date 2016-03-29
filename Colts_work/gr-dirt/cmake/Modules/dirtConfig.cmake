INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DIRT dirt)

FIND_PATH(
    DIRT_INCLUDE_DIRS
    NAMES dirt/api.h
    HINTS $ENV{DIRT_DIR}/include
        ${PC_DIRT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DIRT_LIBRARIES
    NAMES gnuradio-dirt
    HINTS $ENV{DIRT_DIR}/lib
        ${PC_DIRT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DIRT DEFAULT_MSG DIRT_LIBRARIES DIRT_INCLUDE_DIRS)
MARK_AS_ADVANCED(DIRT_LIBRARIES DIRT_INCLUDE_DIRS)

