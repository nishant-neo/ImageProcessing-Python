import cv2
from matplotlib import pyplot as plt

#reading the image
img = cv2.imread('logo.png')
#splitting the image
b,g,r = cv2.split(img)

#plotting the image using matplotlib
#Converting the image to RGB as matplotlib plots in RGB
plt.figure(1)
plt.subplot(221)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.subplot(222)
plt.imshow(b,cmap = plt.cm.gray)
plt.title('Blue')
plt.subplot(223)
plt.imshow(g, cmap = plt.cm.gray)
plt.title('Green')
plt.subplot(224)
plt.imshow(r, cmap = plt.cm.gray)
plt.title('Red')
plt.show()
