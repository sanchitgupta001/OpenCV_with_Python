import cv2
import numpy as np

img = cv2.imread('corner_detection.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray) # Required for the algorithm

corners = cv2.goodFeaturesToTrack(gray, 65, 0.01, 10)
# Arguments : Image, Number of corners, Quality Level, Minimum possible Euclidean distance between the returned corners
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)# Blue colored circle
    
#cv2.imshow('Corner',img)   
cv2.imwrite('Modified.jpg',img)