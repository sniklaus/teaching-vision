import numpy
import cv2

numpyFirst = cv2.imread(filename='./../samples/panorama-1.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0
numpySecond = cv2.imread(filename='./../samples/panorama-2.png', flags=cv2.IMREAD_COLOR).astype(numpy.float32) / 255.0

numpyGrayFirst = cv2.cvtColor(src=cv2.imread(filename='./../samples/panorama-1.png', flags=cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2GRAY)
numpyGraySecond = cv2.cvtColor(src=cv2.imread(filename='./../samples/panorama-2.png', flags=cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2GRAY)

numpyMask = numpy.ones(numpySecond.shape, numpy.float32) # a mask that will be used for composing the output

objectOrb = cv2.ORB_create() # initiate the orb detector

objectKeypointsFirst, objectDescriptorsFirst = objectOrb.detectAndCompute(...) # extract the keypoints and their descriptors from numpyFirst
objectKeypointsSecond, objectDescriptorsSecond = objectOrb.detectAndCompute(...) # extract the keypoints and their descriptors from numpySecond

objectMatches = cv2.BFMatcher(...).match(...) # find matches between the two sets of descriptors, use the hamming norm and enable cross checking

objectMatches = sorted(objectMatches, key=lambda objectMatch: objectMatch.distance)[0:16] # only use the best / closest matches

objectMatchpointsFirst = numpy.array([ objectKeypointsFirst[objectMatch.queryIdx].pt for objectMatch in objectMatches ], numpy.float32) # array of matched keypoints
objectMatchpointsSecond = numpy.array([ objectKeypointsSecond[objectMatch.trainIdx].pt for objectMatch in objectMatches ], numpy.float32) # array of matched keypoints

numpyWarp = cv2.findHomography(...)[0] # find the homography matrix of the matched keypoints - use the default method and not ransac

numpyWarped = cv2.warpPerspective(...) # warp numpySecond based on the homography matrix - use a destination size of 1024 x 1024 pixels, the linear interpolation method and the inverse transform
numpyMask = cv2.warpPerspective(...) # warp numpyMask based on the homography matrix - use a destination size of 1024 x 1024 pixels, the linear interpolation method and the inverse transform

numpyOutput = (numpy.pad(numpyFirst, [(0, 0), (0, 256), (0, 0)], 'constant') * (1.0 - numpyMask)) + numpyWarped # mask out the destination and insert the warped image to compose the output

cv2.imwrite(filename='./2-panorama.png', img=(numpyOutput * 255.0).clip(0.0, 255.0).astype(numpy.uint8))