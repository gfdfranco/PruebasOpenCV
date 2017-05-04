#Vignette filter basicamente se enfoca en el brillo en un punto especifico de la imagen por lo que 
#las otras partes se ven como descolorido

"""
Para lograr esto se necesita hacer el filtro a cada canal en la imagen usando "Gaussian Kernel".
Opencv tiene una funcion "getGaussianKernel", el segundo parametro de esta funcion es interesante
se basa en la desviacion estandar Gaussian y controla el radio del brillo de la region central.

Una vez que se construye el 2D kernel, se necesita contruir una mascara para normalizar el kernel  y escalarlo.
Este paso es importante por que si no se escala, la imagen sera negra. Esto pasa por que todos los
valores de los  pixeles estaran cercanos a 0 despues de sobreponer la mascara en la imagen entrante.
Despues de esto hacemos iteraciones  con todos los canales de colores y aplicamos la mascara a cada canal.

"""

import cv2
import numpy as np

img = cv2.imread('images/ia.jpg')
rows, cols = img.shape[:2]

#Generando masscara vignette usando  Gaussian Kernel
kernel_x = cv2.getGaussianKernel(cols,150)
kernel_y = cv2.getGaussianKernel(rows,150)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

#Aplicando la mascara a cada canal
for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Original', img)
cv2.imshow('Vignette', output)

cv2.waitKey()


