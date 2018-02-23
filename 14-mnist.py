import numpy
import cv2
import torch
import torchvision

# find samples from the dataset that are misclassified by the provided model

# creating a data loader for the training samples of the mnist dataset
# specifying the batch size and making sure it runs in a background thread

objectDataset = torch.utils.data.DataLoader(
	batch_size=64,
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

# reducing the size of the dataset to limit the number of misclassified samples

objectDataset.dataset.test_data = objectDataset.dataset.test_data[:700]

# defining the network, just a basic convolutional neural network from the slides

class Network(torch.nn.Module):
	def __init__(self):
		super(Network, self).__init__()

		self.conv1 = torch.nn.Conv2d(1, 32, kernel_size=5)
		self.conv2 = torch.nn.Conv2d(32, 64, kernel_size=5)
		self.fc1 = torch.nn.Linear(256, 200)
		self.fc2 = torch.nn.Linear(200, 10)
	# end

	def forward(self, x):
		x = self.conv1(x)
		x = torch.nn.functional.relu(x)
		x = torch.nn.functional.max_pool2d(x, kernel_size=3)
		x = self.conv2(x)
		x = torch.nn.functional.relu(x)
		x = torch.nn.functional.max_pool2d(x, kernel_size=2)
		x = x.view(-1, 256)
		x = self.fc1(x)
		x = torch.nn.functional.relu(x)
		x = self.fc2(x)

		return torch.nn.functional.log_softmax(x, dim=1)
	# end
# end

moduleNetwork = Network()

# loading the provided weights, this exercise is not about training the network

moduleNetwork.load_state_dict(torch.load('./14-mnist.pytorch'))

# setting the network to the evaluation mode, this makes no difference here though

moduleNetwork.eval()

# a utility function that you should use to save / dump misclassified samples

intWritten = 0

def write_image(tensorInput, intTarget, intEstimate):
	global intWritten

	assert(tensorInput.size(0) == 1)
	assert(tensorInput.size(1) == 28)
	assert(tensorInput.size(2) == 28)

	intWritten += 1

	numpyInput = numpy.repeat(numpy.rollaxis(tensorInput.numpy(), 0, 3), 3, 2)
	numpyInput = cv2.resize(src=numpyInput, dsize=(280, 280), fx=0.0, fy=0.0, interpolation=cv2.INTER_NEAREST)
	numpyInput = (numpyInput * 255.0).clip(0.0, 255.0).astype(numpy.uint8)

	cv2.putText(img=numpyInput, text='truth: ' + str(intTarget), org=(10, 240), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
	cv2.putText(img=numpyInput, text='estimate: ' + str(intEstimate), org=(10, 270), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

	cv2.imwrite(filename='./14-mnist-' + str(intWritten) + '.png', img=numpyInput)
# end

# iterate over all examples in objectDataset and classify them using moduleNetwork
# notice that cuda is not being used, you do not need a gpu for this exercise
# call write_image for misclassified samples, providing the target label and the estimate









# if the following assert fails then the number of found misclassifications is incorrect

assert(intWritten == 6)