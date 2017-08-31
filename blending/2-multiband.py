import numpy
import cv2

numpyFirst = cv2.imread(filename='./../samples/multiband-apple.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
numpySecond = cv2.imread(filename='./../samples/multiband-orange.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyFirst = [ numpyFirst ]
numpySecond = [ numpySecond ]

# construct a laplacian pyramid with 7 levels for each input image - consult the exercises in the multiresolution exercises for more information

numpyPyramid = []

# combine the two pyramids to a single one - at each level, use the left half that belongs to the first image and the right half that belongs to the second image

# reconstruct the image represented by the pyramid interatively from the bottom up - use the following line as a starting point / hint

numpyOutput = cv2.pyrUp(numpyPyramid[-1]) + numpyPyramid[-2]

cv2.imwrite(filename='./2-multiband.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))