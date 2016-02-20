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
#include "soqpsk_test_impl.h"

namespace gr {
  namespace Research {

    soqpsk_test::sptr
    soqpsk_test::make(int test_var)
    {
      return gnuradio::get_initial_sptr
        (new soqpsk_test_impl(test_var));
    }

    /*
     * The private constructor
     */
    soqpsk_test_impl::soqpsk_test_impl(int test_var)
      : gr::block("soqpsk_test",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(char))),
              d_test_var(test_var)
    {}

    /*
     * Our virtual destructor.
     */
    soqpsk_test_impl::~soqpsk_test_impl()
    {
    }

    void soqpsk_test_impl::forecast(int noutput_items, gr_vector_int &ninput_items_required)
    {
    }

    void soqpsk_test_impl::rotation(double x,
        double y,
        double &xr,
        double &yr)
    {

    }
    int
    soqpsk_test_impl::general_work(int noutput_items,
        gr_vector_int &ninput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];
      double *out = (double *) output_items[0];

      // Do <+signal processing+>

        // Initializations

        // Phase PLL
        gr_vector_void_star aout;
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
        int zetat = 1;
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

        // Detection filter definition
        gr_vector_double DF[20] = { 0.010378066969709,
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

        // Get the sizes of the buffer

        int samples_per_buffer = ninput_items;  // This is passed in by reference; just in case you get errors
        int samples_per_buffer2 = samples_per_buffer/2;

        // Initialize the states
        gr_vector_double S4Di = (18,0);
        gr_vector_double S4Dq = (18,0);

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

        bool DBIT1 = 0;

        double VP1 = 0;
        double EP1 = 0;
        double VT1 = 0;
        double ET1 = 0;

        bool STROBE = 0;
        double MU = 0;
        double NCO = 0;
        double THETA = 0;
        double CTHETA = 1;
        double STHETA = 0;

        // End initialize the states


        double ri1,rq1,ri,rq,x,y,xr,yr,et,xi,yi,xi1,yi1,xi2,yi2,v1,v2,tempFx,tempFy,empFy,ep,w,bk,vt,vp;
        bool d0,d1;
        int pk;
        std::vector<bool> bits; // You may want to change this!!!!
        int downsample = 2;
        //filtering happens here
        for( int i = 0 ; i < samples_per_buffer ; i+downsample) {

            // Filter and downsample at the same time;
            ri1 = real(r(sample_idx+1));
            rq1 = imag(r(sample_idx+1));
            ri = real(r(sample_idx));
            rq = imag(r(sample_idx));

            x = DF[1] * (ri1 + S4Di[18])
                + DF[2] * (ri + S4Di[17])
                + DF[3] * (S4Di[1] + S4Di[16])
                + DF[4] * (S4Di[2] + S4Di[15])
                + DF[5] * (S4Di[3] + S4Di[14])
                + DF[6] * (S4Di[4] + S4Di[13])
                + DF[7] * (S4Di[5] + S4Di[12])
                + DF[8] * (S4Di[6] + S4Di[11])
                + DF[9] * (S4Di[7] + S4Di[10])
                + DF[10] * (S4Di[8] + S4Di[9]);

            y = DF[1] * (rq1 + S4Dq[18])
                + DF[2] * (rq + S4Dq[17])
                + DF[3] * (S4Dq[1] + S4Dq[16])
                + DF[4] * (S4Dq[2] + S4Dq[15])
                + DF[5] * (S4Dq[3] + S4Dq[14])
                + DF[6] * (S4Dq[4] + S4Dq[13])
                + DF[7] * (S4Dq[5] + S4Dq[12])
                + DF[8] * (S4Dq[6] + S4Dq[11])
                + DF[9] * (S4Dq[7] + S4Dq[10])
                + DF[10] * (S4Dq[8] + S4Dq[9]);

            // rotate DF outputs
            xr = x*CTHETA + y*STHETA;
            yr = -x*STHETA + y*CTHETA;

            if(STROBE) {
                //GR_LOG_DEBUG(d_debug_logger, "Strobe on");
                et = 0;
                ep = 0;
            }
            else {
                tempFx = -0.5*xr;
                empFy = -0.5*yr;

                // compute interpolant yi from rotated DF outputs
                v2 = -tempFy + FY1 + FY2 - FY3;
                v1 = tempFy - FY1 + FY6 + FY2 + FY3;
                yi = (v2 * MU + v1) * MU + FY7;

                // compute interpolants xi1 and yi1 rotated DF outputs
                v2 = -FX1 + FX2 + FX3 - FX4;
                v1 = FX1 - FX2 + FX7 + FX3 + FX4;
                xi1 = (v2 * MU + v1) * MU + FX8;

                // Compute interpolants xi1 and yi1 rotated DF outputs
                v2 = -FY1 + FY2 + FY3 - FY4;
                v1 = FY1 - FY2 + FY7 + FY3 + FY4;
                yi1 = (v2 * MU + v1) * MU + FY8;


                // Compute interpolant xi2
                v2 = -FX2 + FX3 + FX4 - FX5;
                v1 = FX2 - FX3 + FX8 + FX4 + FX5;
                xi2 = (v2 * MU + v1) * MU + FX9;

                //Compute et
                et = sign(xi2) * (xi1 - XI3) + sign(yi1) * (yi - YI2);

                // compute ep
                ep = sign(xi2)*YI2 - sign(yi1)*xi1;

                // output
                out[pk] = xi2 + 1i*yi1;
                pk = pk + 1;
                if (xi2 > 0) {
                    d0 = 1;
                }
                else {
                    d0 = 0;
                }


                if (yi1 > 0) {
                    d1 = 1;
                }
                else {
                    d1 = 0;
                }

                bits[bk] = d0^DBIT1;
                bits[bk+1] = d1^d0;
                bk = bk+2;
            }
            vt = VT1 + b0t*et + b1t*ET1;
            vp = VP1 + b0p*ep + b1p*EP1;
            w = vt + 0.5;

            // Compute the next states
            S4Di[18] = S4Di[16];
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
            S4Di[2] = ri;
            S4Di[1] = ri1;

            S4Dq[18] = S4Dq[16];
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
            S4Dq[2] = rq;
            S4Dq[1] = rq1;

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

            if(STROBE) {
                XI3 = xi1;
                YI2 = yi;
                DBIT1 = d1;
            }

            VP1 = vp;
            EP1 = ep;
            VT1 = vt;
            ET1 = et;

            temp = NCO - w;

            if(temp < 0) {
                STROBE = 1;
                MU = NCO/w;
                NCO = 1 + temp;
            }
            else {
                STROBE = 0;
                NCO = temp;
            }

            THETA = THETA + vp;
            CTHETA = cos(THETA);
            STHETA = sin(THETA);
        } // End For

        noutput_items = 0;
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace Research */
} /* namespace gr */

