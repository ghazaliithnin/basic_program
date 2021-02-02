#Run on Python 3.7.2, if other version might occur errors

import cv2
import numpy as np


#cap = cv2.VideoCapture('kav17r3.mp4') #depth 60
cap = cv2.VideoCapture('kav17r2.mp4')
#cap = cv2.VideoCapture('kav17r_67D.mp4') # Kepong A depth 67
#cap = cv2.VideoCapture('kav17r_20D2.mp4') # Kepong A depth 20
#cap = cv2.VideoCapture('pav3r_70D.mp4') # Pulai A 3R depth 70

#cap = cv2.VideoCapture('fkuning.mp4')

#cap = cv2.VideoCapture('kav16r2.mp4')
ratio = 0.3 # image resize ratio
_, f = cap.read()




f = cv2.resize(f, None, fx = ratio, fy = ratio,
     interpolation = cv2.INTER_AREA)

#########
##
'''
kernel = np.array([[-1, -1, -1], [-1,9,-1], [-1,-1,-1]])

f = cv2.filter2D(f, -1, kernel)
'''
##
###########


#g = cv2.medianBlur(f, 5)
g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)

#g = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)


avg = np.float32(g)

image_area = None

centres=[]
cf=0
pcf=0 # pcf = previous count fish
while True:

    _, f = cap.read()


    if _ ==False:
                break


    f = cv2.resize(f, None, fx =ratio, fy = ratio,
     interpolation = cv2.INTER_AREA)
    #############
    '''
    kernel = np.array([[-1, -1, -1], [-1,9,-1], [-1,-1,-1]])

    f = cv2.filter2D(f, -1, kernel)
    '''
    #########################
    image_area = f.shape[0] * f.shape[1]
    #g = cv2.medianBlur(f, 5)

    g = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)






    #cv2.accumulateWeighted(g, avg, 0.1)
    #cv2.accumulateWeighted(g, avg, 0.001)
    cv2.accumulateWeighted(g, avg, 0.01)


    res = cv2.convertScaleAbs(avg)

    sub = cv2.absdiff(res, g)



    #ret, thresh = cv2.threshold(sub, 90, 255, cv2.THRESH_BINARY)
    ret, thresh = cv2.threshold(sub, 25, 255, cv2.THRESH_BINARY) #original

    # Kepong A 20 depth
    #ret, thresh = cv2.threshold(sub, 35, 255, cv2.THRESH_BINARY)
    # Kepong 67 depth
    #ret, thresh = cv2.threshold(sub, 15, 255, cv2.THRESH_BINARY)
    #ret, thresh = cv2.threshold(sub, 20, 255, cv2.THRESH_BINARY)


    (ret,contours, hierarchy) = cv2.findContours(thresh, cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)


    for i in contours:
        contour_area = cv2.contourArea(i)
        #if (contour_area > 0.0001 * image_area) and (contour_area< 0.001 * image_area):
        if (contour_area > 0.001 * image_area) and (contour_area< 0.01 * image_area): #Original
        #if (contour_area > 0.00001 * image_area) and (contour_area< 0.01 * image_area): #67 depth
        #if (contour_area > 0.001 * image_area) and (contour_area< 0.01 * image_area):

            (x, y, w, h) = cv2.boundingRect(i)
            cv2.rectangle(f, (x, y), (x+w, y+h), (0,0,255), 2)

            #calculate box's centroid
            xw= x+w
            yh = y+w

            mx = int((xw-x)/2) # mid points of x axis from the box
            my = int((yh-y)/2) # mid point of y axis

            cx = x + mx # centroid x coordinate
            cy = y + my # centroid y coordinate

            centres.append((cx, cy))

            cf = len(centres) # count fish

            #cf = cf+1
            #print(cf)

            #cv2.putText (f, 'fish %d'%cf,(cx,cy),
                #cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255),1)





    tx = int (f.shape[1]*0.3) # coordinate X text
    ty = int (f.shape[0]-20)
    cv2.putText (f, 'Count =  %d'%cf,(tx,ty),
        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255),2)


    cv2.imshow('img', f)


    centres=[]

    ps = cf # ps = previous state
    cs = ps  # cs = current state
    if cs!= pcf:
        print(cf)
    pcf=cs

    #cv2.imshow('subtract', sub)
    #cv2.imshow('avg', res)
    #cv2.imshow('Threshoold', thresh)
    #cv2.imshow('Strel', Strel)


    k = cv2.waitKey(1)

    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()