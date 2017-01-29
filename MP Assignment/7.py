import cv2
import numpy as np
import random

#reading the image
img = cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE)
x,y = img.shape
out = np.copy(img)

#Adding salt and pepper noise
#Salt Noise
num_salt = int(x * y * 0.01) #number of salt
pts = [(random.randint(0,x-1), random.randint(0,y-1)) for i in range(num_salt)]
for i in pts:
    out[i] = 255

#Pepper Noise
num_pepper = int(x * y * 0.01) # number of pepper noise
pts = [(random.randint(0,x-1), random.randint(0,y-1)) for i in range(num_pepper)]
for i in pts:
    out[i] = 0


#Median Blurring with kernel size = 3
med = cv2.medianBlur(out,3)

res = np.hstack((img,out,med)) # H-Stacking the images
cv2.imshow('Salt and pepper and Median Blurring', res)
cv2.waitKey(0)
