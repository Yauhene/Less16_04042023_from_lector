import cv2

img = cv2.imread('D:\Jack\Java II/test.jpg')

img = cv2.resize(img, (300, 500))

cv2.imshow('Result', img)

cv2.waitKey(0)