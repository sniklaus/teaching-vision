import torch
print(torch.__version__)

import torchvision
print(torchvision.__version__)

import cv2
import numpy

# generate new images by interpolating between two latent representations

# defining the network, a autoencoder that is similar to the one from the slides

class Network(torch.nn.Module):
	def __init__(self):
		super().__init__()

		self.moduleEncoder = torch.nn.Sequential(
			torch.nn.Conv2d(1, 32, kernel_size=5),
			torch.nn.ReLU(),
			torch.nn.Conv2d(32, 64, kernel_size=5),
			torch.nn.ReLU(),
			torch.nn.Conv2d(64, 128, kernel_size=4, stride=2),
			torch.nn.ReLU(),
			torch.nn.Conv2d(128, 256, kernel_size=3, stride=2),
			torch.nn.ReLU(),
			torch.nn.Conv2d(256, 64, kernel_size=4)
		)

		self.moduleDecoder = torch.nn.Sequential(
			torch.nn.ConvTranspose2d(64, 256, kernel_size=4),
			torch.nn.ReLU(),
			torch.nn.ConvTranspose2d(256, 128, kernel_size=3, stride=2),
			torch.nn.ReLU(),
			torch.nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2),
			torch.nn.ReLU(),
			torch.nn.ConvTranspose2d(64, 32, kernel_size=5),
			torch.nn.ReLU(),
			torch.nn.ConvTranspose2d(32, 1, kernel_size=5)
		)
	# end

	def forward(self, x):
		x = self.moduleEncoder(x)
		x = self.moduleDecoder(x)

		return x
	# end
# end

moduleNetwork = Network()

# loading the provided weights, this exercise is not about training the network

moduleNetwork.load_state_dict(torch.load('./17-autoencoder.pytorch'))

# setting the network to the evaluation mode, this makes no difference here though

moduleNetwork.train(False)

# loading two samples and converting them to tensors, each of size 1x1x28x28

tenFirst = torch.FloatTensor(cv2.imread(filename='./samples/fashion-1.png', flags=cv2.IMREAD_GRAYSCALE).astype(numpy.float32) / 255.0).unsqueeze(0).unsqueeze(0)
tenSecond = torch.FloatTensor(cv2.imread(filename='./samples/fashion-2.png', flags=cv2.IMREAD_GRAYSCALE).astype(numpy.float32) / 255.0).unsqueeze(0).unsqueeze(0)

# encode the two samples to retrieve their representation in the latent space
# generate new samples by interpolating between the two latent representations
# use the formula from the slides with alpha = [ x * 0.1 for x in range(11) ]
# append each interpolated result as a tensor of size 28x28 to tenOutputs

tenOutputs = []









# making sure that tenOutputs has the correct size and content using asserts
# afterwards combining all the samples into a single image and saving it to disk

assert(len(tenOutputs) == 11)

for tenOutput in tenOutputs:
	assert(type(tenOutput) == torch.FloatTensor)
	assert(tenOutput.shape[0] == 28)
	assert(tenOutput.shape[1] == 28)
# end

tenOutputs = [ tenFirst[0, 0] ] + tenOutputs + [ tenSecond[0, 0] ]

npyOutput = (numpy.concatenate([ tenOutput.numpy(force=True) for tenOutput in tenOutputs ], 1).clip(0.0, 1.0) * 255.0).astype(numpy.uint8)
npyOutput = cv2.resize(src=npyOutput, dsize=None, fx=2.0, fy=2.0, interpolation=cv2.INTER_NEAREST)

cv2.imwrite(filename='./17-autoencoder.png', img=npyOutput)