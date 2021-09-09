import cv2
import numpy as np

#cap = cv2.VideoCapture("20200619070142.ts")
cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    ret, frame2 = cap2.read()
    numpy_horizontal = np.hstack((frame, frame2))
    numpy_horizontal_concat = np.concatenate((frame, frame2), axis=1)

    #cv2.imshow("Frame", frame)
    cv2.imshow('Numpy Horizontal', numpy_horizontal)
    cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

    key = cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cap2.release()
cv2.destroyAllWindows()



