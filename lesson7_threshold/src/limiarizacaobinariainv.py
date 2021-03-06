import cv2
import numpy as np

# Carrega a imagem na escala cinza 
image = cv2.imread('../img/gradient.jpg',0)
cv2.imshow('Original', image)

# Valores abaixo de 127 irao para 1 (branco) o resto 0 (preto)
ret,thresh2 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('1 Limiarizacao Binaria Invertida', thresh2)

cv2.imwrite('../img/limiarizacaobinariainv.jpg', thresh2)

cv2.waitKey(0) 
cv2.destroyAllWindows()