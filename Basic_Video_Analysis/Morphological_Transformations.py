import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    # hsv : Hue saturation Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    
    # For detecting red value(Object)
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,150])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)       
    
    kernel = np.ones((5,5), np.uint8)
    
    # Erosion
    erosion = cv2.erode(mask, kernel, iterations = 1)
    #Dilation
    dilation = cv2.dilate(mask, kernel, iterations = 1)
    # Opening : Removes False +ve from the background
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # Closing : Removes False +ve within the object
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    #cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
    
cv2.destroyAllWindows()
cap.release()    