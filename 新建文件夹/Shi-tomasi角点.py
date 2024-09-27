import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1读取图像
img = cv2.imread(r"E:\PY\study\pythonProject2\images\tv.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 2角点检测
corners = cv2.goodFeaturesToTrack(gray, 5000, 0.1, 10)
# 3绘制角点
for i in corners:
    x, y = i.ravel()
    x = int(x)  # 妈的，注意看函数要求代码，要整型，垃圾课程
    y = int(y)
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
# 4图像展示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('shi-tomasi')
plt.xticks([]), plt.yticks([])
plt.show()
