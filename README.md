# teaching-vision
This project provides the exercises for my visual computing class in which the students are ought to solve various tasks that are closely related to the course material.

## setup
I highly recommend using Anaconda with Python 3 to do the exercises. You can obtain the version that I will be using by executing the following commands. Feel free to use other environments as well. However, the recommended environment is what will be used for grading. Furthermore, while you are encouraged to use your own machine, please note that I am unable to provide individual support.

```bash
wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p $HOME/anaconda
rm Anaconda3-4.2.0-Linux-x86_64.sh
export PATH="$HOME/anaconda/bin:$PATH"
conda install -y -c menpo opencv3
```

Should you be using the machines in the Linux lab, you also need to make sure that you run the `export` command again when logging out and back in. Since the Linux lab is a shared environment, the `.bashrc` cannot be modified which prevents Anaconda from doing this automatically for you.

## `01-colorspace` (5 points)
Follow the description in "Color Transfer between Images" by Reinhard et al. to convert an image to the LMS color space. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html

Notice that the resulting image will show the LMS color space as an RGB color space, which has little meaning.

## `02-colortransfer` (5 points)
Follow the description in "Color Transfer between Images" by Reinhard et al. to match the color distribution of one image to another. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.mean.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.std.html

Feel free to try this out on images of your own. You may find that the resulting quality varies and that some examples work better than others.

## `03-demosaicing` (10 points)
Implement the bilinear interpolation described in the slides as well as in "Interactions Between Color Plane Interpolation and Other Image Processing Functions in Electronic Photography" by Adams to perform demosaicing of Bayer patterns. Some resources that can potentially help you to achieve this goal are stated below.

* http://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html

Notice that diagonal edges are particularly prone to artifacts with this simple approach. In practice, other algorithms work much better.

## `04-convolution` (5 points)
Use convolutions to implement demosaicing algorithm described in the slides as well as in "Interactions Between Color Plane Interpolation and Other Image Processing Functions in Electronic Photography" by Adams. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#ga27c049795ce870216ddfb366086b5a04

Other than that the output is one pixel larger on each side, the result should otherwise be identical to the previous exercise that does not make use of convolutions. The new approach is likely to be much faster though.

## `05-median` (5 points)
Filter a given image once by using a Gaussian kernel and once by using a median filter. Feel free to use the functions built into OpenCV which are implementations of the theory covered in class. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1
* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#ga564869aa33e58769b4469101aac458f9

Notice that the [implementation](https://github.com/opencv/opencv/blob/master/modules/imgproc/src/smooth.cpp#L2686) of the median filtering is heavily optimized. Our usage of this implementation could potentially be sped up by using `uint8` over `float32` arrays.

## `06-spectrum` (10 points)
Make use of the convolution theorem and implement a convolution as a Hadamard product in the frequency space. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.pad.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.roll.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft2.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.ifft2.html

Make sure to examine the resulting plot of the spectrum and how the diagonal within the filter kernel is resembled in its frequency spectrum.

## `07-pyramid` (5 points)
Implement a Laplacian pyramid described in the slides as well as in "The Laplacian Pyramid as a Compact Image Code" by Burt and Adelson. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#gaf9bba239dfca11654cb7f50f889fc2ff
* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#gada75b59bdaaca411ed6fee10085eb784

Due to the built-in `pyrDown` and `pyrUp` functions of OpenCV, this tasks becomes relatively simple since they directly mimic the `REDUCE` and `EXPAND` operations.

## `08-homography` (10 points)
Given four corresponding points, estimate the Homography matrix and warp the image accordingly. Do this step by step as shown in class and do not use the functions state below.

* https://docs.opencv.org/3.4.0/d9/d0c/group__calib3d.html#ga4abc2ece9fab9398f2e560d53c8c9780
* https://docs.opencv.org/3.4.0/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87

Note that the approach without bilinear interpolation that I showed in class is fairly slow due to Python. A sampling grid could be used to speed this up.

## `09-colorize` (5 points)
Compose a color image from a [Prokudin-Gorskii](https://www.loc.gov/pictures/collection/prok/process.html) photo by aligning the individual exposures and stacking them. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.opencv.org/3.4.0/dc/d6b/group__video__track.html#ga7ded46f9a55c0364c92ccd2019d43e3a
* https://docs.opencv.org/3.4.0/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87

Note that the movement of individual objects in between two exposures is not captured by the Homography transform. We will discuss how to address these in a different lecture.

## `10-multiband` (10 points)
Follow the description in the slides as well as in "Pyramid Methods in Image Processing" by Adelson et al. to implement multiband blending using Laplacian pyramids. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html
* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#gaf9bba239dfca11654cb7f50f889fc2ff
* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#gada75b59bdaaca411ed6fee10085eb784

The sample solution uses `numpy.concatenate` to combine the individual halves. There are many other ways of achieving the same result though.

## `11-seam` (10 points)
Implement seam carving as described in the slides as well as in "Seam Carving for Content-Aware Image Resizing" by Avidan and Shamir. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.copy.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmin.html

This can potentially be slow due to Python, the sample solution takes almost a minute to execute. Multiple seams can have the same energy, make sure to follow the comments to resolve this ambiguity.

## `12-tonemapping` (10 points)
Follow the description in the slides as well as in "Photographic Tone Reproduction for Digital Images" by Reinhard et al. to implement photographic luminance mapping. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html
* https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html

Make sure to use the fixed version of the first equation. Its definition in the paper does not correctly represent the geometric mean.

## `13-fusion` (10 points)
Implement exposure fusion as proposed in "Exposure Fusion" by Mertens et al. as well as described in the slides. Some resources that can potentially help you to achieve this goal are stated below.

* https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html
* https://docs.opencv.org/3.2.0/d7/d1b/group__imgproc__misc.html#ga397ae87e1288a81d2363b61574eb8cab
* https://docs.opencv.org/3.4.0/d4/d86/group__imgproc__filter.html#gad78703e4c8fe703d479c1860d76429e6

Note that you are only asked to extract and normalize the weight maps. The multiband blending is already implemented for you. Please refrain from using OpenCV functions other than `cvtColor` and `Laplacian` for this exercise.

## `14-mnist` (10 points)
Given a provided neural network to classify handwritten digits as well as a test dataset, find samples that are being misclassified. Some resources that can potentially help you to achieve this goal are stated below.

* http://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html
* http://pytorch.org/docs/master/autograd.html#torch.autograd.Variable
* http://pytorch.org/docs/master/tensors.html#torch.Tensor.max

Notice that the misclassified samples are rather ambiguous. In fact, one might remove such samples if they were in the training dataset.

## `15-fashion` (10 points)
Implement a neural network according to the specifications outlined in the comments. Some resources that can potentially help you to achieve this goal are stated below.

* http://pytorch.org/docs/master/tensors.html#torch.Tensor.view
* http://pytorch.org/docs/master/nn.html#torch.nn.BatchNorm2d
* http://pytorch.org/docs/master/nn.html#torch.nn.Conv2d
* http://pytorch.org/docs/master/nn.html#torch.nn.Linear
* http://pytorch.org/docs/master/nn.html#torch.nn.functional.relu
* http://pytorch.org/docs/master/nn.html#torch.nn.functional.max_pool2d
* http://pytorch.org/docs/master/nn.html#torch.nn.functional.dropout

Make sure to use `pip` or `conda` to install `tqdm` in case the import is causing issues. Notice that the provided code is making use of CUDA and hence requires a NVIDIA graphics card. You can remotely connect to a free machine in one of the Linux labs, not `linux.cs.pdx.edu`, and make use of its graphics card. You can also make use of [Colaboratory](https://colab.research.google.com/) which provides a free GPU instance.

## linux lab
When connecting remotely into the Linux lab, please choose one of the machines in the [first](https://cat.pdx.edu/labstatus/labs/cslinlaba/) or the [second](https://cat.pdx.edu/labstatus/labs/cslinlabb/) lab. After selecting a machine, you can use your credentials to establish a connection through ssh. Note that you can alternatively use PuTTY as well.

```
ssh <username>@<machine>.cs.pdx.edu
```

I am well aware that this is rather inconvenient but it is at least guaranteed to work. You are furthermore encouraged to use your own computer without connecting remotely into the Linux lab. However, I am unable to provide individual support to get the framework to run on your own computer.

## virtual machine
Using a virtual machine is always a viable option. I personally do this as well and developed these exercises in a Debian environment that is running within a virtual machine. Note that there are quite a few free virtualizers to choose from and while I have a preferred one, I would like to take the liberty of not making any advertisements here. Therefore, I would recommend reading a few related online resources.

## images
* ahwahnee by [Mark Fairchild](http://rit-mcsl.org/fairchild//HDRPS/Scenes/AhwahneeGreatLounge.html)
* blend by [Juliane Aulbach](https://www.linkedin.com/in/aulbach)
* demosaicing by [Patrick Vandewalle et al.](http://lcavwww.epfl.ch/reproducible_research/VandewalleKAS07)
* fusion, homography, panorama, and text by [Simon Niklaus](https://www.linkedin.com/in/sniklaus)
* fruits by [romanov](https://pixabay.com/en/fruits-sweet-fruit-exotic-82524/)
* multiband by [Peter J. Burt and Edward H. Adelson](http://dl.acm.org/citation.cfm?id=247)
* prokudin by [Sergey Prokudin-Gorsky](https://www.loc.gov/pictures/collection/prok/process.html)
* seam by [Avidan and Shamir](http://www.faculty.idc.ac.il/arik/SCWeb/imret/index.html)
* transfer by [Reinhard et al.](http://ieeexplore.ieee.org/document/946629)

## license
Please refer to the appropriate file within this repository.