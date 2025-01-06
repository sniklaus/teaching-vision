import cv2
import numpy

# this exercise references "Pyramid Methods in Image Processing" by Adelson et al.

npyFirst = cv2.imread(filename='./samples/multiband-apple.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
npySecond = cv2.imread(filename='./samples/multiband-orange.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# blend the apple and the orange using multiband blending with laplacian pyramids

# creating a laplacian pyramid with seven levels for each of the two images

npyFirst = [ npyFirst ]
npySecond = [ npySecond ]

for intLevel in range(6):
	npyFirst.append(cv2.pyrDown(npyFirst[-1]))
	npySecond.append(cv2.pyrDown(npySecond[-1]))

	npyFirst[-2] -= cv2.pyrUp(npyFirst[-1])
	npySecond[-2] -= cv2.pyrUp(npySecond[-1])
# end

# combine the two laplacian pyramids and create a new laplacian pyramid to blend the two images
# specifically, take the left half from npyFirst and the right half from npySecond at each level
# afterwards, collapse npyPyramid to obtain the blended result and store it in npyOutput

npyPyramid = []









cv2.imwrite(filename='./10-multiband.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))