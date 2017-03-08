import sys

import numpy as np
import cv2

from matplotlib import pyplot as plt

im = cv2.imread('highway.jpg')
im3 = im
im4 = im.copy()

#grayscale conversion
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

#bluring
blur = cv2.GaussianBlur(gray,(7,7),0)

#thresholding
#thresh = cv2.adaptiveThreshold(blur,  255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,9) 
ret,thresh = cv2.threshold(blur,110,255,cv2.THRESH_BINARY)
cv2.imshow('Thresholded',thresh)
cv2.waitKey(0)

#erosion and dilation
kernel = np.ones((8,2),np.uint8)#3,2 and 8,5
thresh = cv2.dilate(thresh,kernel,iterations = 4)
cv2.imshow('Dilated',thresh)
cv2.waitKey(0)




#################      Now Using MSER        ###################
mser = cv2.MSER_create()
regions = mser.detectRegions(thresh)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
cv2.polylines(im3, hulls, 3, (0,255,0)) 
cv2.imshow('norm',im3)
key = cv2.waitKey(0)


#################      Now finding Contours         ###################
_,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
samples =  np.empty((0,100))
responses = []
keys = [i for i in range(48,58)]

#validation function for the rectangle
def validate(cnt):    
    rect=cv2.minAreaRect(cnt)  
    box=cv2.boxPoints(rect) 
    box=np.int0(box)  
    output=False
    width=rect[1][0]
    height=rect[1][1]
    if ((width!=0) & (height!=0)):
        if (((height/width>3) & (height>width)) | ((width/height>3) & (width>height))):
            if((height*width<16000) & (height*width>30)): 
                output=True
    return output
for cnt in contours:
    if validate(cnt):
        rect=cv2.minAreaRect(cnt)  
        box=cv2.boxPoints(rect) 
        box=np.int0(box)  
        cv2.drawContours(im4, [box], 0, (0,255,0),2)           
             
            
cv2.imshow('norm',im4)
key = cv2.waitKey(0)
if key == 27:  # (escape to quit)
	sys.exit()
if key in keys:
    responses.append(int(chr(key)))
    sample = roismall.reshape((1,100))
    samples = np.append(samples,sample,0)
