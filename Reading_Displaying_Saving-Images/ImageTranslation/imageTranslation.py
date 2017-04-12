import cv2
import numpy as np 

img=cv2.imread('../images/ia2.jpg')
#obtener numero de columnas y filas de la imagen
num_rows,num_cols=img.shape[:2]
#matriz de traslacion de la imagen que empiece en el punto x=70,y=110
translation_matrix=np.float32([[1,0,70],[0,1,110]])
img_translation=cv2.warpAffine(img,translation_matrix,(num_cols+250,num_rows+110))
#la imagen empieza abajo y las columnas y filas se extienden 70 y 110
cv2.imshow('ventana 1', img_translation)

#la imagen sube y en el punto 0,0 queda la imagen en la coordenada x=500,y=500
translation_matrix=np.float32([[1,0,-500],[0,1,-500]])
img_translation=cv2.warpAffine(img,translation_matrix,(num_cols-500,num_rows-500))
#se ve que la imagen se recorta para que sea ,as chica y solo aparezca la imagen
cv2.imshow('ventana 2', img_translation)
cv2.waitKey()