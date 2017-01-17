import cv2 
import numpy as np
import matplotlib.pyplot as plt
 
#earlier we did was template matching
#so now it can have diff angles, rotation, lighting

img1 = cv2.imread('opencv-temp.jpg', 1)
img2 = cv2.imread('opencv-img.jpg', 1)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags =2)#the number here shows the number of matches to be made

plt.imshow(img3)
plt.show()