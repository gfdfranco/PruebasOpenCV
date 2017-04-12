import cv2
import numpy as np 

#SI se realiza una ampliacion de una imagen es preferible utilizar  una interpolacion LINEAR OR CUBIC
#Cubic interpolacion es mas lenta pero de mayor calidad que una interpolacion LINEAR

img=cv2.imread("../images/ia.jpg")

img_scaled=cv2.resize(img,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LINEAR)
#img_scaled=cv2.resize(img,(450,400),fx=1.2,fy=1.2,interpolation=cv2.INTER_LINEAR)
cv2.imshow("Linear Intepolation",img_scaled)

img_scaled=cv2.resize(img,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_CUBIC)
#img_scaled=cv2.resize(img,(450,400),fx=1.2,fy=1.2,interpolation=cv2.INTER_CUBIC)
cv2.imshow("Cubic Intepolation",img_scaled)

img_scaled=cv2.resize(img,(450,400),interpolation=cv2.INTER_AREA)
cv2.imshow("Skewed size",img_scaled)
cv2.waitKey()