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

import numpy
from gnuradio import gr

class soqpsk_demod_cc(gr.basic_block):
    """
    docstring for block soqpsk_demod_cc
    """
    #state variable test
    state = 0
    DF = [
         0.010378066969709,
         0.023688987704657,
         0.009767134822858,
         -0.027017804469398,
         -0.089762303133391,
         -0.110346523809347,
         -0.051853991233850,
         0.154921158891652,
         0.568943123186263,
         0.792392871766106,
         0.792392871766106,
         0.568943123186263,
         0.154921158891652,
        -0.051853991233850,
        -0.110346523809347,
        -0.089762303133391,
        -0.027017804469398,
         0.009767134822858,
         0.023688987704657,
         0.010378066969709
         ]
    S4Di = [0] * 18
    S4Dq = [0] * 18
    def __init__(self):
        gr.basic_block.__init__(self,
            name="soqpsk_demod_cc",
            in_sig=[numpy.complex64],
            out_sig=[numpy.complex64])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 2*noutput_items
            print ninput_items_required[i],' inputs required for ',noutput_items,' expected outputs.'

    def general_work(self, input_items, output_items):
        print 'inputs: ',input_items[0].size,' outputs: ',output_items[0].size
        samples_per_buffer = len(input_items[0])
        for sample_idx in range(0,samples_per_buffer-1,2):
            # compute outputs
            
            # you filter this and then downsample at the same time
            ## get the next two samples
            ri = input_items[0][sample_idx].real
            ri1 = input_items[0][sample_idx+1].real
            rq = input_items[0][sample_idx].imag
            rq1 = input_items[0][sample_idx+1].imag
            
            # compute detection filter outputs
            # are we missing DF values?
            x = self.DF[0] * (ri1 + self.S4Di[17]) \
                + self.DF[1] * (ri + self.S4Di[16]) \
                +self.DF[2] * (self.S4Di[0] + self.S4Di[15]) \
                +self.DF[3] * (self.S4Di[1] + self.S4Di[14]) \
                +self.DF[4] * (self.S4Di[2] + self.S4Di[13]) \
                +self.DF[5] * (self.S4Di[3] + self.S4Di[12]) \
                +self.DF[6] * (self.S4Di[4] + self.S4Di[11]) \
                +self.DF[7] * (self.S4Di[5] + self.S4Di[10]) \
                +self.DF[8] * (self.S4Di[6] + self.S4Di[9]) \
                +self.DF[9] * (self.S4Di[7] + self.S4Di[8])
                
            y =self.DF[0] * (rq1 + self.S4Dq[17]) \
                +self.DF[1] * (rq + self.S4Dq[16]) \
                +self.DF[2] * (self.S4Dq[0] + self.S4Dq[15]) \
                +self.DF[3] * (self.S4Dq[1] + self.S4Dq[14]) \
                +self.DF[4] * (self.S4Dq[2] + self.S4Dq[13]) \
                +self.DF[5] * (self.S4Dq[3] + self.S4Dq[12]) \
                +self.DF[6] * (self.S4Dq[4] + self.S4Dq[11]) \
                +self.DF[7] * (self.S4Dq[5] + self.S4Dq[10]) \
                +self.DF[8] * (self.S4Dq[6] + self.S4Dq[9]) \
                +self.DF[9] * (self.S4Dq[7] + self.S4Dq[8])
            output_items[0][sample_idx/2-1] = (x+y*1j)
        self.consume_each(len(input_items[0]))
        return len(output_items[0])


		#successful tests

		#Generic way of just putting through inputs
        #output_items[0][0] = input_items[0][0] + self.state
        #self.state = -1*self.state;
        #self.state = self.state + 1;
        #output_items[0][1] = input_items[0][1] + self.state
        #self.state = -1*self.state;
        #self.state = self.state + 1;
        #if self.state == 30: 
        #    self.state=0
        
        #input_size = len(input_items[0])
        #print input_size,' is the iteration length'
        #for i in range(0,input_size,2):
            #print ' iteration: ',i/2
            #output_items[0][i/2] = input_items[0][i] + input_items[0][i+1]
            #print 'output: ',output_items[0][i/2]  

        
