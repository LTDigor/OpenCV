import cv2

imgName = r"src/maxresdefault.jpg"
img1 = cv2.imread(imgName)

cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", img1)

b, g, r = cv2.split(img1)

cv2.namedWindow("Blue", cv2.WINDOW_NORMAL)
cv2.imshow("Blue", b)

cv2.namedWindow("Green", cv2.WINDOW_NORMAL)
cv2.imshow("Green", g)

cv2.namedWindow("Red", cv2.WINDOW_NORMAL)
cv2.imshow("Red", r)

img2 = cv2.merge((b, g, r))
cv2.namedWindow("Image2", cv2.WINDOW_NORMAL)
cv2.imshow("Image2", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
