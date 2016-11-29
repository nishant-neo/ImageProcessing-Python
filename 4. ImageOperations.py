import numpy as np
import cv2

img = cv2.imread("im.jpg", cv2.IMREAD_COLOR)

#we can just print the pixel BGR values and change them to different values
px = img[55,55]
print px
img[55,55] = [255,255,255]
print img[55,55]

#similarly we can change a range of values to a specific values
img[100:150, 100:150] = [255,255,255]

#similarly we can cut an sub-image from image and then paste it somewhere else 
remove = img[37:111, 107:194]
img[0:74, 0:87] = remove

#this is just to display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()