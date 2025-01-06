import cv2
import numpy

# this exercise references "Interactions Between Color Plane Interpolation and Other Image Processing Functions in Electronic Photography" by Adams

npyInput = cv2.imread(filename='./samples/demosaicing.png', flags=cv2.IMREAD_GRAYSCALE).astype(numpy.float32) / 255.0

# demosaic npyInput by using convolutions to mimic bilinear interpolation as shown in the slides and described in section 3.3

# the input has the following beyer pattern, id est that the top left corner is red

# RGRGRG ....
# GBGBGB ....
# RGRGRG ....
# GBGBGB ....
# ...........
# ...........

# to do this using convolutions, the first step is to separate the colors from npyInput into four channels such that npyOutput[:, :, 1] for example becomes

# 0G0G0G ....
# G0G0G0 ....
# 0G0G0G ....
# G0G0G0 ....
# ...........
# ...........

# since this can be tricky and you might not be perfectly familiar with indexing and splicing matrices yet, this is already done for you below

npyOutput = numpy.zeros([ npyInput.shape[0], npyInput.shape[1], 3 ], numpy.float32)

npyOutput[1::2, 1::2, 0] = npyInput[1::2, 1::2]
npyOutput[0::2, 1::2, 1] = npyInput[0::2, 1::2]
npyOutput[1::2, 0::2, 1] = npyInput[1::2, 0::2]
npyOutput[0::2, 0::2, 2] = npyInput[0::2, 0::2]

# for each channel in npyOutput, use a suitable convolution to perform the demosaicing and store the output back in its respective channel in npyOutput
# we already discussed in class what the appropriate kernel for the green channel is, determining the kernel for the other two channels is up to you
# to be able to convolve a channel from npyOutput and storing the result back in the same channel, the convolution must not affect the resolution
# we need padding for the convolution to not affect the resolution, this is already built into OpenCV but make sure to use cv2.BORDER_DEFAULT as the border type









cv2.imwrite(filename='./04-convolution.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))