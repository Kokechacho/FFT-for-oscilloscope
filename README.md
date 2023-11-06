# FFT on wave signals - Python and Q implementation

> Given a discrete function which corresponds to a 2-Dimensional vector, we need to apply the FFT so that we can plot 4 figures:

  1. Raw data (wave signal)
  2. Power espectrum from the data once is transformed
  3. Filtered transformed data
  4. Raw inverted data without noise

An extra requirement is pointing the resonance frequency of that wave, that being the maximum point from the transformed data.

We will first implement a python solution for this problem resulting in the next figures:

![Figure_1](https://github.com/Kokechacho/FFT-for-oscilloscope/assets/67198515/fa125bef-3870-4003-a6f9-f83eab4f89a1)

As you may see, numpy is used for the FFT calculus. This is for efficiency reasons. Nevertheless we can always easily implement it as seen in below.

Now we will try and do it on Q and see the differences.

The problem we face is that Q has no native support for imaginary numbers so we need to implement it ourselves.

