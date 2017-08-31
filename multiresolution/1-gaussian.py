import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/lenna.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyPyramid = [ ... ] # create a gaussian pyramid of numpyInput with 4 levels

for intLevel in range(len(numpyPyramid)):
	cv2.imwrite(filename='./1-gaussian-' + str(intLevel) + '.png', img=(numpyPyramid[intLevel] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
# end