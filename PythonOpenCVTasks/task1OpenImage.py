from cv2 import cv2

imgName = r'src/maxresdefault.jpg'
img = cv2.imread(imgName)

cv2.namedWindow("My img", cv2.WINDOW_NORMAL)
cv2.imshow('My img', img)

#cv2.imwrite(imgName + "new", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
