import torch
print(torch.__version__)

import torchvision
print(torchvision.__version__)

import numpy
import scipy.linalg
import scipy.spatial

# use principal component analysis for classification as discussed in class

# creating a data loader for the training samples of the mnist dataset
# specifying the batch size as well as the normalization transform
# notice that the batch size is huge, we misuse torchvision a little bit

objectTrain = torch.utils.data.DataLoader(
	batch_size=60000,
	shuffle=False,
	num_workers=1,
	pin_memory=False,
	dataset=torchvision.datasets.MNIST(
		root='./mnist/',
		train=True,
		download=True,
		transform=torchvision.transforms.Compose([
			torchvision.transforms.ToTensor(),
			torchvision.transforms.Normalize(tuple([ 0.1307 ]), tuple([ 0.3081 ]))
		])
	)
)

# creating a data loader for the validation samples of the mnist dataset

objectValidation = torch.utils.data.DataLoader(
	batch_size=100,
	shuffle=False,
	num_workers=1,
	pin_memory=False,
	dataset=torchvision.datasets.MNIST(
		root='./mnist/',
		train=False,
		download=True,
		transform=torchvision.transforms.Compose([
			torchvision.transforms.ToTensor(),
			torchvision.transforms.Normalize(tuple([ 0.1307 ]), tuple([ 0.3081 ]))
		])
	)
)

# obtaining the mnist data using the data loader and reshaping it
# principal component analysis expects one-dimensional features

tensorInputTrain, tensorTargetTrain = next(iter(objectTrain))
tensorInputValidation, tensorTargetValidation = next(iter(objectValidation))

numpyInputTrain = tensorInputTrain.view(-1, 784).numpy()
numpyInputValidation = tensorInputValidation.view(-1, 784).numpy()

# calculating the covariance matrix of the zero-mean data points
# calculating the eigenvectors and the corresponding eigenvalues
# sorting the eigenvectors according to their eigenvalues in descending order

numpyCov = numpy.cov(numpyInputTrain - numpyInputTrain.mean(0), None, False, False)
numpyEvals, numpyEvecs = scipy.linalg.eigh(numpyCov)
numpyDescending = numpy.argsort(numpyEvals)[::-1]
numpyEvecs = numpyEvecs[:, numpyDescending]

# evaluating the effect of the number of utilized principal components

for intK in [ 7, 14, 28 ]:
	# transforming the training data points into intK dimensions

	numpyOutputTrain = numpy.dot(numpyInputTrain, numpyEvecs[:, :intK])

	# storing the transformed data points in a k-d tree for efficiency

	objectDatabase = scipy.spatial.KDTree(numpyOutputTrain)

	# transform the validation data points into intK dimensions
	# find the nearest neighbor for each sample in the validation set
	# use the k-d tree for this search, it will speed it up a bit
	# classify the sample based on the class of the nearest neighbor
	# count the correct classifications to determine the accuracy

	dblAccuracy = 0.0









	# printing the number of used features as well as the accuracy
	# the solution does print "7: 0.84", "14: 0.96", and "28: 0.99"

	print(str(intK) + ': ' + str(dblAccuracy))
# end