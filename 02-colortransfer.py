import cv2
import numpy

# this exercise references "Color Transfer between Images" by Reinhard et al.

npyFrom = cv2.imread(filename='./samples/transfer-from.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
npyTo = cv2.imread(filename='./samples/transfer-to.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# match the color statistics of npyTo to those of npyFrom

# in order for make matching the statistics more meaningful, the images are first converted to the LAB color space

npyFrom = cv2.cvtColor(src=npyFrom, code=cv2.COLOR_BGR2Lab)
npyTo = cv2.cvtColor(src=npyTo, code=cv2.COLOR_BGR2Lab)

# not that the paper uses the notation target / source, here the notation is from / to
# calculate the per-channel mean of the data points / intensities of npyTo, and subtract these from npyTo according to equation 10
# calculate the per-channel std of the data points / intensities of npyTo and npyFrom, and scale npyTo according to equation 11
# calculate the per-channel mean of the data points / intensities of npyFrom, and add these to npyTo according to the description after equation 11









# after matching the statistics, some of the intensity values might be out of the valid range and are hence clipped / clamped

npyTo[:, :, 0] = npyTo[:, :, 0].clip(0.0, 100.0)
npyTo[:, :, 1] = npyTo[:, :, 1].clip(-127.0, 127.0)
npyTo[:, :, 2] = npyTo[:, :, 2].clip(-127.0, 127.0)

# finaly, the matched image is being converted back to the RGB color space

npyOutput = cv2.cvtColor(src=npyTo, code=cv2.COLOR_Lab2BGR)

cv2.imwrite(filename='./02-colortransfer.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))