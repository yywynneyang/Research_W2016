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
CMAKE_SOURCE_DIR = /usr/src/gnuradio/gnuradio/gr-TestA

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /usr/src/gnuradio/gnuradio/gr-TestA/build

# Include any dependencies generated for this target.
include swig/CMakeFiles/TestA_swig_swig_2d0df.dir/depend.make

# Include the progress variables for this target.
include swig/CMakeFiles/TestA_swig_swig_2d0df.dir/progress.make

# Include the compile flags for this target's objects.
include swig/CMakeFiles/TestA_swig_swig_2d0df.dir/flags.make

swig/TestA_swig_swig_2d0df.cpp: ../swig/TestA_swig.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/tagged_stream_block.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gnuradio.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/realtime.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/block.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/block_detail.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/constants.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/sync_block.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_shared_ptr.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/block_gateway.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/sync_interpolator.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_types.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/basic_block.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_ctrlport.i
swig/TestA_swig_swig_2d0df.cpp: swig/TestA_swig_doc.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/io_signature.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/top_block.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_extras.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/message.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/tags.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/msg_handler.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/runtime_swig.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/msg_queue.i
swig/TestA_swig_swig_2d0df.cpp: ../swig/TestA_swig.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/buffer.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_swig_block_magic.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/hier_block2.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/runtime_swig_doc.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/feval.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/sync_decimator.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/gr_logger.i
swig/TestA_swig_swig_2d0df.cpp: /usr/local/include/gnuradio/swig/prefs.i
swig/TestA_swig_swig_2d0df.cpp: swig/TestA_swig.tag
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/cmake -E copy /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_swig_2d0df.cpp.in /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_swig_2d0df.cpp

swig/TestA_swig_doc.i: swig/TestA_swig_doc_swig_docs/xml/index.xml
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/src/gnuradio/gnuradio/gr-TestA/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating python docstrings for TestA_swig_doc"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/docs/doxygen && /usr/bin/python2 -B /usr/src/gnuradio/gnuradio/gr-TestA/docs/doxygen/swig_doc.py /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_doc_swig_docs/xml /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_doc.i

swig/TestA_swig.tag: swig/_TestA_swig_swig_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/src/gnuradio/gnuradio/gr-TestA/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating TestA_swig.tag"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && ./_TestA_swig_swig_tag
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/cmake -E touch /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig.tag

swig/TestA_swig_doc_swig_docs/xml/index.xml: swig/_TestA_swig_doc_tag
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/src/gnuradio/gnuradio/gr-TestA/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Generating doxygen xml for TestA_swig_doc docs"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && ./_TestA_swig_doc_tag
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/doxygen /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_doc_swig_docs/Doxyfile

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/flags.make
swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o: swig/TestA_swig_swig_2d0df.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /usr/src/gnuradio/gnuradio/gr-TestA/build/CMakeFiles $(CMAKE_PROGRESS_4)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o -c /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_swig_2d0df.cpp

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.i"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_swig_2d0df.cpp > CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.i

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.s"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swig_swig_2d0df.cpp -o CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.s

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.requires:
.PHONY : swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.requires

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.provides: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.requires
	$(MAKE) -f swig/CMakeFiles/TestA_swig_swig_2d0df.dir/build.make swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.provides.build
.PHONY : swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.provides

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.provides.build: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o

# Object files for target TestA_swig_swig_2d0df
TestA_swig_swig_2d0df_OBJECTS = \
"CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o"

# External object files for target TestA_swig_swig_2d0df
TestA_swig_swig_2d0df_EXTERNAL_OBJECTS =

swig/TestA_swig_swig_2d0df: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o
swig/TestA_swig_swig_2d0df: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/build.make
swig/TestA_swig_swig_2d0df: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable TestA_swig_swig_2d0df"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/TestA_swig_swig_2d0df.dir/link.txt --verbose=$(VERBOSE)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold "Swig source"
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/cmake -E make_directory /usr/src/gnuradio/gnuradio/gr-TestA/build/swig
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && /usr/bin/swig2.0 -python -fvirtual -modern -keyword -w511 -module TestA_swig -DSIZE_T_UL -I/usr/src/gnuradio/gnuradio/gr-TestA/build/swig -I/usr/src/gnuradio/gnuradio/gr-TestA/swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7 -outdir /usr/src/gnuradio/gnuradio/gr-TestA/build/swig -c++ -I/usr/src/gnuradio/gnuradio/gr-TestA/lib -I/usr/src/gnuradio/gnuradio/gr-TestA/include -I/usr/src/gnuradio/gnuradio/gr-TestA/build/lib -I/usr/src/gnuradio/gnuradio/gr-TestA/build/include -I/usr/include -I/usr/include -I/usr/local/include -I/usr/src/gnuradio/gnuradio/gr-TestA/build/swig -I/usr/src/gnuradio/gnuradio/gr-TestA/swig -I/usr/local/include/gnuradio/swig -I/usr/include/python2.7 -I/usr/include/python2.7 -I/usr/include/x86_64-linux-gnu/python2.7 -o /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/TestA_swigPYTHON_wrap.cxx /usr/src/gnuradio/gnuradio/gr-TestA/swig/TestA_swig.i

# Rule to build all files generated by this target.
swig/CMakeFiles/TestA_swig_swig_2d0df.dir/build: swig/TestA_swig_swig_2d0df
.PHONY : swig/CMakeFiles/TestA_swig_swig_2d0df.dir/build

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/requires: swig/CMakeFiles/TestA_swig_swig_2d0df.dir/TestA_swig_swig_2d0df.cpp.o.requires
.PHONY : swig/CMakeFiles/TestA_swig_swig_2d0df.dir/requires

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/clean:
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/TestA_swig_swig_2d0df.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/TestA_swig_swig_2d0df.dir/clean

swig/CMakeFiles/TestA_swig_swig_2d0df.dir/depend: swig/TestA_swig_swig_2d0df.cpp
swig/CMakeFiles/TestA_swig_swig_2d0df.dir/depend: swig/TestA_swig_doc.i
swig/CMakeFiles/TestA_swig_swig_2d0df.dir/depend: swig/TestA_swig.tag
swig/CMakeFiles/TestA_swig_swig_2d0df.dir/depend: swig/TestA_swig_doc_swig_docs/xml/index.xml
	cd /usr/src/gnuradio/gnuradio/gr-TestA/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /usr/src/gnuradio/gnuradio/gr-TestA /usr/src/gnuradio/gnuradio/gr-TestA/swig /usr/src/gnuradio/gnuradio/gr-TestA/build /usr/src/gnuradio/gnuradio/gr-TestA/build/swig /usr/src/gnuradio/gnuradio/gr-TestA/build/swig/CMakeFiles/TestA_swig_swig_2d0df.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/TestA_swig_swig_2d0df.dir/depend

