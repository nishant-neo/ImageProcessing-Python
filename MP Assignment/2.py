import cv2
from matplotlib import pyplot as plt

#Reading the image
img = cv2.imread("lena.png")

#converting from bgr to hsv
hs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#splitting the image 
h, s, v = cv2.split(hs)

#preparing the hue channel
s1 = s
v1 = v.copy()
v1.fill(255)
h1 = cv2.cvtColor(cv2.merge([h,s1,v1]), cv2.COLOR_HSV2BGR)

#plotting the image using matplotlib
plt.figure(1)
plt.subplot(221)
#Plotting & Converting the image to RGB as matplotlib plots in RGB
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.title('original')
plt.subplot(222)
#Plotting & Converting the image to RGB as matplotlib plots in RGB
plt.imshow(cv2.cvtColor(h1,cv2.COLOR_BGR2RGB))
plt.title('Hue')
plt.subplot(223)
plt.imshow(s,cmap = plt.cm.gray)
plt.title('Saturation')
plt.subplot(224)
plt.imshow(v, cmap = plt.cm.gray)
plt.title('Value')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
