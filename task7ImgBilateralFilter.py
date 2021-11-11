import cv2
import numpy as np

imgName = r'src/maxresdefault.jpg'
img = cv2.imread(imgName)

cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
cv2.imshow('Original image, img)

row,col,channel = img.shape
gauss = np.random.normal(0,100.,(row,col,channel))
noisy = img + cv2.max(0,gauss)
noisy = np.array(noisy,dtype = 'uint8')

imgFilered2 = cv2.bilateralFilter(noisy,15,255.,255.)         
cv2.namedWindow('Bilateral filter',cv2.WINDOW_NORMAL)
cv2.imshow('Bilateral filter', imgFilered2)

cv2.waitKey(0)
cv2.destroyAllWindows()
