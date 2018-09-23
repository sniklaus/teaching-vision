import torch
print(torch.__version__)

import torchvision
print(torchvision.__version__)

import numpy
import cv2
import matplotlib.pyplot
import tqdm

# implement a neural network according to the provided specification

dblTrain = []
dblValidation = []

# creating a data loader for the training samples of the fashion dataset
# specifying the batch size and making sure it runs in a background thread

objectTrain = torch.utils.data.DataLoader(
	batch_size=64,
	shuffle=True,
	num_workers=1,
	pin_memory=False,
	dataset=torchvision.datasets.FashionMNIST(
		root='./fashion/',
		train=True,
		download=True,
		transform=torchvision.transforms.Compose([
			torchvision.transforms.ToTensor()
		])
	)
)

# creating a data loader for the validation samples of the fashion dataset

objectValidation = torch.utils.data.DataLoader(
	batch_size=64,
	shuffle=True,
	num_workers=1,
	pin_memory=False,
	dataset=torchvision.datasets.FashionMNIST(
		root='./fashion/',
		train=False,
		download=True,
		transform=torchvision.transforms.Compose([
			torchvision.transforms.ToTensor()
		])
	)
)

# visualizing some samples and their labels from the validation set
# note that this will not work if you are connected to the linux lab

if False:
	objectFigure, objectAxis = matplotlib.pyplot.subplots(2, 4)

	for objectRow in objectAxis:
		for objectCol in objectRow:
			tensorInput, tensorTarget = next(iter(objectValidation))

			objectCol.grid(False)
			objectCol.set_title([ 't-shirt', 'trousers', 'pullover', 'dress', 'coat', 'sandals', 'shirt', 'sneaker', 'bag', 'ankle boot' ][ tensorTarget[0] ])
			objectCol.imshow(tensorInput[0, 0, :, :].cpu().numpy().transpose(1, 2, 0), cmap='gray')
		# end
	# end

	matplotlib.pyplot.show()
# end

# defining the network, this is what you are asked to complete
# the network and its layers are summarized in the table below

class Network(torch.nn.Module):
	#######################################################################
	# OPERATION                 # INPUT              # OUTPUT             #
	#######################################################################
	# BatchNorm2d               # (-1,    1, 28, 28) # (-1,    1, 28, 28) #
	# Conv2d, kernel_size=5     # (-1,    1, 28, 28) # (-1,   64, 24, 24) #
	# relu                      # (-1,   64, 24, 24) # (-1,   64, 24, 24) #
	# max_pool2d, kernel_size=3 # (-1,   64, 24, 24) # (-1,   64,  8,  8) #
	# Conv2d, kernel_size=5     # (-1,   64,  8,  8) # (-1,  512,  4,  4) #
	# relu                      # (-1,  512,  4,  4) # (-1,  512,  4,  4) #
	# max_pool2d, kernel_size=2 # (-1,  512,  4,  4) # (-1,  512,  2,  2) #
	# view(-1, 2048)            # (-1,  512,  2,  2) # (-1, 2048        ) #
	# Linear                    # (-1, 2048        ) # (-1,  256        ) #
	# dropout, p=0.35           # (-1,  256        ) # (-1,  256        ) #
	# relu                      # (-1,  256        ) # (-1,  256        ) #
	# Linear                    # (-1,  256        ) # (-1,  128        ) #
	# dropout, p=0.35           # (-1,  128        ) # (-1,  128        ) #
	# relu                      # (-1,  128        ) # (-1,  128        ) #
	# Linear                    # (-1,  128        ) # (-1,   10        ) #
	#######################################################################

	def __init__(self):
		super(Network, self).__init__()









	# end

	def forward(self, x):









		return torch.nn.functional.log_softmax(x, dim=1)
	# end
# end

moduleNetwork = Network()

# specifying the optimizer based on adaptive moment estimation, adam
# it will be responsible for updating the parameters of the network

objectOptimizer = torch.optim.Adam(params=moduleNetwork.parameters(), lr=0.001)

def train():
	# setting the network to the training mode, some modules behave differently during training

	moduleNetwork.train()
	torch.set_grad_enabled(True)

	# obtain samples and their ground truth from the training dataset, one minibatch at a time

	for tensorInput, tensorTarget in tqdm.tqdm(objectTrain):
		# setting all previously computed gradients to zero, we will compute new ones

		objectOptimizer.zero_grad()

		# performing a forward pass through the network while retaining a computational graph

		variableEstimate = moduleNetwork(variableInput)

		# computing the loss according to the cross-entropy / negative log likelihood
		# the backprop is done in the subsequent step such that multiple losses can be combined

		variableLoss = torch.nn.functional.nll_loss(input=variableEstimate, target=variableTarget)

		variableLoss.backward()

		# calling the optimizer, allowing it to update the weights according to the gradients

		objectOptimizer.step()
	# end
# end

def evaluate():
	# setting the network to the evaluation mode, some modules behave differently during evaluation

	moduleNetwork.eval()
	torch.set_grad_enabled(False)

	# defining two variables that will count the number of correct classifications

	intTrain = 0
	intValidation = 0

	# iterating over the training and the validation dataset to determine the accuracy
	# this is typically done one a subset of the samples in each set, unlike here
	# otherwise the time to evaluate the model would unnecessarily take too much time

	for tensorInput, tensorTarget in objectTrain:
		tensorEstimate = moduleNetwork(tensorInput)

		intTrain += tensorEstimate.max(dim=1, keepdim=False)[1].eq(tensorTarget).sum()
	# end

	for tensorInput, tensorTarget in objectValidation:
		tensorEstimate = moduleNetwork(tensorInput)

		intValidation += tensorEstimate.max(dim=1, keepdim=False)[1].eq(tensorTarget).sum()
	# end

	# determining the accuracy based on the number of correct predictions and the size of the dataset

	dblTrain.append(100.0 * intTrain / len(objectTrain.dataset))
	dblValidation.append(100.0 * intValidation / len(objectValidation.dataset))

	print('')
	print('train: ' + str(intTrain) + '/' + str(len(objectTrain.dataset)) + ' (' + str(dblTrain[-1]) + '%)')
	print('validation: ' + str(intValidation) + '/' + str(len(objectValidation.dataset)) + ' (' + str(dblValidation[-1]) + '%)')
	print('')
# end

# training the model for 100 epochs, one would typically save / checkpoint the model after each one

for intEpoch in range(100):
	train()
	evaluate()
# end

# plotting the learning curve according to the accuracies determined in the evaluation function
# note that this will not work if you are connected to the linux lab via ssh but no x forwarding

if False:
	matplotlib.pyplot.figure(figsize=(8.0, 5.0), dpi=150.0)
	matplotlib.pyplot.ylim(79.5, 100.5)
	matplotlib.pyplot.plot(dblTrain)
	matplotlib.pyplot.plot(dblValidation)
	matplotlib.pyplot.show()
# end