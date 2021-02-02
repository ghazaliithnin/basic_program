import cv2

#cap = cv2.VideoCapture("20200619070142.ts")
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    ret1, frame1 = cap1.read()
    frame1= cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    try:
        ret2, frame2 = cap2.read()
        frame2= cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Frame2", frame2)
    except Exception as e:
        print(e)



    cv2.imshow("Frame1", frame1)


    key = cv2.waitKey(1)
    if key ==27:
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()



