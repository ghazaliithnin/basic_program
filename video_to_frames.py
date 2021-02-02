# Gaz edit 20 july 20

# added args

import cv2
import os
import argparse

# input args = filename, video format

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input", type=str,default="walking_01",
	help="input video filename")
ap.add_argument("-f", "--format", type=str,default=".avi",
	help="video format, e.g(.avi), please add (dot)")

args = vars(ap.parse_args())

#filename = "3006_1715p"
filename = (args["input"])
print(filename)

os.mkdir("frames_"+filename)
cap = cv2.VideoCapture(filename+(args["format"]))
#cap = cv2.VideoCapture(filename+".avi")


count=0
framecount = 0
while True:
    ret, frame = cap.read()


    if ret == True:
        #frame = cv2.resize(frame,(720,480)) # original width = 3840, height= 2160
        #cv2.imshow("Frame", frame)
        #framecount += 30 # 30 fps, this advances One Seconds
        # 10 fps
        #cap.set(1, framecount) #skip frame setting

        cv2.imwrite("frames_"+filename+"//"+filename+"_"+str(count)+".jpg",frame)
        count = count + 1


    elif ret == False:
        print("completed")
        break



    #key = cv2.waitKey(1)
    #if key ==27:
        #print("Stopped, Escape Key Pressed")
        #break

cap.release()
#cv2.destroyAllWindows()



