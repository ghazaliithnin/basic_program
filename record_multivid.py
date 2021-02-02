# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 09:16:51 2020

@author: Ghazali
"""

# Must run on main() function to make it works

import cv2
#import numpy as np 
import concurrent.futures
import multiprocessing

def display_video(vid):

    print("Displaying Video " + vid)
    cap = cv2.VideoCapture(vid)

    writer = cv2.VideoWriter("recording_"+vid, cv2.VideoWriter_fourcc(*'mp4v'), 25, (640, 480))

    while True:
        ret, frames = cap.read()
        
        if ret is False:
            print("Video Finished "+vid)
            break
        
        #cv2.imshow(str(cap),frames)
        writer.write(frames)
        # key = cv2.waitKey(30)
        # if key ==27:
        #     cap.release()
        #     cv2.destroyAllWindows()
        #     break
            

    #cap.release()
    writer.release()
    return vid, frames


def main():
    print("Running Main script")
    vids =["output2.mp4","output3.mp4"]

    
    with concurrent.futures.ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:

        for vid in vids:

            executor.submit(display_video,vid)
            #print("Running = ",vid)
            

    #cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
    
    
        
