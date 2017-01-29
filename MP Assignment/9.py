import cv2
import numpy as np

#reading the image
img = cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE)

#Defining the kernel matrix for Roberts operator and them applying the Roberts operator
roberts_y = np.array(([0,0,0],[0,1,0],[0,0,-1]),dtype="int")
roberts_x = np.array(([0,0,0],[0,0,1],[0,-1,0]), dtype = "int")
rob_x = cv2.filter2D(img, -1, roberts_x)
rob_y = cv2.filter2D(img, -1, roberts_y)

# h-stacking the images and then displaying
res = np.hstack((img,rob_x, rob_y))
cv2.imshow("image", res)
cv2.waitKey(0)
