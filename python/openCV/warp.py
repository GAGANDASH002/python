import cv2 
import numpy as np

width,height=250,350
img=cv2.imread("Photos/Tiger.jpg")
pts1=np.float32([[111,219],[287,188],[154,482],[352,440]])#points of part of image that you want to warp
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])#refernce points of original image
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgOut=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Tiger",img)
cv2.imshow("Output",imgOut)

cv2.waitKey(0)
