import cv2
import numpy

npyInput = cv2.imread(filename='./samples/noise.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# use a gaussian kernel of size 3x3 to blur npyInput and store the result in npyFirst
# let OpenCV determine the appropriate sigma / deviation of the gaussian kernel for you

# use a median filter of size 3x3 to filter npyInput and store the result in npySecond









cv2.imwrite(filename='./05-median-1.png', img=(npyFirst * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./05-median-2.png', img=(npySecond * 255.0).clip(0.0, 255.0).astype(numpy.uint8))