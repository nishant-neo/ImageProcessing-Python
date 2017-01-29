import cv2
import numpy as np

img = cv2.imread("noisy.png",cv2.IMREAD_GRAYSCALE)
img1 = img
i = 3
while i <= 15:
	blur = cv2.GaussianBlur(img, (i,i), 0)	
	res = np.hstack((img,blur)) #stacking images side-by-side
	cv2.imshow('Original and Blurred with i = ' + str(i),res)
	cv2.waitKey(0)
	i = i + 2

