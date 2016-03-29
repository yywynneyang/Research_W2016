#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/usr/src/gnuradio/gnuradio/gr-TestA/lib
export GR_CONF_CONTROLPORT_ON=False
export PATH=/usr/src/gnuradio/gnuradio/gr-TestA/build/lib:$PATH
export LD_LIBRARY_PATH=/usr/src/gnuradio/gnuradio/gr-TestA/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-TestA 
