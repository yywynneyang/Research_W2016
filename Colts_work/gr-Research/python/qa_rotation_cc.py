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
import Research as 
from numpy import array

class qa_rotation_cc (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        print("Hi it FINALLY works")
        src_data = (1, 1, 5, 5, 0.2,0.2)
        expected_result = (1, 1, 5, 5, 0.2,0.2)
        src = blocks.vector_source_f(src_data)
        rotator = Research.rotation_cc()
        snk = blocks.vector_sink_f();
	print("pre-derp")
        self.tb.connect (src, rotator)
        self.tb.connect (rotator, snk)
	print("run")
        self.tb.run ()
	print("derp")
        result_data = snk.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)
	print("is it done?")


if __name__ == '__main__':
    gr_unittest.run(qa_rotation_cc, "qa_rotation_cc.xml")
