import sys
import matplotlib.pyplot as plt
import numpy as np
import math

file_object = open('asd1.txt')  # 不要把open放在try中，以防止打开失败，那么就不用关闭了
try:
    file_context = file_object.read()  # file_context是一个string，读取完后，就失去了对test.txt的文件引用
    #  file_context = open(file_data).read().splitlines()
    # file_context是一个list，每行文本内容是list中的一个元素

    file_data = file_context.split(',')
    i = 0
    y = []
    x = []
    for data in file_data:
        i += 1
        value_y = -float(data) * math.sin(math.radians(i))
        y.append(value_y)
        value_x = -float(data) * math.cos(math.radians(i))
        x.append(value_x)
        #plt.scatter(x, y, s=1, color='r')i
    plt.plot(x, y, linewidth=1, color='g')
    plt.title('(0,0)', size=14)
    #plt.bar(x, y, color='g', width=0.5)
    plt.show()

    # 饼图
    # plt.pie(file_data)
    # plt.show()

    # 折线图
    # x = range(0, 360)
    # plt.plot(x, file_data, linewidth=0.4, color='r')
    # plt.tick_params(axis='y', labelsize=2)
    # plt.tick_params(axis='x', labelsize=6)

    # 散点图
    # x = np.arange(0, 360)
    # x = range(0, len(file_data))
    # plt.scatter(x, file_data, label='data', s=0.3, color='g')
    # plt.tick_params(axis='y', labelsize=2)
    # plt.tick_params(axis='x', labelsize=6)

    # 阿基米德螺线
    # plt.subplot(111, polar=True)
    # plt.ylim([0, 30])
    #
    # N = 4
    # theta = np.arange(0, N * np.pi, np.pi / 100)
    # plt.plot(theta, theta * 2, '--')

    # ax = plt.subplot(111, polar=True)
    # ax.set_thetagrids(np.arange(0.0, 360.0, 30.0))

    # ax.set_theta_zero_location('E')
    # plt.ylim([0, 30])

    # angle = range(0, 360)
    # plt.plot(angle, file_data, '.')

    # plt.show()

finally:
    file_object.close()
