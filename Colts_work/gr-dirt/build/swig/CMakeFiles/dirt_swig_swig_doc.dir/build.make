# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /usr/src/gnuradio/gnuradio/gr-dirt

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr/src/gnuradio/gnuradio/gr-dirt/build

# Utility rule file for dirt_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/dirt_swig_swig_doc.dir/progress.make

swig/CMakeFiles/dirt_swig_swig_doc: swig/dirt_swig_doc.i

swig/dirt_swig_doc.i: swig/dirt_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/src/gnuradio/gnuradio/gr-dirt/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating python docstrings for dirt_swig_doc"
	cd /usr/src/gnuradio/gnuradio/gr-dirt/docs/doxygen && /usr/bin/python2 -B /usr/src/gnuradio/gnuradio/gr-dirt/docs/doxygen/swig_doc.py /usr/src/gnuradio/gnuradio/gr-dirt/build/swig/dirt_swig_doc_swig_docs/xml /usr/src/gnuradio/gnuradio/gr-dirt/build/swig/dirt_swig_doc.i

swig/dirt_swig_doc_swig_docs/xml/index.xml: swig/_dirt_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/src/gnuradio/gnuradio/gr-dirt/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for dirt_swig_doc docs"
	cd /usr/src/gnuradio/gnuradio/gr-dirt/build/swig && ./_dirt_swig_doc_tag
	cd /usr/src/gnuradio/gnuradio/gr-dirt/build/swig && /usr/bin/doxygen /usr/src/gnuradio/gnuradio/gr-dirt/build/swig/dirt_swig_doc_swig_docs/Doxyfile

dirt_swig_swig_doc: swig/CMakeFiles/dirt_swig_swig_doc
dirt_swig_swig_doc: swig/dirt_swig_doc.i
dirt_swig_swig_doc: swig/dirt_swig_doc_swig_docs/xml/index.xml
dirt_swig_swig_doc: swig/CMakeFiles/dirt_swig_swig_doc.dir/build.make
.PHONY : dirt_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/dirt_swig_swig_doc.dir/build: dirt_swig_swig_doc
.PHONY : swig/CMakeFiles/dirt_swig_swig_doc.dir/build

swig/CMakeFiles/dirt_swig_swig_doc.dir/clean:
	cd /usr/src/gnuradio/gnuradio/gr-dirt/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/dirt_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/dirt_swig_swig_doc.dir/clean

swig/CMakeFiles/dirt_swig_swig_doc.dir/depend:
	cd /usr/src/gnuradio/gnuradio/gr-dirt/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/src/gnuradio/gnuradio/gr-dirt /usr/src/gnuradio/gnuradio/gr-dirt/swig /usr/src/gnuradio/gnuradio/gr-dirt/build /usr/src/gnuradio/gnuradio/gr-dirt/build/swig /usr/src/gnuradio/gnuradio/gr-dirt/build/swig/CMakeFiles/dirt_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/dirt_swig_swig_doc.dir/depend

