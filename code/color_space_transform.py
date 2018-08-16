import cv2
import numpy as np


'''
img = cv2.imread('lena.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('Origial', img)
cv2.imshow('Gray', img_gray)


flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

cv2.waitKey(0)
'''
# 视频中特定颜色追踪

capture = cv2.VideoCapture(1)

# 蓝色的范围，不同光照条件下不一样，可灵活调整
lower_blue = np.array([0, 100, 100])
upper_blue = np.array([100, 255, 255])

while (True):
    # 1.捕获视频中的一帧
    ret, frame = capture.read()

    # 2.从BGR转换到HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

    # 3.inRange(): 介于lower/upper之间的为白色，其余为黑色
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 4.只保留原图中蓝色部分
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(20) & 0xff == ord('q'):
        break

blue = np.uint8([[[0, 0, 255]]])
hsv_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
print(hsv_blue)  # [[[120 255 255]]]

capture.release()
cv2.destroyAllWindows()