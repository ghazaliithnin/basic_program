import cv2
from imutils.video import VideoStream
import numpy as np
from contextlib import suppress

vs = VideoStream("rtsp://192.168.1.209:554/media/video1").start() # LAN Switch


count=0
#
while True:

    frame = vs.read()
    if type(frame) !=np.ndarray:
        print("Video lost connection/ no video")
        #vs.stop()
        with suppress(Exception):
            count=count+1
            print("count = ",count)
            
            if count > 100000:
                count=0
                vs = VideoStream("rtsp://192.168.1.209:554/media/video1").start()
                continue
            
        # print("count = ",count)
        # if count==100:
        #     continue

    with suppress(Exception):
        cv2.imshow('frame',frame)

        if cv2.waitKey(1)&0xFF ==ord('q'):
            break

vs.stop()
cv2.destroyAllWindows()
