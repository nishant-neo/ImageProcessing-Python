import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('im.jpg',cv2.IMREAD_GRAYSCALE)
 
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.plot([50,100], 'c', linewidth = 6)
#plt.show()

cv2.imwrite('im.jpg', img)
