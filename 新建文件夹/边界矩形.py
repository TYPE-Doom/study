import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 1图像读取
img = cv.imread(r"G:\test\images\shape.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2转换为二值图
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# 3轮廓提取
contours, hierarchy = cv.findContours(thresh, 1, 2)
# 4将轮廓绘制在图像上
img = cv.drawContours(img, contours, 0, (0, 0, 255), 1)
cnt = contours[0]
# 5边界矩形
# 5.1直边界矩形
x, y, W, h = cv.boundingRect(cnt)
imgRect = cv.rectangle(img, (x, y), (x+W, y+h), (0, 255, 0), 2)
# 5.2旋转边界矩形结果
s = cv.minAreaRect(cnt)
a = cv.boxPoints(s)
a = np.int32(a)  # 转换a的类型为int型
cv.polylines(imgRect, [a], True, (255, 0, 0), 2)
# 6图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(imgRect[:, :, ::-1]), plt.title('res')
plt.xticks([]), plt.yticks([])
plt.show()
