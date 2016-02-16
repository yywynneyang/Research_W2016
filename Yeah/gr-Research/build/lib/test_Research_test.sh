#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/share/gnuradio/gnuradio/gr-Research/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/usr/share/gnuradio/gnuradio/gr-Research/build/lib:$PATH
export LD_LIBRARY_PATH=/usr/share/gnuradio/gnuradio/gr-Research/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-Research 
