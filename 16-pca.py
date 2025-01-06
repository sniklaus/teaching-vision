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

objTrain = torch.utils.data.DataLoader(
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

objValidation = torch.utils.data.DataLoader(
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

tenInputTrain, tenTargetTrain = next(iter(objTrain))
tenInputValidation, tenTargetValidation = next(iter(objValidation))

npyInputTrain = tenInputTrain.view(-1, 784).numpy(force=True)
npyInputValidation = tenInputValidation.view(-1, 784).numpy(force=True)

# calculating the covariance matrix of the zero-mean data points
# calculating the eigenvectors and the corresponding eigenvalues
# sorting the eigenvectors according to their eigenvalues in descending order

npyCov = numpy.cov(npyInputTrain - npyInputTrain.mean(0), None, False, False)
npyEvals, npyEvecs = scipy.linalg.eigh(npyCov)
npyDescending = numpy.argsort(npyEvals)[::-1]
npyEvecs = npyEvecs[:, npyDescending]

# evaluating the effect of the number of utilized principal components

for intK in [ 7, 14, 28 ]:
	# transforming the training data points into intK dimensions

	npyOutputTrain = numpy.dot(npyInputTrain, npyEvecs[:, :intK])

	# storing the transformed data points in a k-d tree for efficiency

	objDatabase = scipy.spatial.KDTree(npyOutputTrain)

	# transform the validation data points into intK dimensions
	# find the nearest neighbor for each sample in the validation set
	# use the k-d tree for this search, it will speed it up a bit
	# classify the sample based on the class of the nearest neighbor
	# count the correct classifications to determine the accuracy

	fltAccuracy = 0.0









	# printing the number of used features as well as the accuracy
	# the solution does print "7: 0.84", "14: 0.96", and "28: 0.99"

	print(str(intK) + ': ' + str(fltAccuracy))
# end