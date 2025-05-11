import cv2 as cv
import math
import numpy as np
import os

canvas_length = 28
canvas_width = 28

pixel_data = np.array([[0]*canvas_length] * canvas_width)

image = cv.imread('/Users/williamvanuitert/Desktop/Pyhton/nine.png', cv.IMREAD_GRAYSCALE)
#cv.imshow('image', image)

if(image is None):
    print("none")
#px = img[28,28]
