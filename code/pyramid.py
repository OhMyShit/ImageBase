import cv2
import numpy as np

img = cv2.imread('image\lena.jpg')

lower = cv2.pyrDown(img)    # 向下采样一级
higher = cv2.pyrUp(img)     # 向上采样一级

# image = np.hstack((img, higher))
cv2.imshow('higher', higher)
cv2.imshow('image', img)
cv2.imshow('lower', lower)
cv2.waitKey(0)