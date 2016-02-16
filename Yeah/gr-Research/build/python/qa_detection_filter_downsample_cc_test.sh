#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/share/gnuradio/gnuradio/gr-Research/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/usr/share/gnuradio/gnuradio/gr-Research/build/python:$PATH
export LD_LIBRARY_PATH=/usr/share/gnuradio/gnuradio/gr-Research/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/usr/share/gnuradio/gnuradio/gr-Research/build/swig:$PYTHONPATH
/usr/bin/python2 /usr/share/gnuradio/gnuradio/gr-Research/python/qa_detection_filter_downsample_cc.py 
