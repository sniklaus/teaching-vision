# teaching-vision
This project provides the framework for my computer vision class in which the students are ought to solve various exercises that are automatically graded by a server.

## overview
The repository contains all the exercises together with individual submission scripts. To effectively make use of the framework, you will need a login that you are going to receive at the beginning of the course.

You can keep track of your progress on the [webinterface](http://mercury.cs.pdx.edu/) of the grading server. The score shown there is used as the basis for the grading. Make sure to respect the deadlines, they are strictly enforced and not negotiable.

TODO: SCREENSHOT OF THE WEBINTERFACE

## download
To download this framework, you can either use the button on the top of this page or clone the repository with the following command. The latter option is recommended as you are encouraged to manage your code in a source repository, even though you might have to install [git](http://git-scm.com) before you will be able to do so.

```
git clone https://github.com/sniklaus/teaching-vision
```

After downloading, please make sure to change the username and password in the setup file. You are going to receive this login information at the beginning of the course.

```bash
strUser="CHANGE THIS"
strPassword="CHANGE THIS"
```

Should you not be using the machines in the Linux lab, you also need to make sure that you have `wget` installed. While you are encouraged to use your own machine, please note that I am unable to provide individual support to get the framework to run outside of the Linux lab.

## setup
TODO

## usage
Every exercise comes with a bash script that uploads the exercise to the grading server and gathers the response. For example, after navigating to the folder that contains the color exercises, you can use the following command to submit the `1-negative` exercise.

```
bash 1-negative.bash
```

This command should complete with a message stating that the submission was successful and the [webinterface](http://mercury.cs.pdx.edu/) of the grading server should now indicate that you received a point for this exercise. This is to be expected since the solution is already provided. Should this message not appear, make sure that you configured the setup file as stated in the download section.

Please note that every exercise only has a single file that you are asked to modify. Therefore, you cannot, for example, add an additional file and add a reference to it since the submission system would not upload it to the grading server.

## grading
You can submit exercises as often as you want until you pass them. This emphasizes the trial-and-error methodology that you encounter in the real world. There is no penalty for failed submissions, the grading is purely based on the score that the webinterface indicates by the time the respective deadline has passed. You do not need to additionally turn in your solutions, your submissions are already stored on the grading server.

## `color/*`
TODO

## `filter/*`
TODO

## `multiresolution/*`
TODO

## `blending/*`
TODO

## `alignment/*`
TODO

## `segmentation/*`
TODO

## `fusion/*`
TODO

## linux lab
When connecting remotely into the Linux lab, please choose one of the machines in the [first](https://cat.pdx.edu/labstatus/labs/cslinlaba/) or the [second](https://cat.pdx.edu/labstatus/labs/cslinlabb/) lab. After selecting a machine, you can use your credentials to establish a connection through ssh. Note that you can alternatively use PuTTY as well.

```
ssh <username>@<machine>.cs.pdx.edu
```

I am well aware that this is rather inconvenient but it is at least guaranteed to work. You are furthermore encouraged to use your own computer without connecting remotely into the Linux lab. However, I am unable to provide individual support to get the framework to run on your own computer.

## virtual machine
Using a virtual machine is always a viable option. I personally do this as well and developed this framework in a Debian environment that is running within a virtual machine. Note that there are quite a few free virtualizers to choose from and while I have a preferred one, I would like to take the liberty of not making any advertisements here. Therefore, I would recommend reading a few related online resources.

## images
* blend by [Juliane Aulbach](https://www.linkedin.com/in/aulbach)
* fusion, homography, panorama, and text by [Simon Niklaus](https://www.linkedin.com/in/sniklaus)
* fruits by [romanov](https://pixabay.com/en/fruits-sweet-fruit-exotic-82524/)
* multiband by [Peter J. Burt and Edward H. Adelson](http://dl.acm.org/citation.cfm?id=247)
* prokudin by [Sergey Prokudin-Gorsky](https://www.loc.gov/pictures/collection/prok/process.html)
* transfer by [Reinhard et al.](http://ieeexplore.ieee.org/document/946629)

## license
Please refer to the appropriate file within this repository.