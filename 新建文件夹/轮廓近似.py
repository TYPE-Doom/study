import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# 1图像读取
img = cv.imread(r"E:\PY\study\pythonProject2\test\images\lunkuo.jpg")
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2转换为二值图
ret, thresh = cv.threshold(imgray, 127, 255, 0)
# 3轮廓提取
contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
cnt = contours[0]
area = cv.contourArea(cnt)
length = cv.arcLength(cnt, True)
print(area)
print(length)
# 4轮廓近似
epsilon = 0.1*cv.arcLength(contours[0], True)
approx = cv.approxPolyDP(contours[0], epsilon, True)
# 5将轮廓绘制在图像上
# 5.1原始轮廓
o_1 = img.copy()
o_2 = img.copy()
img1 = cv.drawContours(o_1, contours, -1, (0, 0, 255), 2)
# 5.2轮廓近似后的结果
img2 = cv.polylines(o_2, [approx], True, (0, 255, 0), 2)
# 6图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.subplot(121), plt.imshow(img1[:, :, ::-1]), plt.title('res1')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img2[:, :, ::-1]), plt.title('res2')
plt.xticks([]), plt.yticks([])
plt.show()
