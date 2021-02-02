#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 15:55:24 2019

@author: sol
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:51:56 2019

#author gaz 30 jun 20
@author: sol
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:44:19 2019

@author: sol
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:16:28 2019

@author: sol
"""

# USAGE
# python recognize_faces_video.py --encodings encodings.pickle
# python recognize_faces_video.py --encodings encodings.pickle --output output/jurassic_park_trailer_output.avi --display 0

# import the necessary packages
from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2
import numpy as np

OFF = 0
ON = 1
DEBUG = OFF


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-e", "--encodings", default = "encodings.pickle",
#	help="path to serialized db of facial encodings")
ap.add_argument("-i", "--input", type=str,default="walking_01.mp4",
	help="path to input video")
ap.add_argument("-o", "--output", type=str,default="testextract.avi",
	help="path to output video")
ap.add_argument("-y", "--display", type=int, default=1,
	help="whether or not to display output frame to screen")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")

ap.add_argument("-r", "--recognizer", default = "recognizer/sgd_frontal/recognizer.sav",
	help="path to model trained to recognize faces")
ap.add_argument("-l", "--le", default = "recognizer/sgd_frontal/le.pickle",
	help="path to label encoder")

args = vars(ap.parse_args())

# load the known faces and embeddings
#print("[INFO] loading encodings...")
#data = pickle.loads(open(args["encodings"], "rb").read())

# initialize the video stream and pointer to output video file, then
# allow the camera sensor to warm up
print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()

#vs = cv2.VideoCapture(0)
#vs = cv2.VideoCapture('rtsp://admin:kayuwood@192.168.1.46/live1.sdp')
#vs = cv2.VideoCapture("in2.mp4")
vs = cv2.VideoCapture(args["input"]) #####
#####################
#####
_, f = vs.read()

#g = cv2.medianBlur(f, 5)
g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)

#g = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)


avg = np.float32(g)

image_area = None
##################
writer = None
time.sleep(2.0)
tolerance = 0.70
flag = 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')


#recognizer = pickle.loads(open(args["recognizer"], "rb").read())
#le = pickle.loads(open(args["le"], "rb").read())

# loop over frames from the video file stream
while True:
	# grab the frame from the threaded video stream
#	_,frame = vs.read()
	ret,frame = vs.read()
	if flag == 0:
		writer = cv2.VideoWriter(args["output"],fourcc, 20.0, (frame.shape[1],frame.shape[0]))
		flag =1

#	key = cv2.waitKey(0) & 0xFF
#	if key == ord("q"):
#		break
#
	if ret == False:
		break

#	frame = cv2.flip(frame,)
	mframe = np.copy(frame)
#	print(frame.shape)

	####################################################
	##########
	image_area = frame.shape[0] * frame.shape[1]


	g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)






	cv2.accumulateWeighted(g, avg, 0.1)

	res = cv2.convertScaleAbs(avg)

	sub = cv2.absdiff(res, g)

	#ret, thresh = cv2.threshold(sub, 90, 255, cv2.THRESH_BINARY)
	#ret, thresh = cv2.threshold(sub, 40, 255, cv2.THRESH_BINARY)
	ret, thresh = cv2.threshold(sub, 15, 255, cv2.THRESH_BINARY)
	#ret, thresh = cv2.threshold(sub, 20, 255, cv2.THRESH_BINARY)


	( contours, hierarchy) = cv2.findContours(thresh, cv2.RETR_TREE,
										   cv2.CHAIN_APPROX_SIMPLE)

	for i in contours:
		contour_area = cv2.contourArea(i)
		#if (contour_area > 0.0001 * image_area) and (contour_area< 0.001 * image_area):
		#if (contour_area > 0.0001 * image_area) and (contour_area< 0.01 * image_area):
		#if (contour_area > 0.01 * image_area) and (contour_area< 0.1 * image_area):

			#(x, y, w, h) = cv2.boundingRect(i)
			#cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 1)
	###############

		#if (contour_area < 0.01 * image_area) and (contour_area> 0.1 * image_area):
		if (contour_area > 0.01 * image_area) and (contour_area< 0.1 * image_area):
			writer.write(frame)
		elif (contour_area < 0.01 * image_area):
			continue


	# if the video writer is None *AND* we are supposed to write
	# the output video to disk initialize the writerq

#	fourcc = cv2.VideoWriter_fourcc(*"MJPG")
#	writer = cv2.VideoWriter(args["output"], fourcc, 20,
#		(frame.shape[1], frame.shape[0]), True)



	# if the writer is not None, write the frame with recognized
	# faces t odisk

	#writer.write(frame) # original save video

	# check to see if we are supposed to display the output frame to
	# the screen
	print("detected")
	cv2.imshow("Frame",frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break



# do a bit of cleanup
cv2.destroyAllWindows()
#vs.stop()
vs.release()

# check to see if the video writer point needs to be released
writer.release()