#Sirve para sobresaltar los bordes de una imagen que no es nitida
#Se puede sobresaltar la parte superior o inferior de una imagen,
#la desventaja es que la imagen se ve mejorada artificialmente.
#Para que la imagen luzca mas natural y resaltar los bordes se puede utilizar
#un filtro para mejorar los bordes utilizando  Gaussian Kernel

import cv2
import numpy as np

img = cv2.imread('images/ia.jpg')
cv2.imshow('Original', img)

# Sharpening
kernel_sharpen_1 = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
kernel_sharpen_2 = np.array([[1,1,1], [1,-7,1], [1,1,1]])
kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1], 
                             [-1,2,2,2,-1], 
                             [-1,2,8,2,-1],
                             [-1,2,2,2,-1],
                             [-1,-1,-1,-1,-1]]) / 8.0
output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)

cv2.imshow('Sharpening', output_1)
cv2.imshow('Excessive Sharpening', output_2)
cv2.imshow('Edge Enhancement', output_3)
cv2.waitKey()