# FFT on Wave Signals - Python and Q Implementation

## Project Overview

This project involves the application of the Fast Fourier Transform (FFT) to analyze wave signals represented as a 2-Dimensional vector. The primary goal is to transform raw wave data, visualize its components, and identify key characteristics of the signal, including its resonance frequency.

## Objectives

The following figures are generated as part of this analysis:

1. **Raw Data**: Displays the original wave signal.
2. **Power Spectrum**: Visualizes the frequency components of the wave after transformation.
3. **Filtered Transformed Data**: Shows the modified data post-transformation, highlighting significant frequency components.
4. **Raw Inverted Data without Noise**: Presents the reconstructed wave signal after removing noise from the data.

Additionally, the project aims to pinpoint the **resonance frequency**, identified as the maximum point in the transformed data.

## Implementation

The implementation consists of a Python solution that facilitates the analysis and visualization of wave signals. The results from the FFT are plotted to provide a comprehensive understanding of the wave characteristics.

### Visualization Output

The following figure illustrates the Fourier transform applied to wave signals from an oscilloscope:

![Figure_1](https://github.com/Kokechacho/FFT-for-oscilloscope/assets/67198515/fa125bef-3870-4003-a6f9-f83eab4f89a1)

## Getting Started

To run this project, ensure you have the required libraries installed:

```bash
pip install numpy matplotlib
