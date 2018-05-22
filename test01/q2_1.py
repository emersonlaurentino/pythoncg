import cv2
import numpy as np

img = np.zeros((140, 200, 3), np.uint8)

diamond = np.array([[0, 70], [0, 140], [200, 140], [100, 0]], np.int32)

cv2.rectangle(img, (0,0), (200, 140),(62, 184, 22), -1)
cv2.fillConvexPoly(img, diamond, (31, 255, 255))
cv2.circle(img,(100,70), 35, (184,22,81), -1)

cv2.imshow('Brazil', img)

cv2.waitKey(0) 
cv2.destroyAllWindows()
