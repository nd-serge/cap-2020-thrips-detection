## Project Context

Study conducted as part of AI4Industry 2026, focusing on the analysis of the impact of controlled noise on improving the detection of insects known as thrips.

## Problem Statement

Can image quality be improved, for example, by adding noise to high-quality images?

## Methodology

The proposed approach consists of the following steps:

- identifying different types of image noise;
- performing data augmentation using additive and multiplicative noise;
- studying the impact of data augmentation on thrips detection performance.

## Noise Types

The following noise models are considered:

- **Gaussian Noise**: additive noise following a normal distribution with mean 0 and variance 0.01.
- **Poisson Noise**: additive noise strongly correlated with the intensity of each pixel.
- **Salt & Pepper Noise**: impulsive noise randomly altering between 5% and 40% of image pixels.

## Results
![Thrips detection results](images/results.png)
*Figure: Results illustrating the impact of controlled noise on thrips detection performance.*

## Additional information
This code allows you to apply noise to either a single image or all images in a folder. The operation is configured via config.yml, which specifies the input path, output path, noise type, and noise parameters. 
The main libraries used include scikit-image, Pillow, OpenCV, numpy, pandas, and PyYAML.
