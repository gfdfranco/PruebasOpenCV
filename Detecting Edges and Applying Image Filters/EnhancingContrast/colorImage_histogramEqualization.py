#Para poder manejar este proceso se recurre al filtro YUV se iguala el canal Y
#y se combina con dos canales para obtener la salida de la imagen.
import cv2
import numpy as np


# Histogram equalization of color images

img = cv2.imread('images/imagen.jpg')

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Color input image', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey()