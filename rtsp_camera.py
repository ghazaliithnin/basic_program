import cv2

#cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.1.46/live3.sdp")
#cap = cv2.VideoCapture("rtsp://192.168.1.39:554/media/video1") # LAN POE
cap = cv2.VideoCapture("rtsp://192.168.0.104:554/media/video1") # LAN POE
#cap = cv2.VideoCapture("rtsp://192.168.1.37:554/media/video1") # LAN Switch
#cap = cv2.VideoCapture("rtsp://192.168.1.13:554/media/video1") # direct to laptop

#rtsp://IP:rtsp port/media/video1
# rtsp://192.168.1.37:554/media/video1

# http://192.168.1.172/
# http://192.168.1.225/
# http://192.168.1.249/
# http://192.168.1.16/


#coordinate crop (191, 911, 102, 1167)
# coordinate (8, 986, 3, 1843)

while(cap.isOpened()):
    ret, frame = cap.read()
    #roi = frame[8:1960, 3:2663]
    roi = frame[8:986, 3:1843] # cropped
    #cv2.imshow('frame',frame)
    cv2.imshow('roi',roi)
    print("Frame = ",frame.shape)
    print("ROI = ",roi.shape)

    if cv2.waitKey(1)&0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
