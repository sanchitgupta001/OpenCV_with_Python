import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
#Other Options:
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0

# Displaying Image using cv2
cv2.imshow('image', img)
cv2.waitKey(0) # Waits for any key to be pressed
cv2.destroyAllWindows()

# Displaying image using Matplotlib
#plt.imshow(img, cmap='gray', interpolation='bicubic')

# Saving modified image
#cv2.imwrite('watchgray.png',img)