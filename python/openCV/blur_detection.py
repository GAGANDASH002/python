import cv2
import numpy as np

img = cv2.imread("Photos/blur.jpg",cv2.IMREAD_GRAYSCALE)

# Helps to find edges
laplacian_var = cv2.Laplacian(img,cv2.CV_64F).var()

# lower the value lesser the sharpness of the image
print(laplacian_var)

cv2.imshow("Img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()