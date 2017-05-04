

#Para cambiar el punto del efecto de la region centro se necesita
#construir un kernel Gaussian mas grande y asegurarse que el pico coincida con la region interesada 
import cv2
import numpy as np

img = cv2.imread('images/ia.jpg')
rows, cols = img.shape[:2]

# Shifting the focus
kernel_x = cv2.getGaussianKernel(int(1.5*cols),200)
kernel_y = cv2.getGaussianKernel(int(1.5*rows),200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
mask = mask[int(0.5*rows):, int(0.5*cols):]
output = np.copy(img)

for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Input', img)
cv2.imshow('Vignette with shifted focus', output)


cv2.waitKey()
