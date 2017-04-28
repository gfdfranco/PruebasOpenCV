#Erosion quita la estructura de pixeles de la capa mas externa
#Dilation agrega pixeles a la estructura de la capa mas externa

import cv2
import numpy as np


# Erosion and dilation
img = cv2.imread('images/img.png',0)
kernel = np.ones((5,5), np.uint8)

#El numero de iteraciones determina que tanto se quiere erode/dilation la imagen dada.
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)
cv2.waitKey()