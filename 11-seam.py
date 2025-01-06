import cv2
import numpy

# this exercise references "Seam Carving for Content-Aware Image Resizing" by Avidan and Shamir

npyInput = cv2.imread(filename='./samples/seam.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# implement content-aware image resizing to reduce the width of the image by one-hundred pixels

# using a heuristic energy function to extract an energy map

npyEnergy = cv2.Sobel(src=cv2.cvtColor(src=npyInput, code=cv2.COLOR_BGR2GRAY), ddepth=-1, dx=1, dy=0, ksize=3, scale=1, delta=0.0, borderType=cv2.BORDER_DEFAULT).__abs__() \
			+ cv2.Sobel(src=cv2.cvtColor(src=npyInput, code=cv2.COLOR_BGR2GRAY), ddepth=-1, dx=0, dy=1, ksize=3, scale=1, delta=0.0, borderType=cv2.BORDER_DEFAULT).__abs__()

# find and remove one-hundred vertical seams, can potentially be slow

for intRemove in range(100):
	intSeam = []

	# construct the cumulative energy map using the dynamic programming approach
	# initialize the cumulative energy map by making a copy of the energy map
	# when iterating over the rows, ignore M(y-1, ...) that are out of bounds

	# several seams can have the same energy, use the following for consistency
	# start at the leftmost M(height-1, x) with the lowest cumulative energy
	# should M(y-1, x) be equal to M(y-1, x-1) or M(y-1, x+1) then use (y-1, x)
	# similarly should M(y-1, x-1) be equal to M(y-1, x+1) then use (y-1, x-1)

	# the intSeam array should be a list of integers representing the seam
	# a seam from the top left to the bottom right: intSeam = [0, 1, 2, 3, 4, ...]
	# a seam that is just the first column: intSeam = [0, 0, 0, 0, 0, 0 , ...]









	# some sanity checks, such that the length of the seam is equal to the height of the image
	# furthermore iterating over the seam and making sure that it is a connected sequence

	assert(len(intSeam) == npyInput.shape[0])

	for intY in range(1, len(intSeam)):
		assert(intSeam[intY] - intSeam[intY - 1] in [ -1, 0, 1 ])
	# end

	# change the following condition to true if you want to visualize the seams that are being removed
	# note that this will not work if you are connected to the linux lab via ssh but no x forwarding

	if False:
		npyM /= npyM.max()

		for intY in range(len(intSeam)):
			npyInput[intY, intSeam[intY], :] = numpy.array([ 0.0, 0.0, 1.0 ], numpy.float32)
			npyM[intY, intSeam[intY]] = numpy.array([ 1.0 ], numpy.float32)
		# end

		cv2.imshow(winname='npyInput', mat=npyInput)
		cv2.imshow(winname='npyM', mat=npyM)
		cv2.waitKey(delay=10)
	# end

	# removing the identified seam by iterating over each row and shifting them accordingly
	# after the shifting in each row, the image and the energy map are cropped by one pixel on the right

	for intY in range(len(intSeam)):
		npyInput[intY, intSeam[intY]:-1, :] = npyInput[intY, (intSeam[intY] + 1 ):, :]
		npyEnergy[intY, intSeam[intY]:-1] = npyEnergy[intY, (intSeam[intY] + 1):]
	# end

	npyInput = npyInput[:, :-1, :]
	npyEnergy = npyEnergy[:, :-1]
# end

cv2.imwrite(filename='./11-seam.png', img=(npyInput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))