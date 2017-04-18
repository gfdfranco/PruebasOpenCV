import cv2
import numpy as np

img = cv2.imread('../images/ia.jpg')
rows, cols = img.shape[:2]

cv2.imshow('Original', img)


output = cv2.blur(img,(3,3))
cv2.imshow('3x3 filter', output)

output = cv2.blur(img,(5,5))
cv2.imshow('5x5 filter', output)

cv2.waitKey()
