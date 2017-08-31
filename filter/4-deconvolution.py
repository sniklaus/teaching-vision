import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/lenna.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyKernel = numpy.identity(15, numpy.float32) / 15.0 # identity matrix that represents our blur kernel

numpyKernel = numpy.roll(numpy.roll(numpy.pad(numpyKernel, [(0, numpyInput.shape[0] - 15), (0, numpyInput.shape[1] - 15)], 'constant'), -7, 0), -7, 1)

numpyB = numpy.abs(numpy.fft.ifft2(numpy.fft.fft2(numpyInput[:, :, 0]) * numpy.fft.fft2(numpyKernel))) # convolution in the frequency space
numpyG = numpy.abs(numpy.fft.ifft2(numpy.fft.fft2(numpyInput[:, :, 1]) * numpy.fft.fft2(numpyKernel))) # convolution in the frequency space
numpyR = numpy.abs(numpy.fft.ifft2(numpy.fft.fft2(numpyInput[:, :, 2]) * numpy.fft.fft2(numpyKernel))) # convolution in the frequency space

numpyBlurry = numpy.stack([numpyB, numpyG, numpyR], 2)

numpyB = ... # perform a deconvolution between the first color channel of numpyBlurry and numpyKernel in the frequency space
numpyG = ... # perform a deconvolution between the second color channel of numpyBlurry and numpyKernel in the frequency space
numpyR = ... # perform a deconvolution between the third color channel of numpyBlurry and numpyKernel in the frequency space

numpyOutput = numpy.stack([numpyB, numpyG, numpyR], 2)

cv2.imwrite(filename='./4-deconvolution-1.png', img=(numpyBlurry * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./4-deconvolution-2.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))