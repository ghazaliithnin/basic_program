import cv2
import numpy as np
 
cropping = False
 
x_start, y_start, x_end, y_end = 0, 0, 0, 0

# bounding box centre referring to image coordinate
xc=0 # x absolute centre
yc=0 # y absolute centre



cap = cv2.VideoCapture(1)

ret, image = cap.read()

oriImage = image.copy()

iw=int(image.shape[1]) #image width
ih=int(image.shape[0]) # image heightq




 
def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, x_end, y_end, cropping,xc,yc
 
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
        #print("Dot",(x_start,y_start))
        xc = int(iw - (x_end/2))
        yc = int (ih - (y_end/2))
        print(xc)
        print(yc)

 
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_crop)
 
while True:
 
    i = image.copy()
    cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)

    cv2.circle(i, (xc, yc), 3,(0, 255, 0), -1)

    #cv2.circle(i, (x_start, y_start), 1,(0, 255, 0), -1)
    

 
 
    cv2.imshow("image", image)
    cv2.imshow("image", i)
 

 
    cv2.waitKey(1)
    
    if cv2.waitKey(1)&0xFF ==ord('q'):
      break
    
 
# close all open windows
cap.release()
cv2.destroyAllWindows()
