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
#include "detection_filter_downsample_cc_impl.h"

#include <fstream>  
#include <iostream>
#include <string>    
#include <complex>
#include <cmath>

namespace gr {
  namespace Research {

    detection_filter_downsample_cc::sptr
    detection_filter_downsample_cc::make(bool gray_code)
    {
      return gnuradio::get_initial_sptr
        (new detection_filter_downsample_cc_impl(gray_code));
    }

    /*
     * The private constructor
     */
    detection_filter_downsample_cc_impl::detection_filter_downsample_cc_impl(bool gray_code)
      : gr::block("detection_filter_downsample_cc",
              gr::io_signature::make(2, 2, sizeof(gr_complex)),
              gr::io_signature::make(2, 2, sizeof(gr_complex)))
	d_gray_code(gray_code)
    {}

    /*
     * Our virtual destructor.
     */
    detection_filter_downsample_cc_impl::~detection_filter_downsample_cc_impl()
    {
    }

    void
    detection_filter_downsample_cc_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }



    int
    detection_filter_downsample_cc_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      gr_complex *out = (gr_complex *) output_items[0];

/*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Initialization
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*/

	// Phase PLL

	double BnTsp = 0.02;
	double zetap = 0.7071;
	int N = 2;
	double kpp = 18.33;
	int k0p = 1;
	double temp = BnTsp/(zetap + 0.25/zetap);
	double denom = 1 + 2*zetap/N*temp + temp*temp/(N*N);
	double k0kpk1p = 4*zetap/N*temp/denom;
	double k0kpk2p = 4*temp*temp/(N*N*denom);
	double k1p = k0kpk1p/(kpp*k0p);
	double k2p = k0kpk2p/(kpp*k0p);

	double b0p = k1p + k2p;
	double b1p = -k1p;

	// Timing PLL

	double BnTst = 0.01;
	double zetat = 1;
	int N = 2;
	double kpt = 12.35;
	int k0t = -1;
	double temp = BnTst/(zetat + 0.25/zetat);
	double denom = 1 + 2*zetat/N*temp + temp*temp/(N*N);
	double k0kpk1t = 4*zetat/N*temp/denom;
	double k0kpk2t = 4*temp*temp/(N*N*denom);
	double k1t = k0kpk1t/(kpt*k0t);
	double k2t = k0kpk2t/(kpt*k0t);

	double b0t = k1t + k2t;
	double b1t = -k1t;

/*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% define the detection filter
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*/

	double DF=[0.010378066969709,0.023688987704657,0.009767134822858,-0.027017804469398,-0.089762303133391,-0.110346523809347,-0.051853991233850,0.154921158891652,0.568943123186263,0.792392871766106,0.792392871766106,0.568943123186263,0.154921158891652,-0.051853991233850,-0.110346523809347,-0.089762303133391,-0.027017804469398,0.009767134822858,0.023688987704657,0.010378066969709];

/*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% load the I/Q baseband data from the USRP
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	ifsteam input_items;
	indata.open("SOQPSK_data.dat");
	complex<double> a;
	complex<double> data_in[10000];
	int i=0;
	while(indata>>a)
	{
		data_in[i]=a;
		i++;
	}

	int samples_per_buffer = i;
	int samples_per_buffer2 = samples_per_buffer/2;*/


/*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% Initialize the states
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*/

	double S4Di = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0];
	double S4Dq = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0];

	double FX1 = 0;
	double FX2 = 0;
	double FX3 = 0;
	double FX4 = 0;
	double FX5 = 0;
	double FX6 = 0;
	double FX7 = 0;
	double FX8 = 0;
	double FX9 = 0;

	double FY1 = 0;
	double FY2 = 0;
	double FY3 = 0;
	double FY4 = 0;
	double FY6 = 0;
	double FY7 = 0;
	double FY8 = 0;

	double XI3 = 0;
	double YI2 = 0;

	double DBIT1 = 0;

	double VP1 = 0;
	double EP1 = 0;
	double VT1 = 0;
	double ET1 = 0;

	double STROBE = 0;
	double MU = 0;
	double NCO = 0;
	double THETA = 0;
	double CTHETA = 1;
	double STHETA = 0;

/*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% End initialize the states
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*/

	gr_complex aout[floor0(ninput_items/4];
	for(int i=0 ; i<floor0(ninput_items/4) ; i++)
	{
		aout[i]=0;
	}
	
	bool bits[floor0(ninput_items/2];
	for(int i=0 ; i<floor0(ninput_items/2) ; i++)
	{
		bits[i]=0;
	}

	double pk = 1;
	double bk = 1;
	int n = 1;                     

    //%%% compute the outputs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    //%%% get next two samples

	for(int sample_idx = 1 ; sample_idx <= ninput_items ; sample_idx=sample_idx+2)
{//for de

    double ri1 = input_items[sample_idx].real;//you dai kao zheng
    double rq1 = input_items[sample_idx].imag;
    double ri = input_items[sample_idx-1].real;
    double rq = input_items[sample_idx-1].imag;
    
    //%%% compute detection filter outputs
    double x = DF[0] * (ri1 + S4Di[17]) + DF[1] * (ri + S4Di[16]) + DF[2] * (S4Di[0] + S4Di[15]) + DF[3] * (S4Di[1] + S4Di[14]) + DF[4] * (S4Di[2] + S4Di[13]) + DF[5] * (S4Di[3] + S4Di[12]) + DF[6] * (S4Di[4] + S4Di[11]) + DF[7] * (S4Di[5] + S4Di[10]) + DF[8] * (S4Di[6] + S4Di[9]) + DF[9] * (S4Di[7] + S4Di[8]);
    
    double y = DF[0] * (rq1 + S4Dq[17]) + DF[1] * (rq + S4Dq[15]) + DF[2] * (S4Dq[0] + S4Dq[15]) + DF[3] * (S4Dq[1] + S4Dq[14]) + DF[4] * (S4Dq[2] + S4Dq[13]) + DF[5] * (S4Dq[3] + S4Dq[12]) + DF[6] * (S4Dq[4] + S4Dq[11]) + DF[7] * (S4Dq[5] + S4Dq[10]) + DF[8] * (S4Dq[6] + S4Dq[9]) + DF[9] * [S4Dq[7] + S4Dq[8]);

   
    //%%% rotate DF outputs
    double xr = x*CTHETA + y*STHETA;
    double yr = -x*STHETA + y*CTHETA;
    
    //%%% if STROBE make decisions and compute timing and phase errors
    if(STROBE == 0)
    {
        double et = 0;
        double ep = 0;
       }
    else
    {//else de
        double tempFx = -0.5*xr;

    S4Di[7] = S4Di[5];
    S4Di[6] = S4Di[4];
    S4Di[5] = S4Di[3];
    S4Di[4] = S4Di[2];
    S4Di[3] = S4Di[1];
    S4Di[2] = S4Di[0];
    S4Di[1] = ri;
    S4Di[0] = ri1;
    
    S4Dq[17] = S4Dq[15];
    S4Dq[16] = S4Dq[14];
    S4Dq[15] = S4Dq[13];
    S4Dq[14] = S4Dq[12];
    S4Dq[13] = S4Dq[11];
    S4Dq[12] = S4Dq[10];
    S4Dq[11] = S4Dq[9];
    S4Dq[10] = S4Dq[8];
    S4Dq[9] = S4Dq[7];
    S4Dq[8] = S4Dq[6];
    S4Dq[7] = S4Dq[5];
    S4Dq[6] = S4Dq[4];
    S4Dq[5] = S4Dq[3];
    S4Dq[4] = S4Dq[2];
    S4Dq[3] = S4Dq[1];
    S4Dq[2] = S4Dq[0];
    S4Dq[1] = rq;
    S4Dq[0] = rq1;

         double tempFy = -0.5*yr;
   
   
        //%%% compute interpolant yi from rotated DF outputs
        double v2 = -tempFy + FY1 + FY2 - FY3;
        double v1 = tempFy - FY1 + FY6 + FY2 + FY3;
        double yi = (v2 * MU + v1) * MU + FY7;
        
        //%%% compute interpolants xi1 and yi1 rotated DF outputs
        v2 = -FX1 + FX2 + FX3 - FX4;
        v1 = FX1 - FX2 + FX7 + FX3 + FX4;
        double xi1 = (v2 * MU + v1) * MU + FX8;
        
        v2 = -FY1 + FY2 + FY3 - FY4;
        v1 = FY1 - FY2 + FY7 + FY3 + FY4;
        double yi1 = (v2 * MU + v1) * MU + FY8;
        
        //%%% compute interpolant xi2 from rotated DF outputs
        
        v2 = -FX2 + FX3 + FX4 - FX5;
        v1 = FX2 - FX3 + FX8 + FX4 + FX5;
        double xi2 = (v2 * MU + v1) * MU + FX9;
        
        //%%% compute et
        double et = [(xi2 > 0) - (xi2 < 0)] * (xi1 - XI3) + [(yi1 > 0) - (yi1 < 0)] * (yi - YI2);
        
        //%%% compute ep
        double ep = [(xi2 > 0) - (xi2 < 0)] * YI2 - [(yi1 > 0) - (yi1 < 0)] * xi1;

	//%%% output
	gr_complex i=sqrt(-1);
	int d0;
	int d1;

        aout[pk-1] = xi2 + 1*i*yi1;
        pk = pk + 1;

        if(xi2 > 0)
            d0 = 1;
        else
            d0 = 0;
 
        if(yi1 > 0)
            d1 = 1;
        else
            d1 = 0;
   

        bits[bk-1] = ( d0 && DBIT1 ) && ( d0 || DBIT1 );
        bits[bk] = !( d0 && d1 ) && ( d0 || d1 );
        bk = bk+2;


    
    }//else de

   
    //%%% compute timing loop filter output
    double vt = VT1 + b0t*et + b1t*ET1;

    S4Di[16] = S4Di[14];
    S4Di[15] = S4Di[13];
    S4Di[14] = S4Di[12];
    S4Di[13] = S4Di[11];
    S4Di[12] = S4Di[10];
    S4Di[11] = S4Di[9];
    S4Di[10] = S4Di[8];
    S4Di[9] = S4Di[7];
    S4Di[8] = S4Di[6];
    S4Di[7] = S4Di[5];
    S4Di[6] = S4Di[4];
    S4Di[5] = S4Di[3];
    S4Di[4] = S4Di[2];
    S4Di[3] = S4Di[1];
    S4Di[2] = S4Di[0];
    S4Di[1] = ri;
    S4Di[0] = ri1;
    
    S4Dq[17] = S4Dq[15];
    S4Dq[16] = S4Dq[14];
    S4Dq[15] = S4Dq[13];
    S4Dq[14] = S4Dq[12];
    S4Dq[13] = S4Dq[11];
    S4Dq[12] = S4Dq[10];
    S4Dq[11] = S4Dq[9];
    S4Dq[10] = S4Dq[8];
    S4Dq[9] = S4Dq[7];
    S4Dq[8] = S4Dq[6];
    S4Dq[7] = S4Dq[5];
    S4Dq[6] = S4Dq[4];
    S4Dq[5] = S4Dq[3];
    S4Dq[4] = S4Dq[2];
    S4Dq[3] = S4Dq[1];
    S4Dq[2] = S4Dq[0];
    S4Dq[1] = rq;
    S4Dq[0] = rq1;
    
    //%%% compute phase loop filter output
    double vp = VP1 + b0p*ep + b1p*EP1;

    //%%% compute NCO input
    double w = vt + 0.5;
        
    //%%% end compute the outputs %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    //%%% compute the next states %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    S4Di[17] = S4Di[15];
    S4Di[16] = S4Di[14];
    S4Di[15] = S4Di[13];
    S4Di[14] = S4Di[12];
    S4Di[13] = S4Di[11];
    S4Di[12] = S4Di[10];
    S4Di[11] = S4Di[9];
    S4Di[10] = S4Di[8];
    S4Di[9] = S4Di[7];
    S4Di[8] = S4Di[6];
    S4Di[7] = S4Di[5];
    S4Di[6] = S4Di[4];
    S4Di[5] = S4Di[3];
    S4Di[4] = S4Di[2];
    S4Di[3] = S4Di[1];
    S4Di[2] = S4Di[0];
    S4Di[1] = ri;
    S4Di[0] = ri1;
    
    S4Dq[17] = S4Dq[15];
    S4Dq[16] = S4Dq[14];
    S4Dq[15] = S4Dq[13];
    S4Dq[14] = S4Dq[12];
    S4Dq[13] = S4Dq[11];
    S4Dq[12] = S4Dq[10];
    S4Dq[11] = S4Dq[9];
    S4Dq[10] = S4Dq[8];
    S4Dq[9] = S4Dq[7];
    S4Dq[8] = S4Dq[6];
    S4Dq[7] = S4Dq[5];
    S4Dq[6] = S4Dq[4];
    S4Dq[5] = S4Dq[3];
    S4Dq[4] = S4Dq[2];
    S4Dq[3] = S4Dq[1];
    S4Dq[2] = S4Dq[0];
    S4Dq[1] = rq;
    S4Dq[0] = rq1;
    
    
    FX5 = FX4;
    FX4 = FX3;
    FX3 = FX2;
    FX2 = FX1;
    FX1 = -0.5*xr;
    FX9 = FX8;
    FX8 = FX7;
    FX7 = FX6;
    FX6 = xr;
    
    FY4 = FY3;
    FY3 = FY2;
    FY2 = FY1;
    FY1 = -0.5*yr;
    FY8 = FY7;
    FY7 = FY6;
    FY6 = yr;
    

    if(STROBE)
    {
        XI3 = xi1;
        YI2 = yi;
        DBIT1 = d1;
       }

    
    VP1 = vp;
    EP1 = ep;
    VT1 = vt;
    ET1 = et;
    
    temp = NCO - w;

    if(temp < 0)
    {
        STROBE = 1;
        MU = NCO/w;
        NCO = 1 + temp;
       }
    else
    {
        STROBE = 0;
        NCO = temp;
       }
 
    
    THETA = THETA + vp;
    CTHETA = cos(THETA);
    STHETA = sin(THETA);
    
    //%%% end compute the next states %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	
        


}// for de

	for(int j=0; j<(pk-1); j++)
	{
	output_items[j]=aout[j];
	}

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

	


  } /* namespace Research */
} /* namespace gr */

