#Lo bordes contienen una alta frecuencia, 
#por lo que para obtenerlos es similar a aplicar un filtro pasa altos
#funcion que utiliza Sobel Filters
import cv2
import numpy as np

img = cv2.imread('images/figuras.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

sobel_horizontal_1 = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


cv2.imshow('Original', img)
cv2.imshow('Sobel horizontal 1', sobel_horizontal_1)
cv2.imshow('Sobel vertical', sobel_vertical)


cv2.waitKey()
