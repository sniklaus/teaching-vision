import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/prokudin.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

intFirst, intSecond = int(1.0 * numpyInput.shape[0] / 3.0), int(2.0 * numpyInput.shape[0] / 3.0)

numpyFirst = numpyInput[:intFirst, :][50:-50, 50:-50, 1] # crop of the blue channel
numpySecond = numpyInput[intFirst:intSecond, :][50:-50, 50:-50, 1] # crop of the green channel
numpyThird = numpyInput[intSecond:, :][50:-50, 50:-50, 1] # crop of the red channel

numpyWarpSecond = cv2.findTransformECC(...)[1] # estimate the homography matrix of numpySecond using numpyFirst as the template - use numpy.eye(3, 3, 0, numpy.float32) as initial homography matrix and stop after 10 iterations
numpyWarpThird = cv2.findTransformECC(...)[1] # estimate the homography matrix of numpyThird using numpyFirst as the template - use numpy.eye(3, 3, 0, numpy.float32) as initial homography matrix and stop after 10 iterations

numpySecond = cv2.warpPerspective(...) # warp numpySecond into the coordinate system of numpyFirst - use the linear interpolation method and the inverse transform
numpyThird = cv2.warpPerspective(...) # warp numpyThird into the coordinate system of numpyFirst - use the linear interpolation method and the inverse transform

numpyOutput = numpy.stack([numpyFirst, numpySecond, numpyThird], 2) # stack the individual channels to compose the output image

cv2.imwrite(filename='./3-colorize.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))