__version__ = "1.0.0"

import cv2 as cv
import numpy as np

def align_images(ref_image, science_image):
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

def diff_images(ref_image, science_image):
    aligned_image = align_images(ref_image, science_image)
    diff_image = ref_image - aligned_image
    return diff_image