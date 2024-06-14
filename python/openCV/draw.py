import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)#takes height,width and 3 color channels i.e BGR and unsigned integers of 8 bits i.e 0-255
img[:]=255,0,0 #makes whole image blue 
# : means for whole image ( a range can also be defined within an image that needs to be colored )

cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)#creates a line 
#img.shape[1]=width of image        img.shape[0]=height of image


cv.rectangle(img,(0,0),(250,350),(234,10,100),cv.FILLED)#creates rectangle

cv.circle(img,(400,50),30,(255,255,0),5)#creates circle - centre,radius,colour,thickness

cv.putText(img,"OPENCV",(300,100),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)#creates text


cv.imshow("image",img)

cv.waitKey(0)