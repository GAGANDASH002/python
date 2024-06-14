import cv2
import numpy as np

def empty(a):
    pass


path="Photos/Tiger.jpg"


#creating TrackBars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("hue min","TrackBars",0,179,empty)
cv2.createTrackbar("hue max","TrackBars",0,179,empty)
cv2.createTrackbar("sat min","TrackBars",0,255,empty)
cv2.createTrackbar("sat max","TrackBars",255,255,empty)
cv2.createTrackbar("val min","TrackBars",0,255,empty)
cv2.createTrackbar("val max","TrackBars",255,255,empty)

while True:
    img=cv2.imread(path)
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)#converting to HSV image
    h_min=cv2.getTrackbarPos("hue min","TrackBars")
    h_max=cv2.getTrackbarPos("hue max","TrackBars")
    s_min=cv2.getTrackbarPos("sat min","TrackBars")
    s_max=cv2.getTrackbarPos("sat max","TrackBars")
    v_min=cv2.getTrackbarPos("val min","TrackBars")
    v_max=cv2.getTrackbarPos("val max","TrackBars")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])

    #creating mask of original image
    mask=cv2.inRange(imgHSV,lower,upper)

    #creating a new image by adding two images with a mask
    imgResult=cv2.bitwise_and(img,img,mask=mask)


cv2.imshow("Original",img)
cv2.imshow("HSV",imgHSV)
cv2.imshow("mask",mask)
cv2.imshow("ImgResult",imgResult)
cv2.waitKey(0)