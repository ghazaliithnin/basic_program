import cv2
import numpy as np

img = cv2.imread('cw3.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




ret, gray = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)

image, contours,hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

centers = []
for i in contours:


    (x,y,w,h)= cv2.boundingRect(i)

    if (w>300) and (h>300) and (w<400) and (h<400):
        #print(w,h)
        xw = x + w
        yh = y + h

        cv2.circle(img,(x,y),3,(0,255,0),-1)
        cv2.circle(img,(xw,yh),3,(100,0,255),-1)
        #cv2.rectangle(img,(x,y),(xw,yh),(0,255,0),2)



        midx = int ((xw-x)/2)
        midy = int ((yh-y)/2)
        cx = x + midx
        cy = y + midy
        #centers.append((cx,cy))

        cv2.circle(img,(cx,cy),3, (100,100,255),-1)

#cv2.imshow('contours',img)







#corners = cv2.goodFeaturesToTrack(gray, 100,0.02,10)
#corners = cv2.goodFeaturesToTrack(gray, 70,0.1,10)
corners = cv2.goodFeaturesToTrack(gray, 30,0.1,10)
corners = np.int0(corners)

#cv2.imshow('result',img)

#print('corners',len(corners))

for i2 in corners:
    x2,y2 = i2.ravel()
    cv2.circle(img,(x2,y2),3,255,-1)
            #print(x,y)





#print('corners',len(corners))

cv2.imshow('corners',img)



cv2.waitKey()
cv2.destroyAllWindows()

