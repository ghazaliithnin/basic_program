import cv2
import numpy as np

img = cv2.imread('cw3.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)




ret, gray = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)

image, contours,hierarchy = cv2.findContours(gray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


for i in contours:
    (x,y,w,h)= cv2.boundingRect(i)

    cv2.circle(img,(x,y),3,(0,255,0),-1)
    cv2.circle(img,(x+w,y+h),3,(100,0,0),-1)

cv2.imshow('contours',img)






'''
corners = cv2.goodFeaturesToTrack(gray, 100,0.1,10)
corners = np.int0(corners)

#cv2.imshow('result',img)

#print('corners',len(corners))

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    #print(x,y)





#print('corners',len(corners))

cv2.imshow('corners',img)
'''



cv2.waitKey()
cv2.destroyAllWindows()

