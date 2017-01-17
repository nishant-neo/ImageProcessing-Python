import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
#we can use an image rather than a video

# we' ll  use morphological transformation to remove white noise or noise from filters
while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150,150,50] )
	upper_red = np.array([180,255,150])
	
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	kernel = np.ones((5,5), np.uint8)
	
	
	#first 2 MT's are: Erosion & Dilation
	#Erosion: gonna go around and erodes away the noise
	# it'll go around and see if there's any pixel with different value
	#Dilation: opposite of ersion
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)	
	
	
	#opening and closing
	#opening: remove false positives or FP ( remv from backgrnd)
	#removing: remove false negatives or FN
	# FP are the noises in the background
	# FN are the noises in the Hat
	opening = cv2.morphologyEx( mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx( mask, cv2.MORPH_CLOSE, kernel)
	
	#It is the difference between i/p img and opening of the img
	cv2.imshow('Tophat',tophat)
	#It is the differnce between the closing of i/p img and i/p img
	cv2.imshow('frame', frame)
	cv2.imshow('res', res)
	cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()
