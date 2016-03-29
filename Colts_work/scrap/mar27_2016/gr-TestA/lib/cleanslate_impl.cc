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
#include "cleanslate_impl.h"

namespace gr {
  namespace TestA {

    cleanslate::sptr
    cleanslate::make(bool test, int foo)
    {
      return gnuradio::get_initial_sptr
        (new cleanslate_impl(test, foo));
    }

    /*
     * The private constructor
     */
    cleanslate_impl::cleanslate_impl(bool test, int foo)
      : gr::block("cleanslate",
              gr::io_signature::make(1,1, sizeof(gr_complex)),
              gr::io_signature::make(1,1, sizeof(gr_complex)))
    {}

    /*
     * Our virtual destructor.
     */
    cleanslate_impl::~cleanslate_impl()
    {
    }

    void
    cleanslate_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
       ninput_items_required[0] = noutput_items;
    }

    int
    cleanslate_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];

      // Basic test
      for(int i = 0 ; i < noutput_items ; i++) {
        out[i] = in[i];
      }
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Detection filter test

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace TestA */
} /* namespace gr */

