import cv2
import numpy

# this exercise references "Exposure Fusion" by Mertens et al.

npyInputs = [
	cv2.imread(filename='./samples/fusion-1.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0,
	cv2.imread(filename='./samples/fusion-2.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0,
	cv2.imread(filename='./samples/fusion-3.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
]

# use the quality measures to extract a weight map for each image according to section 3.1
# set the weighting exponents to one, thus equaling the contrition of contrast, saturation, and exposedness
# make sure to add 0.0000001 to the weight map of each image to avoid divisions by zero in the subsequent step
# normalize the weight maps such that they sum up to one at each pixel as described in section 3.2
# store the three weight maps in the npyWeights array which will be used below to perform the blending

npyWeights = []









# creating the laplacian and gaussian pyramids to perform multiband blending
# defining separate functions for this steps makes the code easier to read

def gaussian_pyramid(npyInput, intLevels):
	npyPyramid = [ npyInput ]

	for intLevel in range(intLevels):
		npyPyramid.append(cv2.pyrDown(npyPyramid[-1]))
	# end

	return npyPyramid
# end

def laplacian_pyramid(npyInput, intLevels):
	npyPyramid = [ npyInput ]

	for intLevel in range(intLevels):
		npyPyramid.append(cv2.pyrDown(npyPyramid[-1]))

		npyPyramid[-2] -= cv2.pyrUp(npyPyramid[-1])
	# end

	return npyPyramid
# end

npyInputs = [ laplacian_pyramid(npyInput, 6) for npyInput in npyInputs ]
npyWeights = [ gaussian_pyramid(npyWeight, 6) for npyWeight in npyWeights ]

# constructing a laplacian pyramid by using the weights from the gaussian pyramid
# eventually obtaining the fused result by recovering the output from the merged pyramid

npyPyramid = []

for intLevel in range(len(npyInputs[0])):
	npyPyramid.append(sum([ npyInputs[intInput][intLevel] * npyWeights[intInput][intLevel][:, :, None] for intInput in range(len(npyInputs)) ]))
# end

npyOutput = npyPyramid.pop(-1)

while len(npyPyramid) > 0:
	npyOutput = cv2.pyrUp(npyOutput) + npyPyramid.pop(-1)
# end

cv2.imwrite(filename='./13-fusion-1.png', img=(npyWeights[0][0] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./13-fusion-2.png', img=(npyWeights[1][0] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./13-fusion-3.png', img=(npyWeights[2][0] * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./13-fusion-4.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))