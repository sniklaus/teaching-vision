import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/fruits.png', flags=cv2.IMREAD_COLOR)

numpyGray = cv2.cvtColor(...) # convert numpyImage to gray scale
numpyRgb = cv2.cvtColor(...) # convert numpyImage to the RGB color space
numpyXyz = cv2.cvtColor(...) # convert numpyImage to the XYZ color space
numpyHsv = cv2.cvtColor(...) # convert numpyImage to the HSV color space
numpyHls = cv2.cvtColor(...) # convert numpyImage to the HLS color space
numpyLab = cv2.cvtColor(...) # convert numpyImage to the Lab color space

cv2.imwrite(filename='./2-convert-gray.png', img=numpyGray)
cv2.imwrite(filename='./2-convert-rgb.png', img=numpyRgb)
cv2.imwrite(filename='./2-convert-xyz.png', img=numpyXyz)
cv2.imwrite(filename='./2-convert-hsv.png', img=numpyHsv)
cv2.imwrite(filename='./2-convert-hls.png', img=numpyHls)
cv2.imwrite(filename='./2-convert-lab.png', img=numpyLab)