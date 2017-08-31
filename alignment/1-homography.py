import numpy
import cv2

numpyFirst = cv2.imread(filename='./../samples/homography-1.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
numpySecond = cv2.imread(filename='./../samples/homography-2.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyWarp = cv2.findHomography(...)[0] # find the homography matrix from the following source points to the destination points - use the default method and not ransac

# source points: numpy.array([[266, 343], [646, 229], [388, 544], [777, 538]], numpy.float32)
# destination points: numpy.array([[302, 222], [746, 231], [296, 490], [754, 485]], numpy.float32)

numpyOutput = cv2.warpPerspective(...) # warp numpySecond based on the estimated homography matrix - use the linear interpolation method

cv2.imwrite(filename='./1-homography.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))