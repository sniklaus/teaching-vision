import cv2
import numpy

# this exercise references "Interactions Between Color Plane Interpolation and Other Image Processing Functions in Electronic Photography" by Adams

npyInput = cv2.imread(filename='./samples/demosaicing.png', flags=cv2.IMREAD_GRAYSCALE).astype(numpy.float32) / 255.0

# demosaic npyInput by using bilinear interpolation as shown in the slides and described in section 3.3

# the input has the following beyer pattern, id est that the top left corner is red

# RGRGRG ....
# GBGBGB ....
# RGRGRG ....
# GBGBGB ....
# ...........
# ...........

# the straightforward way that i see for doing this (there are others as well though) is to iterate over each pixel and resolving each of the four possible cases
# to simplify this, you can iterate from (1 to npyInput.shape[0] - 1) and (1 to npyInput.shape[1] - 1) to avoid corner cases, npyOutput is accordingly one pixel smaller on each side

npyOutput = numpy.zeros([ npyInput.shape[0] - 2, npyInput.shape[1] - 2, 3 ], numpy.float32)

# notice that to fill in the missing greens, you will always be able to take the average of four neighboring values
# however, depending on the case, you either get four or only two neighboring values for red and blue
# this is perfectly fine, in this case you can simply use the average of two values if only two neighbors are available









cv2.imwrite(filename='./03-demosaicing.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))