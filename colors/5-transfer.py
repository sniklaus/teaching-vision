import numpy
import cv2

numpyFrom = cv2.imread(filename='./../samples/transfer-from.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
numpyTo = cv2.imread(filename='./../samples/transfer-to.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# implement the algorithm described in "Color Transfer between Images" by Erik Reinhard, Michael Ashikhmin, Bruce Gooch, and Peter Shirley

# use cv2.cvtColor() to convert the input images into the Lab color space, you do not need to perform this step manually as described in the paper

# calculate the mean color of each channel in numpyTo and subtract it from numpyTo (equation 10)
# transfer the standard deviation of each channel from numpyFrom to numpyTo (equation 11)
# calculate the mean color of each channel in numpyFrom and add it to numpyTo

numpyTo[:, :, 0] = numpyTo[:, :, 0].clip(0.0, 100.0) # making sure that the values are still in the valid range
numpyTo[:, :, 1] = numpyTo[:, :, 1].clip(-127.0, 127.0) # making sure that the values are still in the valid range
numpyTo[:, :, 2] = numpyTo[:, :, 2].clip(-127.0, 127.0) # making sure that the values are still in the valid range

numpyOutput = cv2.cvtColor(src=numpyTo, code=cv2.COLOR_Lab2BGR)

cv2.imwrite(filename='./5-transfer.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))