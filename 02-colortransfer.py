import numpy
import cv2

# this exercise references "Color Transfer between Images" by Reinhard et al.

numpyFrom = cv2.imread(filename='./samples/transfer-from.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
numpyTo = cv2.imread(filename='./samples/transfer-to.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# match the color statistics of numpyTo to those of numpyFrom

# in order for make matching the statistics more meaningful, the images are first converted to the LAB color space

numpyFrom = cv2.cvtColor(src=numpyFrom, code=cv2.COLOR_BGR2Lab)
numpyTo = cv2.cvtColor(src=numpyTo, code=cv2.COLOR_BGR2Lab)

# calculate the per-channel mean of the data points / intensities of numpyTo, and subtract these from numpyTo according to equation 10
# calculate the per-channel std of the data points / intensities of numpyTo and numpyFrom, and scale numpyTo according to equation 11
# calculate the per-channel mean of the data points / intensities of numpyFrom, and add these to numpyTo according to the description after equation 11





# after matching the statistics, some of the intensity values might be out of the valid range and are hence clipped / clamped

numpyTo[:, :, 0] = numpyTo[:, :, 0].clip(0.0, 100.0)
numpyTo[:, :, 1] = numpyTo[:, :, 1].clip(-127.0, 127.0)
numpyTo[:, :, 2] = numpyTo[:, :, 2].clip(-127.0, 127.0)

# finaly, the matched image is being converted back to the RGB color space

numpyOutput = cv2.cvtColor(src=numpyTo, code=cv2.COLOR_Lab2BGR)

cv2.imwrite(filename='./02-colortransfer.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))