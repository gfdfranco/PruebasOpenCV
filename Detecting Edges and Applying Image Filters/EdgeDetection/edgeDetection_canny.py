#se puede utilizar canny para bordes que tiene mucho mejor calidad que laplacian
#En canny si se aumentan los limites los bordes mas debiles seran ignorados
import cv2
import numpy as np

img = cv2.imread('images/ia.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

laplacian = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 50, 240)

cv2.imshow('Original', img)
cv2.imshow('Laplacian', laplacian)
cv2.imshow('Canny', canny)

cv2.waitKey()
