import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/lenna.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyPyramid = [ ... ] # create a laplacian pyramid of numpyInput with 4 levels

for intLevel in range(len(numpyPyramid)):
	if intLevel == len(numpyPyramid) - 1:
		cv2.imwrite(filename='./2-laplacian-' + str(intLevel) + '.png', img=(numpyPyramid[intLevel] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))

	elif intLevel != len(numpyPyramid) - 1:
		cv2.imwrite(filename='./2-laplacian-' + str(intLevel) + '.png', img=cv2.applyColorMap(src=((numpyPyramid[intLevel] + 0.5) * 255.0).clip(0.0, 255.0).astype(numpy.uint8), colormap=cv2.COLORMAP_COOL))

	# end
# end