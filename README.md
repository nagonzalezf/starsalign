# StarsAlign - A package for aligning and comparing high density astronomical images with extreme precision

StarsAlign is a package for aligning and comparing astronomical images using the SIFT algorithm and FLANN based matcher.

It contains functions such as ```align()``` and ```diff()``` that aligns and compute the difference of two single channel images.

The package also contains ```ultra_align()``` and ```ultra_diff()``` functions for extreme precision, but they may require more resources.

Examples of this package usage can be found inside the folder examples: https://github.com/nagonzalezf/starsalign/tree/main/examples

The lastest package version is ```1.0.12```.

| Reference Image  | Science Image | Raw Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/hDQhcy7/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/kmGznJg/002-science-image.png" width="240">  | <img src="https://i.ibb.co/LPXqhCy/003-raw-diff-image.png" width="240">  |

| Reference Image  | Aligned Science Image | Aligned Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/hDQhcy7/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/CtHtLbb/004-aligned-image.png" width="240">  | <img src="https://i.ibb.co/vPs7zLD/005-diff-image.png" width="240">  |

## Important

This package was specifically designed to work with images that have a high amount of information, such as 4096x2048 pixels, with float32 data type, and a range of values between -155.45811 and 43314.49.

It is recommended to use the ```ultra_align()``` and ```ultra_diff()``` functions on lower resolution or lower density images, but it may result in prolonged waiting times.

# Installation

Using pip:

```bash
pip install starsalign
```

Using ```setup.py``` file from root directory

```bash
python setup.py install
```
# Usage examples

Getting the aligned science image using ```align()``` function (faster method)
```
>>> import starsalign as stal
>>> aligned_image = stal.align(ref_image, science_image)
```

Getting the aligned science image with a more precise alignment using ```ultra_align()``` function (slower but more precise)
```
>>> import starsalign as stal
>>> aligned_image = stal.ultra_align(ref_image, science_image)
```
# Supported input formats

By default the package is intended to be use over **float 32** single channel images of wide range, but it can also process other formats such as **uint8** images or even binary images.

The ```align()``` and ```diff()``` functions will only support single channel images.

If you want to process multi channel images you have two options:

1. You can use the ```ultra_align()``` and ```ultra_diff()``` functions, these will automatically get rid of the multi channels and perform the calculations over buffer single channel images to finally process and extract the original multi channel images as output.

2. You can get rid of the extra channels yourself performing some pre-processing tasks such as opencv ```cvtColor()``` and ```COLOR_BGR2GRAY``` functions or similar methods and then process the images using the default ```align()``` and ```diff()``` starsalign functions.

# Difference Image Analysis (DIA) application examples

The main idea behind this technique is to subtract two images of the same portion of the sky, removing all photometrically stable stars, but tipically this images are not aligned by default.

## Example 1 - ```diff()``` function

For this example we will use some float32 images of the NGC6569 globular cluster in the constellation Sagittarius.

| Reference Image  | Science Image | Raw Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/bQsdzKh/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/R7z22P0/002-science-image.png" width="240">  | <img src="https://i.ibb.co/9yPDhMk/003-raw-diff-image.png" width="240">  |

As you can see the reference and science images are not aligned, so the raw difference results are incorrect.

We process the image using ```diff()``` function (faster method):

```
>>> import starsalign as stal
>>> aligned_image = stal.diff(ref_image, science_image)
```
And we get a desired difference result:

| Reference Image  | Aligned Science Image | Aligned Difference Image |
| ------------- | ------------- | ------------- |
| <img src="https://i.ibb.co/bQsdzKh/001-ref-image.png" width="240">  | <img src="https://i.ibb.co/d49V0Zc/004-aligned-image.png" width="240">  | <img src="https://i.ibb.co/GCy1qKc/005-diff-image.png" width="240">  |

# Documentation

Documentation is under construction, in the meantime you can check:

SIFT algorithm docs at: https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

FLANN feature matcher docs at: https://docs.opencv.org/4.x/d5/d6f/tutorial_feature_flann_matcher.html

Wich are the key methods applied.
