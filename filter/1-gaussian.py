import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/fruits.png', flags=cv2.IMREAD_COLOR)

numpyGaussian05 = cv2.GaussianBlur(...) # blur numpyImage using a gaussian filter with a kernel size of 5 x 5 pixels
numpyGaussian15 = cv2.GaussianBlur(...) # blur numpyImage using a gaussian filter with a kernel size of 15 x 15 pixels
numpyGaussian25 = cv2.GaussianBlur(...) # blur numpyImage using a gaussian filter with a kernel size of 25 x 25 pixels
numpyGaussian35 = cv2.GaussianBlur(...) # blur numpyImage using a gaussian filter with a kernel size of 35 x 35 pixels

cv2.imwrite(filename='./1-gaussian-05.png', img=numpyGaussian05)
cv2.imwrite(filename='./1-gaussian-15.png', img=numpyGaussian15)
cv2.imwrite(filename='./1-gaussian-25.png', img=numpyGaussian25)
cv2.imwrite(filename='./1-gaussian-35.png', img=numpyGaussian35)