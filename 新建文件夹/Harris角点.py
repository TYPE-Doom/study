import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# 1读取图像，并转换成灰度图像
img = cv.imread(r"E:\PY\study\pythonProject2\images\qipan.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2角点检测
# 2.1输入图像必须是float32
gray = np.float32(gray)
# 2.2最后一个参数在0.04到0.05之间
dst = cv.cornerHarris(gray, 5, 3, 0.04)
# 3设置阈值，将角点绘制出来，阈值根据图像进行选择
img[dst > 0.001*dst.max()] = [0, 0, 255]
# 4图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('Harris')
plt.xticks([]), plt.yticks([])
plt.show()
