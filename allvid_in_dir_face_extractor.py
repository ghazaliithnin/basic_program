import face_recognition
import numpy as np
import cv2
from imutils.video import FileVideoStream
import os

folder_path = "to_process"
out_name = ""
video_list = os.listdir(folder_path)

fourcc = cv2.VideoWriter_fourcc(*'XVID')



for video_file_name in video_list:
    file_path = folder_path + os.path.sep + video_file_name
    print("[INFO] Running Video from " + file_path)
    video_file_name.split(".")[1]  # File Extension Name
    file_name = video_file_name.split(".")[0] # Name of the file for video
    # cap = VideoStream(src=file_path).start()
    cap = FileVideoStream(file_path).start()
    
    # For some reason, doing this flag thing will enable video recorded normally
    # without this flag, video only record first frame
    vid_flag =0
    
    while True:
        frame = cap.read()
        if vid_flag ==0:
            writer = cv2.VideoWriter("done_process\prcsd_"+file_name+".avi",fourcc, 20.0, (frame.shape[1],frame.shape[0]))
            vid_flag=1
            
        if type(frame) != np.ndarray:
            print("Complete "+ file_path)
            break
        
        boxes = face_recognition.face_locations(frame, model="cnn")
        
        if len(boxes)!=0:
            writer.write(frame)

    cap.stop()
    writer.release()