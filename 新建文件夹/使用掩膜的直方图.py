import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread(r"G:\test\images\orange.jpg", cv2.IMREAD_GRAYSCALE)
mask = np.zeros(image.shape, np.uint8)  # 构建掩膜
mask[100:200, 100:200] = 255
histMI = cv2.calcHist([image], [0], mask, [256], [0, 255])  # 计算统计直方图
histlmage = cv2.calcHist([image], [0], None, [256], [0, 255])
plt.plot(histlmage)     # 绘制图像
plt.plot(histMI)
plt.show()
