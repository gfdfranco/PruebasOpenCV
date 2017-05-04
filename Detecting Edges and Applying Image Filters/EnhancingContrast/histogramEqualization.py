#Ayuda cuando una imagen tiene poca iluminacion o por el contraste algunas partes son oscuras en la imagen
#HIstogram equalization es aplicable a escalas de grises.

import cv2
import numpy as np

img = cv2.imread('images/imagen.jpg', 0)
histeq = cv2.equalizeHist(img)

cv2.imshow('Input', img)
cv2.imshow('Histogram equalized', histeq)

cv2.waitKey()

