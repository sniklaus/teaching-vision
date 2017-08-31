import numpy
import cv2

numpy.random.seed(0) # the random centers of kmeans make it difficult to automatically grade this exercise, a manual seed should make it deterministic though

numpyInput = cv2.imread(filename='./../samples/fruits.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

# this exercise performs segmentation using kmeans cluserting in a feature space in which each pixel is represented by a 5 dimensional vector that represents its color and location

numpyFeaturespace = numpy.zeros([numpyInput.shape[0], numpyInput.shape[1], 5], numpy.float32) # our feature space in which we perform the clustering

numpyFeaturespace[:, :, 0:3] = ... # numpyInput converted to the Lab color space and multiplied by 3 to scale it, making the color more important in the clustering
numpyFeaturespace[:, :, 3] = ... # the y coordinate of each pixel, starting from 1 and not 0 as usually typical for computer scientists - have a look at numpy.linspace(...)
numpyFeaturespace[:, :, 4] = ... # the x coordinate of each pixel, starting from 1 and not 0 as usually typical for computer scientists - have a look at numpy.linspace(...)

_, numpyLabels, numpyCenters = cv2.kmeans(data=numpyFeaturespace.reshape([-1, 5]), K=30, bestLabels=None, criteria=(cv2.TERM_CRITERIA_MAX_ITER, 10, 0.0), attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS)

numpyOutput = numpyCenters[numpyLabels.flatten()][:, 0:3].reshape(numpyInput.shape) # for each pixel, lookup to which of the 30 clusters it belongs and assign it the color of the cluster center

numpyOutput = cv2.cvtColor(src=numpyOutput / 3.0, code=cv2.COLOR_Lab2BGR) # divide the output by 3 to rescale it again and convert it to the regular bgr color space

cv2.imwrite(filename='./2-clustering.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))