import numpy
import cv2

numpyInputs = [
	cv2.imread(filename='./../samples/fusion-1.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0,
	cv2.imread(filename='./../samples/fusion-2.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0,
	cv2.imread(filename='./../samples/fusion-3.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
]

dblC, dblS, dblE = 1.0, 1.0, 1.0 # weighting exponents that are used to adjust the influence of each quality measure

numpyWeights = []

for numpyInput in numpyInputs:
	numpyGray = cv2.cvtColor(src=numpyInput, code=cv2.COLOR_RGB2GRAY)

	numpyC = ... # contrast of numpyGray
	numpyS = ... # saturation of numpyInput
	numpyE = ... # well-exposedness of numpyInput

	numpyWeight = numpy.power(numpyC, dblC) + numpy.power(numpyS, dblS) + numpy.power(numpyE, dblE) # weight based on the quality measures

	numpyWeights.append(numpyWeight)
# end

# normalize numpyWeights as described by the first formula in section 3.2 of "Exposure Fusion" by Tom Mertens, Jan Kautz and Frank Van Reeth

def pyramidGaussian(numpyInput):
	return ... # a gaussian pyramid of numpyInput with 7 levels
# end

def pyramidLaplacian(numpyInput):
	return ... # a laplacian pyramid of numpyInput with 7 levels
# end

numpyPyramidInput = [ pyramidLaplacian(numpyInput) for numpyInput in numpyInputs ] # create a gaussian pyramid for each weight
numpyPyramidWeights = [ pyramidGaussian(numpyWeight) for numpyWeight in numpyWeights ] # create a laplacian pyramid for each input image

numpyPyramid = []

# implement the multiband blending technique described in the second half of section 3.2 in "Exposure Fusion" by Tom Mertens, Jan Kautz and Frank Van Reeth

# reconstruct the image represented by the pyramid interatively from the bottom up - use the following line as a starting point / hint

numpyOutput = cv2.pyrUp(numpyPyramid[-1]) + numpyPyramid[-2]

cv2.imwrite(filename='./3-mertens.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))