import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/fusion-1.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyGray = cv2.cvtColor(src=numpyInput, code=cv2.COLOR_RGB2GRAY)

# implement the quality measures described in "Exposure Fusion" by Tom Mertens, Jan Kautz and Frank Van Reeth

numpyC = ... # contrast of numpyGray - have a look at cv2.Laplacian(...)
numpyS = ... # saturation of numpyInput - have a look at numpy.std(...)
numpyE = ... # well-exposedness of numpyInput - have a look at numpy.prod(...) / numpy.exp(...) / numpy.power(...)

cv2.imwrite(filename='./1-measure-1.png', img=(numpyC * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./1-measure-2.png', img=(numpyS * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./1-measure-3.png', img=(numpyE * 255.0).clip(0.0, 255.0).astype(numpy.uint8))