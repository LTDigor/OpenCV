import cv2
import numpy as np

imgName = r"src/maxresdefault.jpg"
img1 = cv2.imread(imgName)

gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

Gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
Gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)

##Gx = cv2.Scharr(gray, cv2.CV_32F, 1, 0)
##Gy = cv2.Scharr(gray, cv2.CV_32F, 0, 1)

##GGx = cv2.min(255, abs(Gx))
##GGx = GGx.astype(np.uint8)
##cv2.namedWindow("GGx", cv2.WINDOW_NORMAL)
##cv2.imshow("GGx", GGx)
##
##GGy = cv2.min(255, abs(Gy))
##GGy = GGy.astype(np.uint8)
##cv2.namedWindow("GGy", cv2.WINDOW_NORMAL)
##cv2.imshow("GGy", GGy)

G = abs(Gx) + abs(Gy)
G = cv2.min(255, G)
G = G.astype(np.uint8)
cv2.namedWindow("Sobel", cv2.WINDOW_NORMAL)
cv2.imshow("Sobel", G)

canny = cv2.Canny(gray, 100, 200)
cv2.namedWindow("canny", cv2.WINDOW_NORMAL)
cv2.imshow("canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
