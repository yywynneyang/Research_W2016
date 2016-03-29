#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/src/gnuradio/gnuradio/gr-Research/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/usr/src/gnuradio/gnuradio/gr-Research/build/python:$PATH
export LD_LIBRARY_PATH=/usr/src/gnuradio/gnuradio/gr-Research/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/usr/src/gnuradio/gnuradio/gr-Research/build/swig:$PYTHONPATH
/usr/bin/python2 /usr/src/gnuradio/gnuradio/gr-Research/python/qa_rotation_cc.py 
