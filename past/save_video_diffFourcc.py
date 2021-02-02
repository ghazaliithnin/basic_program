import cv2

#cap = cv2.VideoCapture("highway.mp4")
cap = cv2.VideoCapture(0)
#filename= "test_video"


#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#outname=("2_30May19")
#out = cv2.VideoWriter('rekod_'+filename+outname+'.avi',
#out = ('test_save_video.avi',cv2.VideoWriter_fourcc('M','J','P','G'),30,(width, height)) # for different version



##############
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
####
while True:
    ret, frame = cap.read()
    
    out.write(frame)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key ==27:
        break

out.release() 
cap.release()
cv2.destroyAllWindows()



