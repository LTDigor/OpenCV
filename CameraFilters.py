import cv2
import numpy as np

cap = cv2.VideoCapture(0)


# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    row,col,ch= frame.shape

    gauss = np.random.normal(0,100.,(row,col,ch))    
##    gauss = gauss.reshape(row,col,ch)
    noisy = frame + cv2.max(0,gauss)
    noisy = np.array(noisy,dtype = 'uint8')

    cv2.namedWindow('Noisy Image',cv2.WINDOW_NORMAL)
    cv2.imshow('Noisy Image', noisy)

    framefilered1 = cv2.GaussianBlur(noisy,(11, 11),2)
    cv2.namedWindow('Gaussian Blur',cv2.WINDOW_NORMAL)
    cv2.imshow('Gaussian Blur', framefilered1)


    framefilered2 = cv2.medianBlur( noisy, 7)         
    cv2.namedWindow('Median Blur',cv2.WINDOW_NORMAL)
    cv2.imshow('Median Blur', framefilered2)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
