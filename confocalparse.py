# Purpose: Parse confocal images using opencv
# Written by Svena Yu, reference code from pyimagesearch.com
# Aug 24 2021

import cv2
import numpy as np
import argparse
import matplotlib.pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread(args["image"])
image = cv2.medianBlur(image,3)
output = image.copy()
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(output, cv2.HOUGH_GRADIENT, 1, 10)
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
	# show the output image
	cv2.imwrite('output.png', np.hstack([image,output]))
	# cv2.imshow("output", np.hstack([image, output]))
	# cv2.waitKey(0)
else:
	print('No circles were found!')
