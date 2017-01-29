import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

img = cv2.imread("p.png",cv2.IMREAD_GRAYSCALE)
img1 = img

x, y = img.shape
mean = np.mean(img)
variance = np.var(img)
std = math.sqrt(variance)

temp = np.zeros(img.shape)
for i in range( x ):
	for j in range( y ):
		temp[i,j] = (img[i,j] - mean) / std

histEq = cv2.equalizeHist(img1)


#plotting the images through matplotlib
result = plt.figure()

cv2.imshow('Thresh',temp)
cv2.waitKey(0)
res = np.hstack((img1,temp)) #stacking images side-by-side
cv2.imwrite('res.png',res)
