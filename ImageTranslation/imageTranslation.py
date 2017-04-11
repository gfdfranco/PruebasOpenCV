import cv2
import numpy as np 
img=cv2.imread('../images/ia.jpg')
num_rows,num_cols=img.shape[:2]

translation_matrix=np.float32([[1,0,70],[0,1,110]])
img_translation=cv2.warpAffine(img,translation_matrix,(num_cols+70,num_rows+110))

translation_matrix=np.float32([[1,0,-30],[0,1,-50]])
img_translation=cv2.warpAffine(img,translation_matrix,(num_cols+70+530,num_rows+110+50))

cv2.imshow('ventana', img_translation)
cv2.waitKey()