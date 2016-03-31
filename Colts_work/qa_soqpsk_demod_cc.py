#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2016 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import blocks
from soqpsk_demod_cc import soqpsk_demod_cc
import numpy as np
import csv
class qa_soqpsk_demod_cc (gr_unittest.TestCase):

    
    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        #src_data = np.loadtxt('r_data.csv').view(complex)
        #expected_result = np.loadtxt('filter_test.csv').view(complex)
        with open('r_data.csv','rb') as f:
            reader1 = csv.reader(f)
            r_data = list(reader1)[0]
        with open('filter_test.csv','rb') as g:
            reader2 = csv.reader(g)
            filter_data = list(reader2)[0]
        
        
        src_data = [complex(i) for i in r_data]
        expected_results = [complex(i) for i in filter_data]
        
        src = blocks.vector_source_c (expected_results)
        mult = soqpsk_demod_cc ()
        dst = blocks.vector_sink_c ()
        self.tb.connect (src, mult)
        self.tb.connect (mult, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)



if __name__ == '__main__':
    gr_unittest.run(qa_soqpsk_demod_cc, "qa_soqpsk_demod_cc.xml")
