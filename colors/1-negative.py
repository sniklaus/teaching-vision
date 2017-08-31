import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/fruits.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyOutput = 1.0 - numpyInput # it is common practice in computer vision  to scale / normalize images into a range of [0.0, 1.0] and most exercises will do so

cv2.imwrite(filename='./1-negative.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))