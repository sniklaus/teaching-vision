import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/noise.png', flags=cv2.IMREAD_COLOR)

numpyFirst = cv2.GaussianBlur(...) # blur numpyImage using a gaussian filter with a kernel size of 3 x 3 pixels
numpySecond = cv2.medianBlur(...) # blur numpyImage using a median filter with an aperture size of 3 pixels

cv2.imwrite(filename='./3-median-1.png', img=numpyFirst)
cv2.imwrite(filename='./3-median-2.png', img=numpySecond)