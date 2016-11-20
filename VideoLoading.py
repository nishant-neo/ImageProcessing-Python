import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#for saving the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

#for viewing frames
while True:
	ret, frame = cap.read()
	#converting the colored video to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#writing the video's frame
	out.write(frame)
	#displaying the colored image
	cv2.imshow('frame', frame)
	#displaying the grayscale img
	cv2.imshow('gray', gray)
	
	#setting a condition to end the stream
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		

cap.release()
out.release()
cv2.destroyAllWindows()
	
	