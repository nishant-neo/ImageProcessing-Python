import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("search.png")

#converting from bgr to Grayscale)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#plotting the images through matplotlib
result = plt.figure()
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('BGR Image')
plt.subplot(122)
plt.imshow(gray, cmap=plt.cm.gray)
plt.title('Grayscale Image')
plt.show()
