/* -*- c++ -*- */

#define TESTA_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "TestA_swig_doc.i"

%{
#include "TestA/my_qpsk_demod_cb.h"
#include "TestA/cleanslate.h"
%}


%include "TestA/my_qpsk_demod_cb.h"
GR_SWIG_BLOCK_MAGIC2(TestA, my_qpsk_demod_cb);
%include "TestA/cleanslate.h"
GR_SWIG_BLOCK_MAGIC2(TestA, cleanslate);
