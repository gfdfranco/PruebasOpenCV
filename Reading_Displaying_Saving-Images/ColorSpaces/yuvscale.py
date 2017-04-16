#SIRVE PARA FILTAR LUMINOSIDADES, INTENSIDADES DE LUZ Y U/V CHANNELS
import cv2
img=cv2.imread("images/ia2.jpg")
yuv_img=cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
cv2.imshow("imagen normal",img)
cv2.imshow("imagen YUV",yuv_img)
#diferentes canales por separado
cv2.imshow("Y CHANNEL",yuv_img[:,:,0])
cv2.imshow("U CHANNEL",yuv_img[:,:,1])
cv2.imshow("V CHANNEL",yuv_img[:,:,2])
cv2.waitKey()