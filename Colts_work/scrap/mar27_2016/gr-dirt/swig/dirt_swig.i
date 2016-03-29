/* -*- c++ -*- */

#define DIRT_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "dirt_swig_doc.i"

%{
#include "dirt/my_qpsk_demod_cb.h"
%}


%include "dirt/my_qpsk_demod_cb.h"
GR_SWIG_BLOCK_MAGIC2(dirt, my_qpsk_demod_cb);
