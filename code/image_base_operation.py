import cv2

img = cv2.imread('image\lena.jpg')

px = img[100, 100]  # 通过行列来获取某像素的值，对于彩色图，这个值是B，G，R，三个值的列表，对于灰度图，只有一个值
print(px)

# 只获取蓝色blue通道的值
px_blue = img[100, 100, 0]
print(px_blue)

# img.shape获取图像的形状，图片是彩色的话，返回一个包含高度、宽度和通道数的元组，灰度图只返回高度和宽度
print(img.shape)
height, width, channels = img.shape
# 灰度图 heigh, width = img.shape

# img.dtype获取图像的数据类型
print(img.dtype)

# img.size 获取图像的总像素数
print(img.size)     # 350*350*3
print(350*350*3)

# RIO: region of interest 感兴趣区域
# 截取脸部RIO
face = img[150:260, 150:240, 0]
cv2.namedWindow('face', cv2.WINDOW_NORMAL)
cv2.imshow('face', face)
cv2.waitKey(0)
