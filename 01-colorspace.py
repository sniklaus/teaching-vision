import numpy
import cv2

# this exercise references "Color Transfer between Images" by Reinhard et al.

numpyInput = cv2.imread(filename='./samples/fruits.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# convert numpyInput to the LMS color space and store it in numpyOutput according to equation 4

# the two ways i see for doing this (there are others as well though) are as follows
# either iterate over each pixel, performing the matrix-vector multiplication one by one and storing the result in a pre-allocated numpyOutput
# or split numpyInput into its three channels, linearly combining them to obtain the three converted color channels, before using numpy.stack to merge them

# keep in mind that that opencv arranges the color channels typically in the order of blue, green, red





cv2.imwrite(filename='./01-colorspace.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))