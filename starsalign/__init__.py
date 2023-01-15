"""
StarsAlign
==========

A package for aligning and comparing astronomical images.

Specially developed to work over float32 images with a large intensity range, typically found in astronomical imaging.

This package contains functions such as ```align()``` and ```diff()```that aligns and compute the difference of two single channel images using SIFT algorithm and FLANN based matcher.

You can also try functions ```ultra_align()``` and ```ultra_diff()``` for extreme precision, but it may require more resources

Example:
===
    >>> import numpy as np
    >>> import starsalign as stal
    >>>
    >>> diff_image = stal.ultra_diff(ref_image, science_image)
    >>> aligned_image = stal.ultra_align(ref_image, science_image)

Important:
===
This package was specifically designed to work with images that have a high amount of information, such as 4096x2048 pixels, with float32 data type, and a range of values between -155.45811 and 43314.49.

If your images have a high density of information, then the align() and diff() functions should work well. However, if you are working with images of lower resolution or lower information density, it is recommended to use the ultra_align() and ultra_diff() functions.

Warning: Using the ultra_align() and ultra_diff() functions on high-density information and high-resolution images may result in prolonged waiting times.
"""

__version__ = "1.0.7"

import os
import cv2 as cv
import numpy as np

def align(ref_image: np.ndarray, science_image: np.ndarray) -> np.ndarray:
    """
    align()
    ===
    Aligns the science_image to the reference image by finding keypoints and matching them using SIFT algorithm, then finds the homography between the two images, and applies a perspective warp to align the science_image.
    
    Parameters:
        ref_image (np.ndarray): The reference image, to which the science_image will be aligned.
        science_image (np.ndarray): The science image that will be aligned to the reference image.
        
    Returns:
        np.ndarray: The aligned science image.
    
    Example:
    ===
    >>> import starsalign as stal
    >>> aligned_image = stal.align(ref_image, science_image)
    """
    ref_image_uint8 = np.interp(ref_image, (ref_image.min(), ref_image.max()), (0, 255)).astype(np.uint8)
    science_image_uint8 = np.interp(science_image, (science_image.min(), science_image.max()), (0, 255)).astype(np.uint8)

    sift = cv.SIFT_create()
    keypoints1, descriptor1 = sift.detectAndCompute(science_image_uint8, None)
    keypoints2, descriptor2 = sift.detectAndCompute(ref_image_uint8, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptor1, descriptor2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    points1 = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    points2 = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    M, mask = cv.findHomography(points1, points2, cv.RANSAC, 5.0)

    dx = M[0, 2]
    dy = M[1, 2]
    print(f'The displacement on the x-axis is of {dx} pixels')
    print(f'The displacement on the y-axis is of {dy} pixels')

    height = science_image.shape[0]
    width = science_image.shape[1]
    aligned_image = cv.warpPerspective(science_image, M, (width, height))
    
    return aligned_image

def ultra_align(ref_image: np.ndarray, science_image: np.ndarray) -> np.ndarray:
    """
    ultra_align()
    ===
    A more advanced version of the alignment function that uses more channels to perform the calculations, which results in a more precise alignment.
    
    Parameters:
        ref_image (np.ndarray): The reference image, to which the science_image will be aligned.
        science_image (np.ndarray): The science image that will be aligned to the reference image.
        
    Returns:
        np.ndarray: The aligned science image.
    
    Example:
    ===
    >>> import starsalign as stal
    >>> aligned_image = stal.ultra_align(ref_image, science_image)
    """
    cv.imwrite('ref_buffer.png', ref_image)
    cv.imwrite('science_buffer.png', science_image)

    ref_image_uint8 = cv.imread('ref_buffer.png')
    science_image_uint8 = cv.imread('science_buffer.png')

    if os.path.exists('ref_buffer.png'):
        os.remove('ref_buffer.png')

    if os.path.exists('science_buffer.png'):
        os.remove('science_buffer.png')

    gray1 = cv.cvtColor(ref_image_uint8, cv.COLOR_BGR2GRAY)
    gray2 = cv.cvtColor(science_image_uint8, cv.COLOR_BGR2GRAY)

    sift = cv.SIFT_create()
    keypoints1, descriptor1 = sift.detectAndCompute(gray2, None)
    keypoints2, descriptor2 = sift.detectAndCompute(gray1, None)

    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(descriptor1, descriptor2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    points1 = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    points2 = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    M, mask = cv.findHomography(points1, points2, cv.RANSAC, 5.0)

    dx = M[0, 2]
    dy = M[1, 2]
    print(f'The displacement on the x-axis is of {dx} pixels')
    print(f'The displacement on the y-axis is of {dy} pixels')

    height = science_image.shape[0]
    width = science_image.shape[1]
    aligned_image = cv.warpPerspective(science_image, M, (width, height))
    
    return aligned_image

def diff(ref_image: np.ndarray, science_image: np.ndarray) -> np.ndarray:
    """
    diff()
    ===
    Computes the difference between two single channel images by first aligning them and then subtracting them.

    Parameters:
        ref_image (np.ndarray): Reference image, it should be a single channel image.
        science_image (np.ndarray): Science image, it should be a single channel image.

    Returns:
        np.ndarray: The result of the subtraction between the aligned science image and the reference image.

    Example:
    ===
    >>> import starsalign as stal
    >>> diff_image = stal.diff(ref_image, science_image)
    """
    aligned_image = align(ref_image, science_image)
    diff_image = ref_image - aligned_image
    return diff_image

def ultra_diff(ref_image, science_image):
    """
    ultra_diff()
    ===
    A more advanced version of the difference function that uses more channels to perform the calculations, which results in a more precise alignment.
    
    Computes the difference between two images by first aligning them and then subtracting them.

    Parameters:
        ref_image (np.ndarray): Reference image, it should be a single channel image.
        science_image (np.ndarray): Science image, it should be a single channel image.

    Returns:
        np.ndarray: The result of the subtraction between the aligned science image and the reference image.

    Example:
    ===
    >>> import starsalign as stal
    >>> diff_image = stal.ultra_diff(ref_image, science_image)
    """
    aligned_image = ultra_align(ref_image, science_image)
    diff_image = ref_image - aligned_image
    return diff_image

# https://github.com/nagonzalezf/starsalign