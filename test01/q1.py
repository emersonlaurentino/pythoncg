import cv2
import numpy as np

image = cv2.imread('../img/apple.jpg', 0)
cv2.imshow('Original', image)

ret,th1 = cv2.threshold(image, 242, 255, cv2.THRESH_BINARY)

cv2.imshow('LB', th1)
cv2.imwrite('../img/lb.jpg', th1)

cv2.waitKey(0) 
cv2.destroyAllWindows()
