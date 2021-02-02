# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:16:51 2020

@author: Ghazali
"""
import cv2
import numpy as np

def display_video(vid):
    cap = cv2.VideoCapture(vid)
    
    while True:
        ret, frames = cap.read()
        
        if ret is False:
            print("Video Finished")
            break
        
        cv2.imshow(str(cap),frames)
        cv2.waitKey(30)
    cap.release()
    cv2.destroyAllWindows()
    return vid


vid ="output3.avi"

display_video(vid)

