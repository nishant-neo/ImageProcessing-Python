import numpy as np
import cv2

img = cv2.imread("search.png")

#converting from bgr to hsv
hs = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
ht, st, vt = cv2.split(hs)
h, s, v = cv2.split(hs)
s1 = s
#s1.fill(255)


v1 = v
v1.fill(255)
h1 = cv2.cvtColor(cv2.merge([h,s1,v1]), cv2.COLOR_HSV2BGR)





cv2.imshow('Image', img)
#cv2.imwrite('hsv.jpg', hs)
cv2.imwrite('h.jpg', h1)
cv2.imwrite('s.jpg', s)
cv2.imwrite('v.jpg', vt)
cv2.waitKey(0)
cv2.destroyAllWindows()