import cv2
import numpy as np
 
cropping = False
 
x_start, y_start, x_end, y_end = 0, 0, 0, 0

cap = cv2.VideoCapture(1)

ret, image = cap.read()

oriImage = image.copy()
 
 
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping
 
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
 
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
 
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
 
        refPoint = [(x_start, y_start), (x_end, y_end)]
        print("refpoint = ",refPoint)

 
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)
 
while True:
 
    i = image.copy()
    cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)

 
 
    cv2.imshow("image", image)
    cv2.imshow("imagedraw", i)
 

 
    cv2.waitKey(1)
    
    if cv2.waitKey(1)&0xFF ==ord('q'):
      break
    
 
# close all open windows
cap.release()
cv2.destroyAllWindows()
