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

numpyOutput = numpy.zeros(numpyInputs[0].shape, numpy.float32)

for intInput in range(len(numpyInputs)):
	numpyOutput += numpyInputs[intInput] * numpyWeights[intInput][:, :, None] # sum the weighted input images to compose the output
# end

cv2.imwrite(filename='./2-blend.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))