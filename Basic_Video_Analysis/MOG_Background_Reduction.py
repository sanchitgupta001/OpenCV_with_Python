# MOG(Mixtur of Gaussians) Background Reduction
# For more info. : http://docs.opencv.org/3.1.0/db/d5c/tutorial_py_bg_subtraction.html
import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4')

#Initialize MOG Background Subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)
    
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()    
