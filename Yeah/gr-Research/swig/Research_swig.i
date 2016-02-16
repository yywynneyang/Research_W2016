/* -*- c++ -*- */

#define RESEARCH_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "Research_swig_doc.i"

%{
#include "Research/detection_filter_downsample_cc.h"
%}


%include "Research/detection_filter_downsample_cc.h"
GR_SWIG_BLOCK_MAGIC2(Research, detection_filter_downsample_cc);
