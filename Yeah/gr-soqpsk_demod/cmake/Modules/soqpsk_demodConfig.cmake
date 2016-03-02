INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_SOQPSK_DEMOD soqpsk_demod)

FIND_PATH(
    SOQPSK_DEMOD_INCLUDE_DIRS
    NAMES soqpsk_demod/api.h
    HINTS $ENV{SOQPSK_DEMOD_DIR}/include
        ${PC_SOQPSK_DEMOD_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    SOQPSK_DEMOD_LIBRARIES
    NAMES gnuradio-soqpsk_demod
    HINTS $ENV{SOQPSK_DEMOD_DIR}/lib
        ${PC_SOQPSK_DEMOD_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(SOQPSK_DEMOD DEFAULT_MSG SOQPSK_DEMOD_LIBRARIES SOQPSK_DEMOD_INCLUDE_DIRS)
MARK_AS_ADVANCED(SOQPSK_DEMOD_LIBRARIES SOQPSK_DEMOD_INCLUDE_DIRS)

