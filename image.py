import cv2


img = cv2.imread ('download.jpeg', 0)
cv2.imshow('Image', img)
cv2.waitKey(300000)