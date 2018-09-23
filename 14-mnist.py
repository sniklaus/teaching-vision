import torch
print(torch.__version__)

import torchvision
print(torchvision.__version__)

import cv2
import numpy

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

# iterate over all examples in objectDataset and classify them using moduleNetwork
# append each misclassified sample to objectOutputs like in the example below
# note that each entry should also have the true / target as well as the estimated label

objectOutputs = []

# objectOutputs.append({
# 	'tensorInput': torch.rand(28, 28),
# 	'intTarget': 1,
# 	'intEstimate': 2
# })









# making sure that objectOutputs has the correct size and content using asserts
# afterwards combining all the samples into a single image and saving it to disk

assert(len(objectOutputs) == 6)

numpyOutputs = []

for objectOutput in objectOutputs:
	assert(type(objectOutput['tensorInput']) == torch.FloatTensor)
	assert(type(objectOutput['intTarget']) == int)
	assert(type(objectOutput['intEstimate']) == int)
	assert(objectOutput['tensorInput'].size(0) == 28)
	assert(objectOutput['tensorInput'].size(1) == 28)

	numpyOutput = (numpy.repeat(objectOutput['tensorInput'].numpy()[:, :, None], 3, 2).clip(0.0, 1.0) * 255.0).astype(numpy.uint8)
	numpyOutput = cv2.resize(src=numpyOutput, dsize=None, fx=5.0, fy=5.0, interpolation=cv2.INTER_NEAREST)
	numpyOutput = numpy.pad(numpyOutput, [ (0, 40), (0, 0), (0, 0) ], 'constant')

	cv2.putText(img=numpyOutput, text='truth: ' + str(objectOutput['intTarget']), org=(10, 148), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
	cv2.putText(img=numpyOutput, text='estimate: ' + str(objectOutput['intEstimate']), org=(10, 168), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

	numpyOutputs.append(numpyOutput)
# end

numpyOutput = numpy.concatenate(numpyOutputs, 1)

cv2.imwrite(filename='./14-mnist.png', img=numpyOutput)