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

#ifndef INCLUDED_SOQPSK_DEMOD_SOQPSK_DEMOD_CC_IMPL_H
#define INCLUDED_SOQPSK_DEMOD_SOQPSK_DEMOD_CC_IMPL_H
#define DETECTION_FILTER_SIZE 20
#define REGISTER_SIZE 18

#include <soqpsk_demod/soqpsk_demod_cc.h>

namespace gr {
  namespace soqpsk_demod {

    class soqpsk_demod_cc_impl : public soqpsk_demod_cc
    {
        std::vector<double> S4Di;
      	std::vector<double> S4Dq;
      	std::vector<double> FX,FY;
      	double MU,XI3,YI2,VT1,ET1,VP1,EP1,BnTst,zetat,N1,N2,k0t,kpt,BnTsp,zetap,kpp,k0p,NCO,CTHETA,STHETA,THETA;
      	static double DF[DETECTION_FILTER_SIZE];
     private:
      // Nothing to declare in this block.
        void filter(double &x, double &y, const gr_complex &sampleA,const gr_complex &sampleB);
     	void rotation(double &xr, double &yr,double x, double y);
     	double sign(double val_in);
     	bool DBIT1;

     public:
        soqpsk_demod_cc_impl(bool test_var);
        ~soqpsk_demod_cc_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace soqpsk_demod
} // namespace gr

#endif /* INCLUDED_SOQPSK_DEMOD_SOQPSK_DEMOD_CC_IMPL_H */

