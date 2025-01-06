import torch
print(torch.__version__)

import torchvision
print(torchvision.__version__)

import cv2
import numpy

# find samples from the dataset that are misclassified by the provided model

# creating a data loader for the training samples of the mnist dataset
# specifying the batch size and making sure it runs in a background thread

objDataset = torch.utils.data.DataLoader(
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

objDataset.dataset.test_data = objDataset.dataset.test_data[:700]

# defining the network, just a basic convolutional neural network from the slides

class Network(torch.nn.Module):
	def __init__(self):
		super().__init__()

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

moduleNetwork.train(False)

# iterate over all examples in objDataset and classify them using moduleNetwork
# append each misclassified sample to objOutputs like in the example below
# note that each entry should also have the true / target as well as the estimated label

objOutputs = []

# objOutputs.append({
# 	'tenInput': torch.rand(28, 28),
# 	'intTarget': 1,
# 	'intEstimate': 2
# })









# making sure that objOutputs has the correct size and content using asserts
# afterwards combining all the samples into a single image and saving it to disk

assert(len(objOutputs) == 6)

npyOutputs = []

for objOutput in objOutputs:
	assert(type(objOutput['tenInput']) == torch.FloatTensor)
	assert(type(objOutput['intTarget']) == int)
	assert(type(objOutput['intEstimate']) == int)
	assert(objOutput['tenInput'].shape[0] == 28)
	assert(objOutput['tenInput'].shape[1] == 28)

	npyOutput = (numpy.repeat(objOutput['tenInput'].numpy(force=True)[:, :, None], 3, 2).clip(0.0, 1.0) * 255.0).astype(numpy.uint8)
	npyOutput = cv2.resize(src=npyOutput, dsize=None, fx=5.0, fy=5.0, interpolation=cv2.INTER_NEAREST)
	npyOutput = numpy.pad(npyOutput, [ (0, 40), (0, 0), (0, 0) ], 'constant')

	cv2.putText(img=npyOutput, text='truth: ' + str(objOutput['intTarget']), org=(10, 148), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)
	cv2.putText(img=npyOutput, text='estimate: ' + str(objOutput['intEstimate']), org=(10, 168), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(255, 255, 255), thickness=1, lineType=cv2.LINE_AA)

	npyOutputs.append(npyOutput)
# end

npyOutput = numpy.concatenate(npyOutputs, 1)

cv2.imwrite(filename='./14-mnist.png', img=npyOutput)