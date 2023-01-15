"""
This example shows how to use the STARSALIGN package to align two single channel astronomical images.

It loads two images 'ref_image.npy' and 'science_image.npy', then it uses the function 'diff_images' from
the STARSALIGN package to align the images and get the difference image.

Finally, it saves all the images in png format using opencv.

https://github.com/nagonzalezf/starsalign/
"""
import numpy as np
import cv2 as cv
import starsalign as stal

ref_image = np.load('ref_image.npy')
science_image = np.load('science_image.npy')

diff_image = stal.diff(ref_image, science_image)

cv.imwrite('ref_image.png', ref_image)
cv.imwrite('science_image.png', science_image)
cv.imwrite('diff_image.png', diff_image)
