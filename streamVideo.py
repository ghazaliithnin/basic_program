from imutils.video import VideoStream
import numpy as np
import time
import cv2


vs=VideoStream(src=1).start()
time.sleep(2.0)

while True:

    frame= vs.read()

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)& 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()