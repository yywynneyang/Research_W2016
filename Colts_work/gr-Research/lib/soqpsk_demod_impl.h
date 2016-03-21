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

#ifndef INCLUDED_RESEARCH_SOQPSK_DEMOD_IMPL_H
#define INCLUDED_RESEARCH_SOQPSK_DEMOD_IMPL_H

#include <Research/soqpsk_demod.h>
#define DETECTION_FILTER_SIZE 20
#define REGISTER_SIZE 18
namespace gr {
  namespace Research {

    class soqpsk_demod_impl : public soqpsk_demod
    {
////      double S4Di[REGISTER_SIZE] ;
//      double S4Dq[REGISTER_SIZE] ;

      double S4Di[REGISTER_SIZE];
    double S4Dq[REGISTER_SIZE];

      double FX[REGISTER_SIZE];
      double FY[REGISTER_SIZE];
      double MU,XI3,YI2,VT1,ET1,VP1,EP1,BnTst,zetat,N1,N2,k0t,kpt,BnTsp,zetap,kpp,k0p,NCO,CTHETA,STHETA,THETA;
      static double DF[DETECTION_FILTER_SIZE];

     private:
      // Nothing to declare in this block.
     void filter(double &x, double &y, const gr_complex &sampleA,const gr_complex &sampleB);
     void rotation(double &xr, double &yr,double x, double y);
     double sign(double val_in);
     bool DBIT1;
     double return_BnTst();
     public:
      soqpsk_demod_impl(bool test_var);
      ~soqpsk_demod_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace Research
} // namespace gr

#endif /* INCLUDED_RESEARCH_SOQPSK_DEMOD_IMPL_H */

