import cv2
import numpy

# this exercise references "The Laplacian Pyramid as a Compact Image Code" by Burt and Adelson

npyInput = cv2.imread(filename='./samples/lenna.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# create a laplacian pyramid with four levels as described in the slides as well as in the referenced paper

npyPyramid = []









# the following iterates over the levels in npyPyramid and saves them as an image accordingly
# level four is just a small-scale representation of the original input image and can be saved as usual
# the value range for the other levels are outside of [0, 1] and a color mapping is applied before saving them

for intLevel in range(len(npyPyramid)):
	if intLevel == len(npyPyramid) - 1:
		cv2.imwrite(filename='./07-pyramid-' + str(intLevel + 1) + '.png', img=(npyPyramid[intLevel] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))

	elif intLevel != len(npyPyramid) - 1:
		cv2.imwrite(filename='./07-pyramid-' + str(intLevel + 1) + '.png', img=cv2.applyColorMap(src=((npyPyramid[intLevel] + 0.5) * 255.0).clip(0.0, 255.0).astype(numpy.uint8), colormap=cv2.COLORMAP_COOL))

	# end
# end