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
#include "soqpsk_demod_impl.h"

// For the complex datatypes
#include <pmt/pmt.h>
#include <gnuradio/blocks/complex_to_float.h>
#include <gnuradio/blocks/complex_to_imag.h>
#include <complex>  //Not the standard!  Figure this out!

namespace gr {
  namespace Research {

    soqpsk_demod::sptr
    soqpsk_demod::make(bool test_var)
    {
      return gnuradio::get_initial_sptr
        (new soqpsk_demod_impl(test_var));
    }

    /*
     * The private constructor
     */
    soqpsk_demod_impl::soqpsk_demod_impl(bool test_var)
      : gr::sync_block("soqpsk_demod",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(double)))
    {
    }

    /*
     * Our virtual destructor.
     */
    soqpsk_demod_impl::~soqpsk_demod_impl()
    {
    }






    // Detection filter coefficients
    double soqpsk_demod_impl::DF[DETECTION_FILTER_SIZE] = {0.010378066969709,
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

    // Register initializations; easy way of doing it
    std::vector<double> S4Di(REGISTER_SIZE,0);
    std::vector<double> S4Dq(REGISTER_SIZE,0);

    void soqpsk_demod_impl::filter(double &x, double &y, const gr_complex &sampleA,const gr_complex &sampleB) {
        x = DF[1] * (sampleB.real() + S4Di[18])
            + DF[2] * (sampleA.real() + S4Di[17])
            + DF[3] * (S4Di[1] + S4Di[16])
            + DF[4] * (S4Di[2] + S4Di[15])
            + DF[5] * (S4Di[3] + S4Di[14])
            + DF[6] * (S4Di[4] + S4Di[13])
            + DF[7] * (S4Di[5] + S4Di[12])
            + DF[8] * (S4Di[6] + S4Di[11])
            + DF[9] * (S4Di[7] + S4Di[10])
            + DF[10] * (S4Di[8] + S4Di[9]);

        y = DF[1] * (sampleB.imag() + S4Dq[18])
            + DF[2] * (sampleA.imag() + S4Dq[17])
            + DF[3] * (S4Dq[1] + S4Dq[16])
            + DF[4] * (S4Dq[2] + S4Dq[15])
            + DF[5] * (S4Dq[3] + S4Dq[14])
            + DF[6] * (S4Dq[4] + S4Dq[13])
            + DF[7] * (S4Dq[5] + S4Dq[12])
            + DF[8] * (S4Dq[6] + S4Dq[11])
            + DF[9] * (S4Dq[7] + S4Dq[10])
            + DF[10] * (S4Dq[8] + S4Dq[9]);
    }


    // Main function
    int
    soqpsk_demod_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex*) input_items[0];
      double *out = (double *) output_items[0];
    // You could consider using the gr_complexd type to use a complex double rather than a float;
    // The complex type stores both a real and complex float type
      // Do <+signal processing+>

      // Initializations
      double x;
      double y;
      // Defining the detection filter

      // Initialize the states


      // End initializations
      int downsample_val = 2;   // Figure out how to get the sample rate
      for(int i = 0 ; i < noutput_items ; i= i + downsample_val)
      {
            // Output computation ------
            //x = this->filter()
            //std::cout << gr::blocks::complex_to_float(input_items[i]) << endl;
            // Get the next two samples
            this->filter(x,y,in[i],in[i+1]);

      }

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace Research */
} /* namespace gr */

