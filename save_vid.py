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
#cap = cv2.VideoCapture("test.mp4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter(args["output"], fourcc, 20,
  ((int(cap.get(3))), (int(cap.get(4)))), True)
# writer = cv2.VideoWriter("savetest.avi", fourcc, 20,
#   ((int(cap.get(3))), (int(cap.get(4)))), True)

print(args["input"])
while True:
    ret, frame = cap.read()
    #print(ret)
    
    if ret == False:
        print("Habis")
        break
    
    

    #print(frame.shape)
    
    writer.write(frame)
    # cv2.imshow("Frame", frame)

    # key = cv2.waitKey(1)
    # if key ==27:
    #     break

writer.release() 
cap.release()
#cv2.destroyAllWindows()



