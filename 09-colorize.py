import cv2
import numpy

npyInput = cv2.imread(filename='./samples/prokudin.png', flags=cv2.IMREAD_GRAYSCALE).astype(numpy.float32) / 255.0

# align the individual images such that their combination results in a proper color image

# splitting the input into the three individual channels while slightly cropping the boundary

intFirst, intSecond = int(1.0 * npyInput.shape[0] / 3.0), int(2.0 * npyInput.shape[0] / 3.0)

npyB = npyInput[:intFirst, :][50:-50, 50:-50]
npyG = npyInput[intFirst:intSecond, :][50:-50, 50:-50]
npyR = npyInput[intSecond:, :][50:-50, 50:-50]

# find the homography matrices between the images using cv2.findTransformECC
# based on these matrices, warp npyG and npyR towards npyB using cv2.warpPerspective
# make sure to use inverse warping as stated in the documentation of cv2.findTransformECC
# once the channels are aligned, they can simply be stacked to create the color image









npyOutput = numpy.stack([ npyB, npyG, npyR ], 2)

cv2.imwrite(filename='./09-colorize.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))