import cv2 
import numpy as np


cap = cv2.VideoCapture(0)
#we can use an image rather than a video

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#hue saturation value :: another way to represent colors
	#we prefer hsv as we can repressent the range with it, plus
	#the three value doesnt represent a clor combination unkike RGB/ BGR
	
	#lower_red = np.array([0,0,0] )
	#upper_red = np.array([255,255,255])
	#this can be any color, here the stream had red hat, so we'll do hit and trial
	# and get our color
	#so we'll use
	lower_red = np.array([150,150,50] )
	upper_red = np.array([180,255,150])
	
	"""
	we can use this to covert the colors too
	dark_red = np.uint8([[[12,22,121]]])
	dark_red = cv2.cvtColor(dark_red, cv2.COLOR_BGR2HSV)
	"""
	
	#here we'll do out natural filters, by hit and trial
	
	# here the mask is basically everything in the range
	mask = cv2.inRange(hsv, lower_red, upper_red)
	#initially everything inside the frame will be in the mask
	
	#so first we took the  mask, it will be 1 where the color is red
	# and 0 otherwise
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()#lets the webcam go
#if havent done, its using the camera  even if we dont display
	