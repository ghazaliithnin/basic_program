# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:16:51 2020

@author: Ghazali
"""
import cv2
import numpy as np 
import concurrent.futures

def display_video(vid):
    cap = cv2.VideoCapture(vid)
    
    while True:
        ret, frames = cap.read()
        
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
    #cv2.destroyAllWindows()
    return vid

def main():
    print("Running Main script")
    #vids =["output2.mp4","output3.mp4"]
    vids =["0","output3.mp4"]
    vids =[0,"output3.mp4"]
    
    
    
    width, height, n_frames = 640, 480, 30 # 30 frames, resolution 640, 480
    
    #input_filename1 = vids[0]
    #input_filename2 = vids[1]
    
    synthethic_out1 = cv2.VideoWriter("out_1.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (width, height))
    for i1 in range(n_frames):
        img1 = np.full((height, width,3),60, np.uint8)
        cv2.putText(img1, str(i1+1), (width//2-100*len(str(i1+1)), height//2+100), cv2.FONT_HERSHEY_DUPLEX, 10, (30, 255, 30), 20)  # Green number
        synthethic_out1.write(img1)
        
    synthethic_out2 = cv2.VideoWriter("out_2.mp4", cv2.VideoWriter_fourcc(*'mp4v'), 25, (width,height))
    for i2 in range(n_frames):
        img2 = np.full((height, width,3),60, np.uint8)
        cv2.putText(img2, str(i2+1), (width//2-100*len(str(i2+1)), height//2+100), cv2.FONT_HERSHEY_DUPLEX, 10, (30, 255, 30), 20)  # Green number
        synthethic_out2.write(img2)
        
    #display_video(vids)
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=cv2.getNumberOfCPUs()) as executor:
        #for vid in executor.map(display_video, vids):
            #print(vid)
        for vid in vids:
            # if vid == "0":
            #     vid=int(vid)
            #     print(type(vid))
            executor.submit(display_video,vid)
            print("Running = ",vid)
            

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    
    
        
