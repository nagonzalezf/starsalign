"""
This example shows how to use the STARSALIGN package to align two single channel astronomical images.

It loads two images 'ref_image.npy' and 'science_image.npy', then it uses the functions 'fast_align()'
and 'fast_diff()' from the STARSALIGN package to get the aligned and difference images.

Finally, it saves all the images in .png format using opencv.

https://github.com/nagonzalezf/starsalign/
"""
# Imports
import os
import cv2 as cv
import numpy as np
import starsalign as sa

# Load images
ref_image = np.load('ref_image.npy')
science_image = np.load('science_image.npy')

# Get the raw difference image
raw_diff_image = ref_image - science_image

# Use the starsalign align() function to get the aligned image
aligned_image = sa.fast_align(ref_image, science_image)

# Use the starsalign diff() function to get the difference image
diff_image = sa.fast_diff(ref_image, science_image)

# Create outputs folder
if not os.path.exists("example_1_outputs"):
    os.makedirs("example_1_outputs")

# Write stored variables as simple .png images to visualize in explorer
cv.imwrite('example_1_outputs/001_ref_image.png', ref_image)
cv.imwrite('example_1_outputs/002_science_image.png', science_image)
cv.imwrite('example_1_outputs/003_raw_diff_image.png', raw_diff_image)
cv.imwrite('example_1_outputs/004_aligned_image.png', aligned_image)
cv.imwrite('example_1_outputs/005_diff_image.png', diff_image)
