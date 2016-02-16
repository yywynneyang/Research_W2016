INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_RESEARCH Research)

FIND_PATH(
    RESEARCH_INCLUDE_DIRS
    NAMES Research/api.h
    HINTS $ENV{RESEARCH_DIR}/include
        ${PC_RESEARCH_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    RESEARCH_LIBRARIES
    NAMES gnuradio-Research
    HINTS $ENV{RESEARCH_DIR}/lib
        ${PC_RESEARCH_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(RESEARCH DEFAULT_MSG RESEARCH_LIBRARIES RESEARCH_INCLUDE_DIRS)
MARK_AS_ADVANCED(RESEARCH_LIBRARIES RESEARCH_INCLUDE_DIRS)

