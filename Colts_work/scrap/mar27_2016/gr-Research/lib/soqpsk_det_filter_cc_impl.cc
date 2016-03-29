/* -*- c++ -*- */
/*
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "soqpsk_det_filter_cc_impl.h"
#include <pmt/pmt.h>
#include <gnuradio/blocks/complex_to_float.h>
#include <gnuradio/blocks/complex_to_imag.h>
#include <complex>
namespace gr {
  namespace Research {

    soqpsk_det_filter_cc::sptr
    soqpsk_det_filter_cc::make(bool test)
    {
      return gnuradio::get_initial_sptr
        (new soqpsk_det_filter_cc_impl(test));
    }

    /*
     * The private constructor
     */
    soqpsk_det_filter_cc_impl::soqpsk_det_filter_cc_impl(bool test)
      : gr::block("soqpsk_det_filter_cc",
              gr::io_signature::make(1,1, sizeof(gr_complex)),
              gr::io_signature::make(1,1, sizeof(gr_complex)))
    {}

    /*
     * Our virtual destructor.
     */
    soqpsk_det_filter_cc_impl::~soqpsk_det_filter_cc_impl()
    {
    }

    // Detection filter coefficients
    double soqpsk_det_filter_cc_impl::d_DF[DETECTION_FILTER_SIZE] = {0.010378066969709,
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
                               0.010378066969709};

    double d_S4Di[REGISTER_SIZE];
    double d_S4Dq[REGISTER_SIZE];

    void
    soqpsk_det_filter_cc_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
      unsigned ninputs = ninput_items_required.size ();

    for(unsigned i = 0; i < ninputs; i++)
      ninput_items_required[i] = 2*noutput_items;
    }

    void soqpsk_det_filter_cc_impl::filter(double &x, double &y, const gr_complex &sampleA,const gr_complex &sampleB) {


        // you need an alternative way to access class variables; try doing a function or something
        // or maybe the S4D registers are not initiallized
        x = d_DF[1] * (sampleB.real() + d_S4Di[18])
            + d_DF[2] * (sampleA.real() + d_S4Di[17])
            + d_DF[3] * (d_S4Di[1] + d_S4Di[16])
            + d_DF[4] * (d_S4Di[2] + d_S4Di[15])
            + d_DF[5] * (d_S4Di[3] + d_S4Di[14])
            + d_DF[6] * (d_S4Di[4] + d_S4Di[13])
            + d_DF[7] * (d_S4Di[5] + d_S4Di[12])
            + d_DF[8] * (d_S4Di[6] + d_S4Di[11])
            + d_DF[9] * (d_S4Di[7] + d_S4Di[10])
            + d_DF[10] * (d_S4Di[8] + d_S4Di[9]);

        y = d_DF[1] * (sampleB.imag() + d_S4Dq[18])
            + d_DF[2] * (sampleA.imag() + d_S4Dq[17])
            + d_DF[3] * (d_S4Dq[1] + d_S4Dq[16])
            + d_DF[4] * (d_S4Dq[2] + d_S4Dq[15])
            + d_DF[5] * (d_S4Dq[3] + d_S4Dq[14])
            + d_DF[6] * (d_S4Dq[4] + d_S4Dq[13])
            + d_DF[7] * (d_S4Dq[5] + d_S4Dq[12])
            + d_DF[8] * (d_S4Dq[6] + d_S4Dq[11])
            + d_DF[9] * (d_S4Dq[7] + d_S4Dq[10])
            + d_DF[10] * (d_S4Dq[8] + d_S4Dq[9]);

    }

    int
    soqpsk_det_filter_cc_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];

      // Do <+signal processing+>

      // Initializations
      double x,xr,tempFx;
      double y,yr,tempFy;
      bool STROBE =false;
      double et,ep;
      double v1,v2,yi,xi1,yi1,xi2,vt,vp,w;
      int bk,n=1;
      int pk = 0;
      bool d0,d1;
      std::vector<bool> bits(noutput_items*2,false);
      int d_num_inputs = 2*noutput_items;

      // End initializations
      int downsample_val = 2;

      for(int i = 0 ; i < d_num_inputs-1 ; i= i + downsample_val)
      {
            this->filter(x,y,in[i],in[i+1]);

            out[pk] = x + 1i*y;

            d_S4Di[17] = d_S4Di[15];
            d_S4Di[16] = d_S4Di[14];
            d_S4Di[15] = d_S4Di[13];
            d_S4Di[14] = d_S4Di[12];
            d_S4Di[13] = d_S4Di[11];
            d_S4Di[12] = d_S4Di[10];
            d_S4Di[11] = d_S4Di[9];
            d_S4Di[10] = d_S4Di[8];
            d_S4Di[9] = d_S4Di[7];
            d_S4Di[8] = d_S4Di[6];
            d_S4Di[7] = d_S4Di[5];
            d_S4Di[6] = d_S4Di[4];
            d_S4Di[5] = d_S4Di[3];
            d_S4Di[4] = d_S4Di[2];
            d_S4Di[3] = d_S4Di[1];
            d_S4Di[2] = d_S4Di[0];
            d_S4Di[1] = in[i].real();
            d_S4Di[0] = in[i+1].real();

            d_S4Dq[17] = d_S4Dq[15];
            d_S4Dq[16] = d_S4Dq[14];
            d_S4Dq[15] = d_S4Dq[13];
            d_S4Dq[14] = d_S4Dq[12];
            d_S4Dq[13] = d_S4Dq[11];
            d_S4Dq[12] = d_S4Dq[10];
            d_S4Dq[11] = d_S4Dq[9];
            d_S4Dq[10] = d_S4Dq[8];
            d_S4Dq[9] = d_S4Dq[7];
            d_S4Dq[8] = d_S4Dq[6];
            d_S4Dq[7] = d_S4Dq[5];
            d_S4Dq[6] = d_S4Dq[4];
            d_S4Dq[5] = d_S4Dq[3];
            d_S4Dq[4] = d_S4Dq[2];
            d_S4Dq[3] = d_S4Dq[1];
            d_S4Dq[2] = d_S4Dq[0];
            d_S4Dq[1] = in[i].imag();
            d_S4Dq[0] = in[i+1].imag();

      }
      // Tell runtime system how many input items we consumed on
      // each input stream.
this->consume(0,sizeof(in));
      this->consume_each(sizeof(in));
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace Research */
} /* namespace gr */

