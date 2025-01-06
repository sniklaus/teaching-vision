import cv2
import matplotlib.pyplot
import numpy
import os
import zipfile

# this exercise references "Photographic Tone Reproduction for Digital Images" by Reinhard et al.

npyRadiance = cv2.imread(filename='./samples/ahwahnee.hdr', flags=-1)

# perform tone mapping according to the photographic luminance mapping

# first extracting the intensity from the color channels
# note that the eps / delta is to avoid divisions by zero and log of zero

npyIntensity = cv2.cvtColor(src=npyRadiance, code=cv2.COLOR_BGR2GRAY) + 0.0000001

# start off by approximating the key of npyIntensity according to equation 1
# then normalize npyIntensity using a = 0.18 according to equation 2
# afterwards, apply the non-linear tone mapping prescribed by equation 3
# finally obtain npyOutput using the ad-hoc formula with s = 0.6 from the slides









cv2.imwrite(filename='./12-tonemapping.png', img=(npyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))