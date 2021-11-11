import cv2
import numpy as np

imgName = r"src/maxresdefault.jpg"
img = cv2.imread(imgName)

row,col,channel = img.shape
gauss = np.random.normal(0,100.,(row,col,channel))
noisy = img + cv2.max(0,gauss)
noisy = np.array(noisy,dtype = 'uint8')

cv2.namedWindow('Gauss Noisy Image',cv2.WINDOW_NORMAL)
cv2.imshow('Gauss Noisy Image', noisy)

imgFilered1 = cv2.GaussianBlur(noisy,(11, 11),2)
cv2.namedWindow('Gaussian Blur',cv2.WINDOW_NORMAL)
cv2.imshow('Gaussian Blur', imgFilered1)

imgFilered2 = cv2.medianBlur( noisy, 7)         
cv2.namedWindow('Median Blur',cv2.WINDOW_NORMAL)
cv2.imshow('Median Blur', imgFilered2)

imgFilered2 = cv2.bilateralFilter(noisy,15,255.,255.)         
cv2.namedWindow('vdfe',cv2.WINDOW_NORMAL)
cv2.imshow('vdfe', imgFilered2)

cv2.waitKey(0)
cv2.destroyAllWindows()
