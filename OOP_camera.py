import cv2

class Camera():
    def __init__(Camera):
        Camera.cap = cv2.VideoCapture(1)
        #print("Camera warming up...")


    def get_frame(Camera):

        s, img = Camera.cap.read()


        return img

    def release_camera(Camera):
        Camera.cap.release()

while True:
    cam1 = Camera().get_frame()

    cv2.imshow("Frame", cam1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Camera().release_camera()


cv2.destroyAllWindows()