#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/share/gnuradio/gnuradio/gr-soqpsk_demod/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/usr/share/gnuradio/gnuradio/gr-soqpsk_demod/build/python:$PATH
export LD_LIBRARY_PATH=/usr/share/gnuradio/gnuradio/gr-soqpsk_demod/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/usr/share/gnuradio/gnuradio/gr-soqpsk_demod/build/swig:$PYTHONPATH
/usr/bin/python2 /usr/share/gnuradio/gnuradio/gr-soqpsk_demod/python/qa_soqpsk_demod_cc.py 
