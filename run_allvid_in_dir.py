import face_recognition
import numpy as np
import cv2
from imutils.video import FileVideoStream
import os

folder_path = "short_videos"
video_list = os.listdir(folder_path)

for video_file_name in video_list:
    file_path = folder_path + os.path.sep + video_file_name
    print("[INFO] Running Video from " + file_path)
    videoExtension = video_file_name.split(".")[1] #probably check first wheter the file video or not
    # cap = VideoStream(src=file_path).start()
    cap = FileVideoStream(file_path).start()
    # cap = cv2.VideoCapture(file_path)
    
    while True:
        frame = cap.read()
        
        if type(frame) != np.ndarray:
            print(type(frame))
            break
        framekosong = frame.copy()
        
        cv2.imshow("frame",frame)
        key = cv2.waitKey(1)& 0xFF
        if key ==ord("q"):
            break
    cv2.destroyAllWindows()
    cap.stop()