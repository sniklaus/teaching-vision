import numpy
import cv2

numpyInput = cv2.imread(filename='./../samples/fruits.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyFirst = cv2.filter2D(...) # perform a convolution between numpyInput and the following kernel

# [ 0.0, -1.0,  0.0]
# [-1.0,  5.0, -1.0]
# [ 0.0, -1.0,  0.0]

numpySecond = cv2.filter2D(...) # perform a convolution between numpyInput and the following kernel

# [ 0.0, -1.0,  0.0]
# [-1.0,  4.0, -1.0]
# [ 0.0, -1.0,  0.0]

numpyThird = cv2.filter2D(...) # perform a convolution between numpyFirst and the following kernel

# [ 0.0, -1.0,  0.0]
# [-1.0,  4.0, -1.0]
# [ 0.0, -1.0,  0.0]

cv2.imwrite(filename='./2-custom-1.png', img=(numpyFirst * 255.0).clip(0.0, 255.0).astype(numpy.uint8))
cv2.imwrite(filename='./2-custom-2.png', img=cv2.applyColorMap(src=((numpySecond + 0.5) * 255.0).clip(0.0, 255.0).astype(numpy.uint8), colormap=cv2.COLORMAP_COOL))
cv2.imwrite(filename='./2-custom-3.png', img=cv2.applyColorMap(src=((numpyThird + 0.5) * 255.0).clip(0.0, 255.0).astype(numpy.uint8), colormap=cv2.COLORMAP_COOL))