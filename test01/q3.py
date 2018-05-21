import cv2
import numpy as np
from matplotlib import pyplot as plot

image = cv2.imread('../img/predio.jpg')
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

image2[:,:,0] = cv2.equalizeHist(image2[:,:,0])

imageEqualizada = cv2.cvtColor(image2, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', image)
cv2.imshow('Histogram equalized', imageEqualizada)

plot.hist(image.ravel(),256,[0,256])
plot.hist(imageEqualizada.ravel(),256,[0,256])
plot.show()

cv2.waitKey(0) 
cv2.destroyAllWindows()
