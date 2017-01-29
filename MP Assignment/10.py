import cv2
import numpy as np

#reading the image
img = cv2.imread('Lenna.jpg', cv2.IMREAD_GRAYSCALE)
im = img.copy()

#Taking the laplacian
lap = cv2.Laplacian(im, cv2.CV_64F)
#Defining the kernel matrix for Laplacian operator and them applying the laplacian operator
kernel = np.array(([0,-1,0],[-1,4,-1],[0,-1,0]),dtype = "int")
sharp = cv2.filter2D(img,-1, kernel)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.imshow("laplacian",sharp)
cv2.waitKey(0)

#Sharpening of the image using laplacian edges
sharp = sharp + img
sharp = sharp - np.amin(sharp)
sharp = sharp * ( 255 / np.amax(sharp))
res = np.hstack((img,lap, sharp))
cv2.imshow("Sharpened",sharp)
cv2.waitKey(0)
