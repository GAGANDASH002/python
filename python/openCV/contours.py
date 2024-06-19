import cv2
import numpy as np

path="Photos/shape.jpg"
img=cv2.imread(path)
imgContour=img.copy()

def getContours(img): 
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)#RETR_EXTERNAL:finds outer contours
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)#approximate number of corner points
            print(len(approx))
            objCor=len(approx) 
            x , y , w , h =cv2.boundingRect(approx)
            if objCor==3:
                objectType="Triangle"
            elif objCor==4:
                aspectRatio=w/float(h)
                if aspectRatio>0.95 and aspectRatio<1.05:
                    objectType="Square"
                else:
                    objectType="Rectangle"
            elif objCor>4:
                objectType="Circle"
            else:
                objectType="None"

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),3)

           

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny=cv2.Canny(imgBlur,50,50)
getContours(imgCanny)


cv2.imshow("Contour",imgContour)

cv2.imshow("Original",img)
cv2.imshow("GrayScale",imgGray) 
cv2.imshow("Blur",imgBlur) 
cv2.imshow("Canny",imgCanny) 



cv2.waitKey(0)