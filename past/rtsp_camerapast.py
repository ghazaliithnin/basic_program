import cv2

#cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.1.46/live3.sdp")
#cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.0.20/live1.sdp")
cap = cv2.VideoCapture("rtsp://admin:kayuwood@192.168.1.46/live1.sdp")


while(cap.isOpened()):
    ret, frame = cap.read()
    
    frame = cv2.flip(frame,-1)
    #frame = cv2.rotate(frame, cv2.ROTATE_180)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1)&0xFF ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
