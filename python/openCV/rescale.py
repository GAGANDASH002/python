import cv2
import numpy as np

img =cv2.imread('Photos/tiger.jpg')
print(img.shape)#gives shape of image

imgResize= cv2.resize(img,(100,200))

imgCropped = img[0:100,100:200] #takes range of coordinates for height and then width to crop image

cv2.imshow("Tiger",img)
cv2.imshow("Tiger",imgResize)
cv2.imshow("Tiger",imgCropped)

cv2.waitKey(0)