import cv2
img=cv2.imread("../images/ia.jpg")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("scala de gris",img_gray)
cv2.waitKey()