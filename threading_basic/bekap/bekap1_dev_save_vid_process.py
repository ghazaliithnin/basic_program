# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:16:51 2020

@author: Ghazali
"""
import cv2
#import numpy as np 
import concurrent.futures
import multiprocessing

def display_video(vid):
    #count=0
    print("wew")
    cap = cv2.VideoCapture(vid)
    #print(count)
    writer = cv2.VideoWriter("recording_"+vid+".mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))
    #writer =cv2.VideoWriter("recording_" +count, cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))
    #count = count + 1
    while True:
        ret, frames = cap.read()
        
        if ret is False:
            print("Video Finished")
            break
        
        cv2.imshow(str(cap),frames)
        writer.write(frames)
        #cv2.waitKey(30)
        key = cv2.waitKey(30)
        if key ==27:
            cap.release()
            cv2.destroyAllWindows()
            break
            

    cap.release()
    writer.release()
    #cv2.destroyAllWindows()
    return vid, frames

def save_video(vid,frames):
    writer = cv2.VideoWriter("recording_"+vid, cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))
    writer.write(frames)

def main():
    print("Running Main script")
    #vids =["output2.mp4","output3.mp4"]
    #vids =["0","output3.mp4"]
    #vids =[0,"output3.mp4"]
    vids =[0,1]
    
    
    
    #width, height, n_frames = 640, 480, 30 # 30 frames, resolution 640, 480
    #width, height = 640, 480 # 30 frames, resolution 640, 480
    
    #input_filename1 = vids[0]
    #input_filename2 = vids[1]
    
    # synthethic_out1 = cv2.VideoWriter("record_1.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (width, height))
    # synthethic_out1.write(vids)

    # synthethic_out2 = cv2.VideoWriter("record_2.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (width,height))
    # synthethic_out2.write(vids)
        
    #display_video(vids)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        #for vid in executor.map(display_video, vids):
            #print(vid)
        for vid in vids:
            # if vid == "0":
            #     vid=int(vid)
            #     print(type(vid))
            #
            executor.submit(display_video,vid)
        #executor.map(display_video,vid)
            
            #executor.submit(save_video,(vid,frames))
            
            print("Running = ",vid)
            

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    
    
        
