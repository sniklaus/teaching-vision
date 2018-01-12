# teaching-vision
This project provides the exercises for my computer vision class in which the students are ought to solve various tasks that are closely related to the course material.

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
Follow the description in "Color Transfer between Images" by Reinhard et al. to convert an image to the LMS color space. Some resources that can potentially help you to achieve this goal are stated blow.

* https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.stack.html

Notice that the resulting image will show the LMS color space as an RGB color space, which has little meaning.

## `02-colortransfer` (5 points)
Follow the description in "Color Transfer between Images" by Reinhard et al. to match the color distribution of one image to another. Some resources that can potentially help you to achieve this goal are stated blow.

* https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.mean.html
* https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.std.html

Feel free to try this out on images of your own. You may find that the resulting quality varies and that some examples work better than others.

## `03-demosaicing` (10 points)
Implement the bilinear interpolation described in the slides as well as in "Interactions Between Color Plane Interpolation and Other Image Processing Functions in Electronic Photography" by Adams to perform demosaicing of Bayer patterns. Some resources that can potentially help you to achieve this goal are stated blow.

* http://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html
* https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.ndarray.shape.html

Notice that diagonal edges are particularly prone to artifacts with this simple approach. In partice, other algorithms work much better.

## linux lab
When connecting remotely into the Linux lab, please choose one of the machines in the [first](https://cat.pdx.edu/labstatus/labs/cslinlaba/) or the [second](https://cat.pdx.edu/labstatus/labs/cslinlabb/) lab. After selecting a machine, you can use your credentials to establish a connection through ssh. Note that you can alternatively use PuTTY as well.

```
ssh <username>@<machine>.cs.pdx.edu
```

I am well aware that this is rather inconvenient but it is at least guaranteed to work. You are furthermore encouraged to use your own computer without connecting remotely into the Linux lab. However, I am unable to provide individual support to get the framework to run on your own computer.

## virtual machine
Using a virtual machine is always a viable option. I personally do this as well and developed these exercises in a Debian environment that is running within a virtual machine. Note that there are quite a few free virtualizers to choose from and while I have a preferred one, I would like to take the liberty of not making any advertisements here. Therefore, I would recommend reading a few related online resources.

## images
* blend by [Juliane Aulbach](https://www.linkedin.com/in/aulbach)
* demosaicing by [Patrick Vandewalle et al.](http://lcavwww.epfl.ch/reproducible_research/VandewalleKAS07)
* fusion, homography, panorama, and text by [Simon Niklaus](https://www.linkedin.com/in/sniklaus)
* fruits by [romanov](https://pixabay.com/en/fruits-sweet-fruit-exotic-82524/)
* multiband by [Peter J. Burt and Edward H. Adelson](http://dl.acm.org/citation.cfm?id=247)
* prokudin by [Sergey Prokudin-Gorsky](https://www.loc.gov/pictures/collection/prok/process.html)
* transfer by [Reinhard et al.](http://ieeexplore.ieee.org/document/946629)

## license
Please refer to the appropriate file within this repository.