import cv2
import numpy as np

def rotate(img, angle):
    rows, cols, channels = img.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1.0)
    rotated_image = cv2.warpAffine(img, M, (cols, rows))
    return rotated_image

imgName = r"src/maxresdefault.jpg"
angle = 47
img = cv2.imread(imgName)

cv2.namedWindow("My img", cv2.WINDOW_NORMAL)
cv2.imshow("My img", img)

dst = rotate(img, angle)
cv2.namedWindow("Rotated", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated", dst)

dst1 = rotate(dst, -angle)
cv2.namedWindow("Rotated1", cv2.WINDOW_NORMAL)
cv2.imshow("Rotated1", dst1)

dif = 10*np.abs(cv2.subtract(img, dst1))
cv2.namedWindow("dif", cv2.WINDOW_NORMAL)
cv2.imshow("dif", dif)

cv2.waitKey(0)
cv2.destroyAllWindows()
