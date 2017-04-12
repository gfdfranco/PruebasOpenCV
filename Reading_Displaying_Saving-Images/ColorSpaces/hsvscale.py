#Sirve para matiz, saturacion y valores
import cv2
img=cv2.imread("../images/ia2.jpg")
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("imagen normal",img)
cv2.imshow("imagen HSV",hsv_img)
#diferentes canales por separado
cv2.imshow("H CHANNEL",hsv_img[:,:,0])
cv2.imshow("S CHANNEL",hsv_img[:,:,1])
cv2.imshow("V CHANNEL",hsv_img[:,:,2])
cv2.waitKey()