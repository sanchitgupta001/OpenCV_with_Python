# Brute Force Matcher
# For more Info. : http://docs.opencv.org/trunk/dc/dc3/tutorial_py_matcher.html
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('feature_matching_template.jpg',0)
img2 = cv2.imread('feature_matching_image.jpg',0)

 # Initiate ORB(Oriented FAST and Rotated BRIEF) detector
orb = cv2.ORB_create()

 # find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Declaring BruteForce Matcher
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2, matches[:12], None, flags=2) # Draw only for 12 matches
# cv2.imwrite('Matches.jpg',img3)
plt.imshow(img3)
plt.show()