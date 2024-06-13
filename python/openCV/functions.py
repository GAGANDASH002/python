import cv2 as cv
import numpy as np

img = cv.imread('Photos/tiger.jpg')
kernel = np.ones((5,5),np.uint8)#5X5 matrix with only ones


imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)#converts an image into grayscale
imgBlur = cv.GaussianBlur(img,(7,7),0)#blurs image
imgCanny = cv.Canny(img,200,300)#gives Canny images(images with edges only)
imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv.erode(imgDialation,kernel,iterations=1)

cv.imshow("Gray image",imgGray)
cv.imshow("Blur image",imgBlur)
cv.imshow("Canny image",imgCanny)
cv.imshow("Dialated image",imgDialation)
cv.imshow("Eroded image",imgEroded)

cv.waitKey(0)