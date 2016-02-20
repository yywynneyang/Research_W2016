/* -*- c++ -*- */

#define RESEARCH_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "Research_swig_doc.i"

%{
#include "Research/new_qpsk_demod_cb.h"
#include "Research/rotation_cc.h"
#include "Research/multiply_c_ff.h"
#include "Research/soqpsk_demod.h"
%}


%include "Research/new_qpsk_demod_cb.h"
GR_SWIG_BLOCK_MAGIC2(Research, new_qpsk_demod_cb);


%include "Research/rotation_cc.h"
GR_SWIG_BLOCK_MAGIC2(Research, rotation_cc);

%include "Research/multiply_c_ff.h"
GR_SWIG_BLOCK_MAGIC2(Research, multiply_c_ff);

%include "Research/soqpsk_demod.h"
GR_SWIG_BLOCK_MAGIC2(Research, soqpsk_demod);
