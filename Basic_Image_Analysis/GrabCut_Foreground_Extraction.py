import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('sample_image.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (80, 80, 260, 280)
# Grabcut (For more details : http://docs.opencv.org/3.1.0/d8/d83/tutorial_py_grabcut.html)
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
# No. of iterations = 5
mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()