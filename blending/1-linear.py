import numpy
import cv2

numpyFirst = cv2.imread(filename='./../samples/blend-1.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
numpySecond = cv2.imread(filename='./../samples/blend-2.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyNarrow = numpy.zeros(numpyFirst.shape, numpy.float32) # empty image for blending the images using the narrow eight function
numpyWide = numpy.zeros(numpyFirst.shape, numpy.float32) # empty image for blending the images using the wide weight function

# for numpyNarrow, blend numpyFirst and numpySecond using the weight function 1.0 / (1.0 + pow(x / 0.5, 20.0)) for numpyFirst where x in [0.0, 1.0]
# for numpyWide, blend numpyFirst and numpySecond using the weight function 1.0 / (1.0 + pow(x / 0.5, 5.0)) for numpyFirst where x in [0.0, 1.0]

cv2.imwrite(filename='./1-linear-1.png', img=(numpyNarrow * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./1-linear-2.png', img=(numpyWide * 255.0).clip(0.0, 255.0).astype(numpy.uint8))