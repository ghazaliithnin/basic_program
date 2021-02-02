# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:16:51 2020

@author: Ghazali
"""
import cv2
#import numpy as np 
import concurrent.futures
import multiprocessing

def display_video(vid,writer):

    print("wew")
    cap = cv2.VideoCapture(vid)
    print(writer)



    while True:
        
        ret, frames = cap.read()
        writer.write(frames)
        if ret is False:
            print("Video Finished")
            break
        
        cv2.imshow(str(cap),frames)
        
        #cv2.waitKey(30)
        key = cv2.waitKey(30)
        if key ==27:
            cap.release()
            cv2.destroyAllWindows()
            break
            
    
    cap.release()
    writer.release()
    #cv2.destroyAllWindows()
    #return vid, frames


def main():
    print("Running Main script")
    vids =[0,1]
    #writer = cv2.VideoWriter("recording_"".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))
    writer = None
    with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        
        for vid in vids:
            if vid==vids[0]:
                writer = cv2.VideoWriter("recording_in.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))
                executor.submit(display_video,vid,writer,)
                
            elif vid==vids[1]:
                writer = cv2.VideoWriter("recording_out.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))
                executor.submit(display_video,vid,writer,)
        
            print("Running = ",vid)


    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
