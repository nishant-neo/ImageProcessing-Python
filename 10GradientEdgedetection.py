import cv2 
import numpy as np

cap = cv2.VideoCapture(0)
#An image gradient is a directional change in the intensity or color in an image. 
#Image gradients may be used to extract information from images.
#we can use an image rather than a video
while True:
	_, frame = cap.read()
	
	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	#ksize is the kernel size
	#You can specify the direction of derivatives to be taken, vertical or horizontal (by the arguments, yorder and xorder 
	#respectively). You can also specify the size of kernel by the argument ksize.
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1 , 0, ksize = 5 )
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0 , 1, ksize = 5 )
	# these gradients can be used to detect edges
	# but we have built-in edge detectors
	
	#First argument is our input image. Second and third arguments are our minVal and maxVal respectively. 
	#Third argument is aperture_size. It is the size of Sobel kernel used for find image gradients. By default it is 3. 
	#Last argument is L2gradient which specifies the equation for finding gradient magnitude. 
	#If it is True, it uses the equation mentioned above which is more accurate, otherwise it uses this function: Edge\_Gradient \; (G) = |G_x| + |G_y|. By default, it is False.
	edges = cv2.Canny(frame, 100, 200)
	
	
	cv2.imshow('original', frame)
	cv2.imshow('laplacian',laplacian)
	cv2.imshow('sobelx', sobelx)
	cv2.imshow('sobely', sobely)
	cv2.imshow('edges', edges)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
		
cv2.destroyAllWindows()
cap.release()
"""
	In our last example, output datatype is cv2.CV_8U or np.uint8. But there is a slight problem with that. Black-to-White 
	transition is taken as Positive slope (it has a positive value) while White-to-Black transition is taken 
	as a Negative slope (It has negative value). So when you convert data to np.uint8, all negative slopes are made zero. 
	In simple words, you miss that edge. If you want to detect both edges, better option is to keep the output datatype to 
	some higher forms, like cv2.CV_16S, cv2.CV_64F etc, take its absolute value and then convert back to cv2.CV_8U. 
	Below code demonstrates this procedure for a horizontal Sobel filter and difference in results.
"""