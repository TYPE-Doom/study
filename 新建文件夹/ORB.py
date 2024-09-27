import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# 1图像读取
img = cv.imread(r"E:\PY\study\pythonProject2\images\tv.jpg", cv.IMREAD_GRAYSCALE)
# 2 ORB角点检测
# 2.1实例化0RB对象
orb = cv.ORB()
# 2.2检测关键点,并计算特征描述符
try:
    kp, des = orb.detectAndCompute(img, None)
except cv.error as e:
    print(f"ORB检测发生错误: {e}")
# 3将关键点绘制在图像上
img2 = cv.drawKeypoints(img, kp, None, color=(0, 0, 255), flags=0)
# 4.绘制图像
plt. figure(figsize=(10, 8), dpi=100)
plt. imshow(img2[:, :, ::-1])
plt.xticks([]), plt.yticks([])
plt.show()
