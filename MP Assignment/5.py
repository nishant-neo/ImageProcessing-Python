import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

#reading the image
img = cv2.imread("p.png",cv2.IMREAD_GRAYSCALE)
img1 = img

#Whitened Image
x, y = img.shape
mean = np.mean(img)
variance = np.var(img)
std = math.sqrt(variance)

temp = np.zeros(img.shape)
for i in range( x ):
	for j in range( y ):
		temp[i,j] = (img[i,j] - mean) / std

#Histogram Equilized
histEq = cv2.equalizeHist(img1)


#Showing the images 
cv2.imshow('Original Inage',img1)
cv2.waitKey(0)
cv2.imshow('Whitened Image',temp)
cv2.waitKey(0)
cv2.imshow('Histogram Equilized Image',histEq)
cv2.waitKey(0)
res = np.hstack((img1,temp,histEq)) #stacking images side-by-side
cv2.imwrite('res.png',res)
