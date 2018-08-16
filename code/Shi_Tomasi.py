import cv2
import numpy as np

img = cv2.imread('image\corner_sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# Shi_Tomasi角点检测
corners = cv2.goodFeaturesToTrack(gray, 20, 0.1, 10)
corners = np.int0(corners)  # 12个角点坐标

for i in corners:
    # 压缩至一维：[[62, 64]]-> [62, 64]
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

cv2.imshow('dst', img)
cv2.waitKey(0)