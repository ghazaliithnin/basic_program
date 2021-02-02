import cv2

filename = "Abidul_Muntaqim"
cap = cv2.VideoCapture(filename+".mp4")

count=0
framecount = 0
while True:
    ret, frame = cap.read()

    if ret == True:

        cv2.imshow("Frame", frame)
        framecount += 30 # 30 fps, this advances One Seconds
        cap.set(1, framecount)

    elif ret == False:
        print("completed")
        break


    #cv2.imwrite("savevideo_to_frames//gaz"+str(count)+".jpg",frame)
    #cv2.imwrite("savevideo_to_frames//"+filename+str(count)+".jpg",frame)
    count = count + 1

    #cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key ==27:
        print("Stopped, Escape Key Pressed")
        break

cap.release()
cv2.destroyAllWindows()



