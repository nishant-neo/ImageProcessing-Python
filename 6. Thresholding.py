import cv2
import numpy as np

img =  cv2.imread('bookpage.jpg')
# we used here 12 coz the image is low light, if it was bright probably
# would have taken 220, max value = 255
retval, threshold = cv2.threshold( img, 12, 255, cv2.THRESH_BINARY)

# we convertt the image to grayscale and then thresholding as
# the colored thresholding led to colored image
grayscaled = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold( grayscaled, 12, 255, cv2.THRESH_BINARY)
#but we got a lot of black patch in center

#we'll use gaussian thresholding
gaus = cv2.adaptiveThreshold(grayscaled,  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 65,1) 


cv2.imshow('original', img)
cv2.imshow('threshold', threshold2)
cv2.imshow('gauss', gaus)
cv2.waitKey(0)
cv2.destryAllWindows()