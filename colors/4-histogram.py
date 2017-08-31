import numpy
import cv2
import matplotlib.pyplot

numpyInput = cv2.imread(filename='./../samples/lenna.png', flags=cv2.IMREAD_COLOR)

numpyHistograms = []

for intChannel in range(3):
	numpyHistograms.append(cv2.calcHist(...)) # for each color channel in numpyInput, calculate the histogram with 256 bins and a range of [0, 256]
# end

matplotlib.pyplot.figure()
matplotlib.pyplot.xlabel('bins')
matplotlib.pyplot.ylabel('pixels')
for intChannel in range(3):
	matplotlib.pyplot.plot(numpyHistograms[intChannel], color=['b', 'g', 'r'][intChannel])
# end
matplotlib.pyplot.savefig('./4-histogram.png')	