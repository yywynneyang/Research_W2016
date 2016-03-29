INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_TESTA TestA)

FIND_PATH(
    TESTA_INCLUDE_DIRS
    NAMES TestA/api.h
    HINTS $ENV{TESTA_DIR}/include
        ${PC_TESTA_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    TESTA_LIBRARIES
    NAMES gnuradio-TestA
    HINTS $ENV{TESTA_DIR}/lib
        ${PC_TESTA_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(TESTA DEFAULT_MSG TESTA_LIBRARIES TESTA_INCLUDE_DIRS)
MARK_AS_ADVANCED(TESTA_LIBRARIES TESTA_INCLUDE_DIRS)

