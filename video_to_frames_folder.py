# Gaz edit 20 july 20

# added args

import cv2
import os
import argparse

# input args = filename, video format

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input", type=str,default="test",
	help="input video filename")


args = vars(ap.parse_args())


def frame_capture(vid_filename):
    cap = cv2.VideoCapture(vid_filename)
    
    
    count=0
    while True:
        ret, frame = cap.read()
        #print(ret)
    
    
        if ret == True:

            #print("testssss")
            #frame = cv2.resize(frame,(720,480))
            
            dst= gabung+"\\"+filename+"_"+str(count)+".jpg"
            print(dst) # image destination name
            cv2.imwrite(dst,frame)
    
            #cv2.imwrite("frames_"+filename+"//"+filename+"_"+str(count)+".jpg",frame)
            count = count + 1
    
    
        elif ret == False:
            print("completed")
            break
    
    
    
        #key = cv2.waitKey(1)
        #if key ==27:
            #print("Stopped, Escape Key Pressed")
            #break
    
    cap.release()

#filename = "3006_1715p"
foldername = (args["input"])
print(foldername)
list_foldername=os.listdir(foldername)
for index_list,vid_filename in enumerate(list_foldername):
    filename_split=os.path.splitext(vid_filename)
    filename=filename_split[0]
    #gabung=os.path.join(dir_name, vid_filename) # ori
    gabung=os.path.join(foldername, filename)
    vid_dir=os.path.join(foldername, vid_filename)
    os.mkdir(gabung)
    print(vid_dir) # Video File Name
    frame_capture(vid_dir)
    #cap = cv2.VideoCapture(vid_filename)





