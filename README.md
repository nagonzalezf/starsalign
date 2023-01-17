# StarsAlign - A package developed for aligning and comparing high density astronomical images with extreme precision

StarsAlign is a tool for aligning and comparing astronomical images using the SIFT algorithm and FLANN based matcher.

It contains functions such as ```fast_align()``` and ```fast_diff()``` that aligns and compute the difference of two single channel images.

The package also contains ```align()``` and ```diff()``` functions for extreme precision, but they may require more resources.

Examples of this package usage can be found inside the folder: https://github.com/nagonzalezf/starsalign/tree/main/examples

| Reference Image  | Science Image | Raw Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/hDQhcy7/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/kmGznJg/002-science-image.png" width="240">  | <img src="https://i.ibb.co/LPXqhCy/003-raw-diff-image.png" width="240">  |

| Reference Image  | Aligned Science Image | Aligned Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/hDQhcy7/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/CtHtLbb/004-aligned-image.png" width="240">  | <img src="https://i.ibb.co/vPs7zLD/005-diff-image.png" width="240">  |

### Important ###

Functions ```fast_align()``` and ```fast_diff()``` were specifically designed to work with images that have a high amount of information, such as 4096x2048 pixels, with float32 data type, and a range of values between -40000 and 40000.

It is recommended to use the ```align()``` and ```diff()``` functions on lower resolution or lower density images, but it may result in prolonged waiting times for bigger images.

# Installation

Using pip:

```bash
pip install starsalign
```

Using ```setup.py``` file from root directory

```bash
python setup.py install
```
# Examples

Getting the aligned science image using ```fast_align()``` function (faster method)
```
>>> import starsalign as sa
>>> aligned_image = sa.fast_align(ref_image, science_image)
```

Getting the aligned difference image with a more precise alignment using ```diff()``` function (slower but more accurate)
```
>>> import starsalign as sa
>>> aligned_difference_image = sa.diff(ref_image, science_image)
```
# Supported input formats

By default the package is intended to be use over **float 32** single channel images of wide range, but it can also process other formats such as **uint8** images or even binary images.

The ```fast_align()``` and ```fast_diff()``` functions will only support single channel images.

If you want to process multi channel images you have two options:

1. You can use the ```align()``` and ```diff()``` functions, these will automatically get rid of the multi channels and perform the calculations over temporary buffer single channel images to finally process and extract the original multi channel images as output.

2. You can get rid of the extra channels yourself performing some pre-processing tasks such as opencv ```cvtColor()``` and ```COLOR_BGR2GRAY``` functions or similar methods and then process the images using the ```fast_align()``` and ```fast_diff()``` functions.

# Difference Image Analysis (DIA) application examples

The main idea behind this technique is to subtract two images of the same portion of the sky, removing all photometrically stable stars, but tipically this images are not aligned by default.

## Example 1 - ```fast_align()``` & ```fast_diff()``` functions

We are working over two wide-range float32 images of the NGC6569 globular cluster in the constellation Sagittarius. These images were captured using the Dark Energy Camera (DECam) instrument of the Victor M. Blanco 4-meter Telescope at the Cerro Tololo Inter-American Observatory (CTIO) in the Chilean Andes. They were pre-processed using the data reduction pipelines developed by the Rubin Observatory (LSST pipelines).

| Reference Image  | Science Image | Raw Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/bQsdzKh/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/R7z22P0/002-science-image.png" width="240">  | <img src="https://i.ibb.co/9yPDhMk/003-raw-diff-image.png" width="240">  |

The reference and science images are not aligned, so the raw difference results are incorrect.

We process the image using ```fast_align()``` and ```fast_diff()``` functions (faster method):

```
>>> import starsalign as sa
>>> aligned_image = sa.fast_align(ref_image, science_image)
>>> aligned_difference_image = sa.fast_diff(ref_image, science_image)
```
And we get the desired difference result:

| Reference Image  | Aligned Science Image | Aligned Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/bQsdzKh/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/d49V0Zc/004-aligned-image.png" width="240">  | <img src="https://i.ibb.co/GCy1qKc/005-diff-image.png" width="240">  |

### Note: ###
This results were obtained using the lsst.dirac.dev resources (CPU, RAM) and they were calculated in about 8 seconds. If we perform the proccesing under the same conditions using ```align()``` and ```diff()``` functions, then it takes about 20 minutes to complete and we get a slightly more accurate x and y displacement value calculations.

The source float32 images used for this examples can be found at:
https://github.com/nagonzalezf/starsalign/blob/main/examples/ref_image.npy
https://github.com/nagonzalezf/starsalign/blob/main/examples/science_image.npy

# Documentation

Documentation is under construction, in the meantime you can check:

SIFT algorithm docs at: https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

FLANN feature matcher docs at: https://docs.opencv.org/4.x/d5/d6f/tutorial_feature_flann_matcher.html
