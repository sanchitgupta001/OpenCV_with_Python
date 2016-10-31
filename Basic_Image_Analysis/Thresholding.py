import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')

# Threshold all pixels with values greater than 12 will be assigned 255
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
# Above threshold is being applied to the colored image as such before converting it to grayscale

# Below threshold is being applied to the grayscale image after converting original image to grayscale
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

# Adaptive Threshold : the algorithm calculate the threshold for a small regions of the image. 
# So we get different thresholds for different regions of the same image and it gives us better results for images with varying illumination.
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
# It has three ‘special’ input params and only one output argument.
# Adaptive Method - It decides how thresholding value is calculated.
# cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
# Block Size - It decides the size of neighbourhood area.(Should be odd)
# C - It is just a constant which is subtracted from the mean or weighted mean calculated.

#Otsu Threshold
retval3, otsu = cv2.threshold(grayscaled,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#cv2.imshow('original', img)
#cv2.imshow('threshold', threshold)
#cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus',gaus)
#cv2.imshow('otsu', otsu)
#print(retval3)

cv2.waitKey(0)
cv2.destroyAllWindows()