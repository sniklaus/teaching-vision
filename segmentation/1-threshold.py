import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/text.png', flags=cv2.IMREAD_COLOR)

numpyInput = cv2.cvtColor(src=numpyInput, code=cv2.COLOR_BGR2Lab)[:, :, 0] # transform the image into a perceptually uniform color space and use the lightness channel

numpyInput = cv2.GaussianBlur(src=numpyInput, ksize=(7, 7), sigmaX=0.0, sigmaY=0.0, borderType=cv2.BORDER_DEFAULT) # apply a small gaussian blur to make the segmentation less sensitive / noisy

numpyFirst = cv2.threshold(...)[1] # perform a binary threshold of numpyInput using 127 as the threshold
numpySecond = cv2.adaptiveThreshold(...) # perform an adaptive threshold of numpyInput using the mean minus 2 within blocks of size 9 pixels
numpyThird = cv2.adaptiveThreshold(...) # perform an adaptive threshold of numpyInput using the gaussian cross-correlation minus 2 within blocks of size 9 pixels

cv2.imwrite(filename='./1-threshold-1.png', img=numpyFirst)
cv2.imwrite(filename='./1-threshold-2.png', img=numpySecond)
cv2.imwrite(filename='./1-threshold-3.png', img=numpyThird)