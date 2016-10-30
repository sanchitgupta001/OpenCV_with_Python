import cv2
import numpy as np

cap = cv2.VideoCapture(0) # Number indicates the webcam number
# FourCC is a 4-byte code used to specify the video codec(Coder - Decoder)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    # ret : True/False, frame : Video frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # OpenCV stores image in BGR format instead of RGB
    
    # Saving Video
    out.write(frame)
    
    # Displaying frames(Video)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    # Here, 2 frames will be displayed. Colored and Grayscale converted frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # Exits if 'q' is pressed
        break
    
    
cap.release()
out.release()
cv2.destroyAllWindows()    