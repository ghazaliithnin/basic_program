#import urllib
import urllib.request
import cv2
import numpy as np

#url='http://192.168.0.103:8080/shot.jpg'
#url="rtsp://admin:kayuwood@192.168.1.46/live1.sdp"
url ="tcp://192.168.1.46:554"
#url="http://admin:kayuwood@192.168.1.46/dms.jpg"

while True:
    
    #imgResp=urllib.urlopen(url)
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # all the opencv processing is done here
    cv2.imshow('test',img)
    if ord('q')==cv2.waitKey(10):
        exit(0)

