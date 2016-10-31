import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    # For laplacian (To find edges)
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    
    # Sobel operators is a joint Gausssian smoothing plus differentiation operation, so it is more resistant to noise. 
    # We can specify the direction of derivatives to be taken, vertical or horizontal (by the arguments, yorder and xorder respectively). 
    # We can also specify the size of kernel by the argument ksize. 
    # If ksize = -1, a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter.
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    # An image gradient is a directional change in the intensity or color in an image. 
    
    # Edge Detector
    edges = cv2.Canny(frame, 100, 200)
    # Lesser parameter value for Canny edge detector, more is the noise
    
    
    cv2.imshow('original', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()    