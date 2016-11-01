import cv2
import numpy as np

img_bgr = cv2.imread('Template_Matching_1.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('Template_Matching_2.jpg', 0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.787

loc = np.where(res >= threshold)

# zip() : Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables
for pt in zip(*loc[::-1]): 
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)
    
cv2.imshow('detected', img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()

