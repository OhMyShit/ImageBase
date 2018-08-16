import cv2
import numpy as np

# 载入手写数字图片
img = cv2.imread('image\handwriting.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
image, contours, hierarchy = cv2.findContours(thresh, 3, 2)

# 以数字3的轮廓为例
cnt = contours[1]
cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)

# 1.轮廓面积
area = cv2.contourArea(cnt)
print(area)

# 2.轮廓周长
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

# 3. 图像矩   图像的各类几何特征
M = cv2.moments(cnt)
print(M)
print(M['m00'])     # 同前面的面积
cx, cy = M['m10']/M['m00'], M['m01']/M['m00']  # 质心
print(cx, cy)

# 图像外接矩形和最小外接矩形
x, y, w, h = cv2.boundingRect(cnt)  # 外接矩形
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect = cv2.minAreaRect(cnt)         # 最小外接矩形
box = np.int0(cv2.boxPoints(rect))      # 矩形的四个角点并取整
cv2.drawContours(img, [box], 0, (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)

