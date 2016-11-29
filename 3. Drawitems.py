import numpy as np
import cv2

img = cv2.imread('im.jpg', cv2.IMREAD_COLOR)

#for drawing a line
cv2.line( img, (0,0), (150,150), (255,255,255), 15)

#for drwaing a rectangle
#img name, point where im, dimension, color, thickness
cv2.rectangle(img, (80,350), (300,150), (0,255,0), 3)

#for drawing circle
cv2.circle( img, (100, 63), 55, (0,0,255), -1)

#for drawing polylines
#the array of the points
pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
#opencv will take those points and join them
#reshapes the array into 1/2
#pts = pts.reshape((-1,1,2))
#True/false if we want to join the first point with the last point in  polygon
cv2.polylines(img, [pts], True, (0,255,255), 5)

#writing text
font = cv2.FONT_HERSHEY_SIMPLEX
# image, text,  location, font type, size, color, thickness, 
cv2.putText(img, 'Hey! NISHANT', (0,430), font, 3, (200,255,255), 1, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

