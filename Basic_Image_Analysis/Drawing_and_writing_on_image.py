import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150, 150), (255,255,255), 15)
# Arguments : Image, starting point of line, end point of line, BGR , linewidth

cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
# Arguments : Image, left top point, right bottom point, BGR, linewidth

cv2.circle(img, (100,63), 55, (0,0,255), -1)
# Arguments : Image, center coordinate, radius, BGR, -1 for filling circle

pts = np.array([[10,20],[30,40],[80,90],[50,60]], np.int32)
#pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0,255,255), 5)
# Arguments : Image, Coordinates, Whether to connect starting and ending point, BGR, Linewidth

# Writing Text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Watch', (40,130), font, 1, (200,255,255), 2, cv2.LINE_AA)
# Arguments : Image, Text to write, Starting point, font, font size, BGR, Thickness, Line Type

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
