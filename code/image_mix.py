import cv2
import matplotlib.pyplot as plt
import numpy as np

'''图片相加'''
# x = np.uint8([250, 110, 10])
# y = np.uint8([10, 10, 230])
# print(cv2.add(x, y))
# print(x + y)
# print(x)

'''图像混合'''
img1 = cv2.imread('image\lena.jpg')
img2 = cv2.imread('image\opencv-logo-white.png')
print(img1.shape)
print(img2.shape)
# res = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)   # dst = α*img1 + β*img2 + γ  两幅图片的权重不一样，γ相当于一个修正值

'''按位操作'''

# 把logo放在左上角，所以我们只关心这一块
rows, cols = img2.shape[:2]
roi = img1[:rows, :cols]

# 创建掩膜
img2gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)  # 按位非， 只要黑色255部分

# 保留logo外的背景
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
dst = cv2.add(img1_bg, img2)    # 进行融合
img1[:rows, :cols] = dst        # 融合后放在原图上

cv2.imshow('res', img1)
cv2.waitKey(0)
