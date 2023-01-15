# StarsAlign - A package for aligning and comparing high density astronomical images with extreme precision

StarsAlign is a package for aligning and comparing astronomical images using the SIFT algorithm and FLANN based matcher.

It contains functions such as align() and diff() that aligns and compute the difference of two single channel images.

The package also contains ultra_align() and ultra_diff() functions for extreme precision, but they may require more resources.

This package was specifically designed to work with images that have a high amount of information, such as 4096x2048 pixels, with float32 data type, and a range of values between -155.45811 and 43314.49.

It is recommended to use the ultra_align() and ultra_diff() functions on lower resolution or lower density images, but it may result in prolonged waiting times.

The lastest package version is 1.0.7.

# Installation

Using pip:

```bash
pip install starsalign
```

Using setup.py file from root directory

```bash
python setup.py install
```
# Usage examples

Getting the aligned science image using align() function
```
>>> import starsalign as stal
>>> aligned_image = stal.align(ref_image, science_image)
```

Getting the aligned science image with a more precise alignment using ultra_align() function
```
>>> import starsalign as stal
>>> aligned_image = stal.align(ref_image, science_image)
```
