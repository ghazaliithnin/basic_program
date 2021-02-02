import cv2

i = cv2.imread("glove_test1.jpg")

(h, w) = i.shape[:2] 

# calculate the center of the image
center = (w / 2, h / 2) 

M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated90 = cv2.warpAffine(i, M, (h, w)) 

cv2.imshow("rotate",rotated90)
cv2.imwrite("gloverotate.jpg",rotated90)
cv2.waitKey()
cv2.destroyAllWindows()
