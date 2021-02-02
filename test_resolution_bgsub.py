import cv2
import time
#cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.1.46/live3.sdp")
#cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.0.20/live1.sdp")
#cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.1.46/live1.sdp")
#cap = cv2.VideoCapture("outpy.avi")
cap = cv2.VideoCapture(2)
################
######
#cap.set(3,1280)

#cap.set(4,1024)
##

##############
## Max setting for logitech c922, quite slow
cap.set(3,1920)
cap.set(4,1080)
###

#####
#Wide XGA (WXGA-H) ,Minimum, 720p HDTV 	,1280 × 720 ,16∶9 
#cap.set(3,1280)
#cap.set(4,720)
###

########
# this will resize to 800x600 instead of 720x576
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 576)

##

# this will resize to 800x600 instead of 720x480
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

##

########
#cap.set(3,720)
#cap.set(4,576)
##

time.sleep(2)

cap.set(15, -8.0)
##
while(cap.isOpened()):
    ret, frame = cap.read()
    print("frame size = ",frame.shape)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1)&0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
