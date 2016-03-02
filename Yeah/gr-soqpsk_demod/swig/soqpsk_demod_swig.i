/* -*- c++ -*- */

#define SOQPSK_DEMOD_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "soqpsk_demod_swig_doc.i"

%{
#include "soqpsk_demod/soqpsk_demod_cc.h"
%}


%include "soqpsk_demod/soqpsk_demod_cc.h"
GR_SWIG_BLOCK_MAGIC2(soqpsk_demod, soqpsk_demod_cc);
