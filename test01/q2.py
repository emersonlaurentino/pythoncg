import cv2
import numpy as np

heightGreen, widthGreen, colorGreen = 140, 200, "#16B83E"
heightYellow, widthYellow, colorYellow = 140, 200, "#FFE11F"
heightYellow, widthYellow, colorYellow = 140, 200, "#1651B8"
heightYellow, widthYellow, colorYellow = 140, 200, "#FFF"

img = np.zeros((300, 500, 3), np.uint8)

cv2.rectangle(img, (0,0), (500, 300),(22, 184, 62), -1)
cv2.circle(img,(250,150), 100, (255,0,0), -2)

cv2.imshow('Brazil', img)

cv2.waitKey(0) 
cv2.destroyAllWindows()
