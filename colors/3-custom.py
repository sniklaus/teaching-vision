import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/fruits.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyOutput = ... # convert numpyInput to the color space defined by the following transform

# [ L ]   [ 0.3811 0.5783 0.0402 ]   [ R ]
# [ M ] = [ 0.1967 0.7244 0.0782 ] * [ G ]
# [ S ]   [ 0.0241 0.1288 0.8444 ]   [ B ]

cv2.imwrite(filename='./3-custom.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))