import numpy
import cv2

# this exercise references "The Laplacian Pyramid as a Compact Image Code" by Burt and Adelson

numpyInput = cv2.imread(filename='./samples/lenna.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# create a laplacian pyramid with four levels as described in the slides as well as in the referenced paper





# the following iterates over the levels in numpyPyramid and saves them as an image accordingly
# level four is just a small-scale representation of the original input image anc can be safed as usual
# the value range for the other levels are outside of [0, 1] and a color mapping is applied before saving them

for intLevel in range(len(numpyPyramid)):
	if intLevel == len(numpyPyramid) - 1:
		cv2.imwrite(filename='./07-pyramid-' + str(intLevel + 1) + '.png', img=(numpyPyramid[intLevel] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))

	elif intLevel != len(numpyPyramid) - 1:
		cv2.imwrite(filename='./07-pyramid-' + str(intLevel + 1) + '.png', img=cv2.applyColorMap(src=((numpyPyramid[intLevel] + 0.5) * 255.0).clip(0.0, 255.0).astype(numpy.uint8), colormap=cv2.COLORMAP_COOL))

	# end
# end