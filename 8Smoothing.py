import cv2 
import numpy as np

#in last tut, we had a lot of noise around
#so we need to have some way to remove noise


cap = cv2.VideoCapture(0)
#we can use an image rather than a video

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150,150,50] )
	upper_red = np.array([180,255,150])
	

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)
	
	#1
	kernel = np.ones((15,15), np.float32)/225 #the number is product of dim of matrix ie 15 * 15
	# we lost clearity, so it's not the best way
	smoothed = cv2.filter2D(res, -1, kernel)
	
	#2
	#we' ll use gaussian blur
	blur = cv2.GaussianBlur(res, (15,15), 0)
	
	#3
	#we'll use median blur
	median = cv2.medianBlur(res, 15)
	
	#4
	# we'll use bilateral blur
	bilateral = cv2.bilateralFilter(res, 15, 75, 75)
	
	cv2.imshow('frame', frame)
	#cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	#1
	#cv2.imshow('smoothed', smoothed)
	#2
	#cv2.imshow('blur', blur)
	#3
	#cv2.imshow('mdeian', median)
	#4
	cv2.imshow('bilateral', bilateral)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()
	