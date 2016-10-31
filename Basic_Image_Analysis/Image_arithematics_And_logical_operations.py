import cv2
import numpy as np

img1 = cv2.imread('image1.png')
#img2 = cv2.imread('image2.png')

# Note :For addition operations on two images, they should have same resolution

# Following add simply merges two images
#add = img1 + img2

# Following version of add function adds the pixel values of 2 images 
# and then forms the new image with pixel values as sum of respective pixels of 2 images
#add = cv2.add(img1, img2)

#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# Arguments : First Image, Weight of first image, Second Image, weight of second image, Gamma factor

img3 = cv2.imread('python_logo.png')

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img2gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
# Arguments : GrayScale Image, Threshold Value, Value to be assigned if value is
#greater than threshold value, style of thresholding(Here, THRESH_BINARY_INV denotes inverse of what has been assigned)
# ret has same value as the threshold value we used, if we don't use otsu's binarization

mask_inv = cv2.bitwise_not(mask) # For black portion of the mask image

# Stores background of image1 for roi with mask = mask_inv
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Stores foreground of image3 with mask = mask
img3_fg = cv2.bitwise_and(img3, img3, mask = mask)

# Merges two images img1_bg and img3_fg
dst = cv2.add(img1_bg, img3_fg)

# Store the pixel values of merged image in the image1
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
#cv2.imshow('mask_inv', mask_inv)
#cv2.imshow('img1_bg', img1_bg)
#cv2.imshow('img3_bg', img3_fg)
#cv2.imshow('dst', dst)

#cv2.imshow('mask', mask)

#cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()

