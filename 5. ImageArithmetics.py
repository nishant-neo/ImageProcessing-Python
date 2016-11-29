import cv2
import numpy as np

img1 = cv2.imread('im3.jpg')
img2 = cv2.imread('im4.jpg')

add = img1 + img2 #neither images has lost its opaquenes
#we will use a built in function in openCV
add = cv2.add(img1, img2)
#what exctly is happening is the pixel value is added up
#(155, 211,79) + (50,170,200) = 205, 381 , 279 translated to (205,255,255)

#weighted addition of the images
weighted = cv2.addWeighted(img1, 0.4, img2, 0.6 , 0)

#but the image kind of superimposed over each other
#lets try it another way
#but what if we just want the logo part, and not the white background? 
#We can use the same principle as we had used before for the ROI replacement, 
#but we need a way to "remove" the background of the logo, so that the white 
#is not needlessly blocking more of the background image.


img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')
#put logo on top-left corner, So create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# add a threshold
#basically the way it works is it will convert all pixels to either black or white, based on a threshold value. 
#In our case, the threshold is 220, but we can use other values, or even dynamically choose one, which is what the 
#ret variable can be used for.
ret, mask = cv2.threshold( img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
#cv2.imshow("im2g", img2gray)
#cv2.imshow("msk", mask)
#cv2.imshow("msk_inv", mask_inv)
#cv2.imshow("bg", img1_bg)
#cv2.imshow("bg", img2_fg)
cv2.imshow("res", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
