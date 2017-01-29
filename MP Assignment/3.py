import numpy as np
import cv2
from matplotlib import pyplot as plt

#reading the image
img = cv2.imread("demo.png")

#converting from bgr to L*a*b*
hs = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

#splitting the colorspace to individual channels
L,a,b = cv2.split(hs)

#plotting the images through matplotlib
result = plt.figure()
plt.subplot(221)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(222)
plt.imshow(L, cmap=plt.cm.gray)
plt.title('L')
plt.subplot(223)
#plt.imshow(a, cmap=plt.cm.gray)
plt.imshow(a)
plt.title('a*')
plt.subplot(224)
#plt.imshow(b, cmap=plt.cm.gray)
plt.imshow(b)
plt.title('b*')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()