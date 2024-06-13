import cv2 
import numpy as np

img=cv2.imread("Photos/Tiger.jpg")
imgHor=np.hstack((img,img))#Numpy function that joins images horizontally
imgVer=np.vstack((img,img))#joins vertically

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)

cv2.waitKey(0)