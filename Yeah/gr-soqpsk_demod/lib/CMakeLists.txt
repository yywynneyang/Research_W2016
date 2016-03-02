# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND soqpsk_demod_sources
    soqpsk_demod_cc_impl.cc
)

set(soqpsk_demod_sources "${soqpsk_demod_sources}" PARENT_SCOPE)
if(NOT soqpsk_demod_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT soqpsk_demod_sources)

add_library(gnuradio-soqpsk_demod SHARED ${soqpsk_demod_sources})
target_link_libraries(gnuradio-soqpsk_demod ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-soqpsk_demod PROPERTIES DEFINE_SYMBOL "gnuradio_soqpsk_demod_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-soqpsk_demod PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-soqpsk_demod
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_soqpsk_demod_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_soqpsk_demod.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_soqpsk_demod.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_soqpsk_demod_cc.cc
)

add_executable(test-soqpsk_demod ${test_soqpsk_demod_sources})

target_link_libraries(
  test-soqpsk_demod
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-soqpsk_demod
)

GR_ADD_TEST(test_soqpsk_demod test-soqpsk_demod)
