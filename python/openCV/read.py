import cv2 as cv
#Reading Images
#img=cv.imread('Photos/tiger.jpg')

#cv.imshow("Tiger",img)

#cv.waitKey(0)

#Reading Videos
capture=cv.VideoCapture('Videos/dog.gif')

while True:
    isTrue, frame=capture.read()
    cv.imshow('Video',frame)#reads video frame by frame

    if cv.waitKey(20) & 0xFF==ord('d'):#ensures video doesn't play indefinitely:stop video when u press 'd' or after 20ms
        break

capture.release()
cv.destroyAllWindows()

