import cv2

#cap = cv2.VideoCapture("20200619070142.ts")
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key ==27:
        break

cap.release()
cv2.destroyAllWindows()



