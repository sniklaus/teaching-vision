import numpy
import cv2
import math

numpyInput = cv2.imread(filename='./samples/homography-2.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# estimate the homography matrix between matching points and warp the image using bilinear interpolation

# creating the mapping between the four corresponding points

intSrc = [ [266, 343], [646, 229], [388, 544], [777, 538] ]
intDst = [ [302, 222], [746, 231], [296, 490], [754, 485] ]

# construct the linear homogeneous system of equations
# use a singular value decomposition to solve the system
# in practice, cv2.findHomography can be used for this
# however, do not use this function for this exercise









# use a backward warping algorithm to warp the source
# to do so, we first create the inverse transform
# use bilinear interpolation for resampling
# in practice, cv2.warpPerspective can be used for this
# however, do not use this function for this exercise

numpyHomography = numpy.linalg.inv(numpyHomography)

numpyOutput = numpy.zeros(numpyInput.shape, numpy.float32)









cv2.imwrite(filename='./08-homography.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))