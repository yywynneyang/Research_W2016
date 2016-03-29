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
#include "rotation_cc_impl.h"

namespace gr {
  namespace Research {

    rotation_cc::sptr
    rotation_cc::make()
    {
      return gnuradio::get_initial_sptr
        (new rotation_cc_impl());
    }

    /*
     * The private constructor
     */
    rotation_cc_impl::rotation_cc_impl(
//		unsigned int history
	)
      : gr::block("rotation_cc",
              gr::io_signature::make(2,2, sizeof(double)),
              gr::io_signature::make(2,2, sizeof(double)))
    {
		//set_history(18);  // This sets the register length
	}


    /*
     * Our virtual destructor.
     */
    rotation_cc_impl::~rotation_cc_impl()
    {
    }

    void
    rotation_cc_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
	/*unsigned int input_required = noutput_items;
	unsigned ninputs = ninput_items_required.size();
	for(unsigned i = 0 ; i < ninputs; i++)
	{
		ninput_items_required[i] = noutput_items;
	}*/
    }

    int
    rotation_cc_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const double *in = (const double *) input_items[0];
      double *out = (double *) output_items[0];

	//The CTHETA and STHETA values are usually set through a feedback loop set by the Phase Error Detection module, but for this test case we will only test with set values:
	/*double STHETA = 0;
	double CTHETA = 1;
	
      // Do <+signal processing+>
	out[0] = in[0]*CTHETA +  in[1]*STHETA;
	out[1] = - in[0]*STHETA +  in[1]*CTHETA;	*/
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace Research */
} /* namespace gr */

