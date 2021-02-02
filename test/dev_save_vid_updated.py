# Created on 16 nov 20
# Can also be used to convert video's format

import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str,
  help="path to output video")
ap.add_argument("-o", "--output", type=str,
  help="path to output video")

args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["input"])


#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('output_rtsp2.mp4', fourcc, 20.0, (1280,  720)) # macam sama je


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,-1)
    
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer = cv2.VideoWriter(args["output"], fourcc, 20,
      (frame.shape[1], frame.shape[0]), True)
    #print(frame.shape)
    
    writer.write(frame)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key ==27:
        break

writer.release() 
cap.release()
cv2.destroyAllWindows()



